from flask import Flask , request 
import json

app = Flask(__name__)

@app.route('/setinfo' , methods=['POST'])
def show_Set_Information():
    maybe_json = request.get_json(silent=True,cache=False)
    if (maybe_json) :
        strjson = json.dumps(maybe_json,ensure_ascii=False)
        datajson = json.loads(strjson)

        info = datajson['info']
        for i in info :
            print( i['id'] )
            print( i['name'] )

#        print( datajson )

    else :
        strjson = "no json"        

    return strjson

if __name__ == '__main__':
    app.run()