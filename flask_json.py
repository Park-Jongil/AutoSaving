from flask import Flask , request 
import json

app = Flask(__name__)

@app.route('/setinfo' , methods=['POST'])
def show_Set_Information():
    maybe_json = request.get_json(silent=True,cache=False)
    if (maybe_json) :
        thejson = json.dumps(maybe_json)
    else :
        thejson = "no json"
    print (thejson)
    return "Process End"


if __name__ == '__main__':
    app.run()