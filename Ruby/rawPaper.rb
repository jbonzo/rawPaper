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


$r
$home
$good_pics_path
$raw_pics_path
$home = ENV['HOME']
$good_pics_path = "#{$home}/Pictures/rawPaper/goodPics/"
$raw_pics_path = "#{$home}/Pictures/rawPaper/rawPics/"

def authorize
    #authorization
    $r = Redd.it(:script, "gBHKZ4Jy4dAE9w", "ZUUhbl7PeMtwPAyyuLDPQm6gK6I", "jbonzo200", "r110695y")
end




#puts submissions[0]


def set_up
    # remember scope for home if you change it
    system("mkdir #{$home}/Pictures/rawPaper/")
    system("mkdir #{$good_pics_path}")
    system("mkdir #{$raw_pics_path}")
    system("mkdir #{$home}/Pictures/rawPaper/ruby/")
end

def directory_exists?(path)
    File.exist?(path)
end

def get_submissions_from_sub
    print "Enter the subreddit you want: "
    sub = gets.chomp
    sub = $r.subreddit_from_name(sub)
    puts "/r/" + sub.display_name
    sub.get_top(limit:35, t:'all')
end

def get_pics(submissions)
    pics = Hash.new

    submissions.each do |submission|
        url = submission.url
        title = submission.title
        pics[title] = url if url[-3..-1] == "jpg" or url[-3..-1] == "png"
    end

    pics.each do |title, url|
        open("#{$home}/Pictures/rawPaper/ruby/" + title, "wb") do |file|
            file << open(url).read
        end
    end
end

def run
    authorize

    every_directory_exists = directory_exists?($good_pics_path) && directory_exists?($raw_pics_path) && directory_exists?("#{$home}/Pictures/rawPaper/ruby/")
    # as long as the directory doesnt exist -> setup
    set_up unless every_directory_exists

    submissions = get_submissions_from_sub

    get_pics submissions
end

run