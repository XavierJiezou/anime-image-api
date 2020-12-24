【python】7个随机二次元图片api接口汇总（附网页调用示例）

----
# 1. 韩小韩API
## 1.1. 接口文档
> [https://api.vvhan.com/dongman.html](https://api.vvhan.com/dongman.html)
## 1.2. 请求地址
> [https://api.vvhan.com/api/acgimg](https://api.vvhan.com/api/acgimg)

## 1.3. 请求方式
> get

## 1.4. 请求参数
|字段| 类型 | 描述 |
|--|--| -- |
| return | str | 响应数据格式，可选json |
## 1.5. 示例代码
```python
import json, requests
url = 'https://api.vvhan.com/api/acgimg'
params = {'type': 'json'}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))
```
## 1.6. 响应数据
```json
{
  "success": true,
  "imgurl": "https://cdn.jsdelivr.net/gh/uxiaohan/GitImgTypecho/Acg/api.vvhan.com[337].jpg",
  "info": {
    "width": 1920,
    "height": 1080,
    "type": "img"
  }
}
```
## 1.7. 图片预览
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201224150150477.jpg#pic_center)
## 1.8. 温馨提示
调用多次发现，该接口返回的图片尺寸大多是`1920x1800`，且图片`url`地址中只有最后`[ ]`里面的数值在变化，截止目前该变化范围是`0-696`，也就是该接口是从`697`张二次元图片中随机返回一张。如果你想下载该接口所有的`697`张图片，可以使用下方代码：
```python
'''依赖模块
pip install requests
'''
import concurrent.futures as cf
import os, time, requests

# 单张图片下载函数
def down(fname, url):
    res = requests.get(url)
    with open(fname, 'wb') as f:
        f.write(res.content)

# 进度条打印函数
def show(num, _sum,  runTime):
    barLen = 20
    perFin = num/_sum
    numFin = round(barLen*perFin)
    numNon = barLen-numFin
    leftTime = (1-perFin)*(runTime/perFin)
    print(
        f"{num:0>{len(str(_sum))}}/{_sum}",
        f"|{'█'*numFin}{' '*numNon}|",
        f"PROCESS: {perFin*100:.0f}%",
        f"RUN: {runTime:.0f}S",
        f"ETA: {leftTime:.0f}S",
        end='\r'
    )
    if num == _sum:
        print()

# 主函数（多线程）
def main():                  
    floder = './img/'
    os.makedirs(floder, exist_ok=True)
    fmt = 'https://cdn.jsdelivr.net/gh/uxiaohan/GitImgTypecho/Acg/api.vvhan.com[{}].jpg'
    total = 697
    with cf.ThreadPoolExecutor() as tp:
        t1 = time.time()
        futures = []
        for i in range(total):
            url = fmt.format(i)
            fname = floder+os.path.basename(url)
            future = tp.submit(down, fname, url)
            futures.append(future)
        count = 0
        for future in cf.as_completed(futures):
            count += 1
            t2 = time.time()
            show(count, total, t2-t1)
    os.system('pause')


main()
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201224164832570.jpg#pic_center)
# 2. 樱花API
## 2.1. 接口文档
> [http://www.dmoe.cc/](http://www.dmoe.cc/)

## 2.2. 请求地址
> [http://www.dmoe.cc/random.php](http://www.dmoe.cc/random.php)

## 2.3. 请求方式
> get

## 2.4. 请求参数
|字段| 类型 | 描述 |
|--|--| -- |
| return | str | 响应数据格式，设置为json即可|
## 2.5. 示例代码
```python
import json, requests
url = 'http://www.dmoe.cc/random.php'
params = {'return': 'json'}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))
```
## 2.6. 响应数据
```json
{
  "code": "200",
  "imgurl": "https://tva1.sinaimg.cn/large/0072Vf1pgy1foxkil4o6qj31hc0u0nbz.jpg",
  "width": "1920",
  "height": "1080"
}
```
## 2.7. 图片预览
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201224175019138.jpg#pic_center)
# 3. 岁月小筑API
## 3.1. 接口文档
> [http://img.xjh.me/](http://img.xjh.me/)

## 3.2. 请求地址
- https
> [https://img.xjh.me/random_img.php](https://img.xjh.me/random_img.php)

- http

> [http://img.xjh.me/random_img.php](http://img.xjh.me/random_img.php)
## 3.3. 请求方式
> get

## 3.4. 请求参数
|字段| 类型 | 描述 |
|--|--| -- |
| return | str | 响应数据格式，可选json或302 |
| type| str | 返回图片类型，可选bg即背景图 |
| ctype| str | 背景图类型，可选acg或nature |
## 3.5. 示例代码
```python
import json, requests
url = 'https://img.xjh.me/random_img.php'
params = {
    'return': 'json',
    'type': 'bg',
    'cytpe': 'acg'
}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))
```
## 3.6. 响应数据
```json
{
  "error": 0,
  "result": 200,
  "img": "//img.xjh.me/desktop/bg/acg/53829526_p0.jpg"
}
```
## 3.7. 图片预览
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201224185910517.jpg#pic_center)
# 4. Lucky小站API
## 4.1. 接口文档
> [https://www.nck.cc/index.php/archives/3/](https://www.nck.cc/index.php/archives/3/)


## 4.2. 请求地址
> [https://www.rrll.cc/tuceng/ecy.php](https://www.rrll.cc/tuceng/ecy.php)

## 4.3. 请求方式
> get

## 4.4. 请求参数
|字段| 类型 | 描述 |
|--|--| -- |
| return | str | 响应数据格式，可选json |
## 4.5. 示例代码
```python
url = 'https://www.rrll.cc/tuceng/ecy.php'
params = {
    'return': 'json'
}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))
```
## 4.6. 响应数据
```json
{
  "code": "200",
  "acgurl": "https://tva4.sinaimg.cn/large/0072Vf1pgy1foxkgc5msdj31hc0u01cv.jpg",
  "width": "1920",
  "height": "1080",
  "size": "jpg"
}
```
## 4.7. 图片预览
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201224201748118.jpg#pic_center)
# 5. 三秋API
## 5.1. 接口文档
> [https://api.ghser.com/acg.html](https://api.ghser.com/acg.html)

## 5.2. 请求地址
> [https://api.ghser.com/random/api.php](https://api.ghser.com/random/api.php)

## 5.3. 请求方式
> get/post

## 5.4. 请求参数
空
## 5.5. 示例代码
```python
import json, requests
url = 'https://api.ghser.com/random/api.php'
res = requests.get(url)
print(res.url)
```
## 5.6. 响应数据
返回`302`重定向后的图片`url`
```bash
https://tva1.sinaimg.cn/large/006gkh44ly1fz1kddbampj31hc0u0tyb.jpg
```
## 5.7. 图片预览
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201224203052967.jpg#pic_center)
# 6. 汐岑API
## 6.1. 接口文档
> [https://acg.yanwz.cn/](https://acg.yanwz.cn/)

## 6.2. 请求地址
> https://acg.yanwz.cn/wallpaper/api.php

## 6.3. 请求方式
> get

## 6.4. 请求参数
空
## 6.5. 示例代码
```python
import json, requests
url = 'https://acg.yanwz.cn/wallpaper/api.php'
res = requests.get(url)
with open('test.jpg', 'wb') as f:
    f.write(res.content)
