# Title
Edubridge

## Description
EduBridge is an innovative online platform tailored to support business owners and aspiring entrepreneurs, particularly those with limited or no formal education

## Prerequisites
You can find the software requirements in the [requirements.txt](https://github.com/ouredubridge/edutech/blob/main/requirements.txt) file

## Installation
- Clone the repository using the command:
```
git clone https://github.com/ouredubridge/edutech.git
```
- After cloning the repo, ```cd``` (change directory) into the ```edutech``` folder using the command(on Mac OS/ Linux):
```
cd edutech
```
- Create a virtual environment for installing packages and managing dependencies, using the command:
```
python -m venv my_env
```
- Activate the virtual environment:

  -  **On Windows**
  ```
  my_env\Scripts\activate
  ```
  - **On macOS/Linux**
  ```
  source my_env/bin/activate
  ```
- Install Dependencies
Once the virtual environment is activated, you can install the required packages using ```pip```:
```
pip install -r requirements.txt
```
- Run any necessary migrations with:
```
python manage.py migrate
```

## Usage
To run the project on your local machine
- While you are in the root directory, run the command:
```
python manage.py runserver
```
- Then you can access the application in your web browser (usually ```http://127.0.0.1:8000/```)  
