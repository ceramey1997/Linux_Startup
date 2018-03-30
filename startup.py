#! /usr/bin/env python3

import os
import webbrowser
#import pyautogui
import keyboard
from time import sleep
from subprocess import Popen

class Important_Programs_Open():
    stationary_dir = os.getcwd()
    
    #simplify code complexity
    def open_all(self):
        sleep(25)
        self.firefox_open("https://owa.adtran.com/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fowa.adtran.com%2fowa%2f")
        sleep(2)
        self.firefox_open("https://adtran-cn.hipchat.com/chat/room/3197689")
        sleep(2)
        self.vsCode_open()
        sleep(10)
        self.open_terminal()
        sleep(1)
        self.hex_chat()
        sleep(2)
        self.open_slack()

    #used to make sure directory always defaults back home
    def change_dirback(self):
        os.chdir(self.stationary_dir)
    
    #open's firefox
    def firefox_open(self, website):
        webbrowser.get('firefox').open_new_tab(website)

    #open IDE
    def vsCode_open(self):
        os.chdir("/usr/bin")
        Popen(['code'])
        os.chdir(self.stationary_dir)

    #open's Hex Chat
    def hex_chat(self):
        os.chdir("/usr/bin")
        Popen(['hexchat'])
    
    #open's slack
    def open_slack(self):
        os.chdir("/usr/bin")
        Popen(['slack'])
    
    #open's one terminal
    def open_terminal(self):
        keyboard.press('ctrl')
        keyboard.press('alt')
        keyboard.press('t')
        keyboard.release('t')
        keyboard.release('ctrl')
        keyboard.release('alt')
        #pyautogui.hotkey('ctrl', 'alt', 't')

def main():
    starting_computer = Important_Programs_Open()
    starting_computer.open_terminal()
    #starting_computer.open_all()

if __name__ == '__main__':
    main()
