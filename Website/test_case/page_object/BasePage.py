from time import sleep

import yaml

from Website.test_case.model.fixture import filepath

yamlfile = filepath() + '/Setting/' + 'url.yaml'
file = open(yamlfile, encoding='utf-8')
data = yaml.load(file, Loader=yaml.FullLoader)
url = data['base_url']


class Page():

    def __init__(self, driver):
        self.driver = driver
        self.url = url
        self.timeout = 20

    def open(self):
        self.driver.get(url)
        sleep(2)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
