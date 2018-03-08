#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester_17203511` package."""
import sys
sys.path.append('.')

from click.testing import CliRunner
from led_tester_17203511 import led_tester_17203511
from led_tester_17203511 import cli
from led_tester_17203511 import utils

import pytest
@pytest.fixture
def response():
    """Sample pytest fixture.See more at: http://doc.pytest.org/en/latest/fixture.html"""
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None
    
def test_read_file():
    ifile = "./data/input_assign3_a.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n',
 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7\n']
    
