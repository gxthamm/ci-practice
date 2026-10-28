import time

import pytest


@pytest.mark.parametrize("n", range(10))
def test_slow_check(n):
    time.sleep(2)
    assert n >= 0