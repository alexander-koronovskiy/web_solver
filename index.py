from flask import Flask, render_template, request, escape
import re

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, file=log, end='|')
        print(req.remote_addr, file=log, end='|')
        print(req.user_agent, file=log, end='|')
        print(res, file=log, end='|')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':

    # line = 'abc8.3 cde7 1 b 24'
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'

    start = -1
    lines = []
    for i in range(len(phrase)):
        if phrase[i] == '\n':
            lines.append(phrase[start+1:i-1])
            start = i
    lines.append(phrase[start + 1:len(phrase)])

    for i in lines:
        if (i == '\r') and (i.isEmpty()):
            lines.remove(i)

    nums = [re.findall(r'\d*\.\d+|\d+', lines[i]) for i in range(len(lines))]
    results = nums

    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)