from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time



def index(request):
    return render(request, "messageLoop/templates/index.html", {})


def doMessage(request):
    doMessageFoo(request.POST['contact'],request.POST['message'],request.POST['frequency'])
    return render(request, "messageLoop/templates/index.html", {})
    





def doMessageFoo(contact,message,frequency):
    #print(contact,message,frequency)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    contact = contact
    text = message
    driver.get("https://web.whatsapp.com")
    print("Scan QR Code, And then Enter")
    input()
    print("Logged In")
    inp_xpath_search = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    input_box_search = WebDriverWait(driver, 50).until(
        lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    input_box_search.click()
    time.sleep(2)
    input_box_search.send_keys(contact)
    time.sleep(2)
    selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
    selected_contact.click()

    for i in range(0,int(frequency)):
        inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        input_box = driver.find_element_by_xpath(inp_xpath)
        input_box.send_keys(text + Keys.ENTER)