# Gzc
基于脚本的微信bot
# 微信机器人示例

这是一个使用 Gzc 库创建的简单微信机器人示例。该机器人能够执行数学计算、解方程，以及获取并分享歌曲信息。

## 目录

- [功能特性](#功能特性)
- [环境准备](#环境准备)
- [使用说明](#使用说明)
  - [创建微信机器人](#创建微信机器人)
  - [添加命令处理函数](#添加命令处理函数)
  - [注册命令](#注册命令)
  - [启动机器人](#启动机器人)
  - [发送消息和文件](#发送消息和文件)
- [贡献](#贡献)
- [许可证](#许可证)

## 功能特性

- 计算数学表达式
- 解一元一次方程
- 获取歌曲信息及评论

## 环境准备

在使用本库之前，请确保您已安装 Python 和 Gzc 库。您可以使用以下命令安装 Gzc 库（如果尚未安装）:

```bash
pip install Gzc
```

## 使用说明

### 创建微信机器人

首先，导入 Gzc 库并创建一个 `WechatBot` 实例：

```python
from Gzc import *

bot = WechatBot()
```

### 添加命令处理函数

您可以添加自定义处理函数来处理不同的指令。以下是几个示例处理函数：

1. **计算表达式**:

    ```python
    def handle_calculate(text):
        try:
            result = eval(text[4:])
        except Exception:
            result = '未知错误'
        bot.send_message(result)
    ```

2. **解方程**:

    ```python
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
    ```

3. **获取歌曲**:

    ```python
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
    ```

### 注册命令

创建一个字典，将指令与处理函数关联，以便机器人能够识别并处理用户输入的命令：

```python
command_handlers = {
    '/计算': handle_calculate,
    '/解方程': handle_solve_equation,
    '/歌曲': handle_get_song,
}
```

### 启动机器人

使用 `bot.run` 方法启动机器人，并指定命令处理器：

```python
bot.run('qun.png', command_handlers)
```

此方法将启动机器人，监听来自微信的信息，并调用相应的命令处理函数。

### 发送消息和文件

在处理函数中，您可以使用 `bot.send_message(content)` 发送文本消息。

要发送文件，使用 `bot.send_file(file_path)`，其中 `file_path` 是您要发送的文件路径。例如，在 `handle_get_song` 函数中：

```python
bot.send_file('song.png')
```

## 贡献

欢迎您为这个项目贡献代码或提出建议！请提交您的 Pull Request 或 Issues。

## 许可证

该项目使用 MIT 许可证。有关详细信息，请查看 [LICENSE](LICENSE) 文件。
