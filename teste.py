from selenium import webdriver
import time

# Configuração do WebDriver
cService = webdriver.ChromeService(executable_path='C:/Users/mathe/AppData/Local/Programs/Python/Python312/chromedriver.exe')
driver = webdriver.Chrome(service=cService)

# URL de pesquisa no Google
url = "https://www.google.com/search?q=BATERIA+AUTOMOTIVA+HELIAR+CURITIBA"

# Abrir a URL no navegador controlado pelo WebDriver
driver.get(url)

# Aguardar um curto período para o conteúdo ser carregado
time.sleep(5)

# Extrair os links das páginas de resultados
links = driver.find_all("a", attrs={"jsname": "UWckNb"})

# Lista para armazenar as URLs
results = []

for link in links:
    href = link.get_attribute('href')
    if href:
        results.append({'url': href})

# Fechar o navegador controlado pelo WebDriver
driver.quit()

# Imprimir os resultados
print(results)
