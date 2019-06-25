import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="http://localhost:8080/v1/user/", help="url: service url"
    )

@pytest.fixture
def url(request):
    return request.config.getoption("--url")