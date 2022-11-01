from instabot import Bot
import glob
import shutil
import re
from difPy import dif
from dotenv import load_dotenv
import os


# delete any duplicate images
dif("to_be_posted", delete=True, silent_del=True)

posts_list = glob.glob("to_be_posted/*")

# config folder's existence in directory throws an error 
# so following lines checks for it and then removes it each time script is run
try:
    shutil.rmtree("config")
except:
    pass

# Password for the Instagram account being used is stored in .env
load_dotenv('.env')
password = os.getenv("ui_expo_password")

def post_bot():
    
    bot = Bot()
    bot.login(username = "ui.expo", password = password)

    # select post from folder 
    photo = posts_list[0]

    print(photo)

    source = re.findall(r"'([^']*)'", photo)

    # caption
    caption = f"""
    
    🌐 Design source: @{source[0]}

    ++++++
    📣 Want to submit your design? Get in touch!
    ++++++
    📧 uiexpo.contact@gmail.com
    ++++++
    🔮 Follow @ui.expo for daily UI/UX/Web design inspiration

    #ui #ux #webdesign #website #userexperience #appdesign #photoshop #userinterface
    #graphicdesign #webdesigner #interface #designinspiration #webdeveloper #design #uidesign #digitalart #digitaldesign #uiux #uitrends #uiexpo
    #uxinspiration #art #designweb #uxdesign #uidesignpatterns
    """

    print(caption)    

    bot.upload_photo(photo=photo, caption =caption)

    # rename and move post into another folder to archive
    shutil.move(photo + ".REMOVE_ME", 'posted')  

post_bot()
