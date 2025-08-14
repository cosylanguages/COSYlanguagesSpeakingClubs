import requests
from bs4 import BeautifulSoup

def get_random_quote():
    """
    Scrapes a random quote from quotationspage.com.
    Returns a tuple of (quote, author).
    """
    url = 'https://www.quotationspage.com/random.php'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # The quotes are within 'dt' elements on this page
        quotes = soup.find_all('dt')

        if not quotes:
            return "Could not find a quote.", "Unknown"

        # We'll just take the first quote for now
        first_quote = quotes[0]
        quote_text = first_quote.a.get_text(strip=True)

        # The author is in the following 'dd' element
        author_dd = first_quote.find_next_sibling('dd')
        author_text = ""
        if author_dd:
            author_link = author_dd.find('b')
            if author_link:
                author_text = author_link.get_text(strip=True)

        return quote_text, author_text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        return "Could not fetch a quote at this time.", ""

if __name__ == '__main__':
    quote, author = get_random_quote()
    print(f'"{quote}" - {author}')
