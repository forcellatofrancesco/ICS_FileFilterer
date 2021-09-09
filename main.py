from calendarmanager.calendar_manager import files_to_calendar, filter_events, create_ics_file
from calendarmanager.condition import create_condition
from calendarmanager.util import json_parser, event_printer
from threading import Thread
from calendarmanager import logger
from time import time
from calendarmanager import log_messages


def main():
    t = time()  # for debugging purpose it allows to get the execution time
    settings = json_parser('settings.json')  # this parses the setting.json file into a Python dictionary
    log_messages.init(settings)
    logger.init(settings['verbose'], settings['cursor'])
    logger.global_logger.log_ok(log_messages.messages.load_settings)
    # this converts all the input files into a calendar list and a list of opened files.
    calendar_list, ics_file_list = files_to_calendar(settings['calendar_files'])
    logger.global_logger.log_ok(log_messages.messages.load_calendar)
    # this create the condition object used for filtering the input events
    condition = create_condition(settings['conditions'])
    events = []
    for calendar in calendar_list:
        # this extends the list of filtered events with a new list of filtered events by the given calendar
        events.extend(filter_events(calendar, condition))
    logger.global_logger.log_info(log_messages.messages.total_events % len(events))
    # the opened input files are now useless, this closes all the opened files
    for file in ics_file_list:
        file.close()
        logger.global_logger.log_info(log_messages.messages.file_closed % file.name)
    logger.global_logger.log_ok(log_messages.messages.all_files_closed)
    # for optimization purpose, 2 threads are created
    th1 = Thread(target=event_printer, args=[events])  # this one print all the filtered elements on the terminal
    # this one creates the output file
    th2 = Thread(target=create_ics_file, args=[events, settings['output_file']])
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    logger.global_logger.log_ok(log_messages.messages.exec_time % (time() - t))


if __name__ == '__main__':
    main()
