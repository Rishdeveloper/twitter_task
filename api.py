# app/api.py

from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load your data (make sure to specify the correct path)
data_path = 'D:\twitter\twitter-query-system\data\retweet_data.csv'
tweets_df = pd.read_csv(data_path)

@app.route('/tweets', methods=['GET'])
def get_tweets():
    term = request.args.get('term', '')
    filtered_tweets = tweets_df[tweets_df['content'].str.contains(term, na=False, case=False)]
    return jsonify(filtered_tweets.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
