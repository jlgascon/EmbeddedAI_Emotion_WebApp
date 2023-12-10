import json
import requests

def emotion_detector(text_to_analyze):

    ''' Uses request and POST to pass analysis text to WATSON API endpoint for service'''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    #Send POST using requests and pass arguments
    response = requests.post(url=url, headers = header, json=myobj)

    #access the text format response
    response_text = response.text

    # use json fxns to convert response text to dictionary
    extractions = json.loads(response_text)

    # for simplicity, we will establish a var for the nested dict of emotions
    emote_dict = extractions['emotionPredictions'][0]['emotion']

    # dominant emotion found via max using nested dict
    dominant_emotion = max(emote_dict,key=emote_dict.get)

    # copy the emotions and add the dominant emotion to the new formatted dicitonary

    formatted_emotions = emote_dict.copy()
    formatted_emotions['dominant_emotion'] = dominant_emotion
    
    return formatted_emotions
