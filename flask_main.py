from flask import Flask , request
import json
import sqlite3

# configuration
DATABASE = '/tmp/autosaving.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

def connect_db():
    conn = sqlite3.connect('autosaving.db')
    return conn

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/setinfo' , methods=['POST'])
def show_Set_Information():
    maybe_json = request.get_json(silent=True,cache=False)
    if (maybe_json) :
        thejson = json.dumps(maybe_json)
    else :
        thejson = "no json"
    print (thejson)
    return "Json Received"
#    return 'profile : ' + request.form.get('text','인자없음')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    connect_db()
#    init_db()
    app.run()
#    app.run(host='0.0.0.0')