from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method = "Post">
        <label for="rot">Rotate By:</label>
        <input type = "text" name = "rot" value = "{0}" /><br>
        <textarea rows = "10" name = "text">{1}</textarea><br>
        <input type = "Submit" value = "Submit Query" />
      </form>
    </body>
</html>
"""    
@app.route("/")
def index():
    return form.format(0,'')

@app.route("/", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    mytext = request.form['text']
    return form.format(rotate,rotate_string(mytext,rotate)) 
    
    
app.run()