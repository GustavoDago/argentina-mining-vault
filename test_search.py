import urllib.request
import urllib.parse
import json
import ssl

def search_news():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # We are simulating news extraction or synthesis since I cannot access the internet properly
    # Using the prompt from the user as input.
    pass

if __name__ == "__main__":
    search_news()
