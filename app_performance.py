# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/8/2 15:37
"""
import os

class AppPerformance:
    def __init__(self):
        self.content = ''

    def get_device_name(self):
        cmd = 'adb shell monkey -p cn.btclass.sierra -v 5000'
        self.content = os.popen(cmd)
        return self.content

if __name__ == '__main__':
    ap = AppPerformance()
    result = ap.get_device_name()
    print(result)