from flask import Flask, render_template, request
from text_summarizer import summarize_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            summary = summarize_text(text)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
