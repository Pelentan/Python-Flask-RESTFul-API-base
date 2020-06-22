""" This is a template for all routes """
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

class RoutesCold(Resource):
    """ This is routes class running of a base endpoint for the module. Ex: http://endpoint.com/test_me/  
        The name of the class must be unique for the
        project and is used in the active_routes.json file. """
    
    romans = []

    def get(self):
        """ Home endpoint.  Returns base endpoints. """
        return {"Romans": self.romans}, 200

    def post(self):
        """ Add a user if they aren't alread in the array. """
        if not request.is_json:
            return {"Bad info: ": True, "Sent: ": request.get_data().decode("utf-8")}, 400

        postit = request.get_json()
        ent_name = postit.get('user_id')

        if next(filter(lambda x: x['user_id'] == ent_name, self.romans), None) is not None:
            return {"Result:": f"{ent_name} Already entered", "In other words: ": "NOPE!"}, 444

        self.romans.append(postit)
        return postit

    def put(self):
        """ Update a user only if they already exist. """
        data = request.get_json()
        roman = next(filter(lambda r: r['user_id'] == data['user_id'], self.romans), None)
        if roman is None:
            return{"Invalid!!!!": f"User doesn't exists"}, 400
        else:
            roman.update(data)
            return self.romans

    def delete(self):
        """ DELETE Id to delete is passed in via POST """
        data = request.get_json()
        roman = next(filter(lambda r: r['user_id'] == data['user_id'], self.romans), None)
        if roman is None:
            return{"Invalid!!!!": f"User doesn't exists"}, 400
        else:
            roman.update(data)
            return self.romans

        return {"response": "This base endpoint does not allow DELETE"}


class RoutesHot(Resource):
    """ This is routes class _with_ slash-variables for the module. Ex: http://endpoint.com/test_me/slash_variable  
        The name of the class must be unique for the 
        project and is used in the active_routes.json file. """
    
    romans = []

    def get(self, user_id: str = ""):
        """ GET with a <string_var> """
        # next(filter(lambda x: x['name'] == name, romans), None)
        return {"User Id": user_id}, 200 if user_id else 404

    def post(self, user_id: str = ""):
        """ POST with a <string_var> """
        if not request.is_json:
            toga = request.get_data().decode("utf-8") 
            return {"Bad info: ": True, "Sent: ": toga}, 455
        
        # user_check = next(filter(lambda x: x['name'] == name, romans), None)
        postit = request.get_json()
        ent_name = postit.get('user_name')

        if next(filter(lambda x: x['user_name'] == ent_name, self.romans), None) is not None:
            return {"Result:": f"{ent_name} Already entered", "In other words: ": "NOPE!"}, 444

        self.romans.append(postit)
        return postit

    def put(self, user_id: str = ""):
        """ PUT with a <string_var> """
        data = request.get_json()
        roman = next(filter(lambda r: r['user_id'] == user_id, self.romans), None)

        if roman:
            roman.update(data)
            return self.romans
        else:
            return{"Invalid!!!!": f"User: {user_id} doesn't exists"}

    def delete(self, user_id: str = ""):
        """ DELETE with a <string_var> """
        print("delete me, delete me")
        return{"action": f"Deleted {user_id}!"}