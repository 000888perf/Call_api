import base64  #数据解码编码库（pyrhon自带）
import urllib.parse  #url网页操作
import requests  #HTTP库，用于处理HTTP请求
import os #文件控制模块


class cal:
    #图文识别模块
    #带有默认获取token网址和api调用网址

    #获取网页授权
    def __init__(self,API_KEY,SECRET_KEY,token_url,out_url):
        print("欢迎使用")
        #状态符
        self.fire = 0#异常符号

        #密钥
        self.API_KEY = API_KEY#公钥（账号）
        self.SECRET_KEY = SECRET_KEY#私钥（密码）

        #获取token许可和api调用网址
        self.token_url = None
        self.out_url = None

        #接收数据
        self.image_base64 = None
        self.access_token = None
        self.Receive_response = None

        #进行初始化
        self.ORC_init(API_KEY, SECRET_KEY,token_url,out_url)


    #获取token，api授权码
    def get_access_token(self) ->None:
        print("获取token(访问令牌)")
        try:
            url = self.token_url
            params = {
                "grant_type": "client_credentials",#用于指定服务器返回一个 访问令牌
                "client_id": self.API_KEY,
                "client_secret": self.SECRET_KEY
            }
            result = requests.post(url, params=params).json()
            self.access_token = result.get("access_token")

            #return result.get("access_token")#旧方法使用返回值，用类就直接内部修改好了
        except Exception as e:
            print("获取token异常:", e)
            self.fire = 1#fire异常符号

    #base64转换图片格式
    @staticmethod
    def get_file_content_as_base64(path, urlencoded=False):
        print("转换图片格式")
        with open(path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf8")
            if urlencoded:
                content = urllib.parse.quote_plus(content)
        return content

    # 网页请求并且接收数据
    def requests(self) -> None:
        print("等待返回值")
        url = self.out_url
        #网页授权
        params = {
            "access_token": self.access_token  # 网页授权
        }

        #转化后的图片
        payload = {
            "image": self.image_base64
        }

        #请求头
        headers = {  # 告诉api上传文件的类型
            'Content-Type': 'application/x-www-form-urlencoded',
            # Content-Type：指示请求体中数据的类型，通常在POST请求中使用。
        }

        #上传数据
        self.Receive_response = requests.post(url, params=params, data=payload, headers=headers)  # 读取服务器返回值
        # url  网址，params  网页授权，data  上传数据，headers  网页请求头

    #输出服务器返回内容
    @staticmethod#静态方法
    def get_print(response):


        #print(response.text)
        result = response.json()  # 直接转成字典

        # ==============================================
        #识别到的文字
        # ==============================================
        print("=" * 30)
        print("OCR 识别结果：")
        print("=" * 30)

        # 循环取出每一行文字
        for item in result.get("words_result", []):
            print(item["words"])

        print("=" * 30)
        print(f" 共识别到 {result.get('words_result_num', 0)} 行文字")

    #获取网页授权的网址
    def get_token_url(self,get_token_url) ->None:
        self.token_url = get_token_url

    #调用api的网址
    def get_out_url(self,get_out_url) ->None:
        self.out_url = get_out_url

    def ORC_init(self,API_KEY,SECRET_KEY,token_url,out_url):
        print("初始化...")

        ########################################################给变量赋值
        self.token_url = token_url
        self.out_url = out_url
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        #########################################################

        #获取token网址授权
        self.get_access_token()
        if not self.access_token:#判断token是否为空
            print("获取 token 失败！")
            return

        print("初始化成功")

    def input_five(self):
        return self.fire

    def ORC_Use(self,Address):
        #读取图片并转 base64#要转化图片编码
        self.image_base64 = self.get_file_content_as_base64(Address, urlencoded=False)

        #把转化的图片发送到服务器并等待返回值
        self.requests()

        #输出返回值
        self.get_print(self.Receive_response)


    @staticmethod
    def help():
        print("self.ORC_Use() --图片地址 #进入程序"
              "eslf.get_token_url --获取访问令牌网址 #修改token网址"
              "self.get_out_url  --调用api网址 #设置api网址")

if __name__ == '__main__':

    API_KEY = "uYfIjXV6XRi9ZLtRBm6jA4x1"
    SECRET_KEY = "gXnGLyF27JaXHdVLW6B47jede80Sfecr"
    #Address = r"C:\Users\Administrator\Desktop\Python\百度云示范文件\批注 2026-04-16 152003.jpg"#调试地址
    token_url = "https://aip.baidubce.com/oauth/2.0/token"
    out_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"


    #创建类
    a=cal(API_KEY,SECRET_KEY,token_url,out_url)

    while True:
        Address=input("请输入图片地址,输入td退出").strip().strip('"').strip("'")#strip()消除指定字符串

        if Address=="cs":
            print("使用测试图片")
            Address = r"C:\Users\Administrator\Desktop\Python\百度云示范文件\批注 2026-04-16 152003.jpg"

        elif Address == "td":#退出while
            break
        if  os.path.exists(Address):#判断地址是否有效
            print("\n地址有效")
            a.ORC_Use(Address)
        else:
            print("\n无效地址")


    """
          密钥
    #API_KEY = "uYfIjXV6XRi9ZLtRBm6jA4x1"
    #SECRET_KEY = "gXnGLyF27JaXHdVLW6B47jede80Sfecr"

 
    self.token_url = "https://aip.baidubce.com/oauth/2.0/token"
    self.out_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

            headers = {  # 告诉api上传文件的类型
            'Content-Type': 'application/x-www-form-urlencoded',
            # Content-Type：指示请求体中数据的类型，通常在POST请求中使用。}   
    
    """
