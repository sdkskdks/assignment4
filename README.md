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

# Usage examples
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
        
# Example
```python   
for Anchor in news:
    new_row = Tableone(name, Anchor)
    db.session.add(new_row)
    db.session.commit()
    return Anchor
# it will return Anchor and save in database!!!
```
