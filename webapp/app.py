from flask import Flask, render_template, request, Response, url_for
import picamera
import os
import time
import glob

folder = os.path.join('/home/pi/webapp/static')

app = Flask(__name__)
app.config['upload'] = folder

@app.route('/') #main page

def index():
    
    return render_template('index.html')

@app.route('/media') #pictures page

def media():

    
    image_name = os.path.join(folder, 'selfie.jpg')


    return render_template('media.html', image = image_name)    
    



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
