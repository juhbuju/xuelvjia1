from time import sleep


def test_chrome(driver):
    driver.get("http://www.taobao.com")
    sleep(2)
    #点击输入框
    driver.click("//input[@aria-label='请输入搜索文字']")
    sleep(2)
    #输入戴森 //input[@aria-label="请输入搜索文字"]
    driver.send_keys("//input[@aria-label='请输入搜索文字']","戴森")
    sleep(2)
    #点击搜索 //button[text()='搜索']
    driver.click("//button[text()='搜索']")
    sleep(2)
    # 关闭浏览器
    driver.quit()