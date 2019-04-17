# coding = utf-8
import requests
import hashlib
import random
import json

"""
    功能: 接收参数，完成翻译api调用，返回翻译结果
    作者：XH
    日期：2019-4-3
"""


class TransApi:
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    appid = '20190416000288665'
    key = '1gdEzLb90gKV1Rnd_EV6'

    def __init__(self, keyword='hello world', to='zh', from_language='auto'):
        """

        :param keyword: 待翻译文本
        :param from_language: 来源语种，默认自动检测
        :param to: 翻译的目标语种
        """
        self._keyword = keyword
        self._from = from_language
        self._to = to
        self._salt = random.randint(0, 99999)

    def get_sign(self):
        """
        根据百度翻译api接口规范，必须传递一个叫sign的参数，
        此函数用来生成sign
        sign的构成规则为：appid+keyword+salt+密钥 的MD5值
        """

        sign = self.appid + self._keyword + str(self._salt) + self.key
        m5 = hashlib.md5()
        m5.update(sign.encode('utf-8'))
        sign_md5 = m5.hexdigest()


        return sign_md5

    def baidu_trans(self):

        # 发送get 请求 获得响应
        response = requests.get(
            url='https://fanyi-api.baidu.com/api/trans/vip/translate',
            headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'},
            params={
                'q':self._keyword,
                'from': self._from,
                'to': self._to,
                'appid': self.appid,
                'salt': self._salt,
                'sign': self.get_sign()
                    }
        )
        # 解析响应
        content = response.content.decode('utf-8')
        content_str = json.loads(content)
        try:
            return content_str['trans_result'][0]['dst']
        except:
            return 'error'