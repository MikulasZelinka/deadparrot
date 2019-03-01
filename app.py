from flask import Flask, jsonify
app = Flask(__name__)

SLACK_HOOK_URL = "https://hooks.slack.com/services/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"

@app.route('/')
def index():
    requests.post(SLACK_HOOK_URL, json={'text': ''})
    return jsonify(
        response_type='in_channel',
        text='https://media1.giphy.com/media/2MmETUpDuWgCs/giphy.gif',
    )


if __name__ == '__main__':
    app.run()
