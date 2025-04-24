import os
import sys
import json
from unittest import mock
import pytest
# Adding the parent folder to sys.path so we can import modules from the 'scripts' directory (must be done before importing the function)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.load_to_bronze import fetch_launches_data


def test_fetch_launches_data():

    mock_r = mock.Mock() #creating mock object
    mock_r.status_code = 200 #giving the object a status code
    mock_r.json.return_value = {"id": 13, "status": "successful", "center": "Kennedy Space Center"} #giving the object data

    with mock.patch('requests.get', return_value=mock_r): #replacing the requests.get by the fake mock object in the function
        fetch_launches_data()

    file_path = "../data/bronze/raw_data.json"
    assert os.path.exists(file_path), "File does not exist" #checking if the file exists


    with open(file_path, "r") as file: #opening the file to check if data matches
        data = json.load(file)
        assert data == {"id": 13, "status": "successful", "center": "Kennedy Space Center"}, "Data does not match"

    os.remove("../data/bronze/raw_data.json") # deleting the file

