from instagram import Instagram
import constants as const
import GUI.GUI_Main as mainGUI
from emailer import Email

######################################################################
#Main
######################################################################
u_input = mainGUI.main()
username = u_input[0]
password = u_input[1]
hashtags = u_input[2].split('-')
e_username = u_input[3]
e_password = u_input[4]


with Instagram() as bot:
    bot.open_instagram()
    bot.login(username, password)
    body = bot.search_tags(hashtags)
    emailUser = Email(body, e_username, e_password)
    emailUser.sendEmail()
