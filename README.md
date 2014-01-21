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

###Web app
Endpoints to come