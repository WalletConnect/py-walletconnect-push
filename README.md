# WalletConnectPush

Exposes webhook for push notifications mechanism.

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

From the project directory, run these commands to install the wallet-connect-push package in a virtualenv called "wallet-connect-push"
~~~~
$ mkvirtualenv wallet-connect-push
$ pip install -r requirements.txt
$ python setup.py develop
~~~~

Run the project locally
~~~~
$ wallet-connect --push-local --api-local
~~~~

Use a tool like Postman to create requests to interact with the server.
