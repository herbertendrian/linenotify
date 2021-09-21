from linenotify import lineNotifyAPI

notify = lineNotifyAPI('NOTIFY_ACCESS_TOKEN')

# Send Text Message
api = notify.sendTextMessage('Hello World')
# sendTextMessage('Hello World', True) True if you don't want to receive notifications (default: False)
# print(api) -> {'status': 200, 'message': 'ok'}

# Send Image Message
api = notify.sendImageMessage('Cute cat image', 'cuteCat.jpg')
# sendTextMessage('Cute cat image', 'cuteCat.jpg', True) True if you don't want to receive notifications (default: False)
# print(api) -> {'status': 200, 'message': 'ok'}

# Send Image Message with URL
api = notify.sendImageMessageWithURL('Cute cat image', 'https://i.postimg.cc/J4yMmNYR/cuteCat.jpg', 'https://i.postimg.cc/J4yMmNYR/cuteCat.jpg')
# sendImageMessageWithURL('Cute cat image', 'https://i.postimg.cc/J4yMmNYR/cuteCat.jpg', 'https://i.postimg.cc/J4yMmNYR/cuteCat.jpg', True) True if you don't want to receive notifications (default: False)
# print(api) -> {'status': 200, 'message': 'ok'}

# Send Sticker Message
api = notify.sendStickerMessage('Hello world', 1, 1)
# sendStickerMessage('Hello world', 1, 1, True) True if you don't want to receive notifications (default: False)
# print(api) -> {'status': 200, 'message': 'ok'}