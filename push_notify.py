import urequests
import ujson
import gc
import env


def push_notification(msg):

    req_url = 'https://api.pushover.net/1/messages.json'

    # req_data = ujson.dumps({'token': 'axjqcbzqqv84ru7nhpt1e98s1zadwu',
    #                         'user': 'uovw1ofwqjpw51v8j8wnsrh9h4io5z',
    #                         'message': msg})

    req_data = ujson.dumps({'token': env.credentials['pushover_token'],
                            'user': env.credentials['pushover_user'],
                            'message': msg})

    response = urequests.post(
        req_url, headers={'content-type': 'application/json'}, data=req_data).json()

    gc.collect()
