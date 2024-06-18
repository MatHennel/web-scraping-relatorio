import requests

API_KEY = open('API_KEY').read();
SEARCH_ENGINE_ID = open('SEARCH_ENGINE_ID').read();

search_query = 'BATERIA AUTOMOTIVA HELIAR PORTAO';

url = 'https://www.googleapis.com/customsearch/v1';

urlSite = "https://macbateriascuritiba.com.br";

cont = 0;

params = {
    'q' : search_query,
    'key' : API_KEY,
    'cx' : SEARCH_ENGINE_ID
};

response = requests.get(url, params=params)
results = response.json()['items']

for item in results:
    cont += 1;
    if urlSite in item['link']:
        break;

for item in results:
    print(item['link'])  
    
print(cont)
