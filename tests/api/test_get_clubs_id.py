import requests
from jsonschema import validate

from schemas.get_clubs_id_response_schemas import (
    get_clubs_id_response_schema,
    get_clubs_id_unexisting_club_response_schema
)


def test_get_clubs_id_search_exact_club():
    club_id: int = 4

    response = requests.get(f'https://book-club.qa.guru/api/v1/clubs/{club_id}/')
    response_body = response.json()

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}\n')

    assert response.status_code == 200
    validate(response_body, schema = get_clubs_id_response_schema)
    assert response_body['id'] == 4
    assert response_body['bookTitle'] == 'Тестирование Дот Ком'
    assert response_body['bookAuthors'] == 'Роман Савин'
    assert response_body['publicationYear'] == 2007
    assert 'Тестирование Дот Ком' in response_body['description']
    assert response_body['publicationYear'] == 2007
    assert response_body['telegramChatLink'] is not None


def test_get_clubs_id_search_unexisting_club():
    club_id: int = -4

    response = requests.get(f'https://book-club.qa.guru/api/v1/clubs/{club_id}/')
    response_body = response.json()

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}\n')

    assert response.status_code == 404
    validate(response_body, schema = get_clubs_id_unexisting_club_response_schema)
    assert response_body['detail'] == 'No Club matches the given query.'