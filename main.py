import requests
import pyrebase
from province import Province


class Api_data:
    BASE_URL = 'https://api.covid19tracker.ca/'
    URL_REPORTS = BASE_URL + 'reports/'
    URL_POPULATION = BASE_URL + 'provinces/'
    URL_REPORTS_PROVINCE = URL_REPORTS + 'province/'

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

    def __init__(self):
        self.population, self.map_province = self.get_population()

    def return_province_url(self, province_code):
        url = Api_data.URL_REPORTS_PROVINCE + province_code
        return (url)

    def get_population(self):
        sessionpop = requests.Session()

        responsepop = sessionpop.get(Api_data.URL_POPULATION, params=None)
        str_dictPopulation = responsepop.json()
        map_province = {}
        for index, province in enumerate(str_dictPopulation):
            map_province[province['code']] = index

        return str_dictPopulation, map_province

    def population_province(self, province_code):
        return (self.population[self.map_province[province_code]]['population'])

    def data_ab(self):
        session = requests.Session()
        response = session.get(self.return_province_url('ab'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('AB')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('AB')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Alberta', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_bc(self):
        session = requests.Session()
        response = session.get(self.return_province_url('bc'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('BC')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('BC')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('British Columbia', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_mb(self):
        session = requests.Session()
        response = session.get(self.return_province_url('mb'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('MB')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('MB')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Manitoba', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_nb(self):
        session = requests.Session()
        response = session.get(self.return_province_url('nb'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('NB')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('NB')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('New Brunswick', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_nl(self):
        session = requests.Session()
        response = session.get(self.return_province_url('nl'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('NL')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('NL')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Newfoundland and Labrador', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_ns(self):
        session = requests.Session()
        response = session.get(self.return_province_url('ns'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('NS')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('NS')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Nova Scotia', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_nt(self):
        session = requests.Session()
        response = session.get(self.return_province_url('nt'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('NT')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('NT')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Northwest Territories', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_nu(self):
        session = requests.Session()
        response = session.get(self.return_province_url('nu'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('NU')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('NU')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Nunavut', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_on(self):
        session = requests.Session()
        response = session.get(self.return_province_url('on'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('ON')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('ON')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Ontario', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_qc(self):
        session = requests.Session()
        response = session.get(self.return_province_url('qc'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('QC')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('QC')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Quebec', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_pe(self):
        session = requests.Session()
        response = session.get(self.return_province_url('pe'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('PE')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('PE')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Prince Edward Island', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_sk(self):
        session = requests.Session()
        response = session.get(self.return_province_url('sk'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('SK')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('SK')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Saskatchewan', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

    def data_yt(self):
        session = requests.Session()
        response = session.get(self.return_province_url('yt'), params=None)
        str_dict = response.json()['data'][-1::][0]
        vax_percent = float("{:.2f}".format((str_dict['total_vaccinated'] / self.population_province('YT')) * 100))
        booster_percent = float("{:.2f}".format((str_dict['total_boosters_1'] / self.population_province('YT')) * 100))
        date = str_dict['date']
        total_vaccinations = str_dict['total_vaccinations']
        total_hosp = str_dict['total_hospitalizations']
        total_cases = str_dict['total_cases']
        total_fatalities = str_dict['total_fatalities']
        return Province('Yukon', date, vax_percent, booster_percent, total_vaccinations, total_fatalities, total_hosp, total_cases).__dict__

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

    print("main.py run")

if __name__ == "__main__":
    main()




