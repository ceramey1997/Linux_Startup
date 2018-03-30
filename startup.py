#! /usr/bin/env python3

import os
import webbrowser
from time import sleep
from subprocess import Popen

class Streamline_StartUp():
    stationary_dir = os.getcwd()
    
    #simplify code complexity
    def open_all(self):
        sleep(25)
        self.firefox_open("https://owa.adtran.com/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fowa.adtran.com%2fowa%2f")
        sleep(2)
        self.firefox_open_after_first("https://adtran-cn.hipchat.com/chat/room/3197689")
        sleep(2)
        self.vsCode_open()
        sleep(4)
        self.hex_chat()
        sleep(2)
        self.open_slack()

    #used to make sure directory always defaults back home
    def change_dirback(self):
        os.chdir(self.stationary_dir)
    
    #open's firefox
    def firefox_open_after_first(self, website):
        webbrowser.get('firefox').open_new_tab(website)

    #open's firefox first time
    def firefox_open(self, website):
        webbrowser.get('firefox').open_new(website)

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

def main():
    starting_computer = Streamline_StartUp()
    starting_computer.open_all()

if __name__ == '__main__':
    main()
