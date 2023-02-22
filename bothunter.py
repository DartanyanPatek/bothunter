import pyperclip
import time
import pyautogui
import win32api
import keyboard
import re 
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import os 
import pyfiglet
import sys

webhook = DiscordWebhook(url='ENTER DISCORD WEBHOOK')
    
mylist = ['!', '?', '*', '$', '"', '%', '@', '&', '#', '^', '(', ')', '_', "'", '+', '-', ' ', '№', ';', '=', '-']   

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'



token = input('Enter your autorization token:') 


headers = {
'Authorization': token
}

def main(): 
    os.system('cls')
    print("Stress Notify Tool 'Bot Hunter'") 
    user = input('Enter your nickname: ')
    while True:
        for i in range(10000):
            a = pyperclip.paste()
        s = re.sub(str(mylist), '', a)
        nametag = re.sub('https://discord.gg/', '', s)
        ad = pyperclip.copy(s)
        print('Modified from: ' + a + '  ==>  ' + s) 
        if keyboard.is_pressed('ctrl' and 'c'):
            print("Open Link!")
            zapros = requests.post('https://discordapp.com/api/v6/invites/' +  nametag, headers=headers)
            print(zapros)
            embed = DiscordEmbed(title='BOT HUNTER', color=242424)
            embed.add_embed_field(name='User who use:', value=user, inline=False)
            embed.add_embed_field(name='Modify From', value=a, inline=True)
            embed.add_embed_field(name='Modify To', value=s, inline=True)
            webhook.add_embed(embed)
            response = webhook.execute()

if __name__ == '__main__':
    main()
