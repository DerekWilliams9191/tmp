import pytest
from program.module import add, subtract

def test_add():
    """Test add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add_parametrized(a, b, expected):
    """Parametrized test for the add function."""
    assert add(a, b) == expected