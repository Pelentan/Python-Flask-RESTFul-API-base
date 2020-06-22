""" This provides a list of all inputs required by the application and handles verification"""
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

class InputHandler():
    __inputs = {
        "user_name": {
            "type": "str",
            "min-len": 3,
            "max-len": 42,
            "help": "Your user name.",
            "regex": ""
        },
        "email": {
            "type": "str",
            "min-len": 7,
            "max-len": 42,
            "help": "Your email.",
            "regex": ""
        },
        "first_name": {
            "type": "str",
            "min-len": 7,
            "max-len": 42,
            "help": "Your first name.",
            "regex": ""
        },
        "last_name": {
            "type": "str",
            "min-len": 7,
            "max-len": 42,
            "help": "Your last name.",
            "regex": ""
        }
    }

    def getInputs(self):
        return self.__inputs