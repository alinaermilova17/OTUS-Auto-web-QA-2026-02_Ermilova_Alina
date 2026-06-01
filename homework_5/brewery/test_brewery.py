import json

import pytest
import requests

BASE_URL = 'https://api.openbrewerydb.org/v1/'


def test_list_of_breweries():
    list_response = requests.get(f'{BASE_URL}breweries?per_page=3')
    assert list_response.status_code == 200, f'ERROR: {list_response.status_code}, {list_response.text}'
    breweries = list_response.json()

    assert len(breweries) > 0, 'Нет доступных пивоварен'
    print(json.dumps(breweries, indent=4, ensure_ascii=False))


def test_get_a_single_brewery():
    list_response = requests.get(url=f'{BASE_URL}breweries', params={'per_page': 1})
    assert list_response.status_code == 200, f'ERROR: {list_response.status_code}, {list_response.text}'

    breweries = list_response.json()
    assert len(breweries) > 0, 'Нет доступных пивоварен'

    obdb_id = breweries[0]['id']
    print(f'Тестируем пивоварню с ID: {obdb_id}')

    response = requests.get(url=f'{BASE_URL}breweries/{obdb_id}')
    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    res_json = response.json()

    assert 'id' in res_json, "Нет поля 'id'"
    assert 'name' in res_json, "Нет поля 'name'"
    assert 'brewery_type' in res_json, "Нет поля 'brewery_type'"

    print(f" Название: {res_json['name']}")
    print(f" Тип: {res_json['brewery_type']}")


@pytest.mark.parametrize('city', [
    'san_diego',
    'mount_pleasant',
    'austintown'
])
def test_filter_brewery_by_city(city):
    response = requests.get(f'{BASE_URL}breweries?by_city={city}')
    assert response.status_code == 200
    breweries = response.json()

    for brewery in breweries:
        actual_city = brewery.get('city', '').lower().replace(' ', '_')
        assert actual_city == city, f'Ожидался город {city}, получен {actual_city}'

    print(f'В городе {city} найдено {len(breweries)} пивоварен')


def test_brewery_result_sorted():
    response = requests.get(f'{BASE_URL}breweries',
    params = {
        'by_state': 'california',
        'sort': 'type,name:asc',
        'per_page': 3
    })
    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    breweries = response.json()

    assert isinstance(breweries, list), 'Данные должны быть списком'
    assert len(breweries) == 3, f'Ожидалось 3 пивоварни, получено {len(breweries)}'
    print(json.dumps(breweries, indent=4, ensure_ascii=False))


@pytest.mark.parametrize('state, expected_count', [
    ('california', 2),
    ('texas', 2),
    ('new_york', 2),
])
def test_breweries_by_state(state, expected_count):
    response = requests.get(f'{BASE_URL}breweries',
        params={
            'by_state': state,
            'sort': 'type,name:asc',
            'per_page': expected_count
        }
    )

    assert response.status_code == 200
    breweries = response.json(), f'ERROR: {response.status_code}, {response.text}'

    assert len(breweries) == expected_count, f'Для штата {state} ожидалось {expected_count} пивоварен, получено {len(breweries)}'
