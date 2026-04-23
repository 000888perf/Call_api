import os
import BaiduOrcApi#实现代码
import dbini#读取额瓶子文件

"""
1,学习API配置与使用
2，读取ini配置文件
3，学习python规范代码
4，每次Orc的API调用是需要钱的
"""

try:
    # 创建类，使用配置文件
    cal = dbini.dbini()
    # 获取配置文件
    db_API_KEY, db_SECRET_KEY, db_token_url, db_out_url = cal.set()
    API_KEY, SECRET_KEY, token_url, out_url = db_API_KEY, db_SECRET_KEY, db_token_url, db_out_url
    print("<读取配置文件成功>")
except Exception as e:
    print("<错误详情：",e,">")
    input("(按回车退出)")
    exit()

#打包了一个用于打开Orc的函数
def Cal_Api(API_KEY, SECRET_KEY, token_url, out_url):
    try:

        #初始化Orc状态机标志符//用于判断运行状态
        running = False
        #创建类
        ocr_client = BaiduOrcApi.cal(API_KEY, SECRET_KEY, token_url, out_url)

        while running:#标志符值假运行

            #判断运行情况
            check_result = ocr_client.input_five()#如果不能获取token就返回“1”
            if check_result != 0:
                print("<出现警告，正在退出...>")
                running = True
                break
            else:
                #输入文件地址
                Address = input("(请输入图片地址,输入td退出)").strip().strip('"').strip("'")  # strip()消除指定字符串
                print("--->")
                if Address == "cs":
                    print("<使用测试图片>")
                    Address = r"C:\Users\Administrator\Desktop\Python\百度云示范文件\批注 2026-04-16 152003.jpg"

                elif Address == "td":  # 退出while
                    running = True
                    break
                if os.path.exists(Address):  # os判断地址是否有效
                    print("<地址有效>")
                    print("--->")
                    ocr_client.ORC_Use(Address)
                else:
                    print("<无效地址>")
    except Exception as e:
        print("错误详情：", e)
        input("<按回车退出>")
        exit()

#主函数
def main():

    print("<欢迎使用百度OrcApi>")

    #主程序状态机
    running_main = True

    while running_main:

        #选择选项
        mode = input("(请输入选项，按回车确定) \n--->cs进入测试选项   --->mr进入默认选项\n--->zu进入自主选项   --->td退出")
        while mode not in ["cs", "CS","cc","CC","zu", "ZU", "zz","mr","MR","mm","MM","td", "TD"]:
            if mode == "":
                print("<输入为空，请重新输入>")
                mode = input("(请输入选项，按回车确定) \n--->cs进入测试选项   --->mr进入默认选项\n--->zu进入自主选项   --->td退出")
            else:
                print("<不存在选项，请重新选择>")
                mode = input("(请输入选项，按回车确定) \n--->cs进入测试选项   --->mr进入默认选项\n--->zu进入自主选项   --->td退出")

        #测试选项，有固定参数
        if mode in ("cs", "CS","cc","CC"):
            mode = None
            mode_1_cs()

        #自定义选项
        elif mode in ("zu", "ZU", "zz","ZZ"):
            mode = None
            mode_2_zu()

        #默认选项，使用配置文件值，也可自己修改
        elif mode in ('mr','MR','mm','MM'):
            mode_3_mr()
        #退出，退订
        elif mode in ("td", "TD"):
            mode = None
            running_main = False
#-----------------------
def mode_1_cs():
    try:

        print("<进入测试选项>")
        # 测试的默认值
        API_KEY = "uYfIjXV6XRi9ZLtRBm6jA4x1"
        SECRET_KEY = "gXnGLyF27JaXHdVLW6B47jede80Sfecr"
        token_url = "https://aip.baidubce.com/oauth/2.0/token"
        out_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
        # Address = r"C:\Users\Administrator\Desktop\Python\百度云示范文件\批注 2026-04-16 152003.jpg"#调试文件地址

        # 启动Orc
        Cal_Api(API_KEY, SECRET_KEY, token_url, out_url)

    except Exception as e:
        print("错误详情：", e)
        input("<按回车退出>")
        exit()
