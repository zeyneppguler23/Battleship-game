class TestReport:
    def __init__(self, filename):
        self.filename = filename
        # Create the file in the initializer
        with open(self.filename, 'w') as f:
            f.write("Test Report\n")
            f.write("===========\n\n")

    def add_message(self, message):
        # Open the file in append mode and add the message
        with open(self.filename, 'a') as f:
            f.write(message + "\n")


def is_list_of_lists(obj, subtype):
    """
    Used to test if an object is a list of lists of a certain type
    """
    if not isinstance(obj, list):
        return False
    for sublist in obj:
        if not isinstance(sublist, list):
            return False
        if not all(isinstance(item, subtype) or item is None for item in sublist):
            return False
    return True


def is_dict_of_type(obj, key_type, value_type):
    """
    Used to test if an object is a dictionary of a certain type
    """
    if not isinstance(obj, dict):
        return False
    for key, value in obj.items():
        if not isinstance(key, key_type) or not isinstance(value, value_type):
            return False
    return True


def tuple_of_type(obj, type1, type2):
    """
    Used to test if an object is a tuple of a certain type
    """
    if not isinstance(obj, tuple):
        return False
    for item in obj:
        if not isinstance(item, type1) and not isinstance(item, type2):
            return False
    return True
