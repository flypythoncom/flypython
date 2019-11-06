#!/usr/bin/env python3

import fitz  #pip install pymupdf
import re
import os


def find_imag(path,img_path):

    checkXO = r"/Type(?= */XObject)"
    checkIM = r"/Subtype(?= */Image)"

    pdf = fitz.open(path)

    img_count = 0
    len_XREF = pdf._getXrefLength()

    print("文件名:{}, 页数: {}, 对象: {}".format(path, len(pdf), len_XREF - 1))

    for i in range(1, len_XREF):
        text = pdf._getXrefString(i)
        isXObject = re.search(checkXO, text)

        # 使用正则表达式查看是否是图片
        isImage = re.search(checkIM, text)

        # 如果不是对象也不是图片，则continue
        if not isXObject or not isImage:
            continue
        img_count += 1
        # 根据索引生成图像
        pix = fitz.Pixmap(pdf, i)
  
        new_name = path.replace('\\', '_') + "_img{}.png".format(img_count)
        new_name = new_name.replace(':', '')

        # 如果pix.n<5,可以直接存为PNG
        if pix.n < 5:
            pix.writePNG(os.path.join(img_path, new_name))
     
        else:
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.writePNG(os.path.join(img_path, new_name))
            pix0 = None
       
        pix = None
     
        print("提取了{}张图片".format(img_count))


if __name__=='__main__':
    pdf_path = r'test.pdf'
    img_path = r'img'
    m = find_imag(pdf_path, img_path)
