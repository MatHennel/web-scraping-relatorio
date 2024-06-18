import requests
from bs4 import BeautifulSoup
from selenium import webdriver

pesquisa = "BATERIA AUTOMOTIVA HELIAR CURITIBA";
url = "https://macbateriascuritiba.com.br";
pesquisaOtimizada = pesquisa.replace(' ','+');

link = "https://www.google.com/search?q=" + pesquisa;
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"};
requisicao = requests.get(link, headers=headers);
site = BeautifulSoup(requisicao.text, "html.parser");




cont = 0;

hrefs = []


a_elements = site.find_all("a", attrs={"jsname": "UWckNb"})


for a in a_elements:
    href = a.get("href")  
    if href:
        hrefs.append(href)  


for href in hrefs:
    print(href)
    
    
for href in hrefs:
    cont += 1;
    if url in href:
        break;
    

print(cont);




