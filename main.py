import requests

headers={
    'Cache-Control': 'max-age=0',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie':'BAIDUID=264F8964343DAC423D971A473A40689F:FG=1; BIDUPSID=264F8964343DAC423D971A473A40689F; PSTM=1517902528; H_PS_PSSID=25638_1464_21116_17001_22157; PANWEB=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; FP_UID=b27f2fb43e4d8c00883a5e21124a859d; pan_login_way=1; SCRC=70707596e52685bac6e96fafe24383a8; STOKEN=b03658e08a9fc797519e4f68ea219449d4e917152662e4430173f0f4e97a1b7a; cflag=15%3A3; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1517907351,1517907888,1517908586; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1517908586; PANPSC=10699390594692552724%3A4jL3HSqVSCJKre7vQtMDdLHQG6qeixv085lrraly0wTPsWSbQ9iuo6LmN5cEiUSJ6xvOAbnsJmskGiJzAoFozWfj2IOkIzsvIsULmepfTEQeWJt8ExZqCAykIuMps2rwzs5wT6eh4oFlVnBz%2FZp9zD4wgdQ%2F1cWMmgeUfIab6RA1jwuzSnCYVQe6OVID6DFBsHHN9wux3JA%3D'
}


sess = requests.Session()
sess.headers.update(headers)
# resp = sess.get('https://passport.baidu.com/v2/api/?login ',verify=False)
resp = sess.get('https://pan.baidu.com/disk/cmsdata?do=client&t=1517908606560&channel=chunlei&clienttype=0&web=1&logid=MTUxNzkwODYwNjU1NzAuMzQzNjM5MzY4NjM5MzE4OQ==',verify=False)
# resp
print(resp.headers)
