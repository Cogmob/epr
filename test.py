import os
import shutil
from epr.epr_recursive_import import epr_recursive_import

def run():
    path = os.path.dirname(os.path.abspath(__file__))
    set_up(path)
    do_tests(path)

def set_up(path):
    try:
        shutil.rmtree(path + '/tmp_example_data')
    except FileNotFoundError:
        pass
    shutil.copytree(path + '/example_data', path + '/tmp_example_data')
    epr_recursive_import(path + '/tmp_example_data')

def do_tests(path):
    with open(path + '/tmp_example_data/yes01.py') as f:
        if 'from epr import epr' not in f.read():
            print('NOPE')

run()
