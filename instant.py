from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def instant():
    client = OpenAI()
    message = """
Vous êtes sur un site web qui vient d'être mis en production pour la première fois !
Répondez par une annonce enthousiaste pour accueillir les visiteurs sur le site, en expliquant qu'il est en ligne pour la première fois !
"""
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br/>")
    html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"
    return html