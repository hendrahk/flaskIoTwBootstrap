#import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
led = 14
bz = 15

ledSts = 0
BzSts = 0

#GPIO.setup(led, GPIO.OUT)
#GPIO.setup(bz, GPIO.OUT)
#GPIO.output(led, GPIO.LOW)
#GPIO.output(bz, GPIO.LOW)

@app.route("/")
def index():
    #ledSts = GPIO.input(led)
    #bzSts = GPIO.input(bz)
    
 #   templateData = {
 #       'led' : ledSts,
 #       'bz' : bzSts
 #       }
    return render_template('indexbs.html') #, **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    #if deviceName == 'led':
        #actuator = led
   # if deviceName == 'bz':
        #actuator = bz
    
  #  if action == "on":
        #GPIO.output(actuator, GPIO.HIGH)
   # if action == "off":
        #GPIO.output(actuator, GPIO.LOW)
        
  #  ledSts = GPIO.input(led)
   # bzSts = GPIO.input(bz)
    
  #  templateData = {
   #     'led' : ledSts,
   #     'bz' : bzSts
   #     }
    
    return render_template('kontrol.html') #**templateData)
@app.route('/monitor')
def monitor():
    return render_template('monitor.html')

@app.route('/kontrol')
def kontrol():
    return render_template('kontrol.html')


if __name__ == "__main__":
    app.run(port=8080)