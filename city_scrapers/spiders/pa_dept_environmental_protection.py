import datetime
import re

from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider


class PaDeptEnvironmentalProtectionSpider(CityScrapersSpider):
    name = "pa_dept_environmental_protection"
    agency = "PA Department of Environmental Protection"
    timezone = "America/New_York"
    allowed_domains = ["www.ahs.dep.pa.gov"]
    start_urls = ["http://www.ahs.dep.pa.gov/CalendarOfEvents/Default.aspx?list=true"]
    custom_settings = {'ROBOTSTXT_OBEY': False}

    def parse(self, response):
        for meetingChunk in response.xpath('//div[@class = "centered_div padtop"]').getall():
            if '<strong>' in meetingChunk:
                meeting = Meeting(
                    title=self._parse_title(meetingChunk),
                    description=self._parse_description(meetingChunk),
                    location=self._parse_location(meetingChunk),
                    time_notes=self._parse_time_notes(meetingChunk),
                    start=self._parse_start(meetingChunk),
                    end=self._parse_end(meetingChunk),
                    links=self._parse_links(meetingChunk),

                    # title = self._parse_title(item),
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

                # meeting["status"] = self._get_status(meeting)
                # meeting["id"] = self._get_id(meeting)

                yield meeting

    def _parse_title(self, item):
        titleRegex = re.compile(r'(am|pm) : (.)+</td>')
        thisThing = titleRegex.search(item)
        return thisThing.group()[5:-5]

    #TODO: Remove this time_notes parsing, because it just parsing the start time I think
    def _parse_time_notes(self, item):
        timeRegex = re.compile(r'(\d)+/(\d)+/\d\d\d\d')
        thisThing = timeRegex.search(item)
        time_notes = thisThing.group()
        return time_notes

    def _parse_description(self, item):
        descriptionRegex = re.compile(r'Description:(.)+')
        thisThing = descriptionRegex.search(item)
        return thisThing.group()[97:-5]

    def _parse_location(self, item):
        descriptionRegex = re.compile(r'Location:(.)+')
        thisThing = descriptionRegex.search(item)
        return thisThing.group()[91:-5]

    def _parse_start(self, item):
        dateRegex = re.compile(r'(\d)+/(\d)+/\d\d\d\d')
        dateThing = dateRegex.search(item)
        ds = dateThing.group().split("/")
        amRegex = re.compile(r'(\d)+:\d\d')
        amThing = amRegex.search(item)
        amSplit = amThing.group().split(":")

        minutes = 0
        if int(amSplit[1]) > 0:
            minutes = int(amSplit[1])

        d = datetime.datetime(int(ds[2]), int(ds[0]), int(ds[1]), int(amSplit[0]), minutes)
        return d

    # Still working on this, cant seem to find "pm" either
    #It's unclear why I still can't find 'pm', but that being said I think
    #I can use 'to d:dd' or something like that, because the 'to' only happens
    #When there is an end time
    def _parse_end(self, item):
        # amRegex = re.compile(r'(\d)+:\d\d')
        pmRegex = re.compile(r'pm')
        # pmThing = pmRegex.search(item)


        # if linkThing != None:
        #     return "Found"

        return None

    #We don't need the email currently but we do need the occasional link that pops up
    #I don't really understand what it means when they are talking about returning href vs. title, but I'll work on that later I think
    def _parse_links(self, item):
        #Finds the tag inside the href
        linkRegex = re.compile(r'Web address(.)+.aspx(\w)*(\'|\")')
        linkThing = linkRegex.search(item)


        if linkThing != None:
            linkThing = linkRegex.search(item)
            #return linkThing.group()[117:-1]
            return [{"href": str(linkThing.group()[117:-1]), "title": "more info"}]

        #Interested in asking about this in the future
        #Title always equals "more info" - so that seems easy
        #return [{"href": "", "title": ""}]
        return None



    def _parse_classification(self, item):
        return NOT_CLASSIFIED

    def _parse_all_day(self, item):
        return False

    def _parse_source(self, response):
        return response.url
