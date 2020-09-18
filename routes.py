import os
from flask import Flask, request
from flask_cors import CORS
from speech import recive_audio
from nlu import sentiment_nlu
app=Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

#{
#    'car': (string)
#    'text': (string)
#    'audio':(file)
#}


@app.route("/mutipart/form-data", methods=["POST"])
def index():


    car = body['car'].lower().split()
    print(body)
    print(request.files['audio'])

    if  'audio' in request.files:
        text_audio = recive_audio(request.files['audio'])
        recommend = sentiment_nlu(text_audio, car)
        print(text_audio)
        return recommend
        
    
    elif 'text' in request.files
        recommend = sentiment_nlu(request.files['text'], car)
        print(body['text'])  
        return recommend 


def main():
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
