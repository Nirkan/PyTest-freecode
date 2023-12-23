import pytest
import source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81),(3,9)])
def test_multiples_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area



@pytest.mark.parametrize("side_length, expected_perimeter", [(3,12),(4,16),(5,20)])
def test_multiple_perimeter(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter

