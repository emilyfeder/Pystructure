import flask
from flask import json, url_for
from lemmatizer.lemmatokenizer import LemmaTokenizer
import pdb
from werkzeug import ImmutableDict

class FlaskWithHamlish(flask.Flask):
    jinja_options = ImmutableDict(
        extensions=['jinja2.ext.autoescape', 'jinja2.ext.with_', 'hamlish_jinja.HamlishExtension', 'hamlish_jinja.HamlishTagExtension']
    )

app = FlaskWithHamlish(__name__)
app.secret_key = '\xab\x15\xb3\xae\xf7h\xbaDXu6\x0e\xa5Be\x88\xeb\x01\x04\xc0/\xe6\xb9~\x92\x17\x85|#5\xd8'


@app.route('/')
def index():
    return flask.render_template('index.html.haml')

@app.route('/_lemma_tokenize', methods=['POST'])
def lemma_tokenize():
    data = flask.request.form['data']
    if data:
        result = LemmaTokenizer().lemma_tokenize(data)
        return flask.render_template('index.html.haml', result=result)
    else:
        flask.flash("Nothing submitted")
        return flask.redirect(url_for('index'))

def run_app():
    app.debug = True
    app.run()

