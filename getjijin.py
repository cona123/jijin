import requests
import re
from bs4 import BeautifulSoup

def get_html(url):
    global fenshu
    global zongjine
    global chengben
    headers = {
        'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'
 
    }     #模拟浏览器访问
    response = requests.get(url,headers = headers)       #请求访问网站
    html = response.text       #获取网页源码
    serobject =re.findall(r"<td>(\d+-\d+-\d+)</td><td class='tor bold'>(\S+)</td><td class='tor bold'>(\S+)</td>",html, re.M)
    time = ""
    val = ""
    for i in serobject:
        time = i[0]
        val = i[2]

        

    #match=reg.search(str(html))
    #print(reg)
    if time!= "":
        print("时间2：%s   值2：%s" % (time, val))
        zongjine = fenshu*float(val) + 20000
        fenshu = 20000/float(val)+fenshu
        chengben = chengben + 20000
    return html                #返回网页源码
    
    

begintime = 2009
endtime =  2016
chengben = 0.0
zongjine = 0.0
fenshu = 0.0
for i in range(begintime,endtime):
    begintime1 = str(i-1)+"-12-31"
    endtime1 = str(i)+"-01-01"
    aaa = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&sdate=%s&edate=%s&per=40&page=1'
    msg =  aaa %("100032",begintime1,endtime1)
    soup = BeautifulSoup(get_html(msg), 'lxml')   #初始化BeautifulSoup库,并设置解析器
    begintime1 = str(i)+"-06-30"
    endtime1 = str(i)+"-07-01"
    msg =  aaa %("100032",begintime1,endtime1)
    soup = BeautifulSoup(get_html(msg), 'lxml')   #初始化BeautifulSoup库,并设置解析器
    print("zongjine：%s   chengben：%s" % (zongjine, chengben))

