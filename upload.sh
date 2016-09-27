#!/bin/bash
# register with python setup.py register -r pypitest
python setup.py sdist upload -r pypitest
python setup.py sdist upload -r pypi
