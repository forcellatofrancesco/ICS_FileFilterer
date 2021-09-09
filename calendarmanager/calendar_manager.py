from icalendar import Calendar
from calendarmanager import logger, log_messages
from calendarmanager.condition import Condition
from requests import get
import re

IS_URL_REGEX = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def filter_events(cal, condition: Condition):
    """
    Function that filters all the events of a given calendar
    :param cal: calendar to be filtered
    :param condition: custom condition that needs to be checked
    :return: list of filtered elements
    """
    events = []
    for component in cal.walk():
        if component.name == 'VEVENT':
            summary = component.get('summary')
            description = component.get('description')
            location = component.get('location')
            dtstart = component.get('dtstart').dt
            dtend = component.get('dtend').dt
            exdate = component.get('exdate')
            latest_element = events[len(events) - 1] if len(events) > 0 else None
            if (latest_element is None
                or (latest_element.get('dtstart').dt != dtstart
                    and latest_element.get('dtend').dt != dtend)) \
                    and condition.check_location(location) \
                    and condition.check_dtends(dtend) \
                    and condition.check_descriptions(description) \
                    and condition.check_dtstarts(dtstart) \
                    and condition.check_exdates(exdate) \
                    and condition.check_summaries(summary):
                events.append(component)
    logger.global_logger.log_info(log_messages.messages.events_filtered % (len(cal.walk()), len(events)))
    return events


def is_url(string):
    """
    Function used to check if a string is a valid URL
    :param string: element to be checked
    :return: True if string is an URL, False otherwise
    """
    global IS_URL_REGEX
    return re.match(IS_URL_REGEX, string) is not None


def files_to_calendar(file_list):
    """
    Function that open multiple files and returns the list of opened files and the list of calendar created
    :param file_list: list of .ics input files that contains all the events
    :return: list of created calendars, list of opened files
    """
    c_list = []
    f_list = []
    for f in file_list:
        logger.global_logger.log_info(log_messages.messages.loading_file % f)
        if is_url(f):
            r = get(f, allow_redirects=True)
            c_list.append(Calendar.from_ical(r.content))
        else:
            try:
                f_list.append(open(f, 'rb'))
                c_list.append(Calendar.from_ical(f_list[len(f_list) - 1].read()))
            except FileNotFoundError:
                logger.global_logger.log_error(log_messages.messages.file_not_found % f)
    logger.global_logger.log_info(log_messages.messages.successful_calendars % (len(c_list), len(file_list)))
    return c_list, f_list


def create_ics_file(event_list, file_name):
    """
    Function that creates the output files that contains all the filtered events
    :param event_list: list of events to be printed on the file
    :param file_name: output file name
    """
    f = open(file_name, 'wb')
    cal = Calendar()
    for event in event_list:
        cal.add_component(event)
    f.write(cal.to_ical())
    f.close()
    logger.global_logger.log_ok(log_messages.messages.output_created)
