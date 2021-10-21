import requests
import json
import pyrebase
from firebase_admin import db


class Api_data:

    def api_request_province(self,province_code):

        url = 'https://api.covid19tracker.ca/vaccines/age-groups/province/'+province_code
        return(url)

    def population_province(self,province_code):
        sessionpop = requests.Session()
        urlpopulation = 'https://api.covid19tracker.ca/provinces'

        responsepop = sessionpop.get(urlpopulation, params=None)
        str_dictPopulation = responsepop.json()
        map_province = {}
        for index, province in enumerate(str_dictPopulation):
            map_province[province['code']] = index

        return(str_dictPopulation[map_province[province_code]]['population'])

    def data_ontario_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('on'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return((json_dict['Ontario_12plus']['full'] / self.population_province('ON')) * 100)

    def data_quebec_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('qc'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full'] / self.population_province('QC')) * 100)

    def data_alberta_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('ab'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full'] / self.population_province('AB')) * 100)

    def data_saskatoun_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('sk'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full'] / self.population_province('SK')) * 100)

    def data_colombie_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('bc'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return((json_dict['all_ages']['full'] / self.population_province('BC')) * 100)

    def data_nb_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('nb'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full'] / self.population_province('NB')) * 100)

    def data_nl_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('nl'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full']/self.population_province('NL'))*100)

    def data_nt_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('nt'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full']) / self.population_province('NT') * 100)

    def data_ns_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('ns'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full'] / self.population_province('NS')) * 100)

    def data_nu_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('nu'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full'] / self.population_province('NU')) * 100)

    def data_pe_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('pe'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full'] / self.population_province('PE')) * 100)

    def data_yt_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('yt'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full'] / self.population_province('YT')) * 100)

    def data_manitoba_api(self):
        session = requests.Session()
        response = session.get(self.api_request_province('mb'), params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return ((json_dict['all_ages']['full'] / self.population_province('MB')) * 100)

    def data_canada_api(self):
        session = requests.Session()
        url = 'https://api.covid19tracker.ca/vaccines/age-groups'
        response = session.get(url, params=None)
        str_dict = response.json()['data'][-1::][0]['data']
        json_dict = json.loads(str_dict)
        return (json_dict['all_ages']['full'])

    def dict_data(self):
        firebaseconfig = {
            "apiKey": "AIzaSyB-5Z1fz9rsfVhxCLcSQ1n4hfFdBhYmW1c",
            "authDomain": "vaxibase.firebaseapp.com",
            "databaseURL": "https://vaxibase-default-rtdb.firebaseio.com",
            "projectId": "vaxibase",
            "storageBucket": "vaxibase.appspot.com",
            "messagingSenderId": "725075045659",
            "appId": "1:725075045659:web:459aa09befdc1ae2f5b7be"}

        firebase = pyrebase.initialize_app(firebaseconfig)
        db = firebase.database()
        data = {"quebec": self.data_quebec_api(),
                "ontario": self.data_ontario_api(),
                "alberta": self.data_alberta_api(),
                "Britsh coloumbie": self.data_colombie_api(),
                "saskatchewan": self.data_saskatoun_api(),
                "Manitoba": self.data_manitoba_api(),
                "Yukon": self.data_yt_api(),
                "New Brunswick": self.data_nb_api(),
                "Newfoundland and Labrador": self.data_nl_api(),
                "Prince Edward Island": self.data_pe_api(),
                "Nunavute": self.data_nu_api(),
                "Nova Scotia": self.data_ns_api()}

        db.push(data)
        return data