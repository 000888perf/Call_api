import configparser
class dbini:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('db.ini')

        self.db_API_KEY = self.config['database']['API_KEY']
        self.db_SECRET_KEY = self.config['database']['SECRET_KEY']
        self.db_token_url = self.config['database']['token_url']
        self.db_out_url = self.config['database']['out_url']

    def set(self):
        return self.db_API_KEY,self.db_SECRET_KEY,self.db_token_url,self.db_out_url

if __name__ == '__main__':
    cal = dbini()
    print(cal.set())