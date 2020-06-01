from flask import Flask , request
from datetime import datetime
import json
import pymssql

# configuration
DATABASE = '/tmp/autosaving.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

def connect_mssql():
    try :
        conn = pymssql.connect(server='127.0.0.1', user='sa', password='kuku1223!!', database='AutoSaving')
        print( "MSSQL Connect Success" )
        return conn
    except :
        print( "MSSQL Connect Failure" )
        return None

def insert_CarStatus(TEL,CAR,GPS_X,GPS_Y,CurVolt,CarStatus,ProductName,ProdcutVersion):
    try :
        print( "TEL = " + TEL )
        print( "CAR = " + CAR )
        print( "GPS_X = " + str(GPS_X) )
        print( "GPS_Y = " + str(GPS_Y) )
        print( "CurVolt = " + str(CurVolt) )
        print( "CarStatus = " + str(CarStatus) )
        print( "ProductName = " + ProductName )
        print( "ProdcutVersion = " + ProdcutVersion )
        SqlConn = connect_mssql()
        cur = SqlConn.cursor()
        CheckTime = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
        sql_stmt = "INSERT INTO tbl_CarStatus(TEL,CAR,GPS_X,GPS_Y,CurVolt,CarStatus,ProductName,ProductVersion,CheckTime) "
#        sql_stmt = sql_stmt + "VALUES (%s,%s,%f,%f,%f,%d,%s,%s,%s) "
        sql_stmt = sql_stmt + "VALUES ('"+TEL+"','"+CAR+"',"+str(GPS_X)+","+str(GPS_Y)+","+str(CurVolt)+","+str(CarStatus)+",'"+ProductName+"','"+ProdcutVersion+"','"+CheckTime+"') "
        cur.execute( sql_stmt )
#        cur.execute( sql_stmt , (TEL,CAR,GPS_X,GPS_Y,CurVolt,CarStatus,ProductName,ProdcutVersion,CheckTime) )
        SqlConn.commit()
        SqlConn.close()
        print("MSSQL DB insert into CarStatus Success")
        return 1
    except :
        print("MSSQL DB insert into CarStatus Error")
        return 0


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/info.do' , methods=['POST'])
def show_Set_Information():
    maybe_json = request.get_json(silent=True,cache=False)
    if (maybe_json) :
        strjson = json.dumps(maybe_json,ensure_ascii=False)
        CarInfo = json.loads(strjson)
#        for item in parserJson :
        try :
            iRet = insert_CarStatus(CarInfo['TEL'],CarInfo['CAR'],float(CarInfo['CX']),float(CarInfo['CY']),float(CarInfo['CV']),int(CarInfo['CS']),CarInfo['PN'],CarInfo['PV'])
        except :
            print( "Json Parser - 예외처리발생" )
        
    else :
        strjson = "no json"

    return strjson + str(iRet)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    app.run()
#    app.run(host='0.0.0.0')