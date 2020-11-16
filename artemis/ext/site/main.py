from flask import request, render_template
from flask import Blueprint
import numpy as np
import pickle

bp = Blueprint("site", __name__)

def frequency_counter(text, vocabulary):
    frequency = [0] * len(vocabulary)

    for word in text:
        if word in vocabulary:
            position = vocabulary[word]
            frequency[position] += 1
    return frequency

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/bands")

def bands():
    return render_template("bands.html")

    
@bp.route("/admin")
def admin():
    return render_template("admin.html")

@bp.route("/search", methods=["POST"])
def search():
    model = open('modelo.pkl', 'rb')
    modelo = pickle.load(model)

    vocabulario = open('vocabulary.pkl', 'rb') 
    vocabulary = pickle.load(vocabulario)

    lyrics = request.values['lyric'].lower().split()
    frequency = frequency_counter(lyrics, vocabulary)

    transform_2d = np.array(frequency).reshape(1, -1)

    band = modelo.predict(transform_2d) 

    result = "The Rolling Stones" if band == 2 else  "The Beatles"

    return render_template("index.html", lyric=request.values['lyric'].strip(), result=result)
