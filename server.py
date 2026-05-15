from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emot_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"

    dominant_emotion = response['dominant_emotion']
    response.popitem()
    response_subset = response.copy()
    key, value = response_subset.popitem()
    last_item = {key: value}
    formatted_response = str(response_subset).strip("{}")
    formatted_last_item = str(last_item).strip("{}")
        
    return f"For the given statement, the system response is {formatted_response} and {formatted_last_item}. The dominant emotion is {dominant_emotion}"

@app.route('/')
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
