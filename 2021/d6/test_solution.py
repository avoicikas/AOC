import solution


def test_solve():
    """Test with sample input."""
    assert 5934==solution.part1('input2')

def test_solve2():
    """Test with sample input."""
    assert 26984457539==solution.part2('input2',days=256)
