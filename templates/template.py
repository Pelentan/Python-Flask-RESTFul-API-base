"""  Still working out what I want this to be exactly """

class Template:
    """ Still not sure, but a class isn't wrong so... """

    def __init__(self):
        # Don't taze me bro.  This is probably going to be moved out into a config file.  It's just 
        # convenient to have it here for now.
        self.method_errors = {
            "get": {
                "error_code": 405,
                "error_mssg_text": "You can't GET sh@t!",
                "error_template": ""
            },
            "post": {
                "error_code": 405,
                "error_mssg_text": "You can't POST sh@t!",
                "error_template": ""
            },
            "put": {
                "error_code": 405,
                "error_mssg_text": "You can't PUT sh@t!",
                "error_template": ""
            },
            "delete": {
                "error_code": 405,
                "error_mssg_text": "You can't DELETE sh@t!",
                "error_template": ""
            },
            "default": {
                "error_code": 404,
                "error_mssg_text": "There be nothing here!",
                "error_template": ""
            }
        }

    def getTemplate(self, template_requested: str = ''):
        """ This would retrieve any HTML template needed to be passed back.  """
        pass

    def methodError(self, err_type: str = 'default'):
        """ Might make this more generic.  """
        data = self.method_errors.get(err_type.lower())
        err_return = data if data is not None else self.method_errors.get('default')
        return self.__processTemplate(err_return)

    def __processTemplate(self, template_data: dict):
        """ Idea is sperate processing of the info to respond with """
        return template_data
