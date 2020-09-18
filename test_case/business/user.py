from time import sleep

def test_radio(driver):
    # driver.drag_and_drop_by_offset("//span[text()='默认']/..//div[@class='el-tooltip el-slider__button']",100,0).perform()
     driver.drag_and_drop_by_offset("//h3[@id='shu-xiang-mo-shi']/following-sibling::div[1]//div[@class='el-tooltip el-slider__button']",0,-50).perform()




