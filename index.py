from flask import Flask, render_template, request, escape
import solver as s

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, file=log, end='|')
        print(req.remote_addr, file=log, end='|')
        print(req.user_agent, file=log, end='|')
        print(res, file=log, end='|')


@app.route('/lin_solve', methods=['POST'])
def do_linear() -> 'html':

    phrase = request.form['phrase']
    title = 'Here are your results:'
    results = s.put_matrix(phrase)

    log_request(request, results)
    return render_template('linear/results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_results=results,)


@app.route('/diff_solve', methods=['POST'])
def do_differential() -> 'html':

    phrase = request.form['phrase']
    title = 'Here are your results:'
    results = s.put_matrix(phrase)

    log_request(request, results)
    return render_template('differential/results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_results=results,)


@app.route('/')
@app.route('/index')
def title_page() -> 'html':
    return render_template('title.html',
                           the_title='Welcome to WebSolver')


@app.route('/linear')
def lin_page() -> 'html':
    return render_template('linear/page.html',
                           the_title='Solver of linear equation pre-alpha version')


@app.route('/differential')
def diff_page() -> 'html':
    return render_template('differential/page.html',
                           the_title='Solver of differential equation pre-alpha version')


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)
