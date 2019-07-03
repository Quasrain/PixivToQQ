# QQ-bot-FGOpictures

a QQ bot based on coolq and nonebot

## Description
It can send pictures with tags as you want.
Pictures are from http://pixiv.navirank.com/


## File Structure
```
├─Quasrain-bot
   ├─Quasrain
   │  └─plugins
   │      │  
   │      └─ pixiv.py
   │  bot.py
   └─ config.py
```

## Install Requirement
```
Python: Python>=3.6.1
Packages: nonebot>=1.3.0
```


### 2. Get It Work
#### Windows

1. Download [CoolQ](https://cqp.cc/b/news), install it.
> CoolQ Air version is for free but can receive/~send~ image
2. Add CoolQ plugin [CoolQ HTTP API](https://cqhttp.cc/docs/4.10/#/), install it follow the instruction.
3. Run CoolQ and Activate the plugin above.
4. Configure CoolQ HTTP API follow this [instruction](https://none.rclab.tk/guide/getting-started.html#%E9%85%8D%E7%BD%AE-coolq-http-api-%E6%8F%92%E4%BB%B6)
5. Run Bot

#### Linux
Bucause CoolQ has no linux version, but we can run it in docker.
1. Install [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. Get and Run Docker CoolQ (with CoolQ HTTP API) image follow this [instruction](https://cqhttp.cc/docs/4.10/#/?id=%E4%BD%BF%E7%94%A8-docker)
3. Run CoolQ and Activate the plugin above.
4. Configure CoolQ HTTP API follow this [instruction](https://none.rclab.tk/guide/getting-started.html#%E9%85%8D%E7%BD%AE-coolq-http-api-%E6%8F%92%E4%BB%B6), note that you should use post_url as 172.17.0.1 instead of 127.0.0.1 because of using Docker.
5. Run Bot

## Acknowledgements
Thanks for nonebot's very detailed instruction.\
https://none.rclab.tk/

Thanks for help from Akaisora.
