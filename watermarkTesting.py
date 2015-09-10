########## Watermark testing ##########
from PIL import Image, ImageDraw, ImageFont
import os

fontDirectory = "C:\Windows\Fonts/".replace("\\","/")


def watermarkTest():
	filepaths = ["C:/Users/Ricky/Pictures/redditWallpaper/goodPics/", "D:/Users/Ricky/Downloads/" ]
	filepath = ""
	for item in filepaths:
		if os.path.exists(item):
			filepath = item

	pictures = ['Never disc.jpg', 'partypat.jpg']
	picture = ""
	# for item in pictures:
	# 	if os.path.exists(filepath + picture):
	# 		picture = item
	# 		print picture

	print filepath + picture
	base = Image.open(filepath + pictures[1]).convert('RGBA')

	# make a blank image for the text, initialized to transparent text color
	txt = Image.new('RGBA', base.size, (255,255,255,0))
	width = txt.size[0]
	height = txt.size[1]

	# get a font
	fnt = ImageFont.truetype(fontDirectory + "trebucit.ttf", 100)
	#print fnt.getSize("Hello World")
	# get a drawing context
	d = ImageDraw.Draw(txt)

	# draw text, half opacity
	d.text((5 * width / 6, 5 * height / 6), "Hello World", font=fnt, fill=(0,0,255,128))
	# draw text, full opacity
	d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

	out = Image.alpha_composite(base, txt)
	print out
	out.show()

def font():

	image = Image.new("RGBA", (100,100), (255, 255, 255))

	draw = ImageDraw.Draw(image)

	# use a bitmap font
	font = ImageFont.load_default()

	draw.text((10, 10), "hello", font=font)

	# use a truetype font
	font = ImageFont.truetype("arial.ttf", 15)

	draw.text((10, 25), "world", font=font)

watermarkTest()