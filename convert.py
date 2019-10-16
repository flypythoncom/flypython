#!/usr/bin/env  python3

import requests
import os,json

from requests_toolbelt import MultipartEncoder

url = "http://localhost/unoconv/pdf"

def post_file(url,path):
    filename = os.path.basename(path)
    convert_name = str(filename).split('.')[0] + '.pdf'

    m = MultipartEncoder(
        fields= {
            'file':(filename,open(path,'rb')),
        }
    )
    response = requests.request('POST', url, data=m, headers={'Content-Type':m.content_type})

    with open(convert_name, 'wb') as f:
        f.write(response.content)

    return convert_name

path = "./demo.docx"

ret = post_file(url, path)
print(ret)

