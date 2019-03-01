from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data =
    {
        "text": "https://media1.giphy.com/media/2MmETUpDuWgCs/giphy.gif"
    }
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
