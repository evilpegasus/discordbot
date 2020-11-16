from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep
import asyncio

from secrets import aternos_username, aternos_password

options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(options = options)

def login():
    login_url = "https://aternos.org/go/"
    driver.get(login_url)

    element = driver.find_element_by_xpath('//*[@id="user"]')
    element.send_keys(aternos_username)
    element = driver.find_element_by_xpath('//*[@id="password"]')
    element.send_keys(aternos_password)
    element = driver.find_element_by_xpath('//*[@id="login"]')
    element.click()

async def start_server():
    """ Starts the server by clicking on the start button.
        The try except part tries to find the confirmation button, and if it 
        doesn't, it continues to loop until the confirm button is clicked."""
    login()
    await asyncio.sleep(5)
    element = driver.find_element_by_xpath("/html/body/div/main/section/div/div[2]/div[1]/div[1]")
    element.click()
    await asyncio.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="start"]')
    element.click()
    await asyncio.sleep(10)
    element = driver.find_element_by_xpath('//*[@id="nope"]/main/div/div/div/main/div/a[1]')
    element.click()
    state = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[2]/div/div/span[2]/span')
    while state.text == "Waiting in queue":
        state = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[2]/div/div/span[2]/span')
        try:
            element = driver.find_element_by_xpath('//*[@id="confirm"]')
            element.click()
        except ElementNotInteractableException as e:
            pass
    print("Server started!")
    driver.close()
login()
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server())
# driver.quit()