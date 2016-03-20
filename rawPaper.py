# -------- Imports and variable assignments --------- #


import os  # internal file use and system calls

try:
    import praw  # reddit api wrapper. Without python it's just raw
except ImportError, e:
    print "PRAW is not installed\nInstalling PRAW..."
    os.system("sudo pip install praw")
    import praw
try:
    from PIL import Image, ImageDraw, ImageFont  # used for checking image specs and for sub tagging
except ImportError, e:
    print "pillow is not installed\nInstalling pillow..."
    os.system("sudo pip install pillow")
    from PIL import Image, ImageDraw, ImageFont
import urllib  # used for downloading things and putting them places
import shutil  # used for moving between directories
import time  # used to pull time of file
from random import randint  # used to get a random font
from traceback import print_exception  # debugging
import platform  # to check what os we are on
from subprocess import Popen, PIPE, call  # used to run applescript



user_agent = "rawPaper 0.0.7 by /u/jbonzo200"
r = praw.Reddit(user_agent=user_agent)
dicPic = {}
goodPics = []
isWindows = platform.system() == "Windows"
userPath = "C:/Users/%USERNAME%/" if isWindows else "~"
userPath = os.path.expanduser(userPath)
workingDirectory = os.getcwd()
rawDirectoryList = [
    "C:/Users/%USERNAME%/Pictures/redditWallpaper/rawPics/",
    "~/Pictures/redditWallpaper/rawPics/"
]
goodDirectoryList = [
    "C:/Users/%USERNAME%/Pictures/redditWallpaper/goodPics/",
    "~/Pictures/redditWallpaper/goodPics/"
]
rawDirectory = ""
goodDirectory = ""


# pick the right directory
# for path in rawDirectoryList:
# 	if os.path.exists(os.path.expanduser(path)):
# 		rawDirectory = os.path.expanduser(path)
# for path in goodDirectoryList:
# 	if os.path.exists(os.path.expanduser(path)):
# 		goodDirectory = os.path.expanduser(path)

rawDirectory = rawDirectoryList[0] if isWindows else rawDirectoryList[1]
rawDirectory = os.path.expanduser(rawDirectory)
goodDirectory = goodDirectoryList[0] if isWindows else goodDirectoryList[1]
goodDirectory = os.path.expanduser(goodDirectory)

limit = 20


# --------- Class Definitions --------- #

class Subreddit():
    def __init__(self):
        self.sub = ""

    def set(self, sub_input):
        self.sub = sub_input

    def get(self):
        return self.sub


# --------- Function Definitions --------- #

def pull_from_leader(from_):
    if from_:
        from_ = from_.get().lower()

    app = get_app()

    sub = r.get_subreddit(app.sub)

    submission_type = {
        "day": sub.get_top_from_day(limit=limit),
        "week": sub.get_top_from_week(limit=limit),
        "hot": sub.get_hot(limit=limit),
        "all": sub.get_top_from_all(limit=limit),
    }

    print from_, app.sub
    if from_ in submission_type.keys():
        print "ok"
        pullFrom__(submission_type[from_], app.sub)


def pullFrom__(submissions, sub_input):
    counter = 0
    # get x submissions
    submissions = submissions
    # goes through each submission and adds the pictures to a dictionary
    for x in submissions:
        urlString = str(x.url)
        # if the url points to a jpg
        if urlString[len(urlString) - 3:] == "jpg":
            # add to dictionary
            try:
                dicPic[str(x.title[:10]).replace("\"", "")] = urlString
            except UnicodeEncodeError, e:
                dicPic["Unknown Title"] = urlString
    # for every string link in the picList
    for title, link in dicPic.iteritems():
        try:
            # makes the string filename
            title = title.replace("\\", "")
            title = title.replace("/", "")
            rawFile = rawDirectory + title + ".jpg"
            if rawFile[len(goodDirectory) - 1:] not in os.listdir(goodDirectory):
                # downloads the link file and puts it in the drop zone
                urllib.urlretrieve(link, rawFile)
                image = Image.open(rawFile)  # makes into image to be evaluated
                # if the image is good specs
                if image.size[0] >= 1000 and image.size[1] >= 700:
                    shutil.copy(rawFile, goodDirectory)
                    # image.show()
                    # corner = int(raw_input("Do you want the tag in the top left corner?(0)\nOr the bottom left corner?(1)\n"))
                    placeTag(sub_input, rawFile, 0)
                    # collects a list of added pictures for debugging
                    goodPics.append(rawFile)
                    counter += 1
        except IOError, e:
            print rawFile[len(goodDirectory) - 1:]
            print_exception(IOError, e, None)
            # raise e
    pulledPhrase = "picture pulled" if counter == 1 else "pictures pulled"
    print "\t", counter, pulledPhrase


# parameter corner is the corner that the tag
# will be placed on. Either top left (0) or
# bottom left (1)


