from datetime import date

from harlow_bindicator.page_parser import Parser


def test_parse_example_data():
    f = open("tests/resources/example_data", "r")
    html_text = f.read()
    parser = Parser()
    data = parser.parse(html_text)

    assert len(data) == 6
    assert data[1].wheelie.bin_type == "Recycling"
    assert data[1].wheelie.date == date(2023, 2, 10)
    assert data[1].date == date(2023, 2, 10)
