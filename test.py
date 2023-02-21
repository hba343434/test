
import mechanize
import urllib.parse
b=mechanize.Browser()
b.set_handle_robots(False)
b.addheader=[('User-agent', 'Firefox')]
usr_id=int(input('give me starter id '))


while True:
    res=b.open(f'https://www.facebook.com/{usr_id}/')
    
    print(res.geturl())
    if "people" not in b.geturl() :
        usr_id+=1
        continue
    splited=b.geturl().split('/')
    
    usr_name=urllib.parse.unquote(splited[4].replace('-',' '))
    usr_Sid=str(usr_id)
    
    print(usr_name+"|"+usr_Sid)
    usr_id+=1
    print(usr_id)