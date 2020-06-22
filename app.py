""" Flat module just used to start listeners for endpoints  """
import importlib
import json
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

# This file would actually be loaded in through a Kube or Swarm config, not an actual file in code.  Maybe.
routes_file = "./config/active_routes.json"

with open(routes_file) as file_data:
    route_data = json.load(file_data)

for class_name in route_data:
    datum = route_data[class_name]
    module = datum.get("file")
    datum['class'] = importlib.import_module(f"routes.{module}").__getattribute__(class_name)
    api.add_resource(datum['class'], datum['path'])

if __name__ == '__main__':
    app.run(debug=True)
