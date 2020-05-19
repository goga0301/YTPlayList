from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import sys
from os import listdir
from os.path import isfile, join

PATH = r"C:\Program Files\chromedriver.exe"


def getMusics():

    mypath = r"C:\Users\GOGA\Desktop\YTPlayList\Musics"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    musics = []
    for f in onlyfiles:
        musics.append(f)
    return musics


ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument(
    "user-data-dir=C:/Users/GOGA/AppData/Local/Google/Chrome/User Data")


driver = webdriver.Chrome(PATH, chrome_options=ChromeOptions)


def AddToPLaylist(Musics):
    Errored = []
    for m in Musics:
        driver.get("https://www.youtube.com")
        try:

            head = driver.find_element_by_tag_name("ytd-searchbox")
            search = head.find_element_by_id("search")
            search.send_keys(m)

            searchBtn = head.find_element_by_id("search-icon-legacy")
            searchBtn.click()

            sleep(2)
            videoRenderer = driver.find_element_by_tag_name(
                "ytd-video-renderer")
            Video = videoRenderer.find_elements_by_css_selector("#thumbnail")
            Video[0].click()

            sleep(2)
            saveBtnRenderer = driver.find_elements_by_tag_name(
                "ytd-button-renderer")

            saveBtn = saveBtnRenderer[1].find_element_by_xpath(
                "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-button-renderer[2]/a")
            saveBtn.click()

            popup = driver.find_element_by_tag_name("ytd-popup-container")

            sleep(1)
            AddBtn = popup.find_elements_by_id("checkboxContainer")
            AddBtn[1].click()

        except:
            print(sys.exc_info()[0])
            print("error")
            Errored.append(m)
    return Errored


Musics = getMusics()
Errored = AddToPLaylist(Musics)
while True:

    if len(Errored) > 0:
        AddToPLaylist(Errored)
    else:
        break
