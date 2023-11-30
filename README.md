# Linux

## Setup python environment
python3 -m venv venv

## Activate environment
source venv/bin/activate 


## Install required packages
pip install -r requirements.txt


## Add new packages
pip freeze > requirements.txt

## Run
flask run
# Windows

## Setup python environment
python -m venv venv

## Activate environment
venv\Scripts\Activate.ps1


## Install required packages
pip install -r requirements.txt


## Add new packages
pip freeze > requirements.txt

## Run
flask run