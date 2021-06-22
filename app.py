

class App():

    def __init__(self, configuration):
        self._configuration = configuration

    def start(self):
        msg = "Do anything you want"
        print(msg)
        self._configuration.get_logger().debug(msg)
