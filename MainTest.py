import pytest
from main import total

@pytest.mark.parametrize("a,b,c", [(1,2,3),(2,3,5),(3,5,8),(5,8,13),(8,13,21)])
def test_main(a,b,c):
    assert total(a,b) == c