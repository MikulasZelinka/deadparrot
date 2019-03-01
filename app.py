import requests
from flask import Flask, jsonify
app = Flask(__name__)

SLACK_HOOK_URL = "https://hooks.slack.com/services/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"

@app.route('/')
def index():
    requests.post(SLACK_HOOK_URL, json={'text': 'https://media1.giphy.com/media/2MmETUpDuWgCs/giphy.gif'})
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
