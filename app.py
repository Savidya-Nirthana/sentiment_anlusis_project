from flask import Flask, render_template, request, redirect
from prediction import data_cleaning

app = Flask(__name__)

data = {}
reviews = []
positive = 0
negative = 0

@app.route('/')
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html', data=data)

@app.route('/', methods=['post'])
def my_post():
    global reviews
    global positive
    global negative
    text = request.form['text']
    prediction = data_cleaning(text=text)
    if prediction == 0:
        positive += 1
    else:
        negative += 1
    reviews.insert(0,text)
    return redirect(request.url)
if __name__ == '__main__':
    app.run()