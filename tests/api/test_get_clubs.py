import requests
from jsonschema import validate

from schemas.get_clubs_response_schemas import get_clubs_response_schema, get_clubs_page_length_response_schema, \
    get_clubs_unexisting_page_response_schema


def test_get_clubs_search_exact_club():
    page: int = 1
    page_size: int = 10
    search: str = "Тестирование Дот Ком"

    response = requests.get(f'https://book-club.qa.guru/api/v1/clubs/?page={page}&page_size={page_size}&search={search}')
    response_body = response.json()

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}\n')

    assert response.status_code == 200
    validate(response_body, schema = get_clubs_response_schema)
    assert response_body['count'] == 1
    assert response_body['next'] is None
    assert response_body['previous'] is None
    assert response_body['results'][0]['bookTitle'] == search
    assert response_body['results'][0]['bookAuthors'] == 'Роман Савин'
    assert response_body['results'][0]['publicationYear'] == 2007
    assert 'Тестирование Дот Ком' in response_body['results'][0]['description']


def test_get_clubs_page_length():
    page: int = 1
    page_size: int = 9

    response = requests.get(f'https://book-club.qa.guru/api/v1/clubs/?page={page}&page_size={page_size}')
    response_body = response.json()
    results_count = len(response_body['results'])

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}')
    print(f'Number of results: {results_count}\n')

    assert response.status_code == 200
    validate(response_body, schema = get_clubs_page_length_response_schema)
    assert response_body['count'] == 184
    assert response_body['next'] == "https://book-club.qa.guru/api/v1/clubs/?page=2&page_size=9"
    assert response_body['previous'] is None
    assert response_body['results'][0]['id'] == 1
    assert response_body['results'][8]['id'] == 9
    assert results_count == page_size


def test_get_clubs_unexisting_page():
    page: int = 185
    page_size: int = 100

    response = requests.get(f'https://book-club.qa.guru/api/v1/clubs/?page={page}&page_size={page_size}')
    response_body = response.json()

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}')

    assert response.status_code == 404
    validate(response_body, schema = get_clubs_unexisting_page_response_schema)
    assert response_body['detail'] == 'Invalid page.'
    assert 'next' not in response_body
    assert 'previous' not in response_body


