import os
import requests
import re
from bs4 import BeautifulSoup
from zipfile import ZipFile

# fazendo requisão de conteudos para a pasta 
   
url = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'

# local onde os arquivos vao ser baixados

local_file = os.getcwd() #local do arquivo de forma dinamica
print(local_file)

# lista de links dos pdfs

requisicao = requests.get(url)
soup = BeautifulSoup(requisicao.content, 'html.parser')
hrefs = [a['href'] for a in soup.select("#parent-fieldname-text > p:nth-child(n) > a")] # Todos os linkls da pagina

hrefs_filtrados = [href for href in hrefs if re.search('RN_465.2021' , href) and re.search('.pdf' , href)] # links filtrados usando expressoes regulares

# interação para que cada pdf da lista seha baixado e salvo no local_file

for pdf in hrefs_filtrados:
    response = requests.get(pdf)
    if response.status_code == 200:
        basename_file = os.path.basename(pdf)
        print(basename_file)
        file_path = os.path.join(local_file , basename_file)
        print(file_path)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
# criando zip nos quais arquivos serao salvos e copiando
list_files = os.listdir(local_file)

with ZipFile("Arquivos-baixados.zip" , "w") as zip:
    print('Pasta .zip criada com sucesso')
    for file in list_files:
        if ".pdf" in file:
            zip.write(file)
            
            # deletando arquivos da pastar externa a zip

            os.remove(f'{local_file}/{file}')