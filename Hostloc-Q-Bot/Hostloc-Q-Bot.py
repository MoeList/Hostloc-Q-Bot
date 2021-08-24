# encoding=utf-8

import requests
import time
from urllib import parse

hostloc_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", ]
hostloc_title = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", ]
url_1 = "https://www.hostloc.com/"
qq='群号'
port='5700'
while True:
    try:
        with requests.get('https://hostloc.cherbim.ml/', stream=True, timeout=5) as r:
            print(time.strftime("%m-%d %H:%M:%S", time.localtime()))
            for i in r.json()["new_data"][0][15:]:
                if i['主题ID'] in hostloc_list or i['主题'] in hostloc_title:
                    pass
                else:
                    hostloc_list = hostloc_list[1::]
                    hostloc_list.append(i['主题ID'])
                    hostloc_title = hostloc_title[1::]
                    hostloc_title.append(i['主题'])
                    a = "https://www.hostloc.com/thread-{0}-1-1.html".format(i['主题ID'])
                    time_1 = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())
                    if "论坛bug，此贴内容无法查看~" not in i['主题内容'][0:100]:
                        a = a
                    else:
                        a = f"<s>{a}</s>"
                    text = '主        题：' + "{}".format(i['主题'].replace("&", "%26").replace("<", "%26lt%3b").replace(">", "%26gt%3b").replace("#", " ")) + '\n' + '发  布  者：' + '''{1}'''.format(i['发布者链接'], i['发布者']) + '\n' + '时        间：' + time_1 + '\n' + '内容预览：' + '''{0}'''.format(i['主题内容'][0:100].replace("&", "%26").replace("<", "%26lt%3b").replace(">", "%26gt%3b").replace("#", " ")) + "\n" + "直达链接： " + a
                    print(text)
                    requests.get('http://127.0.0.1:' + port + '/send_group_msg?group_id=' + qq + '&message=' + text)
            time.sleep(2)
    except Exception:
        print("网络错误，请稍后重试")
        time.sleep(5)