#facebook login
import requests
from bs4 import BeautifulSoup as bs


def fb_login(d):
        url='http://www.facebook.com'
        headers={'User-Agent':'Mozilla/5.0'}
        r=requests.get(url)
        cookies=r.cookies
        soup=bs(r.text,'html.parser')
        form=soup.find('form',{'id':'login_form'})
        inputs=form.find_all('input')
        load={}
        for i in inputs:
                load[i.get('name')]=i.get('value')
        load['email']=d['email']
        load['pass']=d['pass']
        s=requests.session()
        r=s.post(form.get('action'),data=load,headers=headers,cookies=cookies)
        result={}
        result={'session':s,'resp':r}
        return result



if __name__=='__main__':
        email=input("enter email")
        password=input('enter password')
        s={'email':email,'pass':password}
        res=fb_login(s)
        print('login ready')
        



