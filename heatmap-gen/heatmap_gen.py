from flask import Flask
from flask import request
import os, sys, nltk, soundcloud
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

rp = open('./comments/really_positive.txt', 'r')
really_positive = rp.readlines()

sp = open('./comments/semi_positive.txt', 'r')
semi_positive = sp.readlines()

n = open('./comments/neutral.txt', 'r')
neutral = n.readlines()

neg = open('./comments/negative.txt', 'r')
negative = neg.readlines()

neglist, rplist, splist, neutlist = []

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

customstopwords = ['download', 'link', 'music', 'synth', 'i\'m', 'u', 'balls', 'dl',
                   'people', 'chords', 'you\'re', 'new', 'im', 'guys', 'i\'ve', 'vocals',
                   'would', 'one', 'like', 'tell', 'joel!', 'martin', 'r', 'hardwell', '?',
                   'that\'s', 'check', '...']

wordlist = wordlist = [i for i in getwords(tweets) if not i in stopwords.words('english')]
wordlist = [i for i in wordlist if not i in customstopwords]

training_set = nltk.classify.apply_features(feature_extractor, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

print classifier.show_most_informative_features(n=50)

def get_comments_from_url(target):
    track = client.get('/resolve', url=target)
    id = track.id

    page_size = 200
    comments = []
    current = client.get('/tracks/' + str(id) + '/comments', limit=page_size, offset=0)
    comments += current
    page = 1
    while not len(current) == 0:
        current = client.get('/tracks/' + str(id) + '/comments', limit=page_size, offset=page*page_size)
        comments += current
        page += 1
    return comments

@app.route('/')
def index():
    return 'TBD, landing page'

@app.route('/waveform')
def waveform():
    url = request.args.get('url')
    '''

    Below is snippet to classify a given piece of text
        print "Attempt to classify: " + classifier.classify(feature_extractor("good tune".split()))
    Need to fetch all comments form URL
    Classify each one, and pass to template for rendering with waveform.js

    '''

@app.route('/comments')
def get_comments():
    url = request.args.get('url')
    return str(get_comments_from_url(target=url))

if __name__ == '__main__':
    app.run()
