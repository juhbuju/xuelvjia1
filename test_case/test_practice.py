
from time import sleep

import allure
# @allure.feature("用户模块")
# @allure.story("用户登录")
# @allure.title("登录")
# @allure.step("登录")
def test_radio(driver):
    #打开登陆界面
    driver.get("http://qa.yansl.com/#/login")
    #输入用户名
    driver.send_keys('//input[@placeholder="请输入用户名"]',"admin")
    #输入密码
    driver.send_keys('//input[@placeholder="请输入密码"]',"1234567")
    #点击获取验证码按钮  //span[text()="验证码"]
    driver.click('//span[text()="验证码"]')
    #输入验证码
    driver.send_keys('//input[@placeholder="输入验证码"]',"1111")
    sleep(2)
    #点击登录
    driver.click('//span[text()="登录"]/..')
    sleep(4)
# @allure.step("打开运营管理")
# def test_radio_1(driver):
#     # 点击商品管理
#     driver.click("//span[text()='运营管理']")
#     # 点击运费模板管理
#     driver.click("//span[text()='运费模板管理']")
#     # 点击添加
#     driver.click("//span[text()='添加']")
#     # 输入模板名称
#     driver.send_keys("//label[text()='模板名称']/../div//input","胡文星")
#     # 输入发货地址
#     driver.send_keys("//label[text()='发货地址']/../div//input","上海市")
#     # 输入发货期限
#     driver.send_keys("//label[text()='发货期限']/../div//input","30天")
#     # 选择坚决不包邮
#     driver.click("//span[text()='坚决不包邮']")
#     # 输入计费首次数量
#     driver.send_keys("//label[text()='计费首次数量']/../div//input","5")
#     # 输入计费首次价格
#     driver.send_keys("//label[text()='计费首次价格']/../div//input","15元")
#     # 输入计费续件数量
#     driver.send_keys("//label[text()='计费续件数量']/../div//input","8")
#     # 输入计费续件价格
#     driver.send_keys("//label[text()='计费续件价格']/../div//input","8元")
#     # 点击添加
#     driver.click("//button[@class='el-button el-button--primary el-button--medium is-plain']")
#     # 输入包邮门栏
#     driver.send_keys("//label[text()='包邮门栏']/../div//input","12")
#     # 输入首次数量
#     driver.send_keys("//label[text()='首次数量']/../div//input","12")
#     # 输入首次价格
#     driver.send_keys("//label[text()='首次价格']/../div//input","12元")
#     # 输入续件数量
#     driver.send_keys("//label[text()='续件数量']/../div//input","8")
#     # 输入续件价格
#     driver.send_keys("//label[text()='续件价格']/../div//input","12元")
#     # 选择指定地区北京市
#     driver.click("//span[text()='北京市']")
#     # 点击确定
#     driver.click("(//button[@class='el-button el-button--primary el-button--medium'])[2]")
#     # 点击确定
#     driver.click("(//button[@class='el-button el-button--primary el-button--medium'])[1]")
# @allure.step("修改")
# def test_radio_2(driver):
#     # 点击修改
#     driver.click("//div[text()='胡文星']/../following-sibling::td[last()]//button[1]")
#     # 输入计费首次数量
#     driver.send_keys("//label[text()='计费首次数量']/../div//input","10")
#     # 点击确认
#     driver.click("(//span[text()='确定'])[2]")
# # @allure.step("删除")
# def test_radio_3(driver):
#     # 删除
#     driver.click("//div[text()='胡文星']/../following-sibling::td[last()]//button[@class='el-button el-button--danger el-button--mini']")
#     driver.click("//button[@class='el-button el-button--default el-button--small el-button--primary ']")
#     pass