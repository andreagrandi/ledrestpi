from flask import Flask
import RPi.GPIO as GPIO


app = Flask(__name__)


@app.route("/led/on/")
def led_on():
    GPIO.output(11, GPIO.HIGH)
    return "Led ON"


@app.route("/led/off/")
def led_off():
    GPIO.output(11, GPIO.LOW)
    return "Led OFF"


if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    app.run(host='0.0.0.0')
