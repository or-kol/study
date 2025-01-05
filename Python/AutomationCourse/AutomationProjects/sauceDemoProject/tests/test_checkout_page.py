import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from utils.config_reader import ConfigReader
from utils.general_helpers import GeneralHelp


class TestCheckoutPage:

    def get_to_checkout_page(self):
        prod_list_page = GeneralHelp.login(self)
        GeneralHelp.add_product_to_cart(self, prod_list_page, "Sauce_Labs_Bolt_T-Shirt_position")
        prod_list_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.go_to_checkout_page()

        return CheckoutPage(self.driver)


    valid_checkout_info = [("first_name1", "last_name1", "zip1"),
                     ("first_name2", "last_name2", "zip2"),
                     ("first_name3", "last_name3", "zip3"),
                     ("first_name4", "last_name4", "zip4"),
                     ("first_name5", "last_name5", "zip5")]

    @pytest.mark.parametrize("first_name, last_name, zip", valid_checkout_info)
    def test_fill_checkout_info_valid_info(self, first_name, last_name, zip):
        first_name = ConfigReader.read_config("valid_checkout_data", first_name)
        last_name = ConfigReader.read_config("valid_checkout_data", last_name)
        zip = ConfigReader.read_config("valid_checkout_data", zip)

        checkout_page = self.get_to_checkout_page()
        checkout_page.fill_info(first_name, last_name, zip)

        overview_page = OverviewPage(self.driver)

        expected_result = "Checkout: Overview"
        actual_result = overview_page.get_overview_page_title()

        assert expected_result == actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    invalid_checkout_info = [("first_name1", "last_name1", "zip1"),
                           ("first_name2", "last_name2", "zip2"),
                           ("first_name3", "last_name3", "zip3"),]

    @pytest.mark.parametrize("first_name, last_name, zip", invalid_checkout_info)
    def test_fill_checkout_info_missing_info(self, first_name, last_name, zip):
        first_name = ConfigReader.read_config("invalid_checkout_data", first_name)
        last_name = ConfigReader.read_config("invalid_checkout_data", last_name)
        zip = ConfigReader.read_config("invalid_checkout_data", zip)

        checkout_page = self.get_to_checkout_page()
        checkout_page.fill_info(first_name, last_name, zip)

        expected_result = ""
        if first_name == "":
                expected_result = "Error: First Name is required"
        elif last_name == "":
                expected_result = "Error: Last Name is required"
        elif zip == "":
                expected_result = "Error: Postal Code is required"

        actual_result = checkout_page.get_checkout_error_msg()

        assert expected_result == actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    def test_cancel_button(self):
        checkout_page = self.get_to_checkout_page()
        checkout_page.go_back_to_cart()

        cart_page = CartPage(self.driver)

        expected_result = "Your Cart"
        actual_result = cart_page.get_cart_page_title()

        assert expected_result == actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"
