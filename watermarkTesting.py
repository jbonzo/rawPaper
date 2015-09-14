########## Watermark testing ##########
from PIL import Image, ImageDraw, ImageFont
import os

fontDirectory = "C:\Windows\Fonts/".replace("\\","/")

#list of fonts I like
fonts = ["BRADHITC.ttf", "CALIFR.ttf", "GOTHIC.ttf", "ChaparralPro-LightIt.ttf",
		 "ITCEDSCR.ttf", "simfang.ttf", "IMPRISHA.ttf", "INFROMAN.ttf",
		  ""]
filepaths = ["C:/Users/Ricky/Pictures/redditWallpaper/goodPics/", "D:/Users/Ricky/Pictures/redditWallpaper/goodPics/"
			,"D:/Users/Ricky/Downloads/" ]
filepath = ""
for item in filepaths:
	if os.path.exists(item):
		filepath = item
		break

pictures = ['Never disc.jpg', 'partypat.jpg', 'Undergroun.jpg']
picture = ""
# for item in pictures:
# 	if os.path.exists(filepath + picture):
# 		picture = item
# 		print picture

image = Image.open(filepath + pictures[2]).convert('RGBA')
imageWidth = image.size[0]
imageHeight = image.size[1]
#same size as image
emptyBase = Image.new('RGBA', image.size, (255,255,255,0))

def watermarkTest(subreddit):

	textBase = emptyBase
	# make a blank image for the text, initialized to transparent text color
	width = image.size[0]
	height = image.size[1]

	# get a font
	fnt = ImageFont.truetype(fontDirectory + "BRADHITC.ttf", size=200)
	fntHeight = fnt.getsize(subreddit)[1]
	# creates an object that will be drawn onto textBase
	draw = ImageDraw.Draw(textBase)

	# draw text, half opacity
	#print "image width:", imageWidth, "image height:", imageHeight
	#print "1/6 width", 1 * imageWidth / 6, "1/6 height", 1 * imageHeight / 6
	draw.text((width / 48, 47 * height / 48	- fntHeight), subreddit, font=fnt, fill=(255, 255, 255,255))

	# draw text, full opacity
	#print "the font width is:", draw.textsize(subreddit, font=fnt)[0]
	#d.show()
	textDimensions = draw.textsize(subreddit, font=fnt)
	out = Image.alpha_composite(image, textBase)
	#outWithLines = Image.alpha_composite(out, textPlacementTest(emptyBase, textDimensions))
	
	out.save(filepath + "test.jpg")
	#out.show()


def textPlacementTest(imageLines, textDimensions):
	draw = ImageDraw.Draw(imageLines)
	for y in range(0, imageHeight, imageHeight / 12):
		xY = ((0, y), (imageWidth, y))
		draw.line(xY, fill=(0, 0, 255, 255), width=1)
	xY = (imageWidth / 12, imageHeight / 12 , textDimensions[0], textDimensions[1])
	#draw.rectangle(xY, fill=None, outline=(255,0,0,255))
	return imageLines

def font():

	image = Image.new("RGBA", (100,100), (255, 255, 255))

	draw = ImageDraw.Draw(image)

	# use a bitmap font
	font = ImageFont.load_default()

	draw.text((10, 10), "hello", font=font)

	# use a truetype font
	font = ImageFont.truetype("arial.ttf", 15)

	draw.text((10, 25), "world", font=font)

watermarkTest("/r/woahdude")
#textPlacementTest()