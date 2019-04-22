from flask import Flask
from flask_restful import Api
import resources

app = Flask(__name__)
api = Api(app, catch_all_404s=True)
api.add_resource(resources.Health, '/health/status')
api.add_resource(resources.Recommend, '/recommend/<string:_id>/<int:n>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
