from nonebot import on_command, CommandSession

import requests
import re
import os
from urllib.request import urlopen
from urllib.parse import quote

# on_command 装饰器将函数声明为一个命令处理器
# 这里 pixiv为命令的名字，同时允许使用别名「pictures」
@on_command('pixiv', aliases=('pictures'))
async def pixiv(session: CommandSession):
    # 从会话状态（session.state）中获取tag，如果当前不存在，则询问用户
    tag = session.get('tag', prompt='你想看哪个老婆呢？')
    # 获取在pixiv年鉴上排行最高的十张图片
    for i in range(10):
        pictures = await get_url_of_tag(tag,i)
    # 向用户发送这些图片
        if (pictures == 'none'):
            if (i==0):
                await session.send(pictures)
                break
        await session.send(pictures)
        if (pictures == 'none'):
            break


# pixiv.args_parser 装饰器将函数声明为 pixiv 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@pixiv.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将tag跟在命令名后面，作为参数传入
            # 例如用户可能发送了 pixiv saber
            session.state['tag'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的tag（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的老婆名称不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg

async def get_url_of_tag(tag: str, k) -> str:
    tag = quote(tag)
    url = 'http://pixiv.navirank.com/search/?words='+tag+'&mode=0&type=0&comp=0'
    trueurl = 'http://pixiv.navirank.com/jpg'
    html = urlopen(
        url
    ).read().decode('utf-8')
    Pattern = re.compile('/[a-zA-Z0-9]+/[a-zA-Z0-9]+.jpg')
    result = Pattern.findall(html)
    ans = "none"
    cnt = 0
    for urls in result:
        cnt =cnt+1
        Pattern = re.compile('/[a-zA-Z0-9]+')
        Res = Pattern.findall(urls)
        filename = Res[1]+'.jpg'
        # print(trueurl+Res[0]+'\n')
        # ans = ans+"[CQ:image,file="+'1.jpg'+"]"
        # ans = ans + trueurl + urls+ '\n';
        if (cnt > k):
            ans = "[CQ:image,file=" + trueurl + urls + "]"
            print(trueurl + urls + '\n')
            break
    return ans