from selenium import webdriver  # 引入包
from selenium.webdriver.common.by import By
from time import sleep

# driver = webdriver.Edge()  # 实例化浏览器
# driver.maximize_window()  # 最大化窗口
# driver.get("https://www.baidu.com")  # 打开“百度”
# driver.get("http://www.scut.edu.cn")
# sleep(2)
# # js = 'window.open("https://www.zhihu.com");'    #使用js打开一个窗口
# # driver.execute_script(js)
# driver.back()  # 切换到上一个网页
# print(driver.title)  # 获取网页标题
# print(driver.current_url)  # 获取网页url
# sleep(2)
# driver.forward()  # 切换到下一个网页
# print(driver.title)
# print(driver.current_url)
# driver.refresh()  # 刷新网页
# print(driver.get_window_size())  # 获取网页尺寸
# sleep(3)
# driver.close()  # 关闭网页
# driver.quit()  # 关闭整个浏览器


driver = webdriver.Edge()  # 实例化浏览器
driver.get("https://www.baidu.com")
# driver.find_element(by=By.ID, value="kw")  # 根据ID搜索元素
# driver.find_element(By.NAME, "wd")  # 根据name搜索元素
# driver.find_element(By.CLASS_NAME, "s_ipt")  #根据类名搜索元素
# driver.find_element(By.TAG_NAME, "input")    #根据tag搜索元素
driver.find_element(By.LINK_TEXT, "新闻").click()     #根据链接寻找     #点击“新闻”选项
# driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[5]/div/div/form/span[1]/input')     #XPATH
sleep(3)
driver.forward()


driver.quit()  # 关闭整个浏览器

