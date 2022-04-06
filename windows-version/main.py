import getpass
from requests import get
import time
from os import name, system
import subprocess
from tkinter import *
from tkinter.ttk import *
import webbrowser
import tempfile
import platform
import os
from datetime import datetime
import socket
import re
import uuid
import psutil
import winreg

# Downloads
audacity_d = "https://www.audacityteam.org/download/windows/"
blender_d = "https://www.blender.org/download/release/Blender3.0/blender-3.0.1-windows-x64.msi/"
firefox_d = "https://www.mozilla.org/en-US/firefox/download/thanks/"
internetexplorerenus_d = "https://www.microsoft.com/en-US/download/confirmation.aspx?id=41628"
internetexplorersvse_d = "https://www.microsoft.com/sv-SE/download/confirmation.aspx?id=41628"
internetexplorerzhcn_d = "https://www.microsoft.com/zh-CN/download/confirmation.aspx?id=41628"
internetexplorerjajp_d = "https://www.microsoft.com/ja-JP/download/confirmation.aspx?id=41628"
microsoftedgeen_d = "https://go.microsoft.com/fwlink/?linkid=2108834&Channel=Stable&language=en"
microsoftedgesv_d = "https://go.microsoft.com/fwlink/?linkid=2108834&Channel=Stable&language=sv"
microsoftedgezhcn_d = "https://go.microsoft.com/fwlink/?linkid=2108834&Channel=Stable&language=zh-CN"
microsoftedgeja_d = "https://go.microsoft.com/fwlink/?linkid=2108834&Channel=Stable&language=ja"
winrar_d = "https://www.win-rar.com/postdownload.html?&L=0"

curVer = 0.06


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def portscan():
    clear()

    remoteServer = input("Enter a remote host to scan")
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    t1 = datetime.now()

    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()

    total = t2 - t1

    print('Scanning Completed in: ', total)

        
def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list


ip = get('https://api.ipify.org').content.decode('utf8')
user = getpass.getuser()
boot = "UEFI" if os.path.exists("/sys/firmware/efi") else "BIOS"
cwd = os.getcwd()
cwdfiles = os.listdir(cwd)
# c = webbrowser.get('windows-default')

