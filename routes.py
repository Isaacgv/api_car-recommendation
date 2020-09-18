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


    car = (request.form['car']).lower().split()

    
    if  'audio' in request.files:
        text_audio = recive_audio(request.files['audio'])
        recommend = sentiment_nlu(text_audio, car)
        print(text_audio)
        return recommend
        
    
    else:
        print(request.form['text'])  
        recommend = sentiment_nlu(request.form['text'], car)
        print(request.form['text'])  
        return recommend 
  

def main():
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
