from controllers.GenericController import GenericController
import requests
import json

class BibleController(GenericController):
    def get_votd(self):
        '''Gets the verse of the day and returns it in a dict'''
        return_value = {}
        
        url = "https://beta.ourmanna.com/api/v1/get?format=json&order=daily"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers, json={"key" : "value"})
        
        json_object = json.loads(response.text)
        
        return_value['text'] = json_object['verse']['details']['text']
        return_value['ref'] = json_object['verse']['details']['reference']
        return_value['ver'] = json_object['verse']['details']['version']
        return return_value