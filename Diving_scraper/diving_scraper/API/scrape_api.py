from flask import Flask
from flask_restful import Api, Resource
from tasks import run_spider
import os

app = Flask(__name__)
api = Api(app)

class ScrapeResource(Resource):
    def get(self):
        run_spider.delay()
        return {"message": "Scraping started successfully!"}

api.add_resource(ScrapeResource, '/scrape')

if __name__ == '__main__':
    app.run(debug=True)
