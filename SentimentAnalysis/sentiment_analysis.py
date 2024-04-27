'''lmao'''
import json
import requests

def sentiment_analyzer(text_to_analyse):
    '''lmao2'''
    url1= 'https://sn-watson-sentiment-bert.labs.skills.network/v1'
    url2= '/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    url= url1+url2
    header= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header,timeout=500)
    formatted_response= json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label="None"
        score="None"

    return {"label": label, "score": score}
