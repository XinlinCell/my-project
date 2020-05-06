import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
from_data={
    'i': '我和你都是',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15887314437139',
    'sign': '7bfc9833562d108c53c168d5124f62a4',
    'ts': '1588731443713',
    'bv': 'b016bfc8dd420bcfc5d5a95c5a1600f4',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}

response=requests.post(url,from_data)
print(response)
