import requests

def translate(text, target_language):
    """
    Translate text to target language
    """
    url = 'https://translate.googleapis.com/translate_a/single'
    params = {
        'client': 'gtx',
        'sl': 'en',
        'tl': target_language,
        'dt': 't',
        'q': text
    }
    response = requests.get(url, params=params)
    return response.json()[0][0][0]

