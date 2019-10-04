from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
import re


#This class is inheriting from the CityScrapersSpider, thats what it means when its taking it as an arg I guess
class PaDeptEnvironmentalProtectionSpider(CityScrapersSpider):
    name = "pa_dept_environmental_protection"
    agency = "PA Department of Environmental Protection"

    #It looks like I might want to change this timezone to America/New_York
    #Like the other spiders
    timezone = "America/New_York"
    allowed_domains = ["www.ahs.dep.pa.gov"]
    start_urls = ["http://www.ahs.dep.pa.gov/CalendarOfEvents/Default.aspx?list=true"]
    custom_settings = {'ROBOTSTXT_OBEY' : False}



    def parse(self, response):
        """
        `parse` should always `yield` Meeting items.

        Change the `_parse_title`, `_parse_start`, etc methods to fit your scraping
        needs.
        """

        for meetingChunk in response.xpath('//div[@class = "centered_div padtop"]').getall():
            if '<strong>' in meetingChunk:
                meeting = Meeting(
                    title = self._parse_title(meetingChunk),
                    description=self._parse_description(meetingChunk),
                    location = self._parse_location(meetingChunk),
                    time_notes = self._parse_time_notes(meetingChunk),
                    start = self._parse_start(meetingChunk),

                    #AttributeError: 'str' object has no attribute 'xpath'
                    #It's returning a bunch of strings, so It doesnt want me to use xpath anymore now

                    #So the thing I want to do now is try to use regex on this

                    # phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
                    # >>> mo = phoneNumRegex.search('My number is 415-555-4242.')
                    # >>> print('Phone number found: ' + mo.group())




                    #title = self._parse_title(item),
                    # description=self._parse_description(item),
                    # classification=self._parse_classification(item),
                    # start=self._parse_start(item),
                    # end=self._parse_end(item),
                    # all_day=self._parse_all_day(item),
                    # time_notes=self._parse_time_notes(item),
                    # location=self._parse_location(item),
                    # links=self._parse_links(item),
                    # source=self._parse_source(response),
                )

                #meeting["status"] = self._get_status(meeting)
                #meeting["id"] = self._get_id(meeting)

                yield meeting


    def _parse_title(self, item):
        titleRegex = re.compile(r'(am|pm) : (.)+</td>')
        thisThing = titleRegex.search(item)
        return thisThing.group()[5:-5]

    def _parse_time_notes(self, item):
        timeRegex = re.compile(r'(\d)+/(\d)+/\d\d\d\d')
        thisThing = timeRegex.search(item)
        time_notes = thisThing.group()
        return time_notes

    def _parse_description(self, item):
        #class="DisplayTableData">This is an advisory board sub-committee meeting that is open to the public</td>
        descriptionRegex = re.compile(r'Description:(.)+')
        thisThing = descriptionRegex.search(item)
        return thisThing.group()[97:-5]

    def _parse_location(self, item):
        # return {
        #     "address": "",
        #     "name": "",
        # }

        descriptionRegex = re.compile(r'Location:(.)+')
        thisThing = descriptionRegex.search(item)
        return thisThing.group()[91:-5]


    def _parse_classification(self, item):
        """Parse or generate classification from allowed options."""
        return NOT_CLASSIFIED

    def _parse_start(self, item):
        """Parse start datetime as a naive datetime object."""
        startRegex = re.compile(r'</strong>(.)+(a)')

        #Batman|Tina Fey

        thisThing = startRegex.search(item)
        return thisThing.group()[10:]

    def _parse_end(self, item):
        """Parse end datetime as a naive datetime object. Added by pipeline if None"""
        return None

    def _parse_all_day(self, item):
        """Parse or generate all-day status. Defaults to False."""
        return False



    def _parse_links(self, item):
        """Parse or generate links."""
        return [{"href": "", "title": ""}]

    def _parse_source(self, response):
        """Parse or generate source."""
        return response.url
