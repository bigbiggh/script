# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/6 17:00
# @Author   :Administrator
# @File :pythonlearn.py
# @Description:
# ------------------------------
import threading
import time

exitFlag = 0


class Threading_my(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("start")
        print_time(self.name, 1, self.counter)
        print("end")


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = Threading_my(1, "Thread-1", 5)
thread2 = Threading_my(2, "Thread-2", 2)

# 开启线程
thread1.run()
thread2.run()
