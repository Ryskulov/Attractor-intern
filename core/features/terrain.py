import subprocess
from time import sleep

from lettuce import after, world, before
from selenium import webdriver

from mapping import site_mapping


@before.all
def setup():
    world.server_pid = subprocess.Popen('python3 server.py', shell=True)
    world.browser = webdriver.Firefox()
    world.mapping = site_mapping


@after.all
def teardown(total):
    sleep(10)
    world.browser.close()
    world.server_pid.kill()