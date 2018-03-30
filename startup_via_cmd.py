#! /usr/bin/env python3

import os
import webbrowser
import sys
import argparse
from time import sleep
from subprocess import Popen
import pyautogui

email_hipchat_urls = ["https://owa.adtran.com/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fowa.adtran.com%2fowa%2f", "https://adtran-cn.hipchat.com/home"]

class Important_Programs_Open():
    stationary_dir = os.getcwd()
    
    #used to make sure directory always defaults back home
    def change_dirback(self):
        os.chdir(self.stationary_dir)
    
    #open's firefox
    def firefox_open(self, websites):
        for website in websites:
            webbrowser.get('firefox').open_new_tab(website)

    #open IDE
    def ide_open(self, ide):
        os.chdir("/usr/bin")
        Popen([ide])
        os.chdir(self.stationary_dir)
    
    #open's Hex Chat
    def open_irc(self):
        os.chdir("/usr/bin")
        Popen(['hexchat'])
    
    #open's slack
    def open_slack(self):
        os.chdir("/usr/bin")
        Popen(['slack'])
    
    #open's one terminal
    def open_terminal(self):
        pyautogui.hotkey('ctrl', 'alt', 't')


if __name__ == '__main__':
    programs = Important_Programs_Open()
    parser = argparse.ArgumentParser()
    parser.add_argument("--i", help="put name of IDE as known by your computer")
    parser.add_argument("--w", action='append', default=[], help="url to website you would like to open")
    parser.add_argument("--s", action='store_true', help= "open slack")
    parser.add_argument("--a", help="opens slack, email, hipchat, hexchat, and the given IDE")
    parser.add_argument("--t", action='store_true', help= "open's a terminal... even though that is useless at this point")
    args = parser.parse_args()

    if args.w:
        programs.firefox_open(args.w)
    if args.i:
        programs.ide_open(args.i)
    if args.s:
        programs.open_slack()
    if args.a:
        programs.firefox_open(email_hipchat_urls)
        programs.ide_open(args.a)
        programs.open_slack()
        sleep(6)
        programs.open_irc()
    if args.t:
        programs.open_terminal()






