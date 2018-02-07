import PyQt5
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import sys
import time
from bs4 import BeautifulSoup


class Render(QWebEnginePage):
    def __init__(self, urls, cb):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.urls = urls
        self.cb = cb
        self.crawl()
        self.app.exec_()

    def crawl(self):
        if self.urls:
            #             url = self.urls.pop(0)
            url = self.urls
            print('Downloading', url)
            self.load(QUrl(url))
        else:
            self.app.quit()

    def _loadFinished(self, result):
        try:
            url = 'https://remitano.com/my'
            self.html = self.toHtml(self.Callable)
        except:
            print('toHTML failed')
            self.app.quit()

    def Callable(self, html_str):
        try:
            self.html = html_str
            html = self.html
            self.cb(html)
            time.sleep(20) #20 second
            self.crawl()
        except:
            print('Scrape failed2')
            self.app.quit()

def scrape(html):
    print('start scraping')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.findAll('strong', {'class': 'text-success ng-binding'})
    print(a[0].text)
    b = soup.findAll('strong', {'class': 'text-danger ng-binding'})
    print(b[0].text)
    print()

if __name__ == "__main__":
	urls = 'https://remitano.com/my'

	try:
		r = Render(urls, cb=scrape)
	except:
		r.app.quit()