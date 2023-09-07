from selenium import webdriver  # 引入包
driver = webdriver.Edge()  # 实例化浏览器
driver.maximize_window()    #最大化窗口
driver.get("https://www.baidu.com")     #打开“百度”
driver.get("http://www.scut.edu.cn")
# js = 'window.open("https://www.zhihu.com");'    #使用js打开一个窗口
# driver.execute_script(js)
driver.forward()                #切换到下一个网页
print(driver.title)     #获取网页标题
print(driver.current_url)   #获取网页url
driver.back()    #切换到上一个网页
print(driver.title)
print(driver.current_url)
driver.refresh()        #刷新网页
print(driver.get_window_size()) #获取网页尺寸
driver.close()      #关闭网页
driver.quit()   #关闭整个浏览器