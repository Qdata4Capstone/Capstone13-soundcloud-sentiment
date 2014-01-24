from flask import Flask
from flask import render_template

heatmap_gen = Flask(__name__)

@heatmap_gen.route('/')
def index():
    return render_template('index_thesis.html')

@heatmap_gen.route('/top100')
def top_100():
    return render_template('top100.html')

@heatmap_gen.route('/top100landing')
def top_100landing():
    return render_template('top100landing.html')

@heatmap_gen.route('/ezoo')
def ezoo():
    return render_template('ezoo.html')

if __name__ == '__main__':
    heatmap_gen.run()
