from datetime import datetime
from bs4 import BeautifulSoup

import requests
import logging

startString = (
  "/study/manual/come-follow-me-for-home-and-church-doctrine-and-covenants-2025/"
)

async def get_current_data(hass, language="eng", resource="Come, Follow Me"):
  try:
    # Map resource to actual URLs or endpoints
    url_header = f"https://www.churchofjesuschrist.org"
    resource_paths = {
      "Come, Follow Me": f"/study/manual/come-follow-me-for-home-and-church-doctrine-and-covenants-2025"
    }
    url_footer = f"?lang={language}"

    url = url_header + resource_paths.get(resource, "/study/scripures") + url_footer

    if resource == "Come, Follow Me":
      return await hass.async_add_executor_job(get_current_lesson, url)
  except Exception as err:
    logging.getLogger(__name__).error("Scraping error: %s", err)
    return {}

def get_current_lesson(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  today = datetime.now().date()

  lessons = soup.select(
    'a[href*="/study/manual/come-follow-me-for-home-and-church-doctrine-and-covenants-2025"]'
  )

  for a in lessons:
    href = a["href"]

    weekNumber = href[len(startString) : len(startString) + 2]
    if weekNumber.isdigit():
      weekNumberInt = int(weekNumber)
      try:
        week_num = datetime.now().isocalendar()[1]

        if week_num == weekNumberInt:
          dateRange = a.h6.get_text()
          title = a.h4.get_text()
          return {
            "dateRange": dateRange,
            "title": title,
            "url": f"https://www.churchofjesuschrist.org{href}",
          }
      except:
        continue
  return {"dateRange": "", "title": "No current lesson found", "url": ""}