from flask import Flask
from flask import request
from pprint import pprint
import soundcloud

client = soundcloud.Client(client_id="6504a6ad70b88dd5684e256947c782c0")

app = Flask(__name__)


def getCommentsFromURL(target):
    track = client.get('/resolve', url=target)
    id = track.id

    page_size = 200
    comments = []
    current = client.get('/tracks/' + str(id) + '/comments', limit=page_size)
    comments += current
    page = 1
    while not len(current) == 0:
        current = client.get('/tracks/' + str(id) + '/comments', limit=page_size, offset=page*page_size)
        comments += current
        page += 1
    return len(comments)

@app.route('/')
def index():
    return 'lol index page'

@app.route('/comments')
def getComments():
    url = request.args.get('url')
    return str(getCommentsFromURL(target=url))


if __name__ == '__main__':
    app.run()
