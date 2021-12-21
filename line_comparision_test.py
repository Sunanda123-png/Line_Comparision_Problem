from line_comparision import Line


def test_calculate_length():
    """
    test case for calculate length method
    :return:
    """
    l1 = Line(2, 4, 2, 4)
    assert isinstance(l1, Line) == True
