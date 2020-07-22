import time
import os
import crawler

#时间
def time_time():
	a=time.strftime("%Y-%m-%d", time.localtime())
	return a

#文件创建和检测
def file_detection():
	while True:
		if os.path.exists("./gather//{}".format(time_time())):
			break
		else:
			os.makedirs("./gather//{}".format(time_time()))

