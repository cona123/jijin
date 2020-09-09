import requests
import re
from bs4 import BeautifulSoup
def get_html(url):
    headers = {
        'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'
 
    }     #模拟浏览器访问
    response = requests.get(url,headers = headers)       #请求访问网站
    html = response.text       #获取网页源码
    print(html)
    serobject =re.findall(r"<td>(\d+-\d+-\d+)</td><td class='tor bold'>(\S+)</td><td class='tor bold'>(\S+)</td>",html, re.M)
    print(serobject)
    time = ""
    val = ""
    for i in serobject:
        print ("时间：%s   值：%s" % (i[0], i[2]))
        time = i[0]
        val = i[2]

    #match=reg.search(str(html))
    #print(reg)
    if time!= "":
        print("时间2：%s   值2：%s" % (i[0], i[2]))
    return html                #返回网页源码
    
    

begintime = 2017 
endtime =  2020
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
