import BaiduOrcApi
import os

def Cal_Api(API_KEY, SECRET_KEY, token_url, out_url):
    running = True
    #创建类
    a = BaiduOrcApi.cal(API_KEY, SECRET_KEY, token_url, out_url)

    while running:

        #判断运行情况
        five = a.input_five()
        if five != 0:
            print("出现警告，正在退出")
            running = False

        #输入文件地址
        Address = input("请输入图片地址,输入td退出").strip().strip('"').strip("'")  # strip()消除指定字符串

        if Address == "cs":
            print("使用测试图片")
            Address = r"C:\Users\Administrator\Desktop\Python\百度云示范文件\批注 2026-04-16 152003.jpg"

        elif Address == "td":  # 退出while
            running = False
        if os.path.exists(Address):  # 判断地址是否有效
            print("地址有效")
            a.ORC_Use(Address)
        else:
            print("无效地址")


if __name__ == '__main__':
    print("使用百度OrcApi")

    running_main = True

    while running_main:

        mode=input("回车输入cs进入测试，zu进入自选，td退出")

        if mode in ("cs","CS"):
            mode=None

            #测试的默认值
            API_KEY = "uYfIjXV6XRi9ZLtRBm6jA4x1"
            SECRET_KEY = "gXnGLyF27JaXHdVLW6B47jede80Sfecr"
            token_url = "https://aip.baidubce.com/oauth/2.0/token"
            out_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
            # Address = r"C:\Users\Administrator\Desktop\Python\百度云示范文件\批注 2026-04-16 152003.jpg"#调试文件地址

            #启动Orc
            Cal_Api(API_KEY, SECRET_KEY, token_url, out_url)

        elif mode in ("zu","ZU","zz"):
            mode = None

            #输入参数
            API_KEY = input("输入API_KEY").strip().replace("'","").replace('"',"")
            while API_KEY == "":
                print("API_KEY不能为空")
                API_KEY = input("输入API_KEY").strip().replace("'","").replace('"',"")

            SECRET_KEY = input("输入SECRET_KEY").strip().replace("'","").replace('"',"")
            while SECRET_KEY == "":
                print("SECRET_KEY不能为空")
                SECRET_KEY = input("输入SECRET_KEY").strip().replace("'","").replace('"',"")

            token_url = input("输入token_url").strip().replace("'","").replace('"',"")
            while token_url == "":
                print("token_url不能为空")
                token_url = input("输入token_url").strip().replace("'","").replace('"',"")

            out_url = input("输入out_url").strip().replace("'","").replace('"',"")
            while out_url == "":
                print("out_url不能为空")
                out_url = input("输入out_url").strip().replace("'","").replace('"',"")

            #启动Orc
            Cal_Api(API_KEY, SECRET_KEY, token_url, out_url)

        elif mode in ("td","TD"):
            mode = None
            running_main = False

