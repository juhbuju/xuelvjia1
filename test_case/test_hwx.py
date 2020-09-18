from selenium import webdriver
from time import sleep
def test_chrome(driver):
    #  输入网址
    driver.get("https://cn.student.com/")
    #  输入伦敦
    driver.send_keys("//input[@placeholder='输入城市、大学或公寓名']","伦敦")
    #  点击搜索  //div[@class='hero-banner-dark__search']
    #  伦敦
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[1]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'伦敦')])[1]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'伦敦')])[2]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'伦敦')])[3]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'伦敦')])[4]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'伦敦')])[5]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'伦敦')])[6]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'伦敦')])[7]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'伦敦')])[8]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'伦敦')])[9]")
    driver.click("(//span[@class='search-list-desktop__item__secondary-text'])[1]")
    driver.send_keys("//input[@placeholder='输入城市、大学或公寓名']","london")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[1]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[2]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[3]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[4]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[5]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[6]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[7]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[8]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[9]")
    driver.move_to_element("(//span[@class='search-list-desktop__item__secondary-text'])[10]")



    # def testsearch(driver):
    #     #     name="伦敦"
    #     #     for i in range(9):
    #     #         xpath="(//span[@class='search-list-desktop__item__secondary-text' and contains(text(),'"+name+"')])["+i+"]"
    #     #         assert driver.get_page_source().contains(xpath)