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

