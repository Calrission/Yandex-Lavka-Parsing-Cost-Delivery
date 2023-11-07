import json

from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from time import sleep

driver = Chrome()
driver.get("https://lavka.yandex.ru/")

with open("cookies.json", encoding="utf-8", mode="r") as file:
    cookies = json.loads(file.read())
    for cookie in cookies:
        print(f"Куки {cookie} добавлено")
        driver.add_cookie(cookie)


def wait_such_element(by: By, value: str, interval: int = 1, limit: int = -1) -> WebElement | None:
    attempt = 0
    while True:
        try:
            if attempt == limit:
                return None
            attempt += 1
            return driver.find_element(by, value)
        except NoSuchElementException:
            sleep(interval)


driver.refresh()

info = wait_such_element(By.CSS_SELECTOR, "#root > div.hjhf26i > header > div:nth-child(6) > button")
info.click()

block = wait_such_element(By.CLASS_NAME, "d1brmuze")
block.screenshot("result.png")

input("Далее")
