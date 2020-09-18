from asyncio import sleep

from selenium.webdriver.android import webdriver

from tools.ui import base_ui
def test_radio_1(driver):
    # 点击商品管理
    driver.click("//span[text()='商品管理']")
    # 点击商品列表
    driver.click("//span[text()='商品列表']")
    # 点击添加
    driver.click("//span[text()='添加']")
    # 输入商品名称
    driver.send_keys("//label[text()='商品名称']/../div//input","华为")
    # 输入原始价格    //label[text()='原始价格']/../div//input
    driver.send_keys("//label[text()='原始价格']/../div//input","6000")
    # 输入当前价格    //label[text()='当前价格']/../div//input
    driver.send_keys("//label[text()='当前价格']/../div//input","6000")
    # 输入vip价格     //label[text()='VIP价格']/../div//input
    driver.send_keys("//label[text()='VIP价格']/../div//input","6000")
    driver.click('//input[@placeholder="选择商品运费模板"]/../span//i')
    driver.click('//span[text()="胡文星"]/..')
    # # 下滚屏幕
    # driver.scroll_screen_to_element("//span[text()='胡文星']")
    # 选择下架
    driver.click("//span[text()='在售']")
    # 上传图片
    driver.file_upload("//label[text()='商品图片']/../div//i","D:\\123.jpg")
    sleep(2)
    # 输入商品单位
    driver.send_keys("//label[text()='商品单位']/../div//input","件")
    # # 选择所属类目    //label[text()='所属类目']/../div//input
    driver.click("//label[text()='所属类目']/../div//input")
    # 选择测试
    driver.move_to_element("//span[text()='测试']")
    # 选择虚拟商品
    driver.move_to_element("//span[text()='虚拟商品']")
    # 选择特殊商品
    driver.click("//span[text()='特殊商品']")
    sleep(5)
    # 商品简介        //label[text()='商品简介']/../div//input
    driver.send_keys("//label[text()='商品简介']/../div//input","123456789")
    # iframe框
    driver.switch_to_frame("tag_name=>iframe")
    driver.send_keys("//body[@id='tinymce']","测试一下")
    driver.switch_to_current_frame_out()
    # 点击添加
    driver.click("(//span[text()='添加'])[1]")
    # 输入类型条码
    driver.send_keys("//label[text()='类型条码']/../div//input","hwx")
    # 输入类型名称    //label[text()='类型名称']/../div//input
    driver.send_keys("//label[text()='类型名称']/../div//input","hwx123")
    # 上传图片
    driver.file_upload('//label[text()="图片(可空)"]/../div//i',"D:\\321.png")
    sleep(2)
    # 上传图片
    # driver.file_upload("//label[text()='商品图片']/../div//i","D:\\321.png")
    # 加价原始价格    //label[text()='原始价格']/../div//input
    driver.send_keys("//label[text()='原始价格(元)']/../div//input","550")
    # 加价当前价格    //label[text()='当前价格']/../div//input
    driver.send_keys("//label[text()='当前价格(元)']/../div//input","500")
    # 加价 VIP价格    //label[text()='VIP价格']/../div//input
    driver.send_keys("//label[text()='VIP价格(元)']/../div//input","495")
    # 输入库存        //label[text()='库存']/../div//input
    driver.send_keys("//label[text()='库存']/../div//input","1000")
    # 点击确定
    driver.click("(//span[text()='确定'])[1]")
    # 点击添加商品参数 (
    driver.click("(//span[text()='添加'])[2]")
    # 输入商品参数名称  //label[text()='商品参数名称']/../div//input
    driver.send_keys("//label[text()='商品参数名称']/../div//input","22222")
    # 输入商品参数值    //label[text()='商品参数值']/../div//input
    driver.send_keys("//label[text()='商品参数值']/../div//input","33333")
    # 点击确定
    driver.click("(//span[text()='确定'])[2]")
    # 点击保存商品
    driver.click("//span[text()='保存商品']")
    pass
def test_radio_2(driver):
    # 修改
    driver.click("//div[text()='华为']/../following-sibling::td[last()]//button[1]")
    driver.send_keys("//label[text()='商品单位']/../div//input","件")
    driver.click("//span[text()='更新商品']")
def test_radio_3(driver):
    # 下架
    driver.click("//div[text()='华为']/../following-sibling::td[last()]//button[2]")
    driver.click("//button[@class='el-button el-button--default el-button--small el-button--primary ']")
def test_radio_4(driver):
    # 删除
    driver.click("//div[text()='华为']/../following-sibling::td[last()]//button[3]")
    driver.click("//button[@class='el-button el-button--default el-button--small el-button--primary ']")

    pass
