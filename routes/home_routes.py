from flask import Flask, request
from flask_restful import Resource, Api, reqparse

import templates.template as tp

class HomeRoutes(Resource):
    """ Class names for routes must be unique for application. """
    def __init__(self):
        self.template_engine = tp.Template()
    def get(self):     
        """ Home endpoint.  Returns base endpoints. """   
        endpoints = {
            "users": {
                "pattern": "/users(/<user_id>)",
                "allowed": "GET/POST/PUT/DELETE",
                "notes": ""
            }
        }
        return {"Homepage": True, "endpoints": endpoints}
        
    def post(self):
        """ For non-supported methods, my thought is not to return just a generic error page. 
            By having a programed response, you can include custom template error pages via json. """
        response = self.template_engine.methodError(request.method)
        return response, response.get('error_code')
        
    def put(self):
        """ For non-supported methods, my thought is not to return just a generic error page. 
            By having a programed response, you can include custom template error pages via json. """
        response = self.template_engine.methodError(request.method)
        return response, response.get('error_code')
        
    def delete(self):
        """ For non-supported methods, my thought is not to return just a generic error page. 
            By having a programed response, you can include custom template error pages via json. """
        response = self.template_engine.methodError(request.method)
        return response, response.get('error_code')