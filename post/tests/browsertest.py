from selenium import webdriver
import unittest

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_homepage(self):
        self.browser.get('http://localhost:7000')
        assert '5e' in self.browser.title
        self.fail('finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')