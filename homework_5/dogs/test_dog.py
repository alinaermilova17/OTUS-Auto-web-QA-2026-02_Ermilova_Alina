import requests
import pytest

BASE_URL = 'https://dog.ceo/api/'
breed1='hound'
breed2='afghan'
count = 8

breeds = [
    'hound',
    'retriever',
    'bulldog',
    'poodle',
    'husky',
    'beagle',
    'boxer',
    'chihuahua'
]

def test_get_all_breeds():

    response = requests.get(url=f'{BASE_URL}breeds/list/all')
    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    res_json = response.json()
    breeds = res_json.get('message', {})

    print(f'Всего пород: {len(breeds)}')
    print(f'Первые 10 пород: {list(breeds.keys())[:10]}')


def test_get_random_image():
    response = requests.get(url=f'{BASE_URL}breeds/image/random')
    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    res_json = response.json()

    assert res_json.get('message',{})
    assert res_json.get('status') == 'success', f'ERROR: {res_json.get("message")}'
    print( f'Рандомная картинка успешно выгружена!')


@pytest.mark.parametrize('breed',breeds)
def test_get_list_of_images(breed):
    response = requests.get(url=f'{BASE_URL}breed/{breed}/images')
    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    res_json = response.json()
    images = res_json.get('message', {})

    assert res_json.get('status') == 'success', f'ERROR: {res_json.get("message")}'
    assert isinstance(images, list), f'Изображения должны быть списком, получен {type(images)}'
    assert len(images) > 0, f'Для породы {breed} нет изображений'

    print(f' Всего картинок для породы {breed}: {len(images)}')



def test_get_list_of_sub_breed_images():
    response = requests.get(url=f'{BASE_URL}breed/{breed1}/{breed2}/images')
    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    res_json = response.json()

    images = res_json.get('message', {})
    assert res_json.get('status') == 'success', f'ERROR: {res_json.get("message")}'
    print(f'Всего картинок: {len(images)} породы {breed1} и {breed2}')


def test_get_multiple_images():
    response = requests.get(url=f'{BASE_URL}breeds/image/random/{count}')
    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    res_json = response.json()

    images = res_json.get('message', {})
    assert len(images) == count, f'ERROR: {len(images)}, {count}'
    assert res_json.get('status') == 'success', f'ERROR: {res_json.get("message")}'
    print(f'Выгружено {len(images)} картинок')


@pytest.mark.parametrize('breed', breeds)
def test_get_list_of_images(breed):
    response = requests.get(url=f'{BASE_URL}breed/{breed}/images')
    assert response.status_code == 200, f'ERROR: {response.status_code}, {response.text}'

    res_json = response.json()
    images = res_json.get('message', [])

    assert res_json.get('status') == 'success', f'ERROR: {res_json.get("message")}'
    assert len(images) > 0, f'Для породы {breed} нет изображений'

    print(f'Порода {breed}: {len(images)} изображений')