from qcloud_image import Client
from aip import AipFace
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers

appid = '1256126892'
secret_id = 'AKIDIN2wpmXCDTzL32ao7T7bl0AdK7uqPYMa'
secret_key = 'qPHpTlPmIrD17YMUpTDYns0YX98dNrUs'
bucket = 'face-recognize'
tx_client = Client(appid, secret_id, secret_key, bucket)
tx_client.use_http()
tx_client.set_timeout(30)

APP_ID = '10365287'
API_KEY = 'G7q4m36Yic1vpFCl5t46yH5K'
SECRET_KEY = 'MneS2GDvPQ5QsGpVtSaHXGAlvwHu1XnC '
bd_client = AipFace(APP_ID, API_KEY, SECRET_KEY)
domain=alibaba-inc.com
