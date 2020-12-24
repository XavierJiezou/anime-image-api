# %%1.韩小韩API
import json, requests
url = 'https://api.vvhan.com/api/acgimg'
params = {'type': 'json'}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))


# %%2.樱花API
import json, requests
url = 'http://www.dmoe.cc/random.php'
params = {'return': 'json'}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))


# %%3.岁月小筑API
import json, requests
url = 'https://img.xjh.me/random_img.php'
params = {
    'return': 'json',
    'type': 'bg',
    'cytpe': 'acg'
}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))


# %%4.Lucky小站API
import json, requests
url = 'https://www.rrll.cc/tuceng/ecy.php'
params = {
    'return': 'json'
}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))


# %%5.一叶三秋API
import json, requests
url = 'https://api.ghser.com/random/api.php'
res = requests.get(url)
print(res.url)


# %%6.汐岑API
import json, requests
url = 'https://acg.yanwz.cn/wallpaper/api.php'
res = requests.get(url)
with open('test.jpg', 'wb') as f:
    f.write(res.content)

# %%7.呓喵酱API
import json, requests
url = 'https://api.yimian.xyz/img'
params = {
    'type': 'moe',
    'size': '1920x1080'
}
res = requests.get(url, params=params)
print(res.url)