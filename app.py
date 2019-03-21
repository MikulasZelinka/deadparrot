import logging
import random
import sys
import uuid

from flask import Flask, jsonify, request

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

GIFZ = {
    'aperol': 'https://media2.giphy.com/media/dSY9GgU0fWS8o/giphy.gif',
    'parrot': 'https://media1.giphy.com/media/2MmETUpDuWgCs/giphy.gif',
    'spam': 'https://media1.giphy.com/media/RI4LTRjrVJhTskGtrb/giphy.gif',
    'wound': 'https://media3.giphy.com/media/Tim0q7zolF3fa/giphy.gif',
    'invincible': 'https://media3.giphy.com/media/10M2ZnecwCMVGg/giphy.gif',
    'nudge': 'https://media3.giphy.com/media/13vPE0A3DPqOcg/giphy.gif',
    'walk': 'https://media2.giphy.com/media/RzKHvdYC3uds4/giphy.gif',
    'bastards': 'https://media1.giphy.com/media/tP2fZCu4K9Yac/giphy.gif',
    'different': 'https://media3.giphy.com/media/JLePNN9qrn4is/giphy.gif',
    'boo': 'https://media2.giphy.com/media/HFHTld1DUaLlu/giphy.gif',
    'interview': 'https://media0.giphy.com/media/wi9yHmX7Sztuw/giphy.gif',
    'inquisition': 'https://media0.giphy.com/media/y5W98cY6OCudO/giphy.gif',
    'grannies': 'https://media2.giphy.com/media/DdRljUx9yiZP2/giphy.gif',
    'oui': 'https://i.pinimg.com/originals/af/98/59/af985985493d2763b248fa01001ecd78.gif'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    form_data = request.form
    image_url = GIFZ.get(form_data.get('text', '').strip().lower(), None) 
    if not image_url:
        image_url = random.choice(list(GIFZ.values()))
    return jsonify(
        response_type='in_channel',
        text=f'{image_url}?lul={uuid.uuid4()}',
    )


if __name__ == '__main__':
    app.run()
