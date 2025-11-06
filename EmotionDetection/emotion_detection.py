import requests

def emotion_detector(text_to_analyze):
    # Define the url, headers and input
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": { "text": text_to_analyze }}

    # Get the response
    response = requests.post(url, json = input_json, headers = headers)
    response_json = response.json()
    emotions = response_json["emotionPredictions"][0]["emotion"] # Extract the emotions dictionary
    emotion = max(emotions, key = emotions.get) # Filter the emotion with the highest value
    
    return emotion