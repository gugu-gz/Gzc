import pyautogui
import time
import pygetwindow as gw
import pyperclip
from sympy import symbols, Eq, solve
import wyy


class WechatBot:
    def __init__(self):
        # 获取可见或最小化的微信窗口
        self.wechat_windows = [
            w for w in gw.getWindowsWithTitle('微信') if w.visible or w.isMinimized
        ]
        
        if not self.wechat_windows:
            print('没有找到微信窗口')
            raise RuntimeError('没有找到微信窗口')

        self.wechat_window = self.wechat_windows[0]

    def activate_window(self):
        print('正在激活微信窗口')
        self.wechat_window.restore()
        self.wechat_window.activate()
        time.sleep(1)
        print('正在最大化微信窗口')
        pyautogui.moveTo(10, 10, duration=0.5)
        if not self.find_and_click('images/big.png'):
            print('无需最大化,已跳过流程')

    def find_and_click(self, image, wait_time=1):
        try:
            location = pyautogui.locateOnScreen(image)
            if location:
                pyautogui.click(location)
                time.sleep(wait_time)
                return True
        except Exception as e:
            return False
    
    def send_file(self, file):
        self.find_and_click('images/file.png')
        time.sleep(1)
        self.find_and_click(file)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('enter')

    def run(self,qun,command):
        self.activate_window()
        while True:
            try:
                if self.find_and_click(qun):
                    pyautogui.doubleClick(460, 810)
                    pyautogui.hotkey('ctrl', 'c')
                    text = pyperclip.paste()
                    # ... 处理输入的指令
                    InCommand = text.split(' ')[0]
                    handler = command.get(InCommand)
                    if handler:
                        handler(text)
                    time.sleep(1)
                    
                    # 点击恢复到输入框
                    pyautogui.click(200, 180)
            except Exception as e:
                print(e)

    def send_message(self, result):
        pyautogui.click()
        pyautogui.rightClick(460, 810)
        self.find_and_click('images/reply.png')
        message = f'{result}'
        pyperclip.copy(message)
        pyautogui.click(200, 100)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')