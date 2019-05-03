from flask import Flask
import newscraper
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/headlines')
def getHeadlines():
	return newscraper.getAllHeadlines()

@app.route("/headlines/<source>")
def getHeadlineFromSource(source):
    #source = request.view_args['source']
    print(source)
    return newscraper.getByType(source)



if __name__ == '__main__':
    app.run()

