from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



# @pytest.fixture(scope="session")
# def driver():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9111")
#     base = webdriver.Chrome("../chrome_driver/chromedriver.exe",options=chrome_options)
#     # 最大化浏览器
#     base.maximize_window()
#     yield base
#     base.quit()

def test_chrome():
    # 打开浏览器
    driver = webdriver.Chrome("../chrome_driver/chromedriver.exe")
    # 设置浏览器窗口尺寸
    driver.set_window_size(1000,520)
    sleep(2)
    # 最小化浏览器
    driver.minimize_window()
    sleep(10)
    # 最大化浏览器
    driver.maximize_window()
    sleep(2)
    # 打开网址
    driver.get("http://www.baidu.com")
    sleep(2)
    driver.get("http://www.jd.com")
    sleep(2)
    driver.get("http://www.taobao.com")
    sleep(2)
    # 后退
    driver.back()
    sleep(2)
    # 前进
    driver.forward()
    sleep(2)
    # 刷新
    driver.refresh()
    sleep(2)

    # # 关闭浏览器，不退出driver
    # driver.close()
    # 退出驱动，并关闭浏览器
    driver.quit()

def test_local_element(driver):
    # 根据xpath定位页面元素
    # el = driver.find_element_by_xpath('//input[@placeholder="评论ID"]')
    # 通过id定位
    # el = driver.find_element_by_id("hello")
    # 通过classname定位
    # driver.find_element_by_class_name("")
    # 通过name定位
    # el = driver.find_element_by_name('hello')
    # 根据超链接的展示文本定位
    # el = driver.find_element_by_link_text("百度一下")
    # 根据超链接的展示文本模糊定位
    # el = driver.find_element_by_partial_link_text("百度")
    # 通过css选择器定位
    # el = driver.find_element_by_css_selector("#hello")
    # 通过标签名定位
    # el = driver.find_element_by_tag_name("div")
    # find_elements返回的结果是一个列表
    els = driver.find_elements_by_tag_name("")
    print(els)
    sleep(2)
    # 点击操作
    # el.click()input
    # 清空输入框
    # el.clear()
    # 输入框输入内容
    # el.send_keys("hello")
    pass


def test_element(driver):
    # el = driver.find_element_by_tag_name('select')
    # # 清空输入框内容
    # # el.clear()
    # sleep(2)
    # # # 输入框输入内容
    # # el.send_keys("E:\\1.png")
    # # 按钮操作
    # el.click()

    # driver.find_element_by_xpath("//select/option[text()='梨']").click()
    # sleep(2)
    # 仅使用与原始的select标签
    # # 操作下拉框
    # select = Select(el)
    # # 通过下标选择
    # select.select_by_index(3)
    # sleep(2)
    # # 通过value值选择
    # select.select_by_value("2")
    # sleep(2)
    # # 通过展示文本选择
    # select.select_by_visible_text("苹果")
    # 执行js代码
    # driver.execute_script('document.getElementsByTagName("input")[0].value="2020-01-04";')
    # el = driver.find_element_by_xpath("(//a[text()='女装'])[1]")
    # from selenium.webdriver.common.action_chains import ActionChains
    # action = ActionChains(driver) 实例化ActionChains类
    # 鼠标操作
    # move_to_element(el) 鼠标悬浮
    # action.drag_and_drop()拖拽
    # click_and_hold 鼠标按下不松开
    # release() 释放鼠标
    # double_click()双击
    # context_click() 右击

    # 键盘操作
    # key_down 按键按下
    # key_up 按键弹起
    # send_keys 输入一个按键
    # Keys 功能键集合

    # 执行组合好的方法
    # action.perform()
    # el = driver.find_element_by_xpath("(//a[text()='女装'])[1]")
    from selenium.webdriver.common.action_chains import ActionChains
    # 实例化ActionChains类
    # action = ActionChains(driver)
    # el = driver.find_element_by_tag_name('input')
    # action.move_to_element(el).click(el).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

    # iframe处理
    # 进入iframe
    # driver.switch_to.frame(el)
    # 操作完成之后
    # 退出iframe
    # 退出当前iframe
    # driver.switch_to.parent_frame()
    # 回到页面最外层
    # driver.switch_to.default_content()

    # 浏览器窗口切换
    # 获取浏览器所有窗口的句柄
    # handles = driver.window_handles
    # 使用for循环遍历句柄列表
    # for h in handles:
    #     # 根据窗口句柄切换到指定窗口
    #     driver.switch_to.window(h)
    #     # 判断窗口title中是否包含我们要的结果，如果包含则终止循环
    #     if ("当当" in driver.title):
    #         break

    # 弹框
    # 警示框
    # driver.find_element_by_xpath("//button[text()='警示框']").click()
    # sleep(2)
    # alert = driver.switch_to.alert
    # # 确认
    # # alert.accept()
    # # 获取展示文本
    # print(alert.text)

    # 确认框
    # driver.find_element_by_xpath("//button[text()='确认框']").click()
    # sleep(2)
    # alert = driver.switch_to.alert
    # # 确认
    # # alert.accept()
    # # 获取展示文本
    # print(alert.text)
    # # 取消弹框
    # alert.dismiss()

    # 对话框
    # driver.find_element_by_xpath("//button[text()='对话框']").click()
    # sleep(2)
    # alert = driver.switch_to.alert
    # # 确认
    # # alert.accept()
    # # 获取展示文本
    # # print(alert.text)
    # # 取消弹框
    # # alert.dismiss()
    # # 输入内容
    # alert.send_keys("你好世界")
    # sleep(10)
    # 显式等待和隐式等待
    # 隐式等待
    # driver.implicitly_wait(20) # 等待页面加载
    # driver.find_element_by_xpath("(//span[text()='登录'])[1]").click()
    # from selenium.webdriver.support import expected_conditions as EC
    # from selenium.webdriver.support.wait import WebDriverWait
    #
    # driver.find_element_by_xpath("(//span[text()='商品管理'])[1]").click()
    # WebDriverWait(driver, 50, 0.5).until(EC.visibility_of_element_located((By.XPATH,"(//span[text()='商品类目'])[1]")))
    # driver.find_element_by_xpath("(//span[text()='商品类目'])[1]").click()
    # driver.find_element_by_xpath("(//span[text()='编辑'])[1]").click()


    # 隐式等待浏览器全局设置，设置一次即可。再给定的时间内，判断元素是否加载出来，如果加载出来则继续，超过给定时间则抛异常
    # 显式等待，在给定时间内，持续去判断页面是否满足某种条件。满足则继续，超过给定时间抛异常
    # sleep 是线程等待，程序强制休眠指定时间


    # 界面操作
    # 获取界面源代码
    # print(driver.page_source)
    # 获取浏览器截图
    # driver.get_screenshot_as_file("e:\\1111.png")

    # 获取界面元素内容
    el = driver.find_element_by_xpath("//span[text()='添加']")
    # 获取展示文本
    print(el.text)
    el = driver.find_element_by_xpath("//span[text()='添加']/..")
    # 获取标签名
    print(el.tag_name)
    # 获取元素尺寸
    print(el.size)
    # 获取元素某个属性的值
    print(el.get_attribute("type"))









    pass

