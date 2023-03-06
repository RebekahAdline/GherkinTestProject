import logging
import os
import sys
from configparser import ConfigParser

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from helper.helper_web import get_browser


def before_all(context):
    print("Executing before all")
    config = ConfigParser()
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'behave.ini')
    config.read(initfile)

    # Reading the browser type from the configuration file for Selenium Python Tutorial
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helperfunc = helper_func


def before_feature(context, feature):
    print("Before feature\n")
    # Create logger
    context.logger = logging.getLogger('automation_tests')
    context.logger.setLevel(logging.DEBUG)


def after_all(context):
    context.helperfunc.close()
