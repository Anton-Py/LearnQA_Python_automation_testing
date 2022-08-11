import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com",
        help="This is recuest url"
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
