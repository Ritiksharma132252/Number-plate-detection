from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    # Runs your number_plate.py
    subprocess.run(["python", "number_plate.py"])
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
