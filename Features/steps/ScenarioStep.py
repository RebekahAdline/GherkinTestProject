import os
import sys

from behave import given

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))


@given('I go to 4davanceboy to add item')
def step(context):
    context.helperfunc.open('https://lambdatest.github.io/sample-todo-app/')
    context.helperfunc.maximize()