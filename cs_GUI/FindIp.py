import tkinter
import pygeoip

class FindLocation(object):
    def __init__(self):
        self.gi = pygeoip.GeoIP('./GeoLiteCity.dat')
        self.root = tkinter.Tk()  # 创建主窗口，用于容纳其他组件
        self.root.title('定位IP位置（离线版）')  # 给主窗口设置标题内容
        self.input = tkinter.Entry(self.root, width=30)  # 创建一个输入框，并设置尺寸
        self.display_indo = tkinter.Listbox(self.root, width=50)  # 设置一个回显列表
        self.result_button = tkinter.Button(self.root, command=self.find_position, text="查询")  # 创建一个查询结果按钮

    def gui_arrang(self):  # 完成布局
        self.input.pack()
        self.display_indo.pack()
        self.result_button.pack()

    def find_position(self):  # 逻辑函数
        self.addr = self.input.get()  # 获取输入的信息
        aim = self.gi.record_by_name(self.addr)
        try:
            # 获取目标城市
            city = aim["city"]
            # 获取目标国家
            country = aim["country_name"]
            # 获取目标地区
            region_code = aim["region_code"]
            # 获取目标经度
            longitude = aim["longitude"]
            # 获取目标纬度
            latitude = aim["latitude"]
        except:
            pass
        # 创建临时列表
        the_ip_info = ["所在纬度:" + str(latitude), "所在经度:" + str(longitude), "地域代号:" + str(region_code),
                       "所在城市:" + str(city), "所在国家或地区:" + str(country), "需要查询的ip:" + str(self.addr)]

        # print(the_ip_info)
        for item in range(10):
            # 清空回显列表可见部分
            self.display_indo.insert(0, "")

        # 为回显列表赋值
        for item in the_ip_info:
            self.display_indo.insert(0, item)

def main():
    FL = FindLocation()  # 初始化对象
    FL.gui_arrang()  # 进行布局
    tkinter.mainloop()  # 主程序执行

if __name__ == "__main__":
    main()
