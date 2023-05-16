from bs4 import BeautifulSoup
import requests
import re
import validators
from logger import get_logger
from urllib.parse import urlparse, quote, unquote

logger = get_logger(__name__)

class ContentModel:
    def __init__(self, url):
        if not url:
            raise ValueError("URL must be provided.")
        
        logger.info('Initializing with url: %s', url)
        self.url = unquote(url)
        self.text_content = None
        self.links = None        
        self.soap = None

    def _clean_text(self, text):
        # Remove leading and trailing whitespaces
        text = text.strip()
        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text)
        # Remove extra newlines
        text = re.sub(r'\n+', '\n', text)
        return text

    def get_url_content(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            logger.error('HTTP Error: %s', errh)
            return f"HTTP Error: {errh}"
        except requests.exceptions.ConnectionError as errc:
            logger.error('Error Connecting: %s', errc)
            return f"Error Connecting: {errc}"
        except requests.exceptions.Timeout as errt:
            logger.error('Timeout Error: %s', errt)
            return f"Timeout Error: {errt}"
        except requests.exceptions.RequestException as err:
            logger.error('Something went wrong: %s', err)
            return f"Something went wrong: {err}"

        self.soup = BeautifulSoup(response.content, 'html.parser')
        self.text_content = self._clean_text(self.soup.get_text())           
        
        content_bytes = len(response.content)
        logger.info('Successfully retrieved and cleaned content from: %s. Content size: %s bytes', self.url, content_bytes)
        return None
    
    def get_all_links(self):
        a_elements = self.soup.find_all('a')
        self.links = [
                a['href'] for a in a_elements 
                if 'href' in a.attrs and (a['href'].startswith('http://') or a['href'].startswith('https://'))
                and validators.url(a['href'])
            ]
        
        self.links = sorted(list(set(self.links)))
        link_count = len(self.links)
        logger.info('Successfully retrieved and cleaned all links from: %s. Total links: %s', self.url, link_count)
