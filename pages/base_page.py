
class BasePage(object):
    """Base class to initialize the base page that will be called from all page"""

    def __init__(self, driver):
        self.driver = driver
