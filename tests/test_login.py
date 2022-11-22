from pages.login_page import LoginPage
import pytest


class TestLogin:

    @pytest.mark.smoke
    def test_feathr_login_page_title(self):
        login_page = LoginPage()
        login_page.navigate_to_feathr()
        assert login_page.is_page_title_correct()

    @pytest.mark.sanity
    def test_feathr_invalid_login(self):
        login_page = LoginPage()

        invalid_email_address = "invalid@test.com"
        invalid_password = "Invalid@123"
        invalid_login_message = "You were unable to sign in. Check your email and password, and try again."

        login_page.navigate_to_feathr()
        login_page.enter_email(invalid_email_address)
        login_page.enter_password(invalid_password)
        login_page.click_sign_in_button()
        assert login_page.get_alert_message_text() == invalid_login_message

    @pytest.mark.sanity
    def test_forgot_password(self):
        login_page = LoginPage()

        email_address = "valid@test.com"

        login_page.navigate_to_feathr()
        login_page.click_forgot_your_password_link()
        assert login_page.is_send_me_instructions_button_disabled()
        login_page.enter_email(email_address)
        assert not login_page.is_send_me_instructions_button_disabled()
        login_page.click_return_to_login_link()
        assert login_page.is_sign_in_button_present()

    @pytest.mark.smoke
    def test_feathr_request_demo(self):
        login_page = LoginPage()
        login_page.navigate_to_feathr()
        login_page.click_request_a_demo()
        assert 'demo' in login_page.get_browser_url()

    @pytest.mark.skip
    def test_feathr_valid_login(self):
        # TODO Get valid credentials
        assert True
