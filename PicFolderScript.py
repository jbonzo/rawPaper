######### Imports and variable assignments ##########

import praw #reddit api wrapper which was bullshit to get on my laptop
import urllib #used for downloading things and putting them places
from PIL import Image #used for checking image specs
import shutil #used for moving between directories
import os #internal file use
import time #used to pull time of file

user_agent = "RedditWallpaper 1.0 by /u/jbonzo200"
r = praw.Reddit(user_agent=user_agent)
dicPic = {}
goodPics = []
cont = True
rawDirectoryList = ["C:/Users/Ricky/Pictures/redditWallpaper/rawPics/", 
						"D:/Users/Ricky/Pictures/redditWallpaper/rawPics"] 
goodDirectoryList = ["C:/Users/Ricky/Pictures/redditWallpaper/goodPics/", 
						"D:/Users/Ricky/Pictures/redditWallpaper/goodPics"]
rawDirectory = ""
goodDirectory = ""
subInput = ""

for path1, path2 in rawDirectoryList, goodDirectoryList:
	if os.path.exists(path1):
		rawDirectory = path1
	if os.path.exists(path2):
		goodDirectory = path2

limit = 15

######### Function Definitions ##########

def pullFrom__(submissions, sub):
	print sub
	counter = 0
	#get x submissions
	submissions = submissions
	#goes through each submission and adds the pictures to a dictionary
	for x in submissions:
	    urlString = str(x.url)
	    #if the url points to a jpg
	    if urlString[len(urlString)-3:] == "jpg":
	    	#add to dictionary
	    	dicPic[str(x.title[:10]).strip("\"")] = urlString
	#for every string link in the picList
	try:
		for title, link in dicPic.iteritems():
			#makes the string filename 
			rawFile = rawDirectory + title + ".jpg"
			if rawFile[len(goodDirectory):] not in os.listdir(goodDirectory):
				#downloads the link file and puts it in the drop zone
				urllib.urlretrieve(link, rawFile)
				image = Image.open(rawFile) #makes into image to be evaluated
				#if the image is good specs
				if image.size[0] >= 1000 and image.size[1] >= 700:
					#copy file over with shutil.copy(srcFile, destFile)
					shutil.copy(rawFile, goodDirectory) 
					goodPics.append(rawFile)
					counter += 1
		print counter
	except IOError, e:
		print rawFile[len(goodDirectory):]
		raise e
		

def runner():
	if "y" == str(raw_input("Do you want to clean the folder?")):
		cleaner()
	else:
		subInput = str(raw_input("What subreddit do you want?"))
		sub = r.get_subreddit(subInput)
		submissionType = {"day" : sub.get_top_from_day(limit=limit),
				"week" : sub.get_top_from_week(limit=limit),
				"hot" : sub.get_hot(limit=limit),
				"all" : sub.get_top_from_all(limit=limit)}
		if "y" == str(raw_input("Top from day?")):
			pullFrom__(submissionType["day"], subInput)
		if "y" == str(raw_input("Top from week?")):
			pullFrom__(submissionType["week"], subInput)
		if "y" == str(raw_input("Top from all?")):
			pullFrom__(submissionType["all"], subInput)
		if "y" == str(raw_input("From Hot?")):
			pullFrom__(submissionType["hot"], subInput)

def dateSorted(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))

def cleaner():
	#str = "".replace('\\', '/')
	#months = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5,
	#		  "Jun": 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10,
	#		  "Nov" : 11, "Dec" : 12}

	sortedPics = dateSorted(goodDirectory)
	counter = 0
	while (len(sortedPics) > 15):
		os.remove(goodDirectory + "/" + sortedPics[counter])
		sortedPics.remove(sortedPics[counter]) 
		counter = counter + 1


#for item in os.listdir(goodDirectory):
	#print item

runner()
#cleaner()









#remove file from src folder with os.remove(srcFile)
#use for loop at end that removes from goodPics list
#os.remove(rawFile)

"""
DEBUG:
	subreddit=pics, top from all takes forever
	subreddit= funny, from hot throws IOError: [Errno 22] invalid mode ('wb')
	dditWallpaper/rawPics/CNN\'s "ISI.jpg'
"""
"""
	Make it more entertaining
"""
"""
	Place proportional watermark on image that labels the source subreddit
	example:
		<bottomRight>
			"/r/woahdude"
		</bottomRight>

	Subtasks:
		Create cool dynamic graphic for watermark
		Place it proportionally on corner of image
		Use PIL/Pillow to place watermark on *.jpg
			Find font library

"""

"""
	Make two versions: stream and favorites. 
	Stream changes it constantly throughout the month long process
	Favorites are categorized pictures that are favorited throughout a stream
"""


"""
	have script talk to phone and update phone background 
"""



"""
	make the script go through a subreddit and find popular 
	pictures on random topics. Example: Kanye West, and it would find
	pictures of kanye as the wallpaper theme for the get_top_from_day
"""

"""
For the watermark in pick a corner for the best placement when i download each picture. 
So when each pciture is moved to ghe good directory it is displayed and prompts for the 
best corner so as not to cover important details of the picture
"""