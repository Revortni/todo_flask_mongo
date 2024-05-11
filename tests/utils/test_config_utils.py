import pytest

from utils.db_utils.config_utils import b64_decode


def test_b64_decode():
    assert b64_decode('dGVzdA==') == 'test'


@pytest.mark.parametrize("test_input, expected_output", [('dGVzdA==', 'test')])
def test_b64_decode_parametrized(test_input, expected_output):
    assert b64_decode(test_input) == expected_output
