from asyncio import sleep

from tools.ui import base_ui

def test_tms_1(driver):
    # 打开登陆界面
    driver.get("http://192.168.1.156:8080/")
    # 输入账户
    driver.send_keys("//input[@id='username']","test")
    # 输入密码
    driver.send_keys("//input[@id='password']","123456")
    # 点击登录
    driver.click("//span[text()='登录']")

def test_tms_2(driver):
    # 基础数据 //a[@id='402882b75ff3938e015ff396e33f0003']
    driver.move_to_element("//a[@id='402882b75ff3938e015ff396e33f0003']")
    sleep(3)
    # 点击行政区域
    driver.click("//a[text()='行政区域']")
    # 点击新增
    driver.switch_to_frame("//iframe[@id='iframe402882b76021c758016021ccec660001']")
    driver.click("//a[@id='Zone-add']")
    driver.switch_to_current_frame_out()
    # 输入区域名称 """//input[@onkeyup="pinyinQuery('name','code')"]"""
    driver.switch_to_frame("//iframe[@id='行政区域']")
    driver.send_keys("//th[text()='区域名称']/following-sibling::td//input","乐平市")
    # 输入区域编码
    driver.send_keys("//th[text()='区域编码']/following-sibling::td//input","0798")
    # 输入城市编码
    driver.send_keys("//th[text()='城市编码']/following-sibling::td//input","0000")
    # 选择乡镇级
    driver.click("//div[@id='level']//div")
    driver.click("//div[@id='level-option']//div//li[6]")
    # 选择上级机构
    driver.click("//div[@id='zone']//div")
    driver.click("//div[@title='北京市']")
    driver.switch_to_current_frame_out()
    # driver.click("//div[@id='bbtree1595326045432_1dbf745acecb420aadf899a93a4f9d69']//img")
    # driver.click("//div[@title='北京城区']/img")
    # 确认
    driver.click("//a[text()='确认']")
    pass

