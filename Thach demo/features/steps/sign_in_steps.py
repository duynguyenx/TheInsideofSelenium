from behave import given, when, then
from pageobjects.signin.sign_in import SignIn
from pageobjects.homepage.home_page import HomePage
from hamcrest import assert_that, equal_to
from conf import constants


@given('the user is in the login page')
def step_visit_login_page(context):
    context.driver.get(constants.SITE)


@when('the user enters user name "{user_name}"')
def step_enter_user_name(context, user_name):
    SignIn(context.driver).enter_user_name(constants.LINKEDIN_ACCOUNT[user_name]['USER_NAME'])


@when('the user enters user password "{user_name}"')
def step_enter_password(context, user_name):
    SignIn(context.driver).enter_user_password(constants.LINKEDIN_ACCOUNT[user_name]['PASSWORD'])


@when('the user clicks Sign In button')
def step_click_sign_in_button(context):
    SignIn(context.driver).click_sign_in_button()


@then('the profile name is displayed as "{profile_name}"')
def step_assert_profile_name(context, profile_name):
    actual_profile_name = HomePage(context.driver).get_profile_name()
    assert_that(actual_profile_name, equal_to(profile_name), 'Verify Profile Name')
