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


#Ok so, here we have the parsed items this test will refer to the entire time
#I believe these parsed items come from the parse() method in the spider
parsed_items = [item for item in spider.parse(test_response)]

freezer.stop()



"""
Uncomment below
"""

# def test_title():
#     print("Hello?  This thing on?")
#     print(type(parsed_items))
#     print(len(parsed_items))
#
#     #parsed_items is a list
#     #I'm getting an index error currently because it's a list with nothing inside of it
#     #That's the problem
#
#     #For some reason parsed item
#
#     assert parsed_items[0]["title"] == "titleOfMeeting"


# def test_description():
#     print("parsed_items[0]: ", parsed_items[0])
#     assert parsed_items[0]["description"] == "EXPECTED DESCRIPTION"

def test_location():
    print("hello?")
    print(parsed_items[0]['location'])
    print("There it is")
    assert parsed_items[0]["location"][:38] == "Pennsylvania Department of Agriculture"

    # """Pennsylvania Department of Agriculture
    # 2301 North Cameron Street, Room 309
    # Harrisburg, PA 17110"""

def test_location_two():
    print("length of parsed items", len(parsed_items))

    print("Title of Meeting 8:", parsed_items[8]["title"])
    print("Time Notes 8: ", parsed_items[8]["time_notes"])
    print("Description of Meeting 8:", parsed_items[8]["description"])
    print("Location: ", parsed_items[8]["location"])
    print("Start: ", parsed_items[0]["start"])
    print('\n')

    print("Title of Meeting 9:", parsed_items[9]["title"])
    print("Time Notes 9: ", parsed_items[9]["time_notes"])
    print("Description of Meeting 9:", parsed_items[9]["description"])
    print("Location: ", parsed_items[9]["location"])
    #print("Start: ", parsed_items[9]["start"])
    print('\n')

    print("Title of Meeting 10:", parsed_items[10]["title"])
    print("Time Notes 10: ", parsed_items[10]["time_notes"])
    print("Description of Meeting 10:", parsed_items[10]["description"])
    print("Location: ", parsed_items[10]["location"])
    #print("Start: ", parsed_items[10]["start"])
    print('\n')






    #Length of parsed items was 55 when working with response.css('div')
    #The number of current meetings on the website though is: 31 - there are 31 centered div padtops
    #Actually there are 30, the first thing doesnt have it


    #assert parsed_items[1]["location"][:38] == "Pennsylvania Department of Agriculture"

    #This is just to break it, otherwise we can use the previous statement to make it work
    assert parsed_items[1]["location"][:38] == "yo"




# def test_start():
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
