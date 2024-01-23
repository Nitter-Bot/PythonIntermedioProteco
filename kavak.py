#Uso de beautiful soup para obtener datos de coches del sitio de kavak

#Sitio https://www.kavak.com/mx/compra-de-autos

#Empezamos importnado las librerias
import requests
from bs4 import BeautifulSoup

#LLamamos a la pagina

pagina = requests.get("https://www.kavak.com/mx/seminuevos", timeout = 1)

#Parseamos
paginaParseada = BeautifulSoup(pagina.text,"html.parser")

   
