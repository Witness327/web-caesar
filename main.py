from flask import Flask,  request
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
        <form method="POST">
        <label for="rotation">Rotate by:</label>
        <input type="text" id="rotation" name="rot" value="0">
        <textarea type="text" name="text" >{0}</textarea>        
        <button type="submit">Encrypt</button>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(encrypt())

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
   
    rot = request.form['rot']
    rot = int(rot)
    
    encryption = rotate_string(text,rot)

    return form.format('<h1>' + encryption + '</h1>' + '<h1>' + str(rot) + ' is your encryption key</h1>')

app.run()