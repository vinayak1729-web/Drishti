import RPi.GPIO as GPIO
import time
import subprocess

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for ultrasonic sensors
right_trig = 17
right_echo = 27
left_trig = 23
left_echo = 24
front_trig = 5
front_echo = 6
back_trig = 13
back_echo = 19

# Set GPIO direction (TRIG as OUTPUT, ECHO as INPUT)
GPIO.setup(right_trig, GPIO.OUT)
GPIO.setup(right_echo, GPIO.IN)
GPIO.setup(left_trig, GPIO.OUT)
GPIO.setup(left_echo, GPIO.IN)
GPIO.setup(front_trig, GPIO.OUT)
GPIO.setup(front_echo, GPIO.IN)
GPIO.setup(back_trig, GPIO.OUT)
GPIO.setup(back_echo, GPIO.IN)

# Function to measure distance from ultrasonic sensor
def measure_distance(trig_pin, echo_pin):
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)
    pulse_start = time.time()
    pulse_end = time.time()
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

# Function to speak using Google Assistant
def speak(text):
    subprocess.call(['python3', '-c', 'import google_speech; google_speech.google_tts(text)'])

try:
    while True:
        # Measure distances from ultrasonic sensors
        right_distance = measure_distance(right_trig, right_echo)
        left_distance = measure_distance(left_trig, left_echo)
        front_distance = measure_distance(front_trig, front_echo)
        back_distance = measure_distance(back_trig, back_echo)

        # Check for objects detected by sensors and speak appropriate message
        if right_distance < 30:
            speak("There is an object on the right at {} centimeters, sir. Go to the left.".format(right_distance))
        if left_distance < 30:
            speak("There is an object on the left at {} centimeters, sir. Go to the right.".format(left_distance))
        if front_distance < 30:
            speak("There is an object ahead at {} centimeters, sir. Stop or go back.".format(front_distance))
        if back_distance < 30:
            speak("There is an object behind at {} centimeters, sir. Stop or go ahead.".format(back_distance))

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
