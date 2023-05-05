import time

from msedge.selenium_tools import Edge, EdgeOptions


def getEdgeDownLoadedFileName():
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('edge://downloads/all')
    started = 0
    # define the endTime
    # endTime = time.time() + waitTime
    while True:
        try:
            # get downloaded percentage
            downloadPercentage = driver.execute_script(
                "return document.querySelector('div[role=progressbar]').ariaValueNow")
            print(downloadPercentage)
            if int(downloadPercentage) == 100:
                started = 1
                return driver.execute_script(
                    "return document.querySelector('#downloads-item-1>div>img').ariaLabel")
        except BaseException as err:
            if started == 1:
                print('下载完毕。获取文件名')
                return driver.execute_script(
                    "return document.querySelector('#downloads-item-1>div>img').ariaLabel")
            else:
                # FIXME: 针对秒下载的情况，不等进度条出现就下载完毕了，会一直打印，暂时先不做处理（大多数情况都不会秒下载）
                print('等待开始下载...')

            # print("调试日志：", err)
            pass

        time.sleep(1)


# Launch Microsoft Edge (Chromium)
options = EdgeOptions()
options.use_chromium = True
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\testDownload\\'}
options.add_experimental_option('prefs', prefs)

driver = Edge(executable_path='C:\\Kay\\soft\\edgedriver_win64\\msedgedriver.exe', options=options)

# 可能会秒下载的文件测试
# driver.get('http://sahitest.com/demo/saveAs.htm')
# driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()

driver.get("https://calibre-ebook.com/download_windows64")
driver.find_element_by_xpath('//*[@id="download_block"]/div/a[1]').click()

fileName = getEdgeDownLoadedFileName()
print(fileName)
