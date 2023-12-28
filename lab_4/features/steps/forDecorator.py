from behave import *
from Decorator import Window, Border, Thick

@given('an empty window')
def step_given_empty_window(context):
    context.window = Window()

@given('the border is given')
def step_given_border(context):
    context.border = Border(context.window)

@given('a thick is given')
def step_given_thick(context):
    context.thick = Thick(context.border)

@when('the window works flawlessly')
def step_when_window_works(context):
    context.result = context.window.do_work()

@when('performing work at the border')
def step_when_border_works(context):
    context.result = context.border.do_work()

@when('wonderful work in a thick border')
def step_when_thick_border_works(context):
    context.result = context.thick.do_work()

@then('get the result {expected}')
def step_then_expected_result(context, expected):
    assert context.result == expected, f"Error: expect {expected}, get {context.result}"
