# system testing for user service
## To set up the env
##### Install python
python 3 is required.
##### Install pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
##### Install pytest
```
pip install -U pytest
```
##### Install pytest-dependency
```
pip install pytest-dependency
```
## To run the tests
```
pytest -q --url=${user_service_url}
```