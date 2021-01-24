from flask import Flask,render_template,jsonify

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    #return jsonify({"name":"Hello World"})

@app.route('/search/<sentence>',methods=['GET'])
def search(sentence):
    response=jsonify(message=sentence)
    #return jsonify({"name":"Hello World"})
    response.headers.add("Access-Control-Allow-Origin",'*')
    return response
#images route
#news route
#trending route
app.run()
app.debug=True
##
###