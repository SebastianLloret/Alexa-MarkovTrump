import requests
session_attributes = {}

def build_speechlet_response(title, output, speech, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': "User: " + speech + "\nResponse: " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def lambda_handler(event, context):
    if event["request"]["intent"]["name"] == "GetMarkovIntent":
        markov = requests.get('https://markovifytrump.herokuapp.com/chat?size=tweet')
        markovDictionary = markov.json()
        response = "Quote: " + markovDictionary["content"]
        return build_response(session_attributes, build_speechlet_response("Log:", response, "Topic: N/A", "I'm sorry, I didn't catch that. Ask me what Trump thinks about.", True))
