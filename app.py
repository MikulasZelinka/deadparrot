import sys
import logging

from flask import Flask, jsonify

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def index():
    return jsonify(
        response_type='in_channel',
        text='https://media1.giphy.com/media/2MmETUpDuWgCs/giphy.gif',
    )


if __name__ == '__main__':
    app.run()
