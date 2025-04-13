from autoQA.pages.homepage import HomePage
from autoQA.pages.product import ProductPage


def test_start(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.galaxy()
    product_page = ProductPage(browser)
    product_page.check_title('Samsung galaxy s6')