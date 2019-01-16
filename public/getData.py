import os
from public.openFile import open_yaml
from selenium.webdriver.common.by import By

def get_data(name):
    data = open_yaml("element.yaml")
    element_type = data[name].split(":")[0]
    element_value = data[name].split(":")[1]
    if element_type == "id":
        return (By.ID, element_value)
    elif element_type == "name":
        return (By.NAME, element_value)
    elif element_type == "tagName":
        return (By.TAG_NAME, element_value)
    elif element_type == "linkText":
        return (By.LINK_TEXT, element_value)
    elif element_type == "className":
        return (By.CLASS_NAME, element_value)
    elif element_type == "xpath":
        return (By.XPATH, element_value)