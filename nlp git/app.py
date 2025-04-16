from flask import Flask, render_template, request
from text_summarizer import summarize_text
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(_name_)

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    sentiment = ""
    sentiment_score = 0.0
    if request.method == 'POST':
        if 'text' in request.form:  # If user enters text
            text = request.form.get('text')  # Get the text from the form
            if text:  # Ensure there is text to summarize
                summary = summarize_text(text)  # Call summarize_text function
                sentiment_score = sia.polarity_scores(text)['compound']
                if sentiment_score >= 0.05:
                    sentiment = 'Positive'
                elif sentiment_score <= -0.05:
                    sentiment = 'Negative'
                else:
                    sentiment = 'Neutral'
    
    return render_template('index.html', summary=summary, sentiment=sentiment, sentiment_score=sentiment_score)

if _name_ == '_main_':
    app.run(debug=True)