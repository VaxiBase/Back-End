import requests
import pyrebase
from province import Province

class Api_data:

    BASE_URL = 'https://api.covid19tracker.ca/'
    BASE_URL_REPORTS = BASE_URL + 'reports/'
    BASE_URL_REPORTS_PROVINCE = BASE_URL_REPORTS + 'province/'

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

    def return_province_url(self,province_code):
        url = Api_data.BASE_URL_REPORTS_PROVINCE + province_code
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


    def data_ab(self):
        session = requests.Session()
        response = session.get(self.return_province_url('ab'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('AB')) * 100
        return Province('Alberta', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__

    def data_bc(self):
        session = requests.Session()
        response = session.get(self.return_province_url('bc'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('BC')) * 100
        return Province('British Columbia', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__

    def data_mb(self):
        session = requests.Session()
        response = session.get(self.return_province_url('mb'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('MB')) * 100
        return Province('Manitoba', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__

    def data_nb(self):
        session = requests.Session()
        response = session.get(self.return_province_url('nb'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('NB')) * 100
        return Province('New Brunswick', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__

    def data_nl(self):
        session = requests.Session()
        response = session.get(self.return_province_url('nl'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('NL')) * 100
        return Province('Newfoundland and Labrador', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__

    def data_ns(self):
        session = requests.Session()
        response = session.get(self.return_province_url('ns'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('NS')) * 100
        return Province('Nova Scotia', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__

    def data_nt(self):
        session = requests.Session()
        response = session.get(self.return_province_url('nt'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('NT')) * 100
        return Province('Northwest Territories', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__

    def data_nu(self):
        session = requests.Session()
        response = session.get(self.return_province_url('nu'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('NU')) * 100
        return Province('Nunavut', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__


    def data_on(self):
        session = requests.Session()
        response = session.get(self.return_province_url('on'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('ON')) * 100
        return Province('Ontario', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__

    def data_qc(self):
        session = requests.Session()
        response = session.get(self.return_province_url('qc'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('QC')) * 100
        return Province('Quebec', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__

    def data_pe(self):
        session = requests.Session()
        response = session.get(self.return_province_url('pe'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('PE')) * 100
        return Province('Prince Edward Island', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__
    def data_sk(self):
        session = requests.Session()
        response = session.get(self.return_province_url('sk'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('SK')) * 100
        return Province('Saskatchewan', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__
        
    def data_yt(self):
        session = requests.Session()
        response = session.get(self.return_province_url('yt'), params=None)
        str_dict = response.json()['data'][-2::][0]
        total_vax = (str_dict['total_vaccinated'] / self.population_province('YT')) * 100
        return Province('Yukon', str_dict['date'], total_vax, str_dict['total_vaccinations'], 
            str_dict['total_vaccinated'], str_dict['total_cases'], 
            str_dict['total_hospitalizations'], str_dict['total_fatalities']).__dict__
            
    def data_all_dict(self):
        data = {
            "AB": self.data_ab(),
            "BC": self.data_bc(),
            "MB": self.data_mb(),
            "NB": self.data_nb(),
            "NL": self.data_nl(),
            "NS": self.data_ns(),
            "NT": self.data_nt(),
            "NU": self.data_nu(),
            "ON": self.data_on(),
            "QC": self.data_qc(),
            "PE": self.data_pe(),
            "SK": self.data_sk(),
            "YT": self.data_yt()}
        return data

    def update_db(self):
        
        data = self.data_all_dict()

        self.db.child('province_data').update(data)


def main():
    api = Api_data()
    api.update_db()

if __name__ == "__main__":
    main()