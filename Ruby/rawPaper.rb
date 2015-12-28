=begin
    The following looks at r/ruby and takes the 30 top links of all time and
    prints a list of the ones that are definetely pictures.
    TODO:
        After that I'll need to find a way to run applescripts off
        ruby.
        Also a nice interface
    DONE:
        I need to find a way to download and put them in a directory.
=end
require 'redd'
require 'open-uri'  # used to download images

#authorization
r = Redd.it(:script, "gBHKZ4Jy4dAE9w", "ZUUhbl7PeMtwPAyyuLDPQm6gK6I", "jbonzo200", "r110695y")
sub = r.subreddit_from_name("ruby")
puts "/r/" + sub.display_name
submissions = sub.get_top(limit:35, t:'all')
pics = Hash.new
home = ENV['HOME']

#puts submissions[0]

submissions.each do |submission|
    url = submission.url
    title = submission.title
    if url[url.length - 3...url.length] == "jpg" or url[url.length - 3...url.length] == "png"
        pics[title] = url
    end
end

pics.each do |title, url|
    open(home + "/Pictures/redditWallpaper/ruby/" + title, "wb") do |file|
        file << open(url).read
    end
end



