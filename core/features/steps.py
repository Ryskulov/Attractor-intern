from lettuce import step, world


@step(r'Open "(.*)" page')
def open_page(step, page):
    world.current_page = world.mapping[page]
    world.browser.get(world.current_page['url'])


@step(r'Fill "(.*)" with "(.*)"')
def fill_element_with_text(step, element, value):
    elem = world.browser.find_element_by_xpath(world.current_page[element])
    elem.send_keys(value)


@step(r'Click "(.*)"')
def i_click_xpath(step, element):
    elem = world.browser.find_element_by_xpath(world.current_page[element])
    elem.click()


# @step(r'See "(.*)" in "(.*)"')
# def i_see_text_in_element(step, text, element):
#     elem = world.browser.find_element_by_xpath(world.current_page[element])
#     assert elem.text == text