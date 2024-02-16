from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
  
    with open('polygon.json') as f:
        polygon_data = json.load(f)
    return render_template('index.html', polygon_data=polygon_data)

if __name__ == '__main__':
    app.run(debug=True)