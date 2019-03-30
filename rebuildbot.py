import botconfig
import requests # last time using this...
import urllib.request

def run_bot():
    session = requests.Session()
    req = session.post(botconfig.cpanel_url, data=botconfig.login_data)
    bot_cookies = {
        'mod':urllib.request.unquote(session.cookies.get_dict()['mod']),
    }
    req = session.post(botconfig.cpanel_url + botconfig.bot_action,
        data=botconfig.rebuild_data, cookies=bot_cookies)
    print(req.status_code)

run_bot()
