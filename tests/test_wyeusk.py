#!/usr/bin/env python

"""Tests for `wyeusk` package."""

import pytest
from unittest.mock import Mock

from click.testing import CliRunner
from wyeusk import wyeusk

# Fixture just sets a value in order for subsequent methods to use it
@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')
    skip_v = 1
    return skip_v

# Check if the location exists in a preset list
def test_locations():
    assert 1 == 1


v = 1
# Another method of skipping a test
@pytest.mark.skipif("v == 1")
def test_check_sumink():
    assert 1 == 1

@pytest.fixture
def dummy_db_conn():
    return 1000

# One method of skipping a test
def test_eg_skip(response):
    if response == 1:
        pytest.skip("Test not going to run")
        assert 1 == 1

def test_content():
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert 1 == 1.0

@pytest.mark.xfail
def test_should_fail():
    assert 1 == 100

def test_mock_method(dummy_db_conn):
    dummy_db_conn = Mock()
    with pytest.raises(NameError) as ex:
        x = dddd
    print(ex.value.args)
    assert ex.value.args == ("name 'dddd' is not defined",)




# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'wyeusk.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
