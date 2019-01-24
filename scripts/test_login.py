import allure


def test_a():
    print('aaa')
    assert 1

@allure.step(title="测试登陆的流程")
def test_login():
    allure.attach("登录","输入用户名")
    print("bbbb")

    allure.attach('登录',"输入密码")
    print('cccc')

    allure.attach('登录',"点击登录")
    assert 0
