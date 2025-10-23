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
            url = f"https://www.churchofjesuschrist.org/my-home?lang={self.language}"
            response = await hass.async_add_executor_job(self._get_url, url)
            page_content = response.text

            # Look for JSON data in script tag
            script_start = page_content.find('window.__remixContext')
            if script_start != -1:
                script_start = page_content.find('{', script_start)
                script_end = page_content.find(';}', script_start)

                if script_start != -1 and script_end != -1:
                    json_str = page_content[script_start:script_end + 1]
                    data = json.loads(json_str)

                    # Look for Come Follow Me data which often contains scripture
                    cfm_data = data.get('loaderData', {}).get('routes/my-home/dashboard', {}).get('cfm', {})
                    if cfm_data:
                        title = cfm_data.get('title', '')
                        primary_meta = cfm_data.get('primaryMeta', '')
                        uri = cfm_data.get('uri', '')

                        # Create a scripture reference from CFM data
                        if title and primary_meta:
                            reference = f"{primary_meta} - {title}"
                            scripture_url = f"https://www.churchofjesuschrist.org{uri}" if uri else url

                            return {
                                "text": f"This week's Come Follow Me study: {title}",
                                "reference": reference,
                                "url": scripture_url,
                                "date": datetime.now().strftime("%Y-%m-%d")
                            }

                    # Look for prophetic messages that might contain scripture quotes
                    prophetic_data = data.get('loaderData', {}).get('routes/my-home/dashboard', {}).get('propheticMessages', {}).get('items', [])
                    if prophetic_data:
                        item = prophetic_data[0]
                        title = item.get('title', '')
                        description = item.get('description', '')
                        link_url = item.get('link', {}).get('linkUrl', '')

                        if title and description:
                            return {
                                "text": description[:300] + "..." if len(description) > 300 else description,
                                "reference": title,
                                "url": link_url if link_url.startswith('http') else url,
                                "date": datetime.now().strftime("%Y-%m-%d")
                            }

                    # Look for featured content that might contain scripture
                    featured_data = data.get('loaderData', {}).get('routes/my-home/dashboard', {}).get('moreFeatures', {}).get('items', [])
                    for item in featured_data:
                        description = item.get('description', '')
                        title = item.get('title', '')
                        link_url = item.get('link', {}).get('linkUrl', '')

                        # Look for scripture-related content
                        if any(keyword in description.lower() for keyword in ['scripture', 'verse', 'doctrine', 'covenants', 'book of mormon']):
                            return {
                                "text": description[:300] + "..." if len(description) > 300 else description,
                                "reference": title,
                                "url": link_url if link_url.startswith('http') else url,
                                "date": datetime.now().strftime("%Y-%m-%d")
                            }

        except Exception as err:
            _LOGGER.warning("Error fetching daily scripture: %s", err)

        # Fallback scripture
        return self._get_fallback_scripture()

    async def get_daily_quote(self, hass):
        """Get an inspirational quote from church leaders."""
        try:
            url = f"https://www.churchofjesuschrist.org/my-home?lang={self.language}"
            response = await hass.async_add_executor_job(self._get_url, url)
            page_content = response.text

            # Look for JSON data in script tag
            script_start = page_content.find('window.__remixContext')
            if script_start != -1:
                script_start = page_content.find('{', script_start)
                script_end = page_content.find(';}', script_start)

                if script_start != -1 and script_end != -1:
                    json_str = page_content[script_start:script_end + 1]
                    data = json.loads(json_str)

                    # Look for "Quote of the Day" data
                    widgets_data = data.get('loaderData', {}).get('routes/my-home/dashboard', {})

                    # Look in prophetic messages first
                    prophetic_data = widgets_data.get('propheticMessages', {}).get('items', [])
                    if prophetic_data:
                        item = prophetic_data[0]
                        title = item.get('title', '')
                        description = item.get('description', '')
                        link_url = item.get('link', {}).get('linkUrl', '')

                        if description and title:
                            return {
                                "text": description,
                                "author": "Church Leader",
                                "source": title,
                                "url": link_url if link_url.startswith('http') else url,
                                "date": datetime.now().strftime("%Y-%m-%d")
                            }

                    # Look in featured content for quotes
                    featured_data = widgets_data.get('moreFeatures', {}).get('items', [])
                    for item in featured_data:
                        description = item.get('description', '')
                        title = item.get('title', '')
                        pretitle = item.get('pretitle', '')
                        link_url = item.get('link', {}).get('linkUrl', '')

                        # Look for quote-like content
                        if description and any(keyword in description.lower() for keyword in ['"', 'said', 'teach', 'testament', 'faith', 'hope', 'love']):
                            author = "Church Leader"
                            source = pretitle if pretitle else "The Church of Jesus Christ of Latter-day Saints"

                            # Try to determine author from title or content
                            if 'president' in title.lower() or 'elder' in title.lower():
                                author = title
                                source = "General Conference"
                            elif 'conference' in pretitle.lower():
                                source = "General Conference"
                            elif 'liahona' in pretitle.lower():
                                source = "Liahona Magazine"

                            return {
                                "text": description,
                                "author": author,
                                "source": source,
                                "url": link_url if link_url.startswith('http') else url,
                                "date": datetime.now().strftime("%Y-%m-%d")
                            }

                    # Look in news items for inspirational content
                    news_data = widgets_data.get('newsroom', {}).get('newsItems', [])
                    for item in news_data:
                        description = item.get('description', '')
                        title = item.get('title', '')
                        link_url = item.get('link', {}).get('linkUrl', '')

                        # Look for inspiring news content
                        if description and len(description) > 50 and len(description) < 400:
                            return {
                                "text": description,
                                "author": "Church Newsroom",
                                "source": "Church News",
                                "url": link_url if link_url.startswith('http') else url,
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

    async def get_church_newsroom_headlines(self, hass, limit=5):
        """Get church newsroom headlines with images and links."""
        try:
            url = f"https://www.churchofjesuschrist.org/my-home?lang={self.language}"
            response = await hass.async_add_executor_job(self._get_url, url)
            page_content = response.text

            # Look for JSON data in script tag
            script_start = page_content.find('window.__remixContext')
            if script_start != -1:
                script_start = page_content.find('{', script_start)
                script_end = page_content.find(';}', script_start)

                if script_start != -1 and script_end != -1:
                    json_str = page_content[script_start:script_end + 1]
                    data = json.loads(json_str)

                    # Extract newsroom data
                    widgets_data = data.get('loaderData', {}).get('routes/my-home/dashboard', {})
                    newsroom_data = widgets_data.get('newsroom', {})
                    news_items = newsroom_data.get('newsItems', [])

                    headlines = []
                    for item in news_items[:limit]:
                        title = item.get('title', '')
                        description = item.get('description', '')
                        link_url = item.get('link', {}).get('linkUrl', '')
                        image_url = item.get('imageUrl', '')
                        publish_date = item.get('publishDate', '')

                        # Make sure URLs are absolute
                        if link_url and not link_url.startswith('http'):
                            link_url = f"https://www.churchofjesuschrist.org{link_url}"
                        if image_url and not image_url.startswith('http'):
                            image_url = f"https://www.churchofjesuschrist.org{image_url}"

                        if title:
                            headlines.append({
                                "title": title,
                                "description": description,
                                "link_url": link_url,
                                "image_url": image_url,
                                "publish_date": publish_date,
                                "fetched_date": datetime.now().strftime("%Y-%m-%d")
                            })

                    return headlines

        except Exception as err:
            _LOGGER.warning("Error fetching church newsroom headlines: %s", err)

        return []

    async def get_featured_content(self, hass, limit=5):
        """Get featured content with titles, links, and images."""
        try:
            url = f"https://www.churchofjesuschrist.org/my-home?lang={self.language}"
            response = await hass.async_add_executor_job(self._get_url, url)
            page_content = response.text

            # Look for JSON data in script tag
            script_start = page_content.find('window.__remixContext')
            if script_start != -1:
                script_start = page_content.find('{', script_start)
                script_end = page_content.find(';}', script_start)

                if script_start != -1 and script_end != -1:
                    json_str = page_content[script_start:script_end + 1]
                    data = json.loads(json_str)

                    # Extract featured content data
                    widgets_data = data.get('loaderData', {}).get('routes/my-home/dashboard', {})
                    featured_data = widgets_data.get('moreFeatures', {}).get('items', [])

                    featured_items = []
                    for item in featured_data[:limit]:
                        title = item.get('title', '')
                        description = item.get('description', '')
                        pretitle = item.get('pretitle', '')
                        link_url = item.get('link', {}).get('linkUrl', '')
                        image_url = item.get('imageUrl', '')

                        # Make sure URLs are absolute
                        if link_url and not link_url.startswith('http'):
                            link_url = f"https://www.churchofjesuschrist.org{link_url}"
                        if image_url and not image_url.startswith('http'):
                            image_url = f"https://www.churchofjesuschrist.org{image_url}"

                        if title:
                            featured_items.append({
                                "title": title,
                                "description": description,
                                "pretitle": pretitle,
                                "link_url": link_url,
                                "image_url": image_url,
                                "fetched_date": datetime.now().strftime("%Y-%m-%d")
                            })

                    return featured_items

        except Exception as err:
            _LOGGER.warning("Error fetching featured content: %s", err)

        return []

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
    newsroom_headlines = await fetcher.get_church_newsroom_headlines(hass)
    featured_content = await fetcher.get_featured_content(hass)

    return {
        "scripture": scripture,
        "quote": quote,
        "come_follow_me": come_follow_me,
        "inspirational": inspirational,
        "newsroom_headlines": newsroom_headlines,
        "featured_content": featured_content,
        "language": language,
        "last_updated": datetime.now().isoformat()
    }
