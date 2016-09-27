import os
import shutil
from epr.epr_recursive_import import epr_recursive_import
from epr.epr import epr

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
    epr('expect 8 green workings')

    yes_tests = [
            '/tmp_example_data/subdir/yes01.py',
            '/tmp_example_data/yes01.py',
            '/tmp_example_data/yes02.py',
            '/tmp_example_data/yes03.py']

    no_tests = [
            '/tmp_example_data/subdir/no01.py',
            '/tmp_example_data/no01',
            '/tmp_example_data/no02.py',
            '/tmp_example_data/no03.py']

    for test in yes_tests:
        with open(path + test) as f:
            if 'from epr import epr' not in f.read():
                epr('not working', 'red')
            else:
                epr('working', 'green')

    for test in no_tests:
        with open(path + test) as f:
            if 'from epr import epr' in f.read():
                epr('not working', 'red')
            else:
                epr('working', 'green')

run()
