import random
import time
import asyncio
from roblox import Client
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED + """____            _       _         _           __    ___    ____    ___   _   _   _____   __     _   _              _     _           _  _           __   _  __  _          _                       __ 
 |  _ \    ___   | |__   | |   ___   __  __   | _|  / _ \  / ___|  |_ _| | \ | | |_   _| |_ |      / \     _   _  | |_  | |__     ___    _ __    | _| | |/ / | |   ___  (_)  _ __ ___     ___   |_ |
 | |_) |  / _ \  | '_ \  | |  / _ \  \ \/ /   | |  | | | | \___ \   | |  |  \| |   | |    | |     / _ \   | | | | | __| | '_ \   / _ \  | '__|   | |  | ' /  | |  / _ \ | | | '_ ` _ \   / _ \   | |
 |  _ <  | (_) | | |_) | | | | (_) |  >  <    | |  | |_| |  ___) |  | |  | |\  |   | |    | |    / ___ \  | |_| | | |_  | | | | | (_) | | |      | |  | . \  | | |  __/ | | | | | | | | | (_) |  | |
 |_| \_\  \___/  |_.__/  |_|  \___/  /_/\_\   | |   \___/  |____/  |___| |_| \_|   |_|    | |   /_/   \_\  \__,_|  \__| |_| |_|  \___/  |_|      | |  |_|\_\ |_|  \___| |_| |_| |_| |_|  \___/   | |
                                              |__|                                       |__|                                                    |__|                                           |__|
""")
time.sleep(5)
print("""__        __         _                             _      
 \ \      / /   ___  | |   ___    ___    _ __ ___     ___  | |
  \ \ /\ / /   / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \ | |
   \ V  V /   |  __/ | | | (__  | (_) | | | | | | | |  __/ |_|
    \_/\_/     \___| |_|  \___|  \___/  |_| |_| |_|  \___| (_)
""")
cookiesave = input("youre cookie roblox > ")
while True:
    colorama.init()
    print(Fore.RED + "1.Grab user info 2.Grab place info 3.Grab group info 4.Search username id 5.Grab plugin info")
    answer = int(input("> "))
    client = Client(cookiesave)


    async def main():
        if answer == 1:
            #
            findiduser = int(input("userID > "))
            user = await client.get_user(findiduser)
            status = await user.get_status()

            print("ID:", user.id)
            print("Name:", user.name)
            print("Display Name:", user.display_name)
            print("Created:", user.created.strftime("%m/%d/%Y, %H:%M:%S"))
            print(f"Status: {status!r}")
            print(f"Description: {user.description!r}")
        if answer == 2:
            #
            findidplace = int(input("placeID > "))
            place = await client.get_place(findidplace)

            print("ID:", place.id)
            print("Name:", place.name)
            print(f"Description: {place.description!r}")
            print("Playable:", place.is_playable)
            if not place.is_playable:
                print("Reason:", place.reason_prohibited)
            if place.price > 0:
                print("Price:", place.price)
            print("Creator:", place.builder)
        if answer == 3:
            findIDgroup = int(input("groupID > "))
            group = await client.get_group(findIDgroup)

            print("ID:", group.id)
            print("Name:", group.name)
            print("Members:", group.member_count)
            print("Owner:", group.owner.display_name)
            if group.shout:
                print("Shout:")
                print("\tCreated:", group.shout.created.strftime("%m/%d/%Y, %H:%M:%S"))
                print("\tUpdated:", group.shout.updated.strftime("%m/%d/%Y, %H:%M:%S"))
                print(f"\tBody: {group.shout.body!r}")
                print(f"\tPoster:", group.shout.poster.display_name)
        if answer == 4:
            findID = input("Roblox username > ")
            users = client.user_search(findID, max_items=10)

            async for user in users:
                print("ID:", user.id)
                print("\tName:", user.name)
                print("\tDisplay Name:", user.display_name)
        if answer == 5:
            pluginInfo = int(input("PluginID > "))
            plugin = await client.get_plugin(pluginInfo)

            print("ID:", plugin.id)
            print("Name:", plugin.name)
            print(f"Description: {plugin.description!r}")
            print("Comments Enabled:", plugin.comments_enabled)
            print("Created:", plugin.created.strftime("%m/%d/%Y, %H:%M:%S"))
            print("Updated:", plugin.updated.strftime("%m/%d/%Y, %H:%M:%S"))



    asyncio.get_event_loop().run_until_complete(main())

