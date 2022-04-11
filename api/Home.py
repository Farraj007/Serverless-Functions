import requests



def handler(event, context):

    r = requests.get("https://www.youtube.com/")

    return {"content": r.text}
