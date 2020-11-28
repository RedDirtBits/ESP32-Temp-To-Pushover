import urequests
import ujson
import gc
import env


def push_notification(msg):
    """
     Function to connect to the Pushover API.

     msg: (str) Message to be sent
    """

    req_url = 'https://api.pushover.net/1/messages.json'

    req_data = ujson.dumps({'token': env.credentials['pushover_token'],
                            'user': env.credentials['pushover_user'],
                            'message': msg})

    response = urequests.post(
        req_url, headers={'content-type': 'application/json'}, data=req_data).json()

    gc.collect()
