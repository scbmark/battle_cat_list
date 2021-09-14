import bs4
import requests
import os

# url='cat_list.html'
# root=open(url,encoding='utf-8')
seed='3109254173'
event='2021-08-30_607'
lang='tw'

url=f"https://bc.godfat.org/cats?seed={seed}&event={event}&lang={lang}"
User_Agent={'user_agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

root=requests.get(url,headers=User_Agent)
htmlfile=bs4.BeautifulSoup(root.text,"lxml")
cats_legend=htmlfile.find('ol')
cats_uber=cats_legend.find_next_sibling('ol')
cats_supa=cats_uber.find_next_sibling('ol')
cats_rare=cats_supa.find_next_sibling('ol')


def get_blue():
    cats_blue_name=[]
    cats_blue_name.append('黑獸加迪')
    cats_blue_name.append('幼獸加爾')
    cats_blue_name.append('禍根魔女凱斯莉')
    cats_blue_name.append('災難少女凱斯莉')
    cats_blue_name.append('影傑漆黑達太貓')
    cats_blue_name.append('幼傑達太貓')
    cats_blue_name.append('黑無垢御靈')
    cats_blue_name.append('巫女姬御靈')
    cats_blue_name.append('黑獸牙王')
    cats_blue_name.append('幼獸加歐')
    return cats_blue_name

def get_legend():
    
    cats_legend_list=cats_legend.find_all('li')
    cats_legend_name=[]

    for list in cats_legend_list:
        name=list.find('span')
        cats_legend_name.append(name.string)
    return cats_legend_name

def get_uber():
    cats_uber_list=cats_uber.find_all('li')
    cats_uber_name=[]

    for list in cats_uber_list:
        name=list.find('span')
        cats_uber_name.append(name.string)
    cats_uber_name.remove('黑獸加迪')
    cats_uber_name.remove('幼獸加爾')
    cats_uber_name.remove('禍根魔女凱斯莉')
    cats_uber_name.remove('災難少女凱斯莉')
    cats_uber_name.remove('影傑漆黑達太貓')
    cats_uber_name.remove('幼傑達太貓')
    cats_uber_name.remove('黑無垢御靈')
    cats_uber_name.remove('巫女姬御靈')
    cats_uber_name.remove('黑獸牙王')
    cats_uber_name.remove('幼獸加歐')
    return cats_uber_name

def get_supa():
    cats_supa_list=cats_supa.find_all('li')
    cats_supa_name=[]

    for list in cats_supa_list:
        name=list.find('span')
        cats_supa_name.append(name.string)
    return cats_supa_name

def get_rare():
    cats_rare_list=cats_rare.find_all('li')
    cats_rare_name=[]

    for list in cats_rare_list:
        name=list.find('span')
        cats_rare_name.append(name.string)
    return cats_rare_name