def placeTag(subreddit, imageFile, corner):
    fontDirectory = "C:/Windows/Fonts/" if isWindows else "/Library/Fonts/"

    # list of fonts I like
    windowsFonts = [
        "BRADHITC.ttf",
        "CALIFR.ttf",
        "GOTHIC.ttf",
        "ChaparralPro-LightIt.ttf",
        "ITCEDSCR.ttf",
        "simfang.ttf",
        "IMPRISHA.ttf",
        "INFROMAN.tt"
    ]
    macFonts = ["Bradley Hand Bold.ttf", "Apple Chancery.ttf"]
    # get random font from fonts list
    # but before I do this I need to fix the size difference between each font
    # font = fonts[randint(0, len(fonts) - 1)]
    font = windowsFonts[0] if isWindows else macFonts[randint(0, len(macFonts) - 1)]
    # for possFont in fonts:
    # 	#print fontDirectory + possFont
    # 	#print os.path.exists(fontDirectory + font)
    # 	if os.path.exists(fontDirectory + font):
    # 		font = possFont
    # 		#print font
    # 		break
    # font = fonts[2]

    # setting up image and its attributes
    image = Image.open(imageFile).convert('RGBA')
    imageWidth = image.size[0]
    imageHeight = image.size[1]
    textBase = Image.new('RGBA', image.size, (255, 255, 255, 0))

    # text base for the tag
    Image.new('RGBA', image.size, (255, 255, 255, 0))

    # make the font and the draw object
    try:
        fnt = ImageFont.truetype(fontDirectory + font, size=200)
    except IOError, e:
        print e
    fnt = ImageFont.truetype(fontDirectory + font, size=200)
    fntHeight = fnt.getsize(subreddit)[1]
    cornerPlacement = [(imageWidth / 48, -1), (imageWidth / 48, 47 * imageHeight / 48 - fntHeight)]
    draw = ImageDraw.Draw(textBase)

    draw.text(cornerPlacement[corner], "/r/" + subreddit, font=fnt, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(image, textBase)
    out.save(goodDirectory + imageFile[len(goodDirectory) - 1:])


def dateSorted(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))


def cleaner():
    sortedPics = dateSorted(goodDirectory)
    counter = 0
    while (len(sortedPics) > 15):
        os.remove(goodDirectory + "/" + sortedPics[counter])
        sortedPics.remove(sortedPics[counter])
        counter = counter + 1


def setUp():
    os.system("mkdir " + goodDirectory[:len(goodDirectory) - len("goodPics/")])
    os.system("mkdir " + goodDirectory)
    os.system("mkdir " + rawDirectory)
    if isWindows:
        pass
    else:
        call(["osascript", workingDirectory + "/SystemPref.scpt"])


# --------- Runner --------- #


def runner():
    clear = "cls" if isWindows else "clear"
    clearScreen = lambda: os.system(clear)
    clearScreen()
    if not os.path.exists(goodDirectory):
        setUp()
    if "y" == str(raw_input("Do you want to clean the folder?(y/n)")):
        cleaner()
    pulling = True
    while pulling:
        subInput = str(raw_input("What subreddit do you want?(don't include /r/)"))
        sub = r.get_subreddit(subInput)
        submissionType = {
            "day": sub.get_top_from_day(limit=limit),
            "week": sub.get_top_from_week(limit=limit),
            "hot": sub.get_hot(limit=limit),
            "all": sub.get_top_from_all(limit=limit)
        }
        if "y" == str(raw_input("Top from day?(y/n)")):
            pullFrom__(submissionType["day"], subInput)
        if "y" == str(raw_input("Top from week?(y/n)")):
            pullFrom__(submissionType["week"], subInput)
        if "y" == str(raw_input("Top from all?(y/n)")):
            pullFrom__(submissionType["all"], subInput)
        if "y" == str(raw_input("From Hot?(y/n)")):
            pullFrom__(submissionType["hot"], subInput)
        if not "y" == str(raw_input("Do you want to pull from another subreddit?(y/n)")):
            pulling = False


# runner()

from gui import *

"""
DEBUG:
    subreddit=pics, top from all takes forever
    subreddit= funny, from hot throws IOError: [Errno 22] invalid mode ('wb')
    dditWallpaper/rawPics/CNN\'s "ISI.jpg'
"""

"""
TODO:
Make little algorithim to adjust size depending on font
Possible solutions: use .getsize(text) to find the width and always make the tag
a certain width in proportion to the width of the picture
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
    So when each picture is moved to ghe good directory it is displayed and prompts for the
    best corner so as not to cover important details of the picture

    I've played with this idea but it seems to be a bit annoying. For now I'll keep it on the top left corner untill
    I find a problem with this
"""

"""
    One thing I've noticed is that all my processing and downloading is taking place in one move
    For a more fluid run I should first download every into the rawDirectory and then transfer
    the good pictures into the goodDirectory and then once every picture is in I add the tag
    all at the end with some kind of exit status

    It would be cool to figure out how to download and tag at the same time

    lol found it: http://stackoverflow.com/questions/18864859/python-executing-multiple-functions-simultaneously
"""

"""
    make a script so that it changes the settings for mac to have the screensaver and/or desktop
"""

"""
    Add user artists tag
"""
