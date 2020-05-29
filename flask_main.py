from flask import Flask , request
import json
import sqlite3
import pymssql

# configuration
DATABASE = '/tmp/autosaving.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

def connect_db():
    conn = sqlite3.connect('autosaving.db')
    return conn

def connect_mssql():
    try :
        conn = pymssql.connect(server='127.0.0.1', user='sa', password='kuku1223!!', database='AutoSaving')
        print( "MSSQL Connect Success" )
        return conn
    except :
        print( "MSSQL Connect Failure" )
        return None


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/setinfo' , methods=['POST'])
def show_Set_Information():
    maybe_json = request.get_json(silent=True,cache=False)
    if (maybe_json) :
        strjson = json.dumps(maybe_json,ensure_ascii=False)
        parserJson = json.loads(strjson)
#        for item in parserJson :
        try :
            print( "ID = " + parserJson['id'] )
            print( "Name = " + parserJson['name'] )
            print( "Type = " + str(parserJson['type']) )
        except :
            print( "Json Parser - 예외처리발생" )
        
    else :
        strjson = "no json"

    return strjson


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    SqlConn = connect_mssql()
    app.run()
    SqlConn.close()
#    app.run(host='0.0.0.0')