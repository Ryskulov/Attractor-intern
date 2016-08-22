import subprocess

from lettuce import before, after, world
from selenium import webdriver

from mapping import site_mapping


@before.harvest
def setup(server):
    pid_server = subprocess.Popen('python3 server.py', shell=True)
    world.browser = webdriver.Firefox()
    world.mapping = site_mapping

# @after.all
# def teardown(total):
#     world.browser.close()
