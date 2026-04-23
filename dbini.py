import configparser
class dbini:
    def __init__(self):
        try:

            self.config = configparser.ConfigParser()
            self.config.read('db.ini')

            self.db_API_KEY = self.config['database']['API_KEY']
            self.db_SECRET_KEY = self.config['database']['SECRET_KEY']
            self.db_token_url = self.config['database']['token_url']
            self.db_out_url = self.config['database']['out_url']
        except configparser.NoSectionError:
            print("<配置文件中中没有找到[database]节点，请检查 \"db.ini\" 是否存在或格式正确>")
            input("(按回车退出)")
            exit()

        except configparser.NoOptionError:
            print("<[database]节点缺少项，请检查 \"db.ini\" 是否存在或格式正确>")
            input("(按回车退出)")
            exit()

        except Exception as e:
            print("<读取配置文件出错，请检查 \"db.ini\" 是否存在或格式正确>")
            print("错误详情：",e)
            input("<按回车退出>")
            exit()

    def set(self):
        return self.db_API_KEY,self.db_SECRET_KEY,self.db_token_url,self.db_out_url

if __name__ == '__main__':
    cal = dbini()
    print(cal.set())

    """
    配置文件内容
    [database]
    
    API_KEY = uYfIjXV6XRi9ZLtRBm6jA4x1
    SECRET_KEY = gXnGLyF27JaXHdVLW6B47jede80Sfecr
    token_url = https://aip.baidubce.com/oauth/2.0/token
    out_url = https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic    
    """