
# coding: utf-8

# In[5]:


import itchat
import os

import shutil
import PIL.Image as Image
from os import listdir
import math

itchat.auto_login()

friends = itchat.get_friends(update=True)[0:]

user = friends[0]["NickName"]

print(user)
#修改文件架权限
#os.chmod(user，stat.S_IRWXO)

if os.path.exists(user):
    #删除原有目录
    shutil.rmtree(user)
    # 建立新目录
    os.mkdir(user)
    #os.rmdir(user)
else:
    #新建user目录
    os.mkdir(user)

num = 0

for i in friends:
	img = itchat.get_head_img(userName=i["UserName"])
	fileImage = open(user + "/" + str(num) + ".jpg",'wb')
	fileImage.write(img)
	fileImage.close()
	num += 1

pics = listdir(user)

numPic = len(pics)

print(numPic)

eachsize = int(math.sqrt(float(2560 * 2560) / numPic))

print(eachsize)

numline = int(2560 / eachsize)

toImage = Image.new('RGB', (2560, 2560))


print(numline)

x = 0
y = 0

for i in pics:
	try:
		#打开图片
		img = Image.open(user + "/" + i)
	except IOError:
		print("Error: 没有找到文件或读取文件失败")
	else:
		#缩小图片
		img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
		#拼接图片
		toImage.paste(img, (x * eachsize, y * eachsize))
		x += 1
		if x == numline:
			x = 0
			y += 1


toImage.save(user + ".jpg")

itchat.send_image(user + ".jpg", 'filehelper')


itchat.logout()