import sys
import time

for i in range(101):
    s="\r下载中:%d%% %s"%(i,"#"*i)   #\r表示回车但是不换行，利用这个原理进行百分比的刷新
    sys.stdout.write(s)       #向标准输出终端写内容
    sys.stdout.flush()        #立即将缓存的内容刷新到标准输出
    time.sleep(1)           #设置延迟查看效果