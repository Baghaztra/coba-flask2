from flask import Flask

app=Flask(__name__)
@app.route('/')
def home():
    return "hekko"
@app.route('/a')
def home():
    return "a"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)


