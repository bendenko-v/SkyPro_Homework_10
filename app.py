from flask import Flask, abort

from utils import load_candidates, get_all, get_by_pk, get_by_skill
from config import PATH

app = Flask(__name__)


@app.route('/')
def main_page() -> str:
    return get_all(data)


@app.route('/candidates/<int:user_pk>')
def candidate_page(user_pk):
    if 1 <= user_pk <= len(data):
        return get_by_pk(data[user_pk - 1])
    else:
        abort(404)


@app.route('/skills/<skill>')
def candidates_by_skill_page(skill):
    return get_by_skill(data, skill)


@app.errorhandler(404)
def not_found(error):
    img_url = 'https://miro.medium.com/max/800/1*hFwwQAW45673VGKrMPE2qQ.png'
    html = f'<body style="background-color: black">' \
           f'<div align="center"><img src="{img_url}"></div></body>'

    return html


data = load_candidates(PATH)

if not data:
    print("Error. Failed to load data from json file.")
else:
    app.run(debug=True)
