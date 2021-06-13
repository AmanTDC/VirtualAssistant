from bs4 import BeautifulSoup
import requests
def scrap_answer(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    print(soup.h1.getText())
    paras=soup.find_all('p')
    my_para=""
    for i in paras:
        if(len(i.getText())>40):
            my_para+=i.getText()
            break
    top=''
    top_=''
    my_text=""
    points=0
    lines=[]
    for i in my_para:
        if i=='.':
            points+=1
            lines+=[my_text]
        if points==2:
            break
        if i =='×':
            my_text+='times'
        elif i in ['\:','\"',';','/','ː']:
            print('enc')
        elif i=='[':
            top=i
        elif i==']':
            top=''
        elif i=='(':
            top_=i
        elif i==')':
            top_=''
        elif top!='[' and top_!='(':
            my_text+=i
    print(my_text)
    return [my_text,lines]

def scrap_answer_from_list(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    tables=soup.find_all('table')
    req=0
    for i in range(len(tables)):
        if (len(tables[i].find_all('th')))>2:
            req=i
            break
    my_table=tables[req]
    cols=my_table.find_all('th')
    for i in range(len(cols)):
        if 'name' in cols[i]:
            req=i
    cols=my_table.find_all('td')
    r_str=(cols[req].getText())
    print(r_str)
    return r_str
            
        

#scrap_answer_from_list('https://en.wikipedia.org/wiki/list_of_tallest_people')
        
