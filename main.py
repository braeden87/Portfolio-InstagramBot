from instagram import Instagram
import constants as const


with Instagram() as bot:
    bot.open_instagram()
    bot.login(const.USERNAME_B, const.PASSWORD_B)
    bot.search_tags('movie')
    bot.open_posts(5)