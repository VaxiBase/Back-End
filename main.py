import requests
import pyrebase

class Api_data:

    BASE_URL = 'https://api.covid19tracker.ca/'
    BASE_URL_REPORTS = BASE_URL + 'reports/'
    BASE_URL_REPORTS_PROVINCE = BASE_URL_REPORTS + 'province/'

    def province_url(self,province_code):
        url = Api_data.BASE_URL_REPORTS_PROVINCE + province_code
        return(url)

    def population_province_api(self,province_code):
        sessionpop = requests.Session()
        urlpopulation = 'https://api.covid19tracker.ca/provinces'

        responsepop = sessionpop.get(urlpopulation, params=None)
        str_dictPopulation = responsepop.json()
        map_province = {}
        for index, province in enumerate(str_dictPopulation):
            map_province[province['code']] = index

        return(str_dictPopulation[map_province[province_code]]['population'])

    def data_on_api(self):
        session = requests.Session()
        response = session.get(self.province_url('qc'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('QC')) * 100)

    def data_qc_api(self):
        session = requests.Session()
        response = session.get(self.province_url('qc'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('QC')) * 100)

    def data_ab_api(self):
        session = requests.Session()
        response = session.get(self.province_url('ab'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('AB')) * 100)

    def data_sk_api(self):
        session = requests.Session()
        response = session.get(self.province_url('sk'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('SK')) * 100)

    def data_bc_api(self):
        session = requests.Session()
        response = session.get(self.province_url('bc'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return((str_dict['total_vaccinated'] / self.population_province_api('BC')) * 100)

    def data_nb_api(self):
        session = requests.Session()
        response = session.get(self.province_url('nb'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('NB')) * 100)

    def data_nl_api(self):
        session = requests.Session()
        response = session.get(self.province_url('nl'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated']/self.population_province_api('NL'))*100)

    def data_nt_api(self):
        session = requests.Session()
        response = session.get(self.province_url('nt'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated']) / self.population_province_api('NT') * 100)

    def data_ns_api(self):
        session = requests.Session()
        response = session.get(self.province_url('ns'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('NS')) * 100)

    def data_nu_api(self):
        session = requests.Session()
        response = session.get(self.province_url('nu'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('NU')) * 100)

    def data_pe_api(self):
        session = requests.Session()
        response = session.get(self.province_url('pe'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('PE')) * 100)

    def data_yt_api(self):
        session = requests.Session()
        response = session.get(self.province_url('yt'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('YT')) * 100)

    def data_mb_api(self):
        session = requests.Session()
        response = session.get(self.province_url('mb'), params=None)
        str_dict = response.json()['data'][-1::][0]
        return ((str_dict['total_vaccinated'] / self.population_province_api('MB')) * 100)

    def data_canada_api(self):
        session = requests.Session()
        url = Api_data.BASE_URL_REPORTS
        response = session.get(url, params=None)
        str_dict = response.json()['data'][-1::][0]
        return (str_dict['total_vaccinated'])

    def data_all_api(self):
        data = {
            "AB": self.data_ab_api(),
            "BC": self.data_bc_api(),
            "MB": self.data_mb_api(),
            "NB": self.data_nb_api(),
            "NL": self.data_nl_api(),
            "NS": self.data_ns_api(),
            "NT": self.data_nu_api(),
            "ON": self.data_on_api(),
            "QC": self.data_qc_api(),
            "PE": self.data_pe_api(),
            "SK": self.data_sk_api(),
            "YT": self.data_yt_api()}
        return data

    def update_db(self):
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

        data = self.data_all_api()

        db.child('province_data').update(data)


def main():
    api = Api_data()
    api.update_db()

if __name__ == "__main__":
    main()