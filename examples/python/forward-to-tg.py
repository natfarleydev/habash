#!/usr/bin/env python3

"""A simple script to forward messages from Habitica to a telegram bot.

Several environment variables should be set:
HABITICA_TG_BOT_TOKEN # The bot token for telegram
HABITICA_TG_GROUP # The group ID for telegram
HABITICA_TOKEN # Your Habitica token
HABITICA_UUID # Your Habitica UUID

By default, the script outputs to 'lastpartychat.pkl' in order to know which
chats have already been sent to the chat. It is recommended to run the script first as

    ./forward-to-tg.py --print-only

So that you do not spam your chat with habitica messages on first run! After
this, the script will only post new messages (as long as it's run from the same
directory).

Improvements/pull requests to this script are welcome.

NOTE This is part of the habash project, even though it doesn't use habash. It
also requires the `requests` package. In the future, it may be moved out of the
habash project as it doesn't follow the 'works on a clean *nix system'
philosophy.

"""

import argparse
import json
import logging
import os
import pickle
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Forward Habitica chat to Telegram.')
    parser.add_argument('--print-only', action='store_true', default=False,
                        help='Only print the messages, do not send them to telegram.')
    parser.add_argument('--habitica-tg-bot-token', type=str,
                        default=os.environ['HABITICA_TG_BOT_TOKEN'],
                        help="Telegram bot token to forward the message with")
    parser.add_argument('--habitica-tg-group', type=str,
                        default=os.environ['HABITICA_TG_GROUP'])
    parser.add_argument('--habitica-token', type=str,
                        default=os.environ['HABITICA_TOKEN'],
                        help='Habitica API token')
    parser.add_argument('--habitica-uuid', type=str,
                        default=os.environ['HABITICA_UUID'],
                        help='Habitica UUID')

    return parser.parse_args()


def main(parsed):
    partychat = requests.get('https://habitica.com/api/v3/groups/party/chat',
                        headers={
                            'x-api-key': parsed.habitica_token,
                            'x-api-user': parsed.habitica_uuid,
                        }).json()['data']
    partychat.reverse()
    logger.debug('partychat response: '+ str(partychat))

    try:
        with open('lastpartychat.pkl', 'rb') as f:
            lastpartychat = pickle.load(f)
    except FileNotFoundError:
        lastpartychat = []
    logger.debug(str(lastpartychat))

    chats_to_send = [x for x in partychat if x not in lastpartychat]

    if not chats_to_send:
        print('No chats to send. Returning :)')
        return

    for chat in chats_to_send:
        data_to_send_to_telegram = {
                'chat_id': parsed.habitica_tg_group,
                'text': chat['text'],
                'parse_mode': 'Markdown'
            }

        if parsed.print_only:
            print(data_to_send_to_telegram)
        else:
            requests.post(f'https://api.telegram.org/bot{parsed.habitica_tg_bot_token}/sendMessage',
                          data=data_to_send_to_telegram)

    with open('lastpartychat.pkl', 'wb') as f:
        pickle.dump(partychat, f)

if __name__ == '__main__':
    parsed = parse_arguments()
    main(parsed)
