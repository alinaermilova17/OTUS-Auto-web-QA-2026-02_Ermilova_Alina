import requests


def test_status_code(url, expected_status):
    response = requests.get(url, allow_redirects=True)

    print(f'Проверяем URL: {url}')
    print(f' Ожидаемый статус: {expected_status}')
    print(f'Фактический статус: {response.status_code}')

    assert response.status_code == expected_status, f'Для URL {url} ожидался статус {expected_status}, получен {response.status_code}'
    print(f'URL {url} вернул статус {expected_status}')