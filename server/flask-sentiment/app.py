from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json() or {}
    text = data.get('text', '')
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = 'positive'
    elif polarity < -0.1:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return jsonify({'sentiment': sentiment, 'polarity': polarity})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
