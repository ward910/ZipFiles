# ZipFiles

## A simple program written in python to create .zip and extract .zip for linux

### build:
~~~
git clone https://github.com/ward910/ZipFiles.git
cd ZipFiles && pip install -r requirements.txt
python ./setup.py build
~~~
### install:
~~~
chmod +x build/exe.linux-xxxxxx-x.x/zipfiles
python ./setup.py install
~~~
### run:
~~~
zipfiles
~~~

### command:

#### create a zip file

~~~
zipfiles zip name folder
~~~

#### unzip zip file

~~~
zipfiles unzip name.zip
~~~