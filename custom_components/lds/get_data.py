"""Data fetching for LDS integration."""
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
import re
import random
import requests
import logging
import json

_LOGGER = logging.getLogger(__name__)

class LDSDataFetcher:
    """Class to handle fetching various LDS content."""

    def __init__(self, language="eng"):
        self.language = language
        self.session = requests.Session()
        # Set a user agent to avoid blocking
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; Home Assistant LDS Integration)'
        })

    async def get_daily_scripture(self, hass):
        """Get the daily scripture from the church website."""
        try:
            url = f"https://www.churchofjesuschrist.org/study/scriptures"
            response = await hass.async_add_executor_job(self._get_url, url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for featured scripture or daily reading
            scripture_element = soup.find('div', class_='featured-content') or soup.find('div', class_='daily-scripture')

            if scripture_element:
                text = scripture_element.get_text(strip=True)
                # Try to extract reference
                reference_element = scripture_element.find('cite') or scripture_element.find('span', class_='reference')
                reference = reference_element.get_text(strip=True) if reference_element else "Scripture of the Day"

                return {
                    "text": text,
                    "reference": reference,
                    "url": url,
                    "date": datetime.now().strftime("%Y-%m-%d")
                }
        except Exception as err:
            _LOGGER.warning("Error fetching daily scripture: %s", err)

        # Fallback scripture
        return self._get_fallback_scripture()

    async def get_daily_quote(self, hass):
        """Get an inspirational quote from church leaders."""
        try:
            # Try to get quotes from general conference talks
            url = f"https://www.churchofjesuschrist.org/study/general-conference"
            response = await hass.async_add_executor_job(self._get_url, url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for featured quotes or talks
            quote_elements = soup.find_all('blockquote') or soup.find_all('div', class_='quote')

            if quote_elements:
                quote_element = random.choice(quote_elements)
                quote_text = quote_element.get_text(strip=True)

                # Try to find author nearby
                author_element = (quote_element.find_next('cite') or
                                quote_element.find_previous('h3') or
                                quote_element.find_parent().find('h3'))

                author = author_element.get_text(strip=True) if author_element else "Church Leader"

                return {
                    "text": quote_text,
                    "author": author,
                    "source": "General Conference",
                    "url": url,
                    "date": datetime.now().strftime("%Y-%m-%d")
                }
        except Exception as err:
            _LOGGER.warning("Error fetching daily quote: %s", err)

        # Fallback quote
        return self._get_fallback_quote()

    async def get_come_follow_me(self, hass):
        """Get current Come Follow Me lesson information."""
        try:
            url = f"https://www.churchofjesuschrist.org/study/come-follow-me"
            response = await hass.async_add_executor_job(self._get_url, url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for current lesson
            current_lesson = soup.find('div', class_='current-lesson') or soup.find('div', class_='featured-lesson')

            if current_lesson:
                title_element = current_lesson.find('h1') or current_lesson.find('h2') or current_lesson.find('h3')
                title = title_element.get_text(strip=True) if title_element else "Current Lesson"

                # Get lesson dates
                date_element = current_lesson.find('time') or current_lesson.find('span', class_='date')
                lesson_date = date_element.get_text(strip=True) if date_element else ""

                # Get reading reference
                reading_element = current_lesson.find('cite') or current_lesson.find('span', class_='reference')
                reading = reading_element.get_text(strip=True) if reading_element else ""

                # Try to get lesson URL
                link_element = current_lesson.find('a')
                lesson_url = link_element.get('href') if link_element else url
                if lesson_url.startswith('/'):
                    lesson_url = f"https://www.churchofjesuschrist.org{lesson_url}"

                return {
                    "title": title,
                    "reading": reading,
                    "date_range": lesson_date,
                    "url": lesson_url,
                    "fetched_date": datetime.now().strftime("%Y-%m-%d")
                }
        except Exception as err:
            _LOGGER.warning("Error fetching Come Follow Me: %s", err)

        # Fallback lesson info
        return self._get_fallback_come_follow_me()

    async def get_inspirational_image(self, hass):
        """Get an inspirational image with quote."""
        try:
            url = f"https://www.churchofjesuschrist.org/media/collection/inspirational-picture-quotes-by-verse-of-scripture-images"
            response = await hass.async_add_executor_job(self._get_url, url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find image links
            image_links = soup.find_all('a', href=re.compile(r'/media/image/'))

            if image_links:
                random_link = random.choice(image_links)
                img_tag = random_link.find('img')

                if img_tag:
                    alt_text = img_tag.get('alt', 'Inspirational Quote')
                    img_src = img_tag.get('src') or img_tag.get('data-src')

                    if img_src and not img_src.startswith('http'):
                        img_src = f"https://www.churchofjesuschrist.org{img_src}"

                    page_url = random_link.get('href')
                    if page_url.startswith('/'):
                        page_url = f"https://www.churchofjesuschrist.org{page_url}"

                    return {
                        "title": alt_text,
                        "image_url": img_src,
                        "page_url": page_url,
                        "collection": "Inspirational Picture Quotes",
                        "date": datetime.now().strftime("%Y-%m-%d")
                    }
        except Exception as err:
            _LOGGER.warning("Error fetching inspirational image: %s", err)

        # Return basic info if image fetch fails
        return {
            "title": "Inspirational Quote",
            "image_url": None,
            "page_url": "https://www.churchofjesuschrist.org",
            "collection": "Church Media",
            "date": datetime.now().strftime("%Y-%m-%d")
        }

    def _get_url(self, url):
        """Get URL content with error handling."""
        response = self.session.get(url, timeout=30)
        response.raise_for_status()
        return response

    def _get_fallback_scripture(self):
        """Return a fallback scripture when fetching fails."""
        fallback_scriptures = [
            {
                "text": "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.",
                "reference": "John 3:16",
                "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/3.16",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "text": "Be still, and know that I am God: I will be exalted among the heathen, I will be exalted in the earth.",
                "reference": "Psalm 46:10",
                "url": "https://www.churchofjesuschrist.org/study/scriptures/ot/ps/46.10",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "text": "Trust in the Lord with all thine heart; and lean not unto thine own understanding.",
                "reference": "Proverbs 3:5",
                "url": "https://www.churchofjesuschrist.org/study/scriptures/ot/prov/3.5",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        ]
        return random.choice(fallback_scriptures)

    def _get_fallback_quote(self):
        """Return a fallback quote when fetching fails."""
        fallback_quotes = [
            {
                "text": "Faith is not to have a perfect knowledge of things; therefore if ye have faith ye hope for things which are not seen, which are true.",
                "author": "Alma",
                "source": "Book of Mormon",
                "url": "https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/32.21",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "text": "The worth of souls is great in the sight of God.",
                "author": "Jesus Christ",
                "source": "Doctrine and Covenants",
                "url": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/18.10",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "text": "If any of you lack wisdom, let him ask of God, that giveth to all men liberally.",
                "author": "James",
                "source": "Bible",
                "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/james/1.5",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        ]
        return random.choice(fallback_quotes)

    def _get_fallback_come_follow_me(self):
        """Return fallback Come Follow Me info."""
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)

        return {
            "title": "Come, Follow Me",
            "reading": "Current Week's Study",
            "date_range": f"{week_start.strftime('%b %d')} - {week_end.strftime('%b %d, %Y')}",
            "url": "https://www.churchofjesuschrist.org/study/come-follow-me",
            "fetched_date": datetime.now().strftime("%Y-%m-%d")
        }


# Legacy compatibility functions
async def get_current_data(hass, language="eng"):
    """Legacy function for backward compatibility."""
    fetcher = LDSDataFetcher(language)

    # Get all data types
    scripture = await fetcher.get_daily_scripture(hass)
    quote = await fetcher.get_daily_quote(hass)
    come_follow_me = await fetcher.get_come_follow_me(hass)
    inspirational = await fetcher.get_inspirational_image(hass)

    return {
        "scripture": scripture,
        "quote": quote,
        "come_follow_me": come_follow_me,
        "inspirational": inspirational,
        "language": language,
        "last_updated": datetime.now().isoformat()
    }
