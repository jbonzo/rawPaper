=begin
    The following looks at r/ruby and takes the 30 top links of all time and
    prints a list of the ones that are definetely pictures.
    I need to find a way to download and put them in a directory.
    After that I'll need to find a way to run applescripts off
    ruby.
    Also a nice interface
=end
require 'redd'

#authorization
r = Redd.it(:script, "gBHKZ4Jy4dAE9w", "ZUUhbl7PeMtwPAyyuLDPQm6gK6I", "jbonzo200", "r110695y")
sub = r.subreddit_from_name("ruby")
puts "/r/" + sub.display_name
submissions = sub.get_top(limit:35, t:'all')
picUrls = Array.new

submissions.each do |submission|
    url = submission.url
    if url[url.length - 3...url.length] == "jpg" or url[url.length - 3...url.length] == "png"
        picUrls << url
    end
end

puts picUrls

