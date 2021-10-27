from instagram import Instagram
import constants as const
import GUI.GUI_Main as mainGUI

u_input = mainGUI.main()
username = u_input[0]
password = u_input[1]
hashtags = u_input[2].split('-')

with Instagram() as bot:
    bot.open_instagram()
    bot.login(username, password)
    bot.search_tags(hashtags)
