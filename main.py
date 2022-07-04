import credentials
from selenium import webdriver
from time import sleep
import tkinter as tk
from sys import exit
import chromedriver_binary

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
twitchBrowser = webdriver.Chrome(options=options)
#gmailBrowser = webdriver.Chrome(chrome_options=options)


def closeProgram():
    twitchBrowser.quit()
    exit()

def signin():
    twitchBrowser.get('https://twitch.tv/sergeantlefthand')
    sleep(1)





