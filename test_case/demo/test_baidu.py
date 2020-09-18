# -*- coding:utf-8 -*-

from time import sleep
from tools.ui import base_ui

def test_baidu(driver):
    driver.get('http://www.baidu.com')
    driver.send_keys("//*[@id='kw']",'手机')

def test_radio(driver):
    # 打开登陆界面
    # driver.get("http://qa.yansl.com/#/login")
    # #输入用户名
    # driver.send_keys('//input[@placeholder="请输入用户名"]',"admin")
    # #输入密码
    # driver.send_keys('//input[@placeholder="请输入密码"]',"1234567")
    # #点击获取验证码按钮  //span[text()="验证码"]
    # driver.click('//span[text()="验证码"]')
    # #输入验证码
    # driver.send_keys('//input[@placeholder="输入验证码"]',"1111")
    # sleep(2)
    # #点击登录
    # driver.click('//span[text()="登录"]/..')
    # sleep(4)
    # #点击打开运营管理
    # driver.click("//span[text()='运营管理']")
    # # 点击运费模板管理
    # driver.click("//span[text()='运费模板管理']")
    # # 点击添加
    # driver.click("//span[text()='添加']")
    # # 输入模板名称
    # driver.send_keys("//label[text()='模板名称']/../div//input","123456")
    # # 输入发货地址
    # driver.send_keys("//label[text()='发货地址']/../div//input","上海市")
    # # 输入发货期限
    # driver.send_keys("//label[text()='发货期限']/../div//input","30天")
    # # 选择坚决不包邮
    # driver.click("//span[text()='坚决不包邮']")
    # # 输入计费首次数量
    # driver.send_keys("//label[text()='计费首次数量']/../div//input","5")
    # # 输入计费首次价格
    # driver.send_keys("//label[text()='计费首次价格']/../div//input","15元")
    # # 输入计费续件数量
    # driver.send_keys("//label[text()='计费续件数量']/../div//input","8")
    # # 输入计费续件价格
    # driver.send_keys("//label[text()='计费续件价格']/../div//input","8元")
    # # 点击添加
    # driver.click("//button[@class='el-button el-button--primary el-button--medium is-plain']")
    # # 输入包邮门栏
    # driver.send_keys("//label[text()='包邮门栏']/../div//input","12")
    # # 输入首次数量
    # driver.send_keys("//label[text()='首次数量']/../div//input","12")
    # # 输入首次价格
    # driver.send_keys("//label[text()='首次价格']/../div//input","12元")
    # # 输入续件数量
    # driver.send_keys("//label[text()='续件数量']/../div//input","8")
    # # 输入续件价格
    # driver.send_keys("//label[text()='续件价格']/../div//input","12元")
    # # 选择指定地区北京市
    # driver.click("//span[text()='北京市']")
    # # 下滚屏幕
    # driver.scroll_screen_to_element("(//button[@class='el-button el-button--primary el-button--medium'])[2]")
    # # 点击确定
    # driver.click("(//button[@class='el-button el-button--primary el-button--medium'])[2]")
    # # 点击确定
    # driver.click("(//button[@class='el-button el-button--primary el-button--medium'])[1]")
    # 修改
    # driver.click("(//div[text()='胡文星'])/../../td[last()]//span[text()='修改']")
    # # 修改用户名
    # driver.send_keys("//label[text()='模板名称']/../div//input","春江潮水连海平")
    # # 输入发货地址
    # driver.send_keys("//label[text()='发货地址']/../div//input","上海市")
    # # 输入发货期限
    # driver.send_keys("//label[text()='发货期限']/../div//input","30天")
    # # 选择坚决不包邮
    # driver.click("//span[text()='坚决不包邮']")
    # # 输入计费首次数量
    # driver.send_keys("//label[text()='计费首次数量']/../div//input","5")
    # # 输入计费首次价格
    # driver.send_keys("//label[text()='计费首次价格']/../div//input","15元")
    # # 输入计费续件数量
    # driver.send_keys("//label[text()='计费续件数量']/../div//input","8")
    # # 输入计费续件价格
    # driver.send_keys("//label[text()='计费续件价格']/../div//input","8元")
    # # 点击添加
    # driver.click("//button[@class='el-button el-button--primary el-button--medium is-plain']")
    # # 输入包邮门栏
    # driver.send_keys("//label[text()='包邮门栏']/../div//input","12")
    # # 输入首次数量
    # driver.send_keys("//label[text()='首次数量']/../div//input","12")
    # # 输入首次价格
    # driver.send_keys("//label[text()='首次价格']/../div//input","12元")
    # # 输入续件数量
    # driver.send_keys("//label[text()='续件数量']/../div//input","8")
    # # 输入续件价格
    # driver.send_keys("//label[text()='续件价格']/../div//input","12元")
    # # 选择指定地区北京市
    # driver.click("//span[text()='北京市']")
    # # 点击确定
    # driver.click("(//button[@class='el-button el-button--primary el-button--medium'])[2]")
    # # 点击确定
    # driver.click("(//button[@class='el-button el-button--primary el-button--medium'])[1]")
    # 上传图片
    # driver.file_upload("//label[text()='商品图片']/../div//i","D:\\321.png")
    # 检查驱动版本
    # 检查xpath
    # iframe框
    # 界面未加载出来
    driver.switch_to_frame("tag_name=>iframe")
    driver.send_keys("//body[@id='tinymce']","测试一下")
    driver.switch_to_current_frame_out()
    driver.click("(//span[text()='添加'])[1]")






