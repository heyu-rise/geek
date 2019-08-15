import time

import websocket
from gevent import thread


def on_message(ws, message):
    print('receive ' + message)


def on_open(ws):
    def ago():
        for i in range(5):
            time.sleep(1)
            msg = "{0}".format(i)
            ws.send(msg)
            print(msg)
        time.sleep(1)
        ws.close()
        print('close')

    thread.start_new_thread(ago(), ())


if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://echo.websocket.org/", on_message=on_message, on_open=on_open)
    ws.run_forever()
