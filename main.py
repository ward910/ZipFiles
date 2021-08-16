from os import name
import zipfile

nameFile = input('File name or folder: ')
zip = input('Do you want to create(c) or extract(e) the file: ')

nameZip = nameFile + '.zip'

def zipCreate(name):
      with zipfile.ZipFile(name, 'w') as zip:
            zip.write(name)
print('successfully')

def zipExtract(name):
      with zipfile.ZipFile(name, 'r') as zip:
            zip.extractall(name)
print('successfully')

if (zip == 'c'):
      zipCreate(nameZip)
elif (zip == 'e'):
      zipExtract(nameZip)
else:
      print('Error')