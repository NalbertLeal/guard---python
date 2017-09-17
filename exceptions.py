
class Empty_folder(Exception):
    """ When the main folder is empty this exception will be launch. """
    def __init__(self):
        super(EmptyFolder, self).__init__('This folder is empty.')

class Root_folder_not_directory(Exception):
    """ When the main folder is empty this exception will be launch. """
    def __init__(self):
        super(EmptyFolder, self).__init__('Root folder not directory')
