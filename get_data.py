from datetime import datetime
from bs4 import BeautifulSoup

import requests
import logging
import json

async def get_current_data(hass, language="eng"):
  try:
    url = f"https://www.churchofjesuschrist.org/my-home?lang={language}"
    return await hass.async_add_executor_job(get_current_lesson, url)
  except Exception as err:
    logging.getLogger(__name__).error("Scraping error: %s", err)
    return {}
  
  
def get_current_lesson(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    script = soup.find('script', string=lambda t: t and "__remixContext" in t)
    
    if not script:
        raise RuntimeError("Couldn't find window.ENV in any <script> tag")
    
    js = script.string
    key = "window.__remixContext"
    idx = js.find(key)
    if idx < 0:
        raise RuntimeError("Variable not found")
        
    eq = js.find("=", idx)
    start = js.find("{", eq)
    brace_level = 0
    for i, ch in enumerate(js[start:], start):
        if ch == "{":
            brace_level += 1
        elif ch == "}":
            brace_level -= 1
            if brace_level == 0:
                end = i
                break

    raw_obj = js[start:end+1]
    context = json.loads(raw_obj)
    
    return context