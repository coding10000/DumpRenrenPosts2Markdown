import requests
import os

HTML_DIR = 'original html'
DUMP_DIR = 'markdown'

class LoginRenRen():  
    
    s = requests.Session() 
      
    def __init__(self,name='',password='',domain=''):  
        self.name=name  
        self.password=password  
        self.domain=domain  
          
    def login(self):  
        params = {'domain': self.domain, 'email': self.name, 'password': self.password}  
        
        r = self.s.post(  
            'http://www.renren.com/PLogin.do',  
            data = params,
            allow_redirects = True,
        )  

        print('login.....')  
        
        print(r.url)
        with open(os.path.join(HTML_DIR,'test.html'), mode='w', encoding='utf-8') as f:
            f.write(r.text)


class Get_Blogpost(LoginRenRen):
    
    def __init__(self, name, password, domain):
        self.name=name  
        self.password=password  
        self.domain=domain  
        self.test_post_url = 'http://blog.renren.com/blog/282456584/917107448'  # 日志《漫画家从良》

    def get_test_post(self):
        r = self.s.get(self.test_post_url)
        with open(os.path.join(DUMP_DIR,'test_post.html'), mode='w', encoding='utf-8') as f:
            f.write(r.text)  
              
              
if __name__=='__main__':
    0 if os.path.exists(HTML_DIR) else os.mkdir(HTML_DIR)
    0 if os.path.exists(DUMP_DIR) else os.mkdir(DUMP_DIR)
     
      
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    domain = 'renren.com'  
    #ren = LoginRenRen(username, password, domain)  
    #ren.login()
    
    ren_get_blogpost = Get_Blogpost(username, password, domain)
    ren_get_blogpost.login()
    ren_get_blogpost.get_test_post()
    
    