from flask import Flask
from pprint import pprint
import soundcloud

client = soundcloud.Client(client_id="6504a6ad70b88dd5684e256947c782c0")

app = Flask(__name__)


@app.route('/')
def hello_world():
    page_size = 200

    comments = []
    current = client.get('/tracks/108569036/comments', limit=page_size)
    comments += current
    page = 1
    while not len(current) == 0:
        current = client.get('/tracks/108569036/comments', limit=page_size, offset=page*page_size)
        comments += current
        page += 1
    print len(comments)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
