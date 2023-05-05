# Selenium 环境

## webdriver


Selenium WebDriver for popular browsers can be downloaded from the links mentioned below:

Firefox
https://github.com/mozilla/geckodriver/releases

Chrome
http://chromedriver.chromium.org/downloads


Internet Explorer
https://github.com/SeleniumHQ/selenium/wiki/
InternetExplorerDriver


Microsoft Edge
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

## selenium 依赖

```shell
pip install selenium
```

如果网络超时可以使用国内的镜像：
```shell
pip install -i https://mirrors.aliyun.com/pypi/simple/ selenium
```

[https://selenium-python.readthedocs.io/getting-started.html](https://selenium-python.readthedocs.io/getting-started.html)


如果使用的是 MS Edge 浏览器，需要安装 `msedge-selenium-tools`
```shell
pip install -i https://mirrors.aliyun.com/pypi/simple/ msedge-selenium-tools selenium==3.141
```

参考用法 [selenium-demo/06_use_edge.py](../selenium-demo/06_use_edge.py)

参考文档：
[https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=c-sharp](https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=c-sharp)
[https://github.com/microsoft/edge-selenium-tools](https://github.com/microsoft/edge-selenium-tools)
