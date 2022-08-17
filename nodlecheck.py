#!/usr/bin/python3

import requests
import json
import time
from datetime import datetime


# to edit

enable_telegram = 1
enable_console = 1

#enable one
show_all = 0
show_problem = 1

# subscan API - register on https://pro.subscan.io/login
subscan_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# send /start to @Nodle_Wallet_Checker on telegram
# get chat_id from https://api.telegram.org/bot5578491077:AAG4dWtmcdE2bCyCxULHP_xCRAgQraISMJE/getUpdates
# or create own - https://core.telegram.org/bots#6-botfather
telegram_chatid = '123456789'
#dont edit or create own
telegram_token = '5578491077:AAG4dWtmcdE2bCyCxULHP_xCRAgQraISMJE'

# time after which inform if you do not have an award (in hours)
alert_time = 12

# -------------------------- 

def get_transfers_data(wallet):
    url = "https://nodle.api.subscan.io/api/scan/transfers"
    headers = {'X-API-TOKEN': subscan_token}
    payload = {'row': 1, 'page': 0, 'address': wallet}

    res = requests.post(url, headers=headers, data=payload)
    res_obj = json.loads(res.text)
    #limit in subscan free plan 5req/s
    time.sleep(0.3)
    return res_obj

def get_last_trans(wallet):
    res_obj = get_transfers_data(wallet)
    if res_obj['data']['transfers']:
      lasttrans = res_obj['data']['transfers'][0]['block_timestamp']
    else:
      lasttrans = ''
    return lasttrans

def diff_time(lasttrans):
    now = datetime.now()
    timestamp = round(datetime.timestamp(now))
    td = timestamp - lasttrans
    td_mins = int(round(td / 60))
    return td_mins

def telegram_sendtext(message):
    send_text = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage?chat_id=' + telegram_chatid + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)
    return response.json()

  

wallet = problem_text = info = full_text = out_text = msg = ''
delimit = '--------------=============--------------\n'


with open(os.getcwd() + '/wallets.txt') as wallets:
    for wallet in wallets:
      wallet = wallet.strip().split(';')
      if type(get_last_trans(wallet[1])) == int:
        td_mins = diff_time(get_last_trans(wallet[1]))
        info = wallet[0] + " - last reward %02d:%02dh ago" % (divmod(td_mins, 60))
        if td_mins > alert_time*60:
         problem_text += info + "\n"
      else:
        info = wallet[0] + " - no data"
      full_text += info + "\n"


if show_all == 1:
  out_text = full_text
elseif show_problem == 1:
  out_text = problem_text
else:
  print('Check config')

if out_text:
  msg = delimit + out_text + delimit
  if enable_telegram == 1:
    telegram_sendtext(msg)
  if enable_console == 1:
    print(msg)
