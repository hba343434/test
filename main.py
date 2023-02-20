import mechanize
import urllib.parse
b=mechanize.Browser()
b.set_handle_robots(False)
b.addheader=[('User-agent', 'Firefox')]
usr_id=int(input('give me starter id'))


while True:
    res=b.open(f'https://www.facebook.com/{usr_id}/')
    
    usr_id+=1
    if "people" not in b.geturl() :
        continue
    splited=b.geturl().split('/')
    usr_name=urllib.parse.unquote(splited[4].replace('-',' '))
    usr_Sid=splited[5]
    
    print(usr_name+"|"+usr_Sid)