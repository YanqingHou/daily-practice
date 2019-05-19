# coding = utf-8
from requests_html import HTMLSession
import base64
import json
"""
    作者：TimsXH
    功能:传入验证码图片URL，调用API接口进行验证码识别，返回识别后的字符串
    日期:2019-5-19
    version:0.1
"""


class Captcha_Recognition:

    def __init__(self):
        self.session = HTMLSession()

    def _download_captcha(self, url: str):
        """
        下载验证码
        :return:返回base64字符串
        """
        jpg = self.session.get(url=url)  # 发起请求获得图片数据
        b64_jpg = base64.b64encode(jpg.content)  # base64加密
        return b64_jpg

    def _recognize(self, b64_jpg):
        """
        调用API接口,返回识别后的字符串
        :return:
        """
        b64_jpg = b'data:image/jpg;base64,' + b64_jpg  # 根据API接口要求构建base64数据
        url = 'http://apigateway.jianjiaoshuju.com/api/v_1/yzm.html'  # API接口URL
        headers = {
            'appCode': '********************************',    # 根据API文档传入的请求头数据
            'appkey': '*******************************',
            'appSecret': '**************************'
        }
        data = {
            'v_pic': b'data:image/jpg;base64,' + b64_jpg,  # 图片数据
            'v_type': 'e4'                                  # 图片类型，4位英文字符
        }
        r = self.session.post(url=url,headers=headers,data=data)  # 发起请求获取json格式的响应
        content = json.loads(r.content)   # 使用json模块将字符串变为可以用字典方式操作的json
        print(content['v_code'])
        return content['v_code']


    def parse(self,url):
        b64_jpg = self._download_captcha(url)
        result = self._recognize(b64_jpg)
        return result

