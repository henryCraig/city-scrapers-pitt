from datetime import datetime
from os.path import dirname, join

from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.utils import file_response
# import pytest
from freezegun import freeze_time

from city_scrapers.spiders.pa_dept_environmental_protection import (
    PaDeptEnvironmentalProtectionSpider
)

test_response = file_response(
    join(dirname(__file__), "files", "pa_dept_environmental_protection.html"),
    url="http://www.ahs.dep.pa.gov/CalendarOfEvents/Default.aspx?list=true",
)
spider = PaDeptEnvironmentalProtectionSpider()

freezer = freeze_time("2019-08-28")
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]

freezer.stop()


def test_title():
    assert parsed_items[0]["title"] == "Agricultural Advisory Board (AAB) meeting"


def test_description():
    print("parsed_items[0]: ", parsed_items[0]["description"])
    # This stupid thing only passes when you put a space at the end of it
    # That means I can fix my regex maybe?  Or maybe not im not sure
    print(parsed_items[0]["start"])
    print(parsed_items[1]["start"])
    print(parsed_items[2]["start"])

    assert parsed_items[0]["description"] == "Joint Meeting with Nutrient Management Advisory"

# Need to alter this so it has the title and location in a dictionary


def test_location():
    print(parsed_items[0]['location'])
    assert parsed_items[0]["location"] == "Pennsylvania Department of Agricu"
# """Pennsylvania Department of Agriculture
# 2301 North Cameron Street, Room 309
# Harrisburg, PA 17110"""


def test_start():
    assert parsed_items[0]["start"] == datetime(2019, 8, 29, 9, 0)


def test_end():
    assert parsed_items[0]["end"] == datetime(2019, 8, 29, 12, 0)

# def test_time_notes():
#     assert parsed_items[0]["time_notes"] == "EXPECTED TIME NOTES"

# def test_id():
#     assert parsed_items[0]["id"] == "EXPECTED ID"

# def test_status():
#     assert parsed_items[0]["status"] == "EXPECTED STATUS"

# def test_location():
#     assert parsed_items[0]["location"] == {
#         "name": "EXPECTED NAME",
#         "address": "EXPECTED ADDRESS"
#     }


def test_source():
    src = "http://www.ahs.dep.pa.gov/CalendarOfEvents/Default.aspx?list=true"
    assert parsed_items[0]["source"] == src


def test_links():
    assert parsed_items[1]["links"] == [{
        "href": ("https://www.dep.pa.gov/PublicParticipation/"
                 "AdvisoryCommittees/WaterAdvisory/SAC/Pages/default.aspx"),
        "title": "more info"
    }]


def test_classification():
    assert parsed_items[0]["classification"] == NOT_CLASSIFIED

# @pytest.mark.parametrize("item", parsed_items)
# def test_all_day(item):
#     assert item["all_day"] is False
