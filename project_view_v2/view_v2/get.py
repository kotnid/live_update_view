import requests
import bs4

from .check import check

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

def get():
    r = requests.get("https://ani.gamer.com.tw" , "html.parser" , headers= header)
    soup = bs4.BeautifulSoup(r.text , 'lxml')
    datas = soup.find_all("a", {"class": "anime-card-block"})

    for data in datas:
        details = data.find_all("p",{"class":""})

        if len(list(details)) == 3:
            if "萬" in list(details)[2].string:
                num = int(float(list(details)[2].string.replace("萬","")))*10000
                check(list(details)[1].string,num)
            elif "統計中" in list(details)[2].string:
                num = 0
                check(list(details)[1].string,num) 
            else:
                num = int(list(details)[2].string)
                check(list(details)[1].string,num)
             

        if len(list(details)) == 2:
            if "萬" in list(details)[1].string:
                num = int(float(list(details)[1].string.replace("萬","")))*10000
                check(list(details)[0].string,num)
            elif "統計中" in list(details)[1].string:
                num = 0 
                check(list(details)[0].string,num)
            else:
                num = int(list(details)[1].string)
                check(list(details)[0].string,num)

if __name__ == "__main__":
    get()                    