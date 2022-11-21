from flask import Flask, abort  # render_template

from utils import load_candidates
from config import PATH

data = load_candidates(PATH)

app = Flask(__name__)


@app.route('/')
def get_all() -> str:
    html = '<pre>\n'
    for candidate in data:
        html += f"Имя кандидата - {candidate['name']}\n" \
                f"Позиция кандидата - {candidate['position']}\n" \
                f"Навыки - {','.join(candidate['skills'].split(','))}\n\n"
    html += '</pre>'

    return html


@app.route('/candidates/<int:user_pk>')
def get_by_pk(user_pk):
    try:
        img_url = data[user_pk - 1]['picture']
        html = f'<img src="{img_url}"><br>\n'

        html += f"<pre>" \
                f"Имя кандидата - {data[user_pk - 1]['name']}\n" \
                f"Позиция кандидата - {data[user_pk - 1]['position']}\n" \
                f"Навыки - {','.join(data[user_pk - 1]['skills'].split(','))}\n" \
                f"</pre>"
    except (IndexError, TypeError):
        raise abort(404)

    return html


@app.route('/skills/<skill>')
def get_by_skill(skill):
    html = '<pre>\n'
    result = ''
    for candidate in data:
        if skill.lower() in candidate['skills'].lower():
            result += f"Имя кандидата - {candidate['name']}\n" \
                    f"Позиция кандидата - {candidate['position']}\n" \
                    f"Навыки - {','.join(candidate['skills'].split(','))}\n\n"
    if not result:
        result = 'No candidates found for this skill!'

    html += result + '</pre>'

    return html


@app.errorhandler(404)
def not_found(error):
    img_url = 'https://miro.medium.com/max/800/1*hFwwQAW45673VGKrMPE2qQ.png'
    html = f'<body style="background-color: black">' \
           f'<div align="center"><img src="{img_url}"></div></body>'

    return html


if __name__ == '__main__':
    app.run(debug=True)
