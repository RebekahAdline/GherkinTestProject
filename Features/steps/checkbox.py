import os
import sys
from behave import then
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))


@then('I Click on first checkbox and second checkbox')
def click_on_checkbox_one(context):
    context.helperfunc.find_by_name('li1').click()
    context.helperfunc.find_by_name('li2').click()