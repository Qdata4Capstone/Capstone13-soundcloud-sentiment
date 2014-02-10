##SoundCloud Sentiment Research
###Jasdev Singh - Senior Thesis Repository, 2013 - 2014
###Advisor: Dr. Yanjun Qi
---
This repo is a work in progress and will serve as central place for code and datasets related to my research in the 2013 - 2014 school year.
Four main areas I will be focusing on are:
* Using timed comment sentiment to generate a heatmap associated with a given SoundCloud track
* Clustering timed comments for intelligent previews
* Looking for trends in the BeatPort top charts
* Looking for trends in the DJ Mag Top 100 charts (17 years worth of data)
* Graphing artists' use of other musician's songs in their sets at festivals such as Electric Zoo

All subtasks and goals are open to the public and can be viewed here: https://trello.com/b/Ii6IK0Mi

###Usage
To run the SoundCloud sentiment analyzer locally, clone this repo and cd into `heatmap-gen/`. To install dependencies, run `pip install -r requirements.txt`. From here, run `python sc_runner.py sc_url`, to get output on metadata for the track (where sc_url is a valid SoundCloud URL for a given track).

###Structure
* `heatmap-gen/comments/` contains the training sets for Bayesian classifier to distinguish sentiment. There are four labelings: negative, neutral, semi-positive, and really-positive. The raw comment corpus is housed in `comments.json` under this directory
* `heatmap-gen/static/datasets` contains a few sets of interest. `dj-mag-top-100.json` and `dj-mag-top-100.csv` contain the DJ Magazine Top 100 poll results for the past 17 years. Moreover, `electric-zoo-2013.json` contains set data for the Electric Zoo NY 2013 festival, where each object in the outermost json array contains the artists each DJ 'imports' into their set and rank data.
* `aux.py`, `heatmap_gen.py`, `top_100.py` are all auxiliary files needed to help the web app run and aren't necessary to perform local analysis