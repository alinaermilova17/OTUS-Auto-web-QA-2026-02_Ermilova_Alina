import pytest

def pytest_addoption(parser):
    parser.addoption(
        '--url',
        action='store',
        default='https://ya.ru',
    )
    parser.addoption(
        '--status_code',
        action='store',
        default='200',
    )


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='session')
def expected_status(request):
    return int(request.config.getoption('--status_code'))