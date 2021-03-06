import requests,re

url = 'http://www.xicidaili.com/nn/1'
header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

def get_html(url): #访问代理网站
    response = requests.get(url,headers=header)
    if response.status_code==200:
        html = response.text
        return html
    else:
        print('error')
def get_index(html):#获得IP数据
    pattern = '<table id="ip_list">(.+?)</table>'
    data = re.search(pattern,html,re.S).group()
    pat = '<tr(.+?)</tr>'
    d2=re.findall(pat,data,re.S)
    return d2
def get_ip(list):#获得IP地址
    ips=[]
    for l in list[1:]:
        regex = '<td>(.+?)</td>'
        base_ip = re.findall(regex, l)
        ip = base_ip[0]+':'+base_ip[1]
        ips.append(ip)
    return ips
def test_ip(ips):#检测IP地址是否有效，删除失效IP
    url = 'https://www.baidu.com/'
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    for ip in ips:
        proxy = {'http': 'http://%s' %ip}
        try:
            response = requests.get(url, headers=header, proxies=proxy,time_out=10)
            if response.status_code != 200:
                #print('此IP失效', ip)
                ips.remove(ip)
        except:
            #print('此IP失效', ip)
            ips.remove(ip)
def main():
    html = get_html(url)
    list = get_index(html)
    ips = get_ip(list)
    test_ip(ips)
    return ips

