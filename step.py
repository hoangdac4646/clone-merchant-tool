from typing import List

from selenium.webdriver.android import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UIElements import UIElement, IdentifyElement, InputCbbElement, InputTxtElement, ButtonElement


class TestStep:
    id: int
    name: str
    ui_elements: List[UIElement]
    web_driver: webdriver

    weight: int = 0
    env: str
    url = ''
    is_active: bool = True

    __identify_elements: List[IdentifyElement]
    __input_txt_elements: List[InputCbbElement]
    __input_cbb_elements: List[InputTxtElement]
    __button_elements: List[ButtonElement]

    def execute(self):
        pass

    def __init__(self,
                 id: int,
                 name: str,
                 web_driver: webdriver,
                 url: str,
                 ui_elements: List[UIElement],
                 weight: int = 0,
                 env: str = 'dev',
                 is_active: bool = True,
                 ):
        self.id = id
        self.name = name
        self.web_driver = web_driver
        self.url = url
        self.ui_elements = ui_elements
        self.weight = weight
        self.env = env
        self.is_active = is_active

        for element in self.ui_elements:
            pass

    def identify(self):
        for element in self.__identify_elements:
            WebDriverWait(self.web_driver, 10).until(
                EC.presence_of_element_located((By.XPATH, element)))

    def submit_form(self, mode: str):
        pass


