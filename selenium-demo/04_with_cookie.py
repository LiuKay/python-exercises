import json
import time

from selenium import webdriver
from pyquery import PyQuery as pq

url = "https://music.163.com/"

options = webdriver.ChromeOptions()
options.add_argument('blink-settings=imagesEnabled=false')

experimentalFlags = [
    # 【机器翻译官方说明】站点必须指定SameSite=None才能启用第三方使用。0默认1开启2关闭
    'same-site-by-default-cookies@2',
    # 【机器翻译官方说明】如果设置了没有SameSite限制的cookie而没有Secure属性，则将拒绝该cookie。0默认1开启2关闭
    'cookies-without-same-site-must-be-secure@2', ]
chromeLocalStatePrefs = {'browser.enabled_labs_experiments': experimentalFlags}
options.add_experimental_option('localState', chromeLocalStatePrefs)

browser = webdriver.Chrome(chrome_options=options)
browser.get(url)

with open('../163_cookies.json', 'r') as f:
    cookies = json.load(f)

print("add cookies")
for cookie in cookies:
    try:
        cookie.pop('sameSite')
    except:
        pass
    browser.add_cookie(cookie)

current_handle = browser.current_window_handle
print("句柄：", current_handle)

print("sleep 3s")
time.sleep(3)

print("refresh")
# browser.refresh()


browser.get("https://music.163.com/#/song?id=1816224210")

handles = browser.window_handles  # 这个时候会生成一个新窗口或新标签页的句柄，代表这个窗口的模拟driver
for window in handles:
    if window != current_handle:
        browser.switch_to.window(window)
current_window = browser.current_window_handle  # 获取当前窗口handle name

