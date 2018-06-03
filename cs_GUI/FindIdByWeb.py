import tkinter
from selenium import webdriver
from bs4 import BeautifulSoup
import json

class FindIP():
    def __init__(self):
        self.root = tkinter.Tk()  # 创建主窗口，用于容纳其他组件
        self.root.title('定位IP位置')  # 给主窗口设置标题内容
        self.input = tkinter.Entry(self.root, width=30)  # 创建一个输入框，并设置尺寸
        # self.api_url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % self.input
        self.display_indo = tkinter.Listbox(self.root, width=50)  # 设置一个回显列表
        self.result_button = tkinter.Button(self.root, command=self.find_position, text="查询")  # 创建一个查询结果按钮

    def gui_arrang(self):  # 完成布局
        self.input.pack()
        self.display_indo.pack()
        self.result_button.pack()

    def get_html(self, url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        # print(url)
        data = driver.page_source
        soup = BeautifulSoup(data, 'lxml')
        info = soup.find('body').text
        dd = json.loads(info, encoding='utf-8')
        # print(dd)
        # print(type(dd))
        find_info = dd['data']
        # print(find_info)
        return find_info

    def find_position(self):  # 逻辑函数
        addr = self.input.get()  # 获取输入的信息
        url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % addr
        find_info = self.get_html(url)
        # print(find_info)
        try:

            # 获取目标国家
            country = find_info["country"]
            # 获取目标城市
            region = find_info["region"]
            # 获取目标地区
            city = find_info["city"]
            # 获取运营商
            isp = find_info["isp"]
            # 获取ip
            ip = find_info["ip"]
        except:
            pass
        # 创建临时列表
        the_ip_info = ["运营商:" + str(isp), "IP:" + str(ip),
                       "所在城市:" + str(city), "所在国家或地区:" + str(country)]

        # print(the_ip_info)
        for item in range(10):
            # 清空回显列表可见部分
            self.display_indo.insert(0, "")

        # 为回显列表赋值
        for item in the_ip_info:
            self.display_indo.insert(0, item)

def main():
    FL = FindIP()  # 初始化对象
    FL.gui_arrang()  # 进行布局
    tkinter.mainloop()  # 主程序执行

if __name__ == '__main__':
    main()
