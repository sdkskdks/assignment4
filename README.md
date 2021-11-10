# Web server with providing database

Made by: Abdumanap Bexultan, (SE-2012)

# Installing

Flask_SQLAlchemy==2.5.1
```bash
pip install sqlalchemy
```
Flask
```bash
pip install Flask
```
flaskr
```bash
pip install Flask
```
psycopg2
```bash
pip install psycopg2-binary
```
Selenium
```bash
pip install -U selenium
```

Beautifulsoup
```bash
pip install beautifulsoup4
```

### Downloading geckodriver

The geckodriver executable can be downloaded [here](https://github.com/SeleniumHQ/selenium/blob/trunk/py/docs/source/index.rst)

#### Python3 venv

Download the geckodriver executable from the above link and extract it to env/bin/ to make it accessible to only the virtual environment.

In your python code, you will now be able to do the following:
```bash
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://stackoverflow.com/")
```

#### Linux

If you would like to make it available system wide, download the geckodriver executable from the above link and extract it to `/usr/bin/` (or anything inside of your $PATH)

#### Windows

Note: *this needs a windows user to test and confirm*

Download geckodriver from the above link and extract it to `C:\Windows\System32\` (or anything inside your Path environment variable).
