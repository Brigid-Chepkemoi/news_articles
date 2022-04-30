Building Flask Application Steps
1. Create a virtual environment with the command; python3 -m venv --without-pip virtual
2. Activate the virtual environment using command; source virtual/bin/activate
3. Install pip using the command: curl https://bootstrap.pypa.io/get-pip.py | python
4. Install flask; pip install flask
5. Create the files appropriately according to the needs of the application
        *Create run.py file in which apllication will be run from
        *Create folder app
        *In app folder create templates folder to hold htmls templates
        *In app create __init__.py to initialize the flask application
        *In templates create index.html
        *In app create models folder to hold class files where you define the objects of your class and in it create __init__.py file
        *In app create views.py file to route your application
        *In app create co
6. Intialize flask in the app __init__.py by importing flask from Flask and setting the app to Flask(__name__)
7. Set the routes of the application in the views.py
8. Set up the server in the config.py; classify the environments and the configurations for each i.e Dev,Prod. set the Dev environment to DEBUG=True
9. Incase of API consumption,
        *get the API key from the  host website
        *Create instance folder to hold keys and in it create config.py file to store the api
        *In gitignore file set the instance folder to be ignored/protected from publishing