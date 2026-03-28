import requests
from jsonschema import validate

from schemas.get_clubs_reviews_response_schemas import response_schema, all_reviews_response_schema, \
    unexisting_review_response_schema


def test_get_clubs_reviews_search_existing_review():
    page: int = 1
    page_size: int = 10
    club_id: int = 292
    search_phrase: str = 'Night'

    response = (requests.
                get(f'https://book-club.qa.guru/api/v1/clubs/reviews/?club={club_id}&page={page}&page_size={page_size}'))
    response_body = response.json()

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}\n')

    assert response.status_code == 200
    validate(response_body, schema = response_schema)
    assert response_body['count'] == 1
    assert response_body['next'] is None
    assert response_body['previous'] is None
    assert response_body['results'][0]['id'] == 40
    assert response_body['results'][0]['club'] == club_id
    assert response_body['results'][0]['user']['id'] == 795
    assert response_body['results'][0]['user']['username'] == 'EmmanuelHorace'
    assert search_phrase in response_body['results'][0]['review']
    assert response_body['results'][0]['assessment'] == 1
    assert response_body['results'][0]['readPages'] == 266
    assert response_body['results'][0]['created'] is not None


def test_get_clubs_reviews_search_all_existing_reviews():
    # page: int = 1
    # page_size: int = 10
    club_id: int = 292
    search_phrase: str = 'Night'

    response = requests.get(f'https://book-club.qa.guru/api/v1/clubs/reviews/')
    response_body = response.json()
    results_count = len(response_body['results'])

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}\n')

    assert response.status_code == 200
    validate(response_body, schema = all_reviews_response_schema)
    assert response_body['count'] is not None
    assert response_body['next'] is None
    assert response_body['previous'] is None
    assert results_count == response_body['count']

    for review in response_body['results']:
        if review.get('id') == 40:
            assert review.get('club') == club_id
            assert review.get('user').get('id') == 795
            assert review.get('user').get('username') == 'EmmanuelHorace'
            assert search_phrase in review.get('review')
            assert review.get('assessment') == 1
            assert review.get('readPages') == 266
            assert review.get('created') is not None


def test_get_clubs_reviews_search_unexisting_review():
    page: int = 1
    page_size: int = 10
    club_id: int = 4

    response = (requests.
                get(f'https://book-club.qa.guru/api/v1/clubs/reviews/?club={club_id}&page={page}&page_size={page_size}'))
    response_body = response.json()
    results_count = len(response_body['results'])

    print(f'\nStatus code: {response.status_code}')
    print(f'Response headers: {response.headers}')
    print(f'Response body: {response.text}')

    assert response.status_code == 200
    validate(response_body, schema = unexisting_review_response_schema)
    assert response_body['count'] == 0
    assert response_body['next'] is None
    assert response_body['previous'] is None
    assert results_count == 0


