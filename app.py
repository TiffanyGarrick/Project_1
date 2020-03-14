import os
from flask import Flask 
app = Flask(__name__)

@app.route("/")
def home():
    return 'My Home Page'
#@app.route("/<myname>")
#def hello(myname='person'):
#    return "Hello {0}".format(myname)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080) 
    #app.run(debug=True, host=os.getenv("IP",'0.0.0.0'),port=int(os.getenv("PORT", 8080) )) 

