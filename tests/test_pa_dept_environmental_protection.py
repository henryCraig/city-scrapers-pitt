from datetime import datetime
from os.path import dirname, join

import pytest
from freezegun import freeze_time
from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.utils import file_response

from city_scrapers.spiders.pa_dept_environmental_protection import PaDeptEnvironmentalProtectionSpider

test_response = file_response(
    join(dirname(__file__), "files", "pa_dept_environmental_protection.html"),
    url="http://www.ahs.dep.pa.gov/CalendarOfEvents/Default.aspx?list=true",
)
spider = PaDeptEnvironmentalProtectionSpider()

freezer = freeze_time("2019-08-28")
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]

freezer.stop()



"""
Uncomment below
"""

def test_title():
    assert parsed_items[0]["title"] == "Agricultural Advisory Board (AAB) meeting"

def test_description():
    print("parsed_items[0]: ", parsed_items[0]["description"])
    assert parsed_items[0]["description"] == "Joint Meeting with Nutrient Management Advisory"

# def test_location():
#     print("hello?")
#     print(parsed_items[0]['location'])
#     print("There it is")
#     assert parsed_items[0]["location"] == "Pennsylvania Department of Agricu"

    # """Pennsylvania Department of Agriculture
    # 2301 North Cameron Street, Room 309
    # Harrisburg, PA 17110"""

def test_location_two():
    print("length of parsed items", len(parsed_items))

    print("Title of Meeting 8:", parsed_items[8]["title"])
    print("Time Notes 8: ", parsed_items[8]["time_notes"])
    print("Description of Meeting 8:", parsed_items[8]["description"])
    print("Location: ", parsed_items[8]["location"])
    print("Start: ", parsed_items[8]["start"])
    print("End: ", parsed_items[8]["end"])
    print('\n')

    print("Title of Meeting 9:", parsed_items[9]["title"])
    print("Time Notes 9: ", parsed_items[9]["time_notes"])
    print("Description of Meeting 9:", parsed_items[9]["description"])
    print("Location: ", parsed_items[9]["location"])
    print("Start: ", parsed_items[9]["start"])
    print("End: ", parsed_items[10]["end"])
    print('\n')

    print("Title of Meeting 10:", parsed_items[10]["title"])
    print("Time Notes 10: ", parsed_items[10]["time_notes"])
    print("Description of Meeting 10:", parsed_items[10]["description"])
    print("Location: ", parsed_items[10]["location"])
    print("Start: ", parsed_items[10]["start"])
    print("End: ", parsed_items[10]["end"])
    print('\n')






    #Length of parsed items was 55 when working with response.css('div')
    #The number of current meetings on the website though is: 31 - there are 31 centered div padtops
    #Actually there are 30, the first thing doesnt have it


    #assert parsed_items[1]["location"][:38] == "Pennsylvania Department of Agriculture"

    assert parsed_items[1]["location"][:38] == "yo"




# def test_start():

    #So actually, instead of doing time notes - which I'm not even sure what those refer to actually...
    #We are returning the start time as a datetime object
    #Apprently thats true for the end time as well
    #It would be year, month, day, hour, minutes
    #So for example if it starts at 6:30 it would be
#     assert parsed_items[0]["start"] == datetime(2019, 1, 1, 0, 0)


# def test_end():
#     assert parsed_items[0]["end"] == datetime(2019, 1, 1, 0, 0)


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


# def test_source():
#     assert parsed_items[0]["source"] == "EXPECTED URL"


# def test_links():
#     assert parsed_items[0]["links"] == [{
#       "href": "EXPECTED HREF",
#       "title": "EXPECTED TITLE"
#     }]


# def test_classification():
#     assert parsed_items[0]["classification"] == NOT_CLASSIFIED


# @pytest.mark.parametrize("item", parsed_items)
# def test_all_day(item):
#     assert item["all_day"] is False
