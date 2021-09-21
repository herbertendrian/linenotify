import requests

"""
Full documentation :
https://notify-bot.line.me/doc/en/
"""

__version__ = 'V1.0-190821'

class lineNotifyAPI:
    def __init__(self, notify_access_token):
        self.host = 'https://notify-api.line.me/api'
        self.token = notify_access_token
        self.session = requests.Session()
        self.session.headers.update(
            {
                'User-Agent': 'bert-line-notify/{}'.format(__version__)
            }
        )

    @staticmethod
    def _log(data):
        print(data)
    
    def _getContent(self, path, **kwargs):
        return self.session.get(path, **kwargs).json()
    
    def _postContent(self, path, **kwargs):
        result = self.session.post(path, **kwargs)
        self._log(result.headers)
        return result.json()

    def statusAccessToken(self):
        _headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        return self._getContent(self.host + '/status', headers=_headers)
    
    def revokeAccessToken(self):
        _headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer {}'.format(self.token)
        }
        return self._postContent(self.host + '/revoke', headers=_headers)
    
    def sendTextMessage(self, message: str, notification_disabled=False):
        _headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer {}'.format(self.token)
        }
        _data = {
            'message': message,
            'notificationDisabled': notification_disabled if notification_disabled else False
        }
        return self._postContent(self.host + '/notify', headers=_headers, data=_data)
    
    def sendImageMessage(self, message: str, image_file_path: str, notification_disabled=False):
        _headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        _data = {
            'message': message,
            'notificationDisabled': notification_disabled if notification_disabled else False
        }
        _files = {
            'imageFile': open(image_file_path, 'rb')
        }
        return self._postContent(self.host + '/notify', headers=_headers, data=_data, files=_files)
    
    def sendImageMessageWithURL(self, message: str, thumbnail_url: str, full_size_url: str, notification_disabled=False):
        _headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        _data = {
            'message': message,
            'imageThumbnail': thumbnail_url,
            'imageFullsize': full_size_url,
            'notificationDisabled': notification_disabled if notification_disabled else False
        }
        return self._postContent(self.host + '/notify', headers=_headers, data=_data)
    
    def sendStickerMessage(self, message: str, sticker_package_id: int, sticker_id: int, notification_disabled=False):
        """
        All available sticker package id : https://developers.line.biz/en/docs/messaging-api/sticker-list/#sticker-definitions
        """
        _headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer {}'.format(self.token)
        }
        _data = {
            'message': message,
            'stickerPackageId': int(sticker_package_id),
            'stickerId': int(sticker_id),
            'notificationDisabled': notification_disabled if notification_disabled else False
        }
        return self._postContent(self.host + '/notify', headers=_headers, data=_data)