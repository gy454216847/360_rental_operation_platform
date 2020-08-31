from time import sleep

from Website.test_case.model import myunit, function
from Website.test_case.page_object.LoginPage import LoginPage


class LoginTest(myunit.StartEnd):
    def test_login_normal(self):
        print('test_login_normal start....')
        po = LoginPage(self.driver)
        po.Login_action('admin', 'password')
        sleep(3)

        self.assertEqual(po.type_loginPass_hint().text, '360租房运营平台')
        function.inser_img(self.driver, 'login_normal.png')
        print('test_login_normal end....')

    def test_login_fail(self):
        print('test_login_fail start.....')
        po = LoginPage(self.driver)
        po.Login_action('admin', '123456')
        sleep(3)

        self.assertEqual(po.type_loginFail_hint().text, '账号或密码错误，请重新输入')
        function.inser_img(self.driver, 'Login_fail.png')
        print('test_login_fail end......')
