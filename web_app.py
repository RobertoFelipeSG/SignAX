from flask import Flask
from flask import Flask, render_template
import datetime
import webbrowser

app = Flask(__name__)

#webbrowser.open('http://127.0.0.1:5000')  # Go to Web Server --> What is the IP of the host?

@app.route("/")
def main():
    return render_template('stim.html')#, **templateData)
    
@app.route("/StimName")
def stim():

    if stimName == 'rtDCS':
        actuator = rtDCS
    if stimName == 'tACS':
        actuator = tACS
        
    if action == "on":
        print('Stimulating')
    if action == "off":
        print('System is OFF')
        
    return render_template('stim.html')#, **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

