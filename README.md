# Gzc
基于脚本的微信bot
概述
该文档介绍如何使用Gzc库创建微信机器人，包括如何添加函数和指令，如何启动机器人，以及如何发送消息和文件。

环境准备
在使用本库之前，请确保您已安装Python和Gzc库。可以使用以下命令安装Gzc库（如果尚未安装）:

pip install Gzc
基本用法
创建微信机器人
首先，我们需要实例化一个WechatBot对象：

from Gzc import *

bot = WechatBot()
添加命令处理函数
您可以添加自定义处理函数，来处理不同指令。

以下是几个示例处理函数:

计算表达式:

def handle_calculate(text):
    try:
        result = eval(text[4:])
    except Exception:
        result = '未知错误'
    bot.send_message(result)
解方程:

from sympy import symbols, Eq, solve

def handle_solve_equation(text):
    try:
        x = symbols('x')
        equation_str = text[5:].split('=')
        equation = Eq(eval(equation_str[0]), eval(equation_str[1]))
        result = solve(equation, x)
    except Exception as e:
        print(e)
        result = str(e)
    bot.send_message(result)
获取歌曲:

def handle_get_song(text):
    song = wyy.getSong(text[4:])
    if song:
        bot.send_message(f"曲名:{song['songName']}\n曲师:{song['artists']}")
        time.sleep(1)
        if song['comments'] and song['comments'][0]['content'] != '暂无评论':
            comment = song['comments'][0]
            bot.send_message(f"评论top1:\n{comment['content']}\n点赞数:{comment['likedCount']}\nby {comment['nickname']}\n{comment['time']}")
            bot.send_file('song.png')
    else:
        bot.send_message('没有找到歌曲呢......')
注册命令
创建一个字典，映射指令到处理函数，以便机器人能够识别并处理用户输入的命令。

command_handlers = {
    '/计算': handle_calculate,
    '/解方程': handle_solve_equation,
    '/歌曲': handle_get_song,
}
启动机器人
使用bot.run方法来启动机器人并指定命令处理器。

bot.run('qun.png', command_handlers)
此方法将启动机器人，监听来自微信的信息，并调用相应的命令处理函数。

发送消息和文件
在处理函数中，您可以使用bot.send_message(content)来发送文本消息。

要发送文件，可以使用bot.send_file(file_path)，其中file_path是您想要发送的文件的路径。

例如，在handle_get_song函数中，我们使用：

bot.send_file('song.png')
来发送名为song.png的文件。

总结
引入Gzc库并实例化WechatBot。
定义处理函数以处理特定指令。
创建一个命令映射字典。
启动机器人并指定命令处理器。
通过send_message和send_file发送消息和文件。
通过遵循以上步骤，您可以快速上手并扩展您的微信机器人功能。你也可以根据需要添加更多处理函数和命令以丰富bot的功能。
