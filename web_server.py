from flask import Flask, render_template
from flask import request
from database import Tableone
from database import db
from database import app
from selenium import webdriver
from bs4 import BeautifulSoup


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/coin',  methods = ['POST'])
def coin():
    if request.method == 'POST':
        name = request.form['name']
        url = 'https://coinmarketcap.com/currencies/'+ str(name) + "/news/" 
        driver = webdriver.Firefox()
        driver.get(url)
        page = driver.page_source
        soup = BeautifulSoup(page,'html.parser')
        
        news = []
        findAllNews = []
        findAllNews = soup.findAll('div', class_='sc-16r8icm-0 jKrmxw container')
        
        for news_item in findAllNews:
            if news_item.find('p', class_='sc-1eb5slv-0 svowul-3 ddtKCV') is not None:
                news.append(news_item.text)
      
        for p in news:
            new_row = Tableone(name, p)
            db.session.add(new_row)
            db.session.commit()
            return p


if __name__ == '__main__':
    app.run(debug=True)