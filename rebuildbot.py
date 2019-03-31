import botconfig
import requests # last time using this...
import urllib.request
import traceback

def run_bot():
    try:
        session = requests.Session()
        req = session.post(botconfig.cpanel_url, data=botconfig.login_data)
        bot_cookies = {
            'mod':urllib.request.unquote(session.cookies.get_dict()['mod']),
        }
        req = session.post(botconfig.cpanel_url + botconfig.bot_action,
            data=botconfig.rebuild_data, cookies=bot_cookies)
        print(req.status_code)
    except Exception as err:
        with open("err_log.txt", "a+") as log:
            print(str(traceback.format_exc()))
            log.write(str(traceback.format_exc()) + "\n\n")
            log.close