print("You are using version " + str(curVer) + " of senaw-console-tools")
while True:
    stdin = input(user + "> ")

    if stdin == "help":
        print("help | This command allows you to see all commands\n"
              "IP | This command allows you to see your public IP address\n"
              "software_installed | This command allows you to see all installed software on your computer\n"
              "pc_specs | This command allows you to see a variety of your computer's specifications\n"
              "IP_MEME | This command allows you to run a D4DJ IP meme. "
              "This will display your actual public IP so be careful\n"
              "clear | This command allows you to clear out all previous commands\n"
              "portscan | This command allows you to scan ports, please consider consequences and your nations regulations and laws if you are planning to scan networks beside your own\n"
              "open | This command allows you to open software\n"
              "web_browse | This command allows you to visit a website\n"
              "web_search | This command allows you to search using google\n"
              "sourcec | This command allows you to see information about this program\n"
              "license | This command sends you to the MIT license\n"
              "boot | This command checks if your system is booted with bios or uefi\n"
              "download | This command allows you to download programs from a library of listed programs\n"
              "downloads | This command allows you to see all possible downloads\n"
              "github | This command sends you to the github repository for this project\n"
              "cwd | This command allows you to see  your current working directory\n"
              "cwd_files | This command allows you to look inside your current working directory\n"
              "exit | This command allows you to leave this console")

    if stdin == "IP":
        print(ip)

    if stdin == "IP_MEME":
        ip = get('https://api.ipify.org').content.decode('utf8')
        website = "https://www.youtube.com/watch?v=Fah9BwbyUEo"

        webbrowser.open(website)
        time.sleep(2)
        print(ip)

        root = Tk()
        w = 1920
        h = 100
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        print(ws, hs)
        # x = (ws/2) - (w/2)
        # y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, 0, 0))

        ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
                b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
                b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x01\x00\x00\x00\x01') + b'\x00' * 1282 + b'\xff' * 64

        _, ICON_PATH = tempfile.mkstemp()
        with open(ICON_PATH, 'wb') as icon_file:
            icon_file.write(ICON)

        root.title("")
        root.iconbitmap(default=ICON_PATH)

        label = Label(root, text=str(ip), font="-weight bold -size 55").pack()

        root.mainloop()
        
    if stdin == "portscan":
        portscan()
    
    if stdin == "downloads":
        print("audacity\n"
              "blender\n"
              "firefox\n"
              "ie-en-US\n"
              "ie-sv-SE\n"
              "ie-zh-CH\n"
              "ie-ja-JP\n"
              "me-en-US\n"
              "me-sv-SE\n"
              "me-zh-CH\n"
              "me-ja-JP\n"
              "winrar\n")

    if stdin == "github":
        webbrowser.open("https://github.com/senawDragon/senaw-console-tools")

    if stdin == "boot":
        print("The system is booted with %s" % boot)

    if stdin == "cwd":
        print(cwd)

    if stdin == "cwd_files":
        print(cwdfiles)

    if stdin == "sourcec":
        print("Program use | This program can be used to obtain different information about your computer."
              " It can also be used to open software, use web browsers and even download other programs\n"
              "Google Chrome | This program uses google chrome as browser\n"
              "Source code | Visit senawDragon's github page to find the source code in one of my repositories\n"
              "License | MIT license, find more about the license in my github repo or"
              " by using the license command.\n"
              "senawDragon | License owner and the sole owner and creator of this project")

    if stdin == "license":
        webbrowser.open("https://opensource.org/licenses/MIT")

    if stdin == "open":
        openin = input(user + "_open> ")
        if openin == "exit":
            break
        else:
            subprocess.call([openin])

    if stdin == "download":
        downloadin = input(user + "_download> ")
        if downloadin == "exit":
            break

        if downloadin == "audacity":
            url = audacity_d
            webbrowser.open(url)

        if downloadin == "blender":
            url = blender_d
            webbrowser.open(url)

        if downloadin == "firefox":
            url = firefox_d
            webbrowser.open(url)

        if downloadin == "ie-en-US":
            url = internetexplorerenus_d
            webbrowser.open(url)

        if downloadin == "ie-sv-SE":
            url = internetexplorerenus_d
            webbrowser.open(url)

        if downloadin == "ie-en-US":
            url = internetexplorerenus_d
            webbrowser.open(url)

        if downloadin == "ie-zh-CH":
            url = internetexplorerzhcn_d
            webbrowser.open(url)

        if downloadin == "me-ja-JP":
            url = internetexplorerjajp_d
            webbrowser.open(url)

        if downloadin == "me-en-US":
            url = internetexplorerenus_d
            webbrowser.open(url)

        if downloadin == "me-sv-SE":
            url = internetexplorerenus_d
            webbrowser.open(url)

        if downloadin == "me-en-US":
            url = internetexplorerenus_d
            webbrowser.open(url)

        if downloadin == "me-zh-CH":
            url = internetexplorerzhcn_d
            webbrowser.open(url)

        if downloadin == "me-ja-JP":
            url = internetexplorerjajp_d
            webbrowser.open(url)

        if downloadin == "winrar":
            url = winrar_d
            webbrowser.open(url)

    if stdin == "web_search":
        searchin = input(user + "_web-search> ")
        if searchin == "exit":
            break
        else:
            webbrowser.open("google.com/search?q=" + searchin)

    if stdin == "web_browse":
        browsein = input(user + "_web-browse> ")
        if browsein == "exit":
            break
        else:
            webbrowser.open(browsein)

    if stdin == "software_installed":
        software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE,
                                                                                     winreg.KEY_WOW64_64KEY) + foo(
            winreg.HKEY_CURRENT_USER, 0)
        for software in software_list:
            print('Name=%s, Version=%s, Publisher=%s' % (software['name'], software['version'], software['publisher']))
        print('Number of installed apps: %s' % len(software_list))


    if stdin == "pc_specs":
        print("Operative System |", platform.system(), "| Operative system release |", platform.release(), "| Operative system version", platform.version())
        print("Architecture |", platform.machine())
        print("Hostname |", socket.gethostname())
        print("Private IP-address |", socket.gethostbyname(socket.gethostname()))
        print("MAC-address |", ':'.join(re.findall('..', '%012x' % uuid.getnode())))
        print("Processor |", platform.processor())
        print("Amount of RAM-memory |", str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")

    if stdin == "clear":
        clear()

    if stdin == "exit":
        break
