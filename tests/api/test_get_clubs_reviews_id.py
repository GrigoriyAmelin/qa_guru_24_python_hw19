import requests
from jsonschema import validate

from schemas.get_clubs_reviews_id_response_schemas import (
    response_schema,
    unexisting_review_response_schema
)


def test_get_clubs_reviews_id_search_exact_review():
    review_id: int = 40
    club_id: int = 292
    search_phrase: str = 'Night'

    response = requests.get(f'https://book-club.qa.guru/api/v1/clubs/reviews/{review_id}/')
    response_body = response.json()

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}\n')

    assert response.status_code == 200
    validate(response_body, schema = response_schema)
    assert response_body['id'] == 40
    assert response_body['club'] == club_id
    assert response_body['user']['id'] == 795
    assert response_body['user']['username'] == 'EmmanuelHorace'
    assert search_phrase in response_body['review']
    assert response_body['assessment'] == 1
    assert response_body['readPages'] == 266
    assert response_body['created'] is not None
    assert response_body['modified'] is None


def test_get_clubs_id_search_unexisting_club():
    review_id: int = -40

    response = requests.get(f'https://book-club.qa.guru/api/v1/clubs/reviews/{review_id}/')
    response_body = response.json()

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}\n')

    assert response.status_code == 404
    validate(response_body, schema = unexisting_review_response_schema)
    assert response_body['detail'] == 'No BookReview matches the given query.'