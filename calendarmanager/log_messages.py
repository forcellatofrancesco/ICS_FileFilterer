global messages


def init(settings):
    """
    Function to initialize the global object that contains all the messages
    :param settings: this contains all the languages with all the default sentences per language
    """
    global messages
    messages = Messages(settings)


class Messages:
    def __init__(self, settings):
        self.load_calendar = settings['log_messages'][settings['language']]['load_calendar']
        self.load_settings = settings['log_messages'][settings['language']]['load_settings']
        self.loading_file = settings['log_messages'][settings['language']]['loading_file']
        self.file_not_found = settings['log_messages'][settings['language']]['file_not_found']
        self.successful_calendars = settings['log_messages'][settings['language']]['successful_calendars']
        self.events_filtered = settings['log_messages'][settings['language']]['events_filtered']
        self.file_closed = settings['log_messages'][settings['language']]['file_closed']
        self.all_files_closed = settings['log_messages'][settings['language']]['all_files_closed']
        self.output_created = settings['log_messages'][settings['language']]['output_created']
        self.total_events = settings['log_messages'][settings['language']]['total_events']
        self.exec_time = settings['log_messages'][settings['language']]['exec_time']
        self.event = settings['log_messages'][settings['language']]['event']
