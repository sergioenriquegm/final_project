from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route to render the main web page
@app.route("/")
def render_index():
    return render_template("index.html")

# Route to read the input text and analyze the emotions
@app.route("/emotionDetector", methods = ["GET"])
def emotion_detector_web():
    # Calls the application to analyze the input text
    input_text = request.args.get("textToAnalyze")
    emotion = emotion_detector(input_text)
    # Format the result
    formatted_output = f'''For the given statement,
    the system response is 'anger' : {emotion.get('anger')}, 
    'disgust' : {emotion.get('disgust')}, 'fear' : {emotion.get('fear')}, 
    'joy' : {emotion.get('joy')}, 'sadness' : {emotion.get('sadness')}. 
    The dominant emotion is {emotion.get('dominant_emotion')}.
    '''
    return formatted_output

# Run the application
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)

