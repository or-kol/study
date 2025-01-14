import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsList(BasePage):

    SAUCE_LABS_BACKPACK_BTN = (By.CSS_SELECTOR, "#item_4_title_link")
    SAUCE_LABS_BIKE_LIGHT_BTN = (By.CSS_SELECTOR, "#item_0_title_link")
    SAUCE_LABS_BOLT_TSHIRT_BTN = (By.CSS_SELECTOR, "#item_1_title_link")
    SAUCE_LABS_FLEECE_JACKET_BTN = (By.CSS_SELECTOR, "#item_5_title_link")
    SAUCE_LABS_ONESIE_BTN = (By.CSS_SELECTOR, "#item_2_title_link")
    TEST_ALL_THE_THINGS_BTN = (By.CSS_SELECTOR, "#item_3_title_link")
    GO_TO_CART_BTN = (By.CSS_SELECTOR, "#shopping_cart_container")
    PRODUCT_LIST_PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    SAUCE_LABS_BACKPACK_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    SAUCE_LABS_BIKE_LIGHT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
    SAUCE_LABS_BOLT_TSHIRT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    SAUCE_LABS_FLEECE_JACKET_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
    SAUCE_LABS_ONESIE_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    TEST_ALL_THE_THINGS_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id^='add-to-cart-test']")
    SAUCE_LABS_BACKPACK_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    SAUCE_LABS_BIKE_LIGHT_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-bike-light")
    SAUCE_LABS_BOLT_TSHIRT_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt")
    SAUCE_LABS_FLEECE_JACKET_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-fleece-jacket")
    SAUCE_LABS_ONESIE_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")
    TEST_ALL_THE_THINGS_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "[id^='remove-test']")
    PRODUCT_SORT = (By.CSS_SELECTOR, ".product_sort_container")
    CART_BADGE = (By.CSS_SELECTOR, "#shopping_cart_container")
    PRODUCTS_NAMES_LIST = (By.CSS_SELECTOR,
            ".inventory_list>.inventory_item>.inventory_item_description>.inventory_item_label>[data-test$='title-link']>.inventory_item_name")
    PRODUCTS_PRICES_LIST = (By.CSS_SELECTOR,
            ".inventory_list>.inventory_item>div.inventory_item_description>div.pricebar>div")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Go to product page (product number in DB is : {prod})")
    def go_to_prod_page(self, prod):
        match prod:
            case 1:
                self.click(self.SAUCE_LABS_BACKPACK_BTN)
            case 2:
                self.click(self.SAUCE_LABS_BIKE_LIGHT_BTN)
            case 3:
                self.click(self.SAUCE_LABS_BOLT_TSHIRT_BTN)
            case 4:
                self.click(self.SAUCE_LABS_FLEECE_JACKET_BTN)
            case 5:
                self.click(self.SAUCE_LABS_ONESIE_BTN)
            case 6:
                self.click(self.TEST_ALL_THE_THINGS_BTN)
            case _:
                print(f"{prod} is invalid input")

    @allure.step("Get products list page title")
    def get_prod_list_page_title(self):
        return self.get_text(self.PRODUCT_LIST_PAGE_TITLE)

    @allure.step("Add product to cart from products list page (product number in DB is : {prod})")
    def quick_add_item_to_cart(self, prod):
        match prod:
            case 1:
                self.click(self.SAUCE_LABS_BACKPACK_ADD_TO_CART_BTN)
            case 2:
                self.click(self.SAUCE_LABS_BIKE_LIGHT_ADD_TO_CART_BTN)
            case 3:
                self.click(self.SAUCE_LABS_BOLT_TSHIRT_ADD_TO_CART_BTN)
            case 4:
                self.click(self.SAUCE_LABS_FLEECE_JACKET_ADD_TO_CART_BTN)
            case 5:
                self.click(self.SAUCE_LABS_ONESIE_ADD_TO_CART_BTN)
            case 6:
                self.click(self.TEST_ALL_THE_THINGS_ADD_TO_CART_BTN)
            case _:
                print(f"{prod} is invalid input")

    @allure.step("Remove product from cart from products list page (product number in DB is : {prod})")
    def quick_remove_item_from_cart(self, prod):
        match prod:
            case 1:
                self.click(self.SAUCE_LABS_BACKPACK_REMOVE_FROM_CART_BTN)
            case 2:
                self.click(self.SAUCE_LABS_BIKE_LIGHT_REMOVE_FROM_CART_BTN)
            case 3:
                self.click(self.SAUCE_LABS_BOLT_TSHIRT_REMOVE_FROM_CART_BTN)
            case 4:
                self.click(self.SAUCE_LABS_FLEECE_JACKET_REMOVE_FROM_CART_BTN)
            case 5:
                self.click(self.SAUCE_LABS_ONESIE_REMOVE_FROM_CART_BTN)
            case 6:
                self.click(self.TEST_ALL_THE_THINGS_REMOVE_FROM_CART_BTN)
            case _:
                print(f"{prod} is invalid input")

    @allure.step("Go to cart")
    def go_to_cart(self):
        self.click(self.GO_TO_CART_BTN)

    @allure.step("Get the product in position {n} in the page")
    def get_nth_product_in_page(self, n):
        return self.get_text((By.CSS_SELECTOR, f"#inventory_container>div>div:nth-child({n}).inventory_item"))

    @allure.step("Sort products list")
    def sort_products(self, option):
        self.select_option(self.PRODUCT_SORT, option)

    @allure.step("Get amount of products in cart")
    def get_amount_of_prod_in_cart(self):
        return self.get_text(self.CART_BADGE)

    @allure.step("Get products names list from in products list page")
    def get_products_names_list(self):
        return [element.text for element in self.get_elements_list(self.PRODUCTS_NAMES_LIST)]

    @allure.step("Get products prices list from in products list page")
    def get_products_prices_list(self):
        return [element.text for element in self.get_elements_list(self.PRODUCTS_PRICES_LIST)]

