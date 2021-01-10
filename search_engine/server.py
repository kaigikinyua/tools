from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

#images route
#news route
#trending route
app.run()