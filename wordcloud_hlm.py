from os import path
from wordcloud import WordCloud
import jieba
import re
#
# special_character_removal = re.compile(r'[，。、【 】“”：；（）《》‘’{}？！⑦%>℃.^-——=&#@￥『』]', re.IGNORECASE)
#
# #
# # text =""
# fw=open("hlm_seg.txt","w",encoding="utf-8")
# with open('hlm.txt',encoding="utf-8") as fp:
#     for line in fp:
#         l = special_character_removal.sub('', line.strip())
#         words=jieba.cut(l)
#
#         t=" ".join(words)
#         fw.write(t)
#         fw.write("\n")
# fw.close()


# import numpy as np
# from PIL import Image, ImageDraw, ImageFont
# background_image =  np.array(Image.open("background.png"))
d = path.dirname(__file__)
# Read the whole text.
text = open(path.join(d, 'hlm_seg.txt'),encoding="utf-8").read()
# Generate a word cloud image
# font=path.join(d, "simkai.ttf")
font='C:/Windows/Fonts/simkai.ttf'
wordcloud = WordCloud(font_path=font,#设置中文字体，不指定就会出现中文不显示
                      width=1024,#宽
                      height=840,#高
                      background_color='white',#设置背景色
                      # mask=background_image#背景
                      # max_words=100,#最大词汇数
                      # max_font_size=100#最大号字体
                      ).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt

# lower max_font_size
# wordcloud = WordCloud(max_font_size=40).generate(text)

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
