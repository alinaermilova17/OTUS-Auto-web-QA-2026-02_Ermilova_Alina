import requests
import pytest

BASE_URL = 'https://jsonplaceholder.typicode.com'


def test_get_post():
    response = requests.get(f'{BASE_URL}/posts/1')

    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    data = response.json()
    assert data['id'] == 1, 'ID поста не совпадает'
    assert 'title' in data, 'Отсутствует поле title'
    assert 'body' in data, 'Отсутствует поле body'

    print('\n Тест GET пройден')


def test_create_post():
    new_post = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    response = requests.post(f'{BASE_URL}/posts', json=new_post)

    assert response.status_code == 201, f'ERROR: {response.status_code}, {response.text}'

    data = response.json()
    assert data['title'] == new_post['title'], 'Заголовок не совпадает'
    assert data['body'] == new_post['body'], 'Тело не совпадает'
    assert data['id'] == 101, 'ID не совпадает с ожидаемым (101)'

    print('\n Тест POST пройден')


def test_update_post():
    updated_post = {
        'id': 1,
        'title': 'Updated Title PUT',
        'body': 'Updated Body PUT',
        'userId': 1
    }

    response = requests.put(f'{BASE_URL}/posts/1', json=updated_post)

    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    data = response.json()
    assert data['title'] == updated_post['title'], 'Заголовок не обновлен'
    assert data['body'] == updated_post['body'], 'Тело не обновлено'
    print('\n Тест PUT пройден')


def test_delete_post():
    response = requests.delete(f'{BASE_URL}/posts/1')

    assert response.status_code in [200, 204], f'ERROR: {response.status_code}, {response.text}'

    print('\n Тест DELETE пройден')


@pytest.mark.parametrize('user_id, expected_post_count', [
    (1, 10),
    (2, 10),
    (3, 10),
])
def test_posts_by_user(user_id, expected_post_count):
    response = requests.get(f'{BASE_URL}/posts', params={'userId': user_id})

    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'
    posts = response.json()

    assert len(posts) == expected_post_count, f'У пользователя {user_id} ожидалось {expected_post_count} постов, получено {len(posts)}'

    print(f'\n Пользователь {user_id}: {len(posts)} постов')


