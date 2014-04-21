import os
import sys
import nltk
import soundcloud
import json
import math
import urllib
import Image
import ImageDraw
import unirest
import pyimgur
from nltk.corpus import stopwords

client = soundcloud.Client(client_id='6504a6ad70b88dd5684e256947c782c0')
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

#Pull out all of the words, formatted in tuples.
def getwords(comments):
    allwords = []
    for (words, sentiment) in comments:
        allwords.extend(words)
    return allwords

def feature_extractor(doc):
    docwords = set(doc)
    features = {}
    for i in wordlist:
        features['contains(%s)' % i] = (i in docwords)
    return features

rp = open('./comments/really_positive.txt', 'r')
really_positive = rp.readlines()

sp = open('./comments/semi_positive.txt', 'r')
semi_positive = sp.readlines()

n = open('./comments/neutral.txt', 'r')
neutral = n.readlines()

neg = open('./comments/negative.txt', 'r')
negative = neg.readlines()

neglist, rplist, splist, neutlist = [], [], [], []

for i in range(0,len(really_positive)):
    rplist.append('really_positive')

for i in range(0,len(semi_positive)):
    splist.append('semi_positive')

for i in range(0,len(neutral)):
    neutlist.append('neutral')

for i in range(0,len(negative)):
    neglist.append('negative')

#Tag comments with their appropriate category
rptagged = zip(really_positive, rplist)
sptagged = zip(semi_positive, splist)
neuttagged = zip(neutral, neutlist)
negtagged = zip(negative, neglist)

taggedcomments = negtagged + neuttagged + sptagged + rptagged

comments = []

for (word, sentiment) in taggedcomments:
    word_filter = [i.lower() for i in word.split()]
    comments.append((word_filter, sentiment))

customstopwords = ['download', 'link', 'music', 'synth', 'i\'m', 'u', 'balls', 'dl',
                   'people', 'chords', 'you\'re', 'new', 'im', 'guys', 'i\'ve', 'vocals',
                   'would', 'one', 'like', 'tell', 'joel!', 'martin', 'r', 'hardwell', '?',
                   'that\'s', 'check', '...', 'dj', 'thing', 'listening', 'tune', 'remix', 'gonna',
                   'take', 'first', 'gives', 'animals', '-', 'it\'s', 'gets', 'make', '.', 'it.', 'get',
                   'deadmau5', 'work', 'ride', 'it!', 'track!', 'this.', 'dude', 'job', 'god', 'cookies',
                   'milk', 'work.', 'go', 'dick', 'ass', 'n', 'please']

#Remove stopwords, which don't add to the sentiment of the comment, standard library of these and custom
wordlist = [i for i in getwords(comments) if not i in stopwords.words('english')]
wordlist = [i for i in wordlist if not i in customstopwords]

training_set = nltk.classify.apply_features(feature_extractor, comments)
classifier = nltk.NaiveBayesClassifier.train(training_set)

# print classifier.show_most_informative_features(n=50)


def get_comments_from_url(target):
    track = client.get('/resolve', url=target)

    id = track.id
    waveform = track.waveform_url
    duration = track.duration

    page_size = 200
    comments = []
    current = client.get('/tracks/' + str(id) + '/comments', limit=page_size, offset=0)

    for comment in current:
        value = {}
        value['body'] = comment.body
        value['timestamp'] = comment.timestamp
        value['created_at'] = comment.created_at
        comments.append(value)

    page = 1
    while not len(current) == 0:
        current = client.get('/tracks/' + str(id) + '/comments', limit=page_size, offset=page*page_size)

        for comment in current:
            value = {}
            value['body'] = comment.body
            value['timestamp'] = comment.timestamp
            value['created_at'] = comment.created_at
            comments.append(value)

        page += 1

    corpus = []
    for comment in comments:
        corpus.extend(comment['body'].split())

    corpus_post = " ".join(corpus)

    response = unirest.post("https://gatheringpoint-word-cloud-maker.p.mashape.com/index.php",
                            headers={"X-Mashape-Authorization": 'i27GpdJndOzwUF62rpd7oyoMucwxIdL1'},
                            params={"height": 500, "textblock": corpus_post, "width": 500, "config": ""})

    scores = score_comments(comments, duration)
    interval_tuple = find_window(scores, duration, 8000)
    interval = interval_tuple[0]
    window = interval_tuple[1]
    upload = draw_lines(waveform, scores, interval)

    result = {'id': id, 'word_cloud_url': response.body['url'], 'waveform': upload, 'window_left': get_readable_time(window[0]), 'window_right': get_readable_time(window[1])}
    return result

