# py-walletconnect-push

Exposes webhook for push notifications mechanism, written in Python 3.

## Getting Started
If you'd like to keep a separate Python environment for this project's installs, set up virtualenv
~~~~
$ pip install virtualenv virtualenvwrapper
~~~~

Add the following to your ~/.bashrc
~~~
export WORKON_HOME=$HOME/.virtualenvs~
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
~~~~

From the project directory, run these commands to install the walletconnect-push package in a virtualenv called "walletconnect-push"
~~~~
$ mkvirtualenv walletconnect-push
$ pip install -r requirements.txt
$ python setup.py develop
~~~~

Run the project locally
~~~~
$ walletconnect-push --push-local --api-local
~~~~


In production, use the following where <FCM_SERVER_KEY> is the server key specified in your Firebase project account.
~~~~
$ walletconnect-push --fcm-server-key <FCM_SERVER_KEY>
~~~~

Use a tool like Postman to create requests to interact with the server.
