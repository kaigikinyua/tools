from flask import Flask

import webbrowser
import os

app=Flask(__name__)


#save color
@app.route('/savecolor/<str:color>')
def saveColor(color):
    pass
#fetch color
#delete color

#add_to_template


def openPage(pagePath):
    url="file:///"+pagePath
    webbrowser.open(url)

if __name__=="__main__":
    cwd=os.getcwd()
    cwd=cwd+"/Assets/index.html"
    openPage(cwd)
    app.run(debug=True)