from selenium.webdriver.common.by import By

from Website.test_case.page_object.BasePage import Page


class LoginPage(Page):
    username_loc = (By.CLASS_NAME, 'el-input__inner')
    password_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div/section[3]/div[2]/div/input')
    submit_loc = (By.CLASS_NAME, 'btn_login')

    def Login_action(self, username, password):
        self.open()
        username_text = self.find_element(*self.username_loc)
        password_text = self.find_element(*self.password_loc)
        submit_btn = self.find_element(*self.submit_loc)
        username_text.clear()
        username_text.send_keys(username)
        password_text.clear()
        password_text.send_keys(password)
        submit_btn.click()

    LoginFail_loc = (By.CLASS_NAME, 'info_wrap-p')
    LoginPass_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/section/h1')

    def type_loginPass_hint(self):
        return self.find_element(*self.LoginPass_loc)

    def type_loginFail_hint(self):
        return self.find_element(*self.LoginFail_loc)
