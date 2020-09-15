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
    return str(val)                #返回网页源码
    
    

begintime = 2015
endtime =  2021
chengben = 0.0
zongjine = 0.0
fenshu = 0.0
fenshu1 = 0.0
fenshu2 = 0.0
for i in range(begintime,endtime):
    begintime1 = str(i-1)+"-12-31"
    endtime1 = str(i)+"-01-01"
    aaa = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&sdate=%s&edate=%s&per=40&page=1'
    msg =  aaa %("100032",begintime1,endtime1)
    #val = BeautifulSoup(get_html(msg), 'lxml')   #初始化BeautifulSoup库,并设置解析器
    val = get_html(msg)
    aaa = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&sdate=%s&edate=%s&per=40&page=1'
    msg =  aaa %("000834",begintime1,endtime1)
    val1 = get_html(msg)#, 'lxml')   #初始化BeautifulSoup库,并设置解析器
    aaa = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&sdate=%s&edate=%s&per=40&page=1'
    msg =  aaa %("217011",begintime1,endtime1)
    #val = BeautifulSoup(get_html(msg), 'lxml')   #初始化BeautifulSoup库,并设置解析器
    val2 = get_html(msg)
    zongjine = fenshu*float(val) +fenshu1*float(val1) +fenshu2*float(val2)+ 20000
    fenshu = zongjine*0.35/float(val)
    fenshu1 = zongjine*0.35/float(val1)
    fenshu2 = zongjine*0.3/float(val2)
    chengben = chengben + 20000
    begintime1 = str(i)+"-06-30"
    endtime1 = str(i)+"-07-01"
    msg =  aaa %("100032",begintime1,endtime1)
    val = get_html(msg)#, 'lxml')   #初始化BeautifulSoup库,并设置解析器
    aaa = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&sdate=%s&edate=%s&per=40&page=1'
    msg =  aaa %("000834",begintime1,endtime1)
    val2 = get_html(msg)#, 'lxml')   #初始化BeautifulSoup库,并设置解析器    
    aaa = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&sdate=%s&edate=%s&per=40&page=1'
    msg =  aaa %("217011",begintime1,endtime1)
    val2 = get_html(msg)
    zongjine = fenshu*float(val) +fenshu1*float(val1) +fenshu2*float(val2)+ 20000
    fenshu = zongjine*0.35/float(val)
    fenshu1 = zongjine*0.35/float(val1)
    fenshu2 = zongjine*0.3/float(val2)
    chengben = chengben + 20000
    print("zongjine：%s   chengben：%s" % (zongjine, chengben))

