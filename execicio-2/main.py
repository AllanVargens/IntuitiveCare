import tabula
import os
from zipfile import ZipFile
import csv,sys

file = ''

with ZipFile("Arquivos-baixados.zip" , "r") as zip:
    for file_name in zip.namelist():
        if "Anexo I" == True : 
            continue
        else: 
            if "Anexo_I_Rol" in file_name:
                zip.extract(file_name)
                new_name = os.rename(file_name, 'Anexo I.pdf')
                file = new_name

tabula.convert_into('Anexo I.pdf', "Anexo_I_Original.csv", output_format="csv", pages="3-180", lattice=True) #esta retornando uma lista de data frames e nao o dataframe em si


new_line = ""
content = ""
row_one = ""
row_check = 0
nome_ficheiro = 'C:/Users/Homer Chapado/Documents/Projetos/IntuitiveCare/Exercicios/Anexo_I_Original.csv'
with open('Anexo_I_Original.csv', newline="") as ficheiro:
    reader = csv.reader(ficheiro, delimiter=',', quotechar="|")
    try:
        for linha in reader:
            if row_check == 0:
                row_one = linha[-1]
                del linha[-1]
                content = content + ", ".join(linha)
                row_check += 1
            elif row_check == 1:
                final_row = row_one + ' ' + linha[0] + ','
                del linha[0]
                content = content + final_row + ", ".join(linha) + "\n"
                row_one = ""
                row_check = 0
    except csv.Error as e:
        sys.exit('ficheiro , linha %d: %s' % (nome_ficheiro, reader.line_num, e))


csv_final = open('AnexoFinal.csv', 'w+')
csv_final.write(content)
csv_final.close()
