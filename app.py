#### Building Url Dynamically
### Variable Rules and URL Building
## push test


from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@app.route('/humidity')
def humidity():
    return render_template('humidity.html')

@app.route('/voc')
def voc():
    return render_template('vocs.html')

if __name__ == '__main__':
    app.run(port=5001)