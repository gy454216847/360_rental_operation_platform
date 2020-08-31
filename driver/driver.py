from selenium import webdriver


def browser():
    # driver = webdriver.Chrome()
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=option)
    return driver


if __name__ == '__main__':
    browser()