def get_readable_time(milliseconds):
    seconds = milliseconds / 1000
    minutes = seconds / 60
    seconds %= 60

    return str(minutes) + ":" + str(seconds)

def score_comments(comments, time):
    scores = []
    for comment in comments:
        try:
            percent = float(str(comment['timestamp'])) / time
            score = classifier.classify(feature_extractor(comment['body'].split()))
            timestamp = str(comment['timestamp'])
            scores.append((percent, score, timestamp))
        except ValueError:
            pass
    return scores

def find_window(scores, duration, window_size):
    left = 0
    best_sum = 0
    best_time_window = (0, window_size)
    best_window = (0, float(window_size) / duration)

    for right in range(window_size, duration, 1000):
        window_sum = 0
        comments_in_window = [x for x in scores if left <= int(x[2]) <= right]
        for (percent, score, time) in comments_in_window:
            if score == "negative":
                window_sum -= 1
            elif score == "semi_positive":
                window_sum += 1
            elif score == "really_positive":
                window_sum += 2
        if window_sum > best_sum:
            best_sum = window_sum
            best_window = (float(left) / duration, float(right) / duration)
            best_time_window = (left, right)
        left += 1000
    return best_window, best_time_window

def draw_lines(url, scores, interval):
    location = "./static/img/" + url.split('/')[-1]
    urllib.urlretrieve(url, location)
    im = Image.open(location)
    im = im.convert("RGBA")
    im = im.point(lambda x: x * .9)
    draw = ImageDraw.Draw(im)
    width = im.size[0]
    height = im.size[1]

    box = (math.floor(width*interval[0]), 0, math.floor(width*interval[1]), height)
    draw.rectangle(box, fill=(255, 0, 0))

    for (percent, score, time) in scores:
        comment_x = math.floor(width*percent)
        if score == "negative":
            draw.line((comment_x, 0, comment_x, height), fill=(255, 0, 0))
        elif score == "neutral":
            draw.line((comment_x, 0, comment_x, height), fill=(128, 128, 128))
        elif score == "semi_positive":
            draw.line((comment_x, 0, comment_x, height), fill=(0, 153, 153))
        else:
            draw.line((comment_x, 0, comment_x, height), fill=(0, 153, 0))

    destination_file = "./static/img/processed_" + url.split('/')[-1]
    im.save(destination_file)

    im = pyimgur.Imgur('3aa9b7ef8d192ea')
    uploaded_image = im.upload_image(destination_file, title="Waveform")

    return uploaded_image.link


def precision_tests(label, corpus):
    tp, fp = 0, 0

    for (comment, sent) in corpus:
        prediction = classifier.classify(feature_extractor(comment))
        if prediction == label and sent == label:
            tp += 1
        elif prediction == label and sent != label:
            fp += 1

    print tp, fp

    return float(tp) / (tp + fp)


def recall_tests(label, corpus):
    tp, p = 0, 0

    for (comment, sent) in corpus:
        prediction = classifier.classify(feature_extractor(comment))
        if prediction == label and sent == label:
            tp += 1
        if sent == label:
            p += 1

    print tp, p

    return float(tp) / p


def cv_test(num_folds, training):
    subset_size = len(training)/num_folds
    accuracies = []

    for i in range(num_folds):
        testing_this_round = training[i*subset_size:][:subset_size]
        training_this_round = training[:i*subset_size] + training[(i+1)*subset_size:]

        training_set = nltk.classify.apply_features(feature_extractor, training_this_round)
        classifier = nltk.NaiveBayesClassifier.train(training_set)

        correct = 0

        for (comment, sent) in testing_this_round:
            prediction = classifier.classify(feature_extractor(comment))

            if prediction == sent:
                correct += 1

        accuracies.append(float(correct)/len(testing_this_round))

    return sum(accuracies)/len(accuracies)


if __name__ == '__main__':
    print json.dumps(get_comments_from_url(target=sys.argv[1]))