def mode_2_zu():
    try:
        print("<进入自主选项>")

        # 输入参数
        API_KEY = input("(请输入API_KEY)").strip().replace("'", "").replace('"', "")
        while API_KEY == "":
            print("<API_KEY不能为空>")
            API_KEY = input("(请输入API_KEY)").strip().replace("'", "").replace('"', "")

        SECRET_KEY = input("(请输入SECRET_KEY)").strip().replace("'", "").replace('"', "")
        while SECRET_KEY == "":
            print("<SECRET_KEY 不能为空>")
            SECRET_KEY = input("(请输入SECRET_KEY)").strip().replace("'", "").replace('"', "")

        token_url = input("(请输入token_url)").strip().replace("'", "").replace('"', "")
        while token_url == "":
            print("<token_url 不能为空>")
            token_url = input("(请输入token_url)").strip().replace("'", "").replace('"', "")

        out_url = input("(请输入out_url)").strip().replace("'", "").replace('"', "")
        while out_url == "":
            print("<out_url 不能为空>")
            out_url = input("(请输入out_url)").strip().replace("'", "").replace('"', "")

        #起到Orc
        Cal_Api(API_KEY, SECRET_KEY, token_url, out_url)
    except Exception as e:
        print("错误详情：", e)
        input("<按回车退出>")
        exit()
def mode_3_mr():
    try:
        # 神秘bug
        # 因为没有输入参数，函数内部存在修改变量的操作，所以内部生成了同名空变量，直接从新赋值一次创建新的内部变量
        API_KEY, SECRET_KEY, token_url, out_url = db_API_KEY, db_SECRET_KEY, db_token_url, db_out_url

        # 初始化模式选择变量
        mode_mr = None

        print("<进入默认选项>")
        """
        print(f"<历史默认值为(回车使用历史值，输入序号进行修改)>"
              f"\n--->   <1，API_KEY:{db_API_KEY}>"
              f"\n--->   <2，SECRET_KEY:{db_SECRET_KEY}>"
              f"\n--->   <3，token_url:{db_token_url}>"
              f"\n--->   <4，out_url:{db_out_url}>"
              )
        """

        # 输入判断
        while mode_mr is None:
            mode_mr = input(f"<历史默认值为(回车使用历史值，输入序号进行修改)>"
              f"\n--->   <1，API_KEY:{db_API_KEY}>"
              f"\n--->   <2，SECRET_KEY:{db_SECRET_KEY}>"
              f"\n--->   <3，token_url:{db_token_url}>"
              f"\n--->   <4，out_url:{db_out_url}>")
            try:
                if int(mode_mr) > 4:
                    print("<不存在序号，请重新输入>")
                    mode_mr = None
            except ValueError:
                print("<确认参数，进入Orc>")

        #进入选项
        while mode_mr != "":#判断是否有正确的选项
            while mode_mr == "1":

                Str = input(
                    "API_KEY值为:   " + API_KEY + "\n修改为：(回车确认，输入为空将使用历史值)   ").strip().replace("'","").replace('"', "")
                if Str != "":
                    API_KEY = Str
                    print(f"API_KEY<修改成功>:   {API_KEY}")
                    mode_mr = None
                    break
                elif Str == "":
                    print(f"输入为空，将使用历史值:   {API_KEY}")
                    mode_mr = None
                    break

            while mode_mr == "2":
                Str = input(
                    "SECRET_KEY值为:   " + SECRET_KEY + "\n修改为：(回车确认,输入为空将使用历史值)   ").strip().replace("'","").replace('"', "")
                if Str != "":
                    SECRET_KEY = Str
                    print(f"SECRET_KEY<修改成功>:   {SECRET_KEY}")
                    mode_mr = None
                    break
                elif Str == "":
                    print(f"输入为空，将使用历史值:   {SECRET_KEY}")
                    mode_mr = None
                    break

            while mode_mr == "3":
                Str = input("token_url值为:   " + token_url + "\n修改为(回车确认，输入为空将使用历史值)   ").strip().replace("'", "").replace('"', "")
                if Str != "":
                    token_url = Str
                    print(f"token_url<修改成功>:   {token_url}")
                    mode_mr = None
                    break
                elif Str == "":
                    print(f"输入为空，将使用历史值:   {token_url}")
                    mode_mr = None
                    break

            while mode_mr == "4":
                Str = input("out_url值为:   " + out_url + "\n修改为：(回车确认,输入为空将使用历史值)   ").strip().replace("'", "").replace('"', "")
                if Str != "":
                    out_url = Str
                    print(f"out_url<修改成功>:   {out_url}")
                    mode_mr = None
                    break
                elif Str == "":
                    print(f"输入为空，将使用历史值:   {out_url}")
                    mode_mr = None
                    break

            #确认是否修改
            while mode_mr is None:
                mode_mr = input("\n（按回车确认修改,点击序号继续修改）")
                try:
                    if int(mode_mr) > 4:
                        print("<不存在序号，请重新输入>")
                        mode_mr = None
                except ValueError:
                    print("--->")

        # 启动Orc
        Cal_Api(API_KEY, SECRET_KEY, token_url, out_url)
    except Exception as e:
        print("错误详情：", e)
        input("<按回车退出>")
        exit()
#------------------------
if __name__ == '__main__':
    main()

