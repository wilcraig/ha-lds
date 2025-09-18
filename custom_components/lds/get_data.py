from datetime import datetime
from bs4 import BeautifulSoup
import re
import random

import requests
import logging
import json
import chardet

async def get_current_data(hass, language="eng"):
  try:
    url = f"https://www.churchofjesuschrist.org/my-home?lang={language}"
    data = await hass.async_add_executor_job(get_current_lesson, url)

    # Add inspirational picture quote
    inspirational_quote = await hass.async_add_executor_job(get_inspirational_picture_quote, language)
    if inspirational_quote:
      data["inspirational_picture_quote"] = inspirational_quote

    return data
  except Exception as err:
    logging.getLogger(__name__).error("Scraping error: %s", err)
    return {}


def get_current_lesson(url):
    response = requests.get(url)
    response.encoding = chardet.detect(response.content)["encoding"]
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


def get_inspirational_picture_quote(language="eng"):
    """Get a random inspirational picture quote from the Church's collection."""
    try:
        url = f"https://www.churchofjesuschrist.org/media/collection/inspirational-picture-quotes-by-verse-of-scripture-images?lang={language}"
        response = requests.get(url)
        response.encoding = chardet.detect(response.content)["encoding"]
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image links in the collection
        image_links = soup.find_all('a', href=re.compile(r'/media/image/.*'))

        if not image_links:
            return None

        # Select a random image
        random_link = random.choice(image_links)
        href = random_link.get('href')

        # Extract image title and alt text
        img_tag = random_link.find('img')
        if img_tag:
            title = img_tag.get('alt', 'Inspirational Quote')
            # Build full URL
            full_url = f"https://www.churchofjesuschrist.org{href}"

            # Try to get the actual image URL
            try:
                img_response = requests.get(full_url)
                img_soup = BeautifulSoup(img_response.text, 'html.parser')

                # Look for the main image
                main_img = img_soup.find('img', class_='main-image') or img_soup.find('img', {'data-src': True}) or img_soup.find('img', src=True)
                if main_img:
                    img_src = main_img.get('data-src') or main_img.get('src')
                    if img_src and not img_src.startswith('http'):
                        img_src = f"https://www.churchofjesuschrist.org{img_src}"
                else:
                    img_src = None

            except:
                img_src = None

            return {
                "title": title,
                "page_url": full_url,
                "image_url": img_src,
                "collection_name": "Inspirational Picture Quotes by Scripture"
            }

        return None

    except Exception as err:
        logging.getLogger(__name__).error("Error fetching inspirational quote: %s", err)
        return None
