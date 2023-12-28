from behave import *
import Fabric_method

@given('a polar point with radius {radius:d} and angle {angle:d} degrees')
def step_impl(context, radius, angle):
    context.radius = radius
    context.angle = angle

@when('converting the polar point to Cartesian coordinates')
def step_impl(context):
    context.result = Fabric_method.Polar().Print(context.radius, context.angle)

@then('the resulting Cartesian coordinates should be x: {result_x:f}, y: {result_y:f}')
def step_impl(context, result_x, result_y):
    assert str(context.result) == f'x: {result_x}, y: {result_y}', f"Error: expected {result_x}, {result_y} but got {context.result_x}, {context.result_y}."



@given('a Cartesian point with x-coordinate {x:d} and y-coordinate {y:d}')
def step_impl(context, x, y):
    context.x = x
    context.y = y

@when('converting the Cartesian point to polar coordinates')
def step_impl(context):
    context.result = Fabric_method.Decart().Print(context.x, context.y)

@then('the resulting coordinates should be x: {result_x:w}, y: {result_y:w}')
def step_impl(context, result_x, result_y):
    assert str(context.result) == f'x: {result_x}, y: {result_y}', f"Error: expected {result_x}, {result_y} but got {context.result_x}, {context.result_y}."