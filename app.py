from flask import Flask, render_template, request, flash
import pickle
import numpy as np
import pandas as pd
# Load model and scaler
model = pickle.load(open("random_forest_model.pkl", "rb"))

#flash app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predic():
    pass




#python main
if __name__ == "__main__":
    app.run(debug=True)