```
## 6.6. 响应数据
二进制流图片
## 6.7. 图片预览
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201224204302803.jpg#pic_center)
# 7. 呓喵酱API
## 7.1. 接口文档
> [https://www.eee.dog/tech/rand-pic-api.html](https://www.eee.dog/tech/rand-pic-api.html)

## 7.2. 请求地址
> [https://api.yimian.xyz/img](https://api.yimian.xyz/img)

## 7.3. 请求方式
> get/post

## 7.4. 请求参数
|字段| 类型 | 描述 |
|--|--| -- |
| type| str | 图片类型，可选moe为二次元图 |
| size| str | 图片大小，可选1920x1080 |
## 7.5. 示例代码
```python
import json, requests
url = 'https://api.yimian.xyz/img'
params = {
    'type': 'moe',
    'size': '1920x1080'
}
res = requests.get(url, params=params)
print(res.url)
```
## 7.6. 响应数据
返回`302`重定向后的图片`url`
```bash
https://yimian-image.obs.cn-east-2.myhuaweicloud.com/moe/img_865_2048x1152_96.5199966430664_null_normal.jpg?AWSAccessKeyId=6LJRZC0YN3MQXXFOWMIH&Expires=1608815304&Signature=C5BWWC/r1/o230t1VVLHHmH0kF4%3D
```
## 7.7. 图片预览
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201224210829846.jpg#pic_center)
# 8. 调用代码汇总
```python
# %%1. 韩小韩API
import json, requests
url = 'https://api.vvhan.com/api/acgimg'
params = {'type': 'json'}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))


# %%2. 樱花API
import json, requests
url = 'http://www.dmoe.cc/random.php'
params = {'return': 'json'}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))


# %%3. 岁月小筑API
import json, requests
url = 'https://img.xjh.me/random_img.php'
params = {
    'return': 'json',
    'type': 'bg',
    'cytpe': 'acg'
}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))


# %%4. Lucky小站API
import json, requests
url = 'https://www.rrll.cc/tuceng/ecy.php'
params = {
    'return': 'json'
}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))


# %%5. 一叶三秋API
import json, requests
url = 'https://api.ghser.com/random/api.php'
res = requests.get(url)
print(res.url)


# %%6. 汐岑API
import json, requests
url = 'https://acg.yanwz.cn/wallpaper/api.php'
res = requests.get(url)
with open('test.jpg', 'wb') as f:
    f.write(res.content)

# %%7. 呓喵酱API
import json, requests
url = 'https://api.yimian.xyz/img'
params = {
    'type': 'moe',
    'size': '1920x1080'
}
res = requests.get(url, params=params)
print(res.url)
```
# 9. 网页调用示例
以`樱花API`为例
- 插入图片
```html
<img src="http://www.dmoe.cc/random.php"/>
```
- 背景图片
```html
<body style="background: url(http://www.dmoe.cc/random.php);"></body>
```
其它`API`只需要替换`src`或`url`属性值为以下值
```bash
1. 韩小韩API
https://api.vvhan.com/api/acgimg
2. 樱花API
http://www.dmoe.cc/random.php
3. 岁月小筑API
https://img.xjh.me/random_img.php?return=302
4. Lucky小站API
https://www.rrll.cc/tuceng/ecy.php
5. 一叶三秋API
https://api.ghser.com/random/api.php
6. 汐岑API
https://acg.yanwz.cn/wallpaper/api.php
7. 呓喵酱API
https://api.yimian.xyz/img
```