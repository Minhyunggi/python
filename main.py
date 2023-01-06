from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_jobs

jobs = extract_jobs("python")
print(jobs)
