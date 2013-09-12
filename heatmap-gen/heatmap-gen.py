from flask import Flask
from flask import request

import soundcloud

app = Flask(__name__)
app.config.from_envvar('SC_SENTIMENT_SETTINGS')

client = soundcloud.Client(client_id=app.config['SOUNDCLOUD_ID'])

def getCommentsFromURL(target):
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

@app.route('/comments')
def getComments():
    url = request.args.get('url')
    return str(getCommentsFromURL(target=url))

if __name__ == '__main__':
    app.run()
