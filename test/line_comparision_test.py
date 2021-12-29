from line_comparision import Line
from line_comparision import LineComparision


def test_calculate_length():
    """
    test case for calculate length method
    :return:
    """
    line_dict = {"name": "sunanda", "x1": 2, "x2": 4, "y1": 2, "y2": 4}
    line = Line(line_dict)
    assert isinstance(line, Line) == True


def test_add_line():
    """
    test case for add line method
    :return:
    """
    line_comparision = LineComparision()
    line_dict = {"name": "sunanda", "x1": 2, "x2": 4, "y1": 2, "y2": 4}
    line = Line(line_dict)
    line_comparision.add_line(line)
    assert len(line_comparision.line_list) > 0


def test_finding_length():
    line_comparision = LineComparision()
    line_dict = {"name": "sunanda", "x1": 2, "x2": 4, "y1": 2, "y2": 4}
    line = Line(line_dict)
    line_comparision.add_line(line)

    name, value = line_comparision.finding_length()
    assert name == "sunanda" and value == 2.8284271247461905
