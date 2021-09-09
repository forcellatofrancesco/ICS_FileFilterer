def _check_in(obj, string):
    """
    The 'i' substring of the list 'obj' needs to be in 'string' at least once
    :param obj: list of substring
    :param string: element that needs to be checked
    :return: True if a 'obj' substring is contained in 'string', False otherwise
    """
    for i in obj:
        if i in string:
            return True
    return False


def _check_not_in(obj, string):
    """
    The 'i' substring of the list 'obj' must not be in 'string
    :param obj: list of substring
    :param string: element that needs to be checked
    :return: False if a 'obj' substring is contained in 'string', True otherwise
    """
    for i in obj:
        if i in string:
            return False
    return True


def create_condition(dictionary):
    res = Condition()
    res.locations['in'] = dictionary['location']['in']
    res.locations['not_in'] = dictionary['location']['not_in']
    res.summaries['in'] = dictionary['summaries']['in']
    res.summaries['not_in'] = dictionary['summaries']['not_in']
    res.descriptions['in'] = dictionary['descriptions']['in']
    res.descriptions['not_in'] = dictionary['descriptions']['not_in']
    res.dtstarts['in'] = dictionary['dtstarts']['in']
    res.dtstarts['not_in'] = dictionary['dtstarts']['not_in']
    res.dtends['in'] = dictionary['dtends']['in']
    res.dtends['not_in'] = dictionary['dtends']['not_in']
    res.exdates['in'] = dictionary['exdates']['in']
    res.exdates['not_in'] = dictionary['exdates']['not_in']
    return res


class Condition:
    def __init__(self):
        self.locations = {"in": [], "not_in": []}
        self.summaries = {"in": [], "not_in": []}
        self.descriptions = {"in": [], "not_in": []}
        self.dtstarts = {"in": [], "not_in": []}
        self.dtends = {"in": [], "not_in": []}
        self.exdates = {"in": [], "not_in": []}

    def check_location(self, string):
        """
        This function is used to check if a custom location is contained in string
        :param string: element to be checked
        :return: True if it is contained in the 'in' list in the settings, True if it is not contained in the 'not_in'
        list
        """
        return _check_in(self.locations['in'], string) or _check_not_in(self.locations['not_in'], string)

    def check_summaries(self, string):
        """
        This function is used to check if a custom summary is contained in string
        :param string: element to be checked
        :return: True if it is contained in the 'in' list in the settings, True if it is not contained in the 'not_in'
        list
        """
        return _check_in(self.summaries['in'], string) or _check_not_in(self.summaries['not_in'], string)

    def check_descriptions(self, string):
        """
        This function is used to check if a custom description is contained in string
        :param string: element to be checked
        :return: True if it is contained in the 'in' list in the settings, True if it is not contained in the 'not_in'
        list
        """
        return _check_in(self.descriptions['in'], string) or _check_not_in(self.descriptions['not_in'], string)

    def check_dtstarts(self, string):
        """
        This function is used to check if a custom dtstart is contained in string
        :param string: element to be checked
        :return: True if it is contained in the 'in' list in the settings, True if it is not contained in the 'not_in'
        list
        """
        return _check_in(self.dtstarts['in'], string) or _check_not_in(self.dtstarts['not_in'], string)

    def check_dtends(self, string):
        """
        This function is used to check if a custom dtend is contained in string
        :param string: element to be checked
        :return: True if it is contained in the 'in' list in the settings, True if it is not contained in the 'not_in'
        list
        """
        return _check_in(self.dtends['in'], string) or _check_not_in(self.dtends['not_in'], string)

    def check_exdates(self, string):
        """
        This function is used to check if a custom exdate is contained in string
        :param string: element to be checked
        :return: True if it is contained in the 'in' list in the settings, True if it is not contained in the 'not_in'
        list
        """
        return _check_in(self.exdates['in'], string) or _check_not_in(self.exdates['not_in'], string)
