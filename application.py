from flask import Flask, redirect, render_template, request, url_for
import nltk
import helpers
from analyzer import Analyzer
import os
import sys
app = Flask(__name__)

@app.route("/") #if / query
def index():
    return render_template("index.html")

@app.route("/search") # when the user visits /search
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "") # why 2nd parameter is empty?
    if not screen_name:
        return redirect(url_for("index")) # what happeing?
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    # TODO
    positive, negative, neutral = 0.0, 0.0, 0.0 #why 100?
    scores=0
    counter=0
    tokenizer=nltk.tokenize.TweetTokenizer()
    for j in range(len(tweets)):
        tokens=tokenizer.tokenize(tweets[j])
        for i in range(len(tokens)):
            scores=analyzer.analyze(tokens[i])
            counter=counter+scores
        if counter > 0.0:
            positive=positive+1
        elif counter<0.0:
            negative=negative+1
        else:
            neutral=neutral+1
        counter=0
    total=positive+negative+neutral
    positive=(positive/total)*100
    negative=(negative/total)*100
    neutral=(neutral/total)*100


    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
