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
#driver.find_element(By.LINK_TEXT, "新闻").click()  # 根据链接寻找     点击“新闻”选项

sleep(3)
#driver.forward()
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("华南理工大学")  # XPATH       输入“内容”
sleep(1)
#driver.find_element(By.XPATH, '//*[@id="kw"]').clear()          #清除内容
element = driver.find_element(By.ID, "kw")
print("搜索框里的内容是：", element.get_attribute("value"))
print('搜索框的class属性：',element.get_attribute('class'))
print('搜索框的type属性：',element.get_attribute('type'))
print('搜索框的坐标位置：',element.location)
print('搜索框是否可操作：',element.is_displayed())
sleep(3)
driver.find_element(By.XPATH, '//*[@id="kw"]').submit()     #提交表单
sleep(1)
driver.quit()  # 关闭整个浏览器
