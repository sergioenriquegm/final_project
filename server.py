from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")
@app.route("/emotionDetector", methods = ["GET"])
def emotion_detector_web():
