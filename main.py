import requests
import json
from firebase_admin import db

def api_request_province(province_code):

    url = 'https://api.covid19tracker.ca/vaccines/age-groups/province/'+province_code
    return(url)

def population_province(province_code):
    sessionpop = requests.Session()
    urlpopulation = 'https://api.covid19tracker.ca/provinces'

    responsepop = sessionpop.get(urlpopulation, params=None)
    str_dictPopulation = responsepop.json()
    map_province = {}
    for index, province in enumerate(str_dictPopulation):
        map_province[province['code']] = index

    return(str_dictPopulation[map_province[province_code]]['population'])

def data_ontario_api():
    session = requests.Session()
    response = session.get(api_request_province('on'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['Ontario_12plus']['full']/population_province('ON'))*100)

def data_quebec_api():
    session = requests.Session()
    response = session.get(api_request_province('qc'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('QC'))*100)

def data_alberta_api():
    session = requests.Session()
    response = session.get(api_request_province('ab'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('AB'))*100)

def data_saskatoun_api():
    session = requests.Session()
    response = session.get(api_request_province('sk'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('SK'))*100)

def data_colombie_api():
    session = requests.Session()
    response = session.get(api_request_province('bc'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('BC'))*100)

def data_nb_api():
    session = requests.Session()
    response = session.get(api_request_province('nb'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('NB'))*100)

def data_nl_api():
    session = requests.Session()
    response = session.get(api_request_province('nl'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('NL'))*100)

def data_nt_api():
    session = requests.Session()
    response = session.get(api_request_province('nt'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full'])/population_province('NT')*100)

def data_ns_api():
    session = requests.Session()
    response = session.get(api_request_province('ns'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('NS'))*100)

def data_nu_api():
    session = requests.Session()
    response = session.get(api_request_province('nu'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('NU'))*100)

def data_pe_api():
    session = requests.Session()
    response = session.get(api_request_province('pe'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('PE'))*100)

def data_yt_api():
    session = requests.Session()
    response = session.get(api_request_province('yt'), params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print((json_dict['all_ages']['full']/population_province('YT'))*100)

def data_canada_api():
    session = requests.Session()
    url = 'https://api.covid19tracker.ca/vaccines/age-groups'
    response = session.get(url, params=None)
    str_dict = response.json()['data'][-1::][0]['data']
    json_dict = json.loads(str_dict)
    print(json_dict['all_ages']['full'])

data_quebec_api()
data_ns_api()
data_nl_api()
data_nb_api()
data_ontario_api()
data_colombie_api()
data_saskatoun_api()
data_nu_api()
data_pe_api()
data_yt_api()
data_nt_api()
data_alberta_api()

