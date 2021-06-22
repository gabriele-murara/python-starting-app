import sys
import argparse
from settings import defaults, constants
from config import Configuration
from app import App

app_description = "{} ({}) version {} ".format(
    constants.__app_name__, constants.__app_alias__, constants.__version__
)
def getOptions(args=sys.argv[1:]):
    description = app_description
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-c", "--config", help="Your configuration file.")
    parser.add_argument(
        "-v", "--version", help="Print version and exit.", action="store_true"
    )
    options = parser.parse_args(args)
    return options

options = getOptions()
if options.version:
    print(app_description)
    exit(0)


settings_module = 'defaults'
if options.config is not None:
    settings_module = options.config
else:
    msg = "No configuration file passed. Use the default setting module '{}'";
    print(msg.format(settings_module))

configuration = Configuration(settings_module)
dict = configuration.get()
logger = configuration.get_logger()

app = App(configuration)
app.start()
