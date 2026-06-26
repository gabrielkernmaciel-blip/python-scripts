#Esse codigo organiza o diretório que focê quiser for extensão do arquivo (colocar na linha 10)
import os

full_file_list = []

def getExtension(file):
    return os.path.splitext(file)[1] 


os.chdir(r"C:\Users\SuperUser\Documentos") #coloque o diretório que deseja organizar aqui

for i in os.listdir("."):
    if os.path.isfile(i):
        full_file_list.append([i,getExtension(i)]) 


for file in full_file_list:
    if not file[1]:
        continue

    if not os.path.exists(file[1]):
        os.mkdir(file[1])

    os.rename(file[0], os.path.join(file[1], file[0]))

print("ok!")
