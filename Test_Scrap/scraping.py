
from bs4 import BeautifulSoup
import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(id = "ResultsContainer")

print(results.prettify())