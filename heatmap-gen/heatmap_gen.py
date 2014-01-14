from flask import Flask
from flask import request
from flask import render_template
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

app = Flask(__name__)
app.config.from_envvar('SC_SENTIMENT_SETTINGS')

client = soundcloud.Client(client_id=app.config['SOUNDCLOUD_ID'])
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

#Pull out all of the words in a list of tagged tweets, formatted in tuples.
def getwords(tweets):
    allwords = []
    for (words, sentiment) in tweets:
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

taggedtweets = negtagged + neuttagged + sptagged + rptagged

tweets = []

for (word, sentiment) in taggedtweets:
    word_filter = [i.lower() for i in word.split()]
    tweets.append((word_filter, sentiment))

customstopwords = ['download', 'link', 'music', 'synth', 'i\'m', 'u', 'balls', 'dl',
                   'people', 'chords', 'you\'re', 'new', 'im', 'guys', 'i\'ve', 'vocals',
                   'would', 'one', 'like', 'tell', 'joel!', 'martin', 'r', 'hardwell', '?',
                   'that\'s', 'check', '...', 'dj', 'thing', 'listening', 'tune', 'remix', 'gonna',
                   'take', 'first', 'gives', 'animals', '-', 'it\'s', 'gets', 'make', '.', 'it.', 'get',
                   'deadmau5', 'work', 'ride', 'it!', 'track!', 'this.', 'dude', 'job', 'god', 'cookies',
                   'milk', 'work.', 'go', 'dick', 'ass', 'n', 'please']

#Remove stopwords, which don't add to the sentiment of the comment, standard library of these and custom
wordlist = wordlist = [i for i in getwords(tweets) if not i in stopwords.words('english')]
wordlist = [i for i in wordlist if not i in customstopwords]

training_set = nltk.classify.apply_features(feature_extractor, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

print classifier.show_most_informative_features(n=50)

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
                            headers={"X-Mashape-Authorization": app.config['MASHAPE_KEY']},
                            params={"height": 500, "textblock": corpus_post, "width": 500, "config": ""})

    scores = score_comments(comments, duration)
    interval = find_window(scores, duration, 8000)
    upload = draw_lines(waveform, scores, interval)

    result = {'id': id, 'word_cloud_url': response.body['url'], 'waveform': upload}
    return result

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
        left += 1000
    return best_window

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

    im = pyimgur.Imgur(app.config['IMGUR_KEY'])
    uploaded_image = im.upload_image(destination_file, title="Waveform")

    return uploaded_image.link

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tomorrowworld')
def tomorrowworld():
    return render_template('tomorrowworld.html')

@app.route('/top100')
def top_100():
    return render_template('top100.html')

@app.route('/top100landing')
def top_100landing():
    return render_template('top100landing.html')

@app.route('/comments')
def get_comments():
    url = request.args.get('url')
    return json.dumps(get_comments_from_url(target=url))

if __name__ == '__main__':
    app.run()
