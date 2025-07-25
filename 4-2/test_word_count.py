import pytest
from flask import Flask
#from word_count import count_words

from stand_up_api_word_count import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_single_word(client):
    response = client.get('/count', query_string={'text': 'word'})
    assert response.status_code == 200
    assert response.get_json() == {'count': 1}

def test_get_two_words(client):
    response = client.get('/count', query_string={'text': 'two words'})
    assert response.status_code == 200
    assert response.get_json() == {'count': 2}
