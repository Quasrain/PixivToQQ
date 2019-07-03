from nonebot import on_command, CommandSession

import requests
import re
import os
from urllib.request import urlopen
from urllib.parse import quote

# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('pixiv', aliases=('pictures'))
async def pixiv(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    tag = session.get('tag', prompt='你想看哪个老婆呢？')
    # 获取城市的天气预报
    for i in range(4):
        pictures = await get_url_of_tag(tag,i)
    # 向用户发送天气预报
        await session.send(pictures)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@pixiv.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['tag'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的老婆名称不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg

async def get_url_of_tag(tag: str,k) -> str:
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    tag = quote(tag)
    url = 'http://pixiv.navirank.com/tag/'+tag
    trueurl = 'http://pixiv.navirank.com/jpg'
    path = 'C:/tools/CQP-xiaoi/酷Q Pro/data/image'
    html = urlopen(
        url
    ).read().decode('utf-8')
    Pattern = re.compile('/[a-zA-Z0-9]+/[a-zA-Z0-9]+.jpg')
    result = Pattern.findall(html)
    ans = ""
    cnt = 0
    for urls in result:
        cnt =cnt+1
        Pattern = re.compile('/[a-zA-Z0-9]+')
        Res = Pattern.findall(urls)
        filename = Res[1]+'.jpg'
        # print(trueurl+Res[0]+'\n')
        print(trueurl+urls+'\n')
        ans = "[CQ:image,file="+trueurl+urls+"]"
        # ans = ans+"[CQ:image,file="+'1.jpg'+"]"
        # ans = ans + trueurl + urls+ '\n';
        if (cnt > k):
            break
    return ans