from subprocess import call

# know the name of the file or folder
nameFile = input('File name or folder: ')
# know it's a file or folder
fileFolder = input('And a file(file) or folder(folder): ')
# knows that the person who creates a zip or extracts a zip
zip = input('Do you want to create(c) or extract(e) the file: ')
nameZip = nameFile + '.zip'

def zipCreate(name, fileFolder):
      # for files    
      if (fileFolder == 'file'):
            call(f'zip {nameZip} {name}', shell=True)
      else:
      # for folders
            call(f'zip -r {nameZip} {name}', shell=True)

def zipExtract(name):
      # extract .zip
      call(f'unzip {name}', shell=True)

if (zip == 'c'):
      zipCreate(nameFile, fileFolder)
elif (zip == 'e'):
      zipExtract(nameFile)
else:
      print('Error')