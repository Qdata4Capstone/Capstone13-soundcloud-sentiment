import heatmap_gen
import json
import nltk
from nltk.corpus import stopwords

def check_dups(file_contents):
    tracks = set()
    dupFound = False

    for line in file_contents:
        if line in tracks:
            print 'Duplicate: ' + line
            dupFound = True
        else:
            tracks.add(line)
    return dupFound


def scrape_comments_json(file_contents):
    out_list = []
    count = 1

    for url in file_contents:
        print 'Fetching comments for ' + str(count)
        comments = heatmap_gen.getCommentsFromURL(url)
        for comment in comments:
            if hasattr(comment.obj, 'id'):
                out_list.append(parseFields(comment.obj))
            else:
                out_list.append(parseFields(comment))
        count += 1

    with open('comments.json', 'a') as outfile:
        json.dump(out_list, outfile, indent=2)

def scrape_comments_flat(file_contents):
    out_list = []
    count = 1

    for url in file_contents:
        print 'Fetching comments for ' + str(count)
        comments = heatmap_gen.getCommentsFromURL(url)
        for comment in comments:
            if hasattr(comment.obj, 'id'):
                out_list.append(parseFields(comment.obj)['body'])
            else:
                out_list.append(parseFields(comment)['body'])
        count += 1

    with open('comments.txt', 'a') as outfile:
        for line in out_list:
            outfile.write(line.encode('utf8') + "\n")

def parseFields(comment):
    out = {'id': comment.id, 'timestamp': comment.timestamp, 'body': comment.body, 'track_id': comment.track_id}
    return out

#Pull out all of the words in a list of tagged tweets, formatted in tuples.
def getwords(tweets):
    allwords = []
    for (words, sentiment) in tweets:
        allwords.extend(words)
    return allwords

#Order a list of tweets by their frequency.
def getwordfeatures(listoftweets):
    #Print out wordfreq if you want to have a look at the individual counts of words.
    wordfreq = nltk.FreqDist(listoftweets)
    words = wordfreq.keys()
    return words

def feature_extractor(doc):
    docwords = set(doc)
    features = {}
    for i in wordlist:
        features['contains(%s)' % i] = (i in docwords)
    return features

rp = open('really_positive.txt', 'r')
really_positive = rp.readlines()

sp = open('semi_positive.txt', 'r')
semi_positive = sp.readlines()

n = open('neutral.txt', 'r')
neutral = n.readlines()

neg = open('negative.txt', 'r')
negative = neg.readlines()

neglist = []
rplist = []
splist = []
neutlist = []

for i in range(0,len(really_positive)):
    rplist.append('really_positive')

for i in range(0,len(semi_positive)):
    splist.append('semi_positive')

for i in range(0,len(neutral)):
    neutlist.append('neutral')

for i in range(0,len(negative)):
    neglist.append('negative')

rptagged = zip(really_positive, rplist)
sptagged = zip(semi_positive, splist)
neuttagged = zip(neutral, neutlist)
negtagged = zip(negative, neglist)

taggedtweets = negtagged + neuttagged + sptagged + rptagged

tweets = []

for (word, sentiment) in taggedtweets:
    word_filter = [i.lower() for i in word.split()]
    tweets.append((word_filter, sentiment))

wordlist = wordlist = [i for i in getwords(tweets) if not i in stopwords.words('english')]

training_set = nltk.classify.apply_features(feature_extractor, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

print getwordfeatures(getwords(tweets))
print classifier.show_most_informative_features(n=50)

print "Attempt to classify: " + classifier.classify(feature_extractor("good tune".split()))

if __name__ == '__main__':
    #target = open('URLs.txt', 'r')
    #lines = target.read().splitlines()
    #target.close()
    #
    #if not check_dups(lines):
    #     print 'All good'
    #     scrape_comments_flat(lines)
    pass