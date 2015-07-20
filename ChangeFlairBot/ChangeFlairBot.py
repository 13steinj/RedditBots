"""
A bot to change the flair of all posts in a subreddit
Written by /u/SmBe19, small modification by /u/13steinj to use search pages
"""

import praw
import OAuth2Util

# ### USER CONFIGURATION ### #

# The bot's useragent. It should contain a short description of what it does and your username. e.g. "RSS Bot by /u/SmBe19"
USERAGENT = ""

# The name of the subreddit to operate on. The bot has to be a mod there.
SUBREDDIT = ""

# The old and new flair text and css class. Set to None to use a wildcard.
# Setting the flairs via search will only work if OLD_FLAIR_TEXT is not set to None.
OLD_FLAIR_TEXT = ""
OLD_FLAIR_CSS = ""
NEW_FLAIR_TEXT = ""
NEW_FLAIR_CSS = ""
# Set to True if you only want to see how many posts would be altered. No flairs will be altered with this set to True.
ONLY_TEST = True

# ### END USER CONFIGURATION ### #
try:
# A file containing infos for testing.
    import bot
    USERAGENT = bot.useragent
    SUBREDDIT = bot.subreddit
except ImportError:
    pass

def setting_variables():
    r = praw.Reddit(USERAGENT)
    o = OAuth2Util.OAuth2Util(r)
    sub = r.get_subreddit(SUBREDDIT)
    FLAIR_QUERY = "flair:'{0}'".format(OLD_FLAIR_TEXT)

def run_hot_flair_setting():
    print("Will now replace link flairs with a text of \"{0}\" and a class of \"{1}\" to have a text of \"{2}\" and a class of \"{3}\" via the \"Hot\" page".format(OLD_FLAIR_TEXT, OLD_FLAIR_CSS, NEW_FLAIR_TEXT, NEW_FLAIR_CSS)
    try:
        last_hot_element = None
        hot_posts = sub.get_hot(limit=100)
        found_new_hot_post = True
        hot_changed = 0
        active_hot_page = 0
        while found_new_hot_post:
            active_hot_page += 1
            print("Searching the", active_hot_page, "Hot Page")
            found_new_hot_post = False
            for post in hot_posts:
                found_new_hot_post = True
                if (post.link_flair_css_class == OLD_FLAIR_CSS or not OLD_FLAIR_CSS) and (post.link_flair_text == OLD_FLAIR_TEXT or not OLD_FLAIR_TEXT):
                    if ONLY_TEST:
                        print ("Flair would be changed")
                        hot_changed += 1
                    else:
                        print("Changing flair")
                        post.set_flair(NEW_FLAIR_TEXT, NEW_FLAIR_CSS)
                        hot_changed += 1
                last_hot_element = post.name
            hot_posts = sub.get_hot(limit=100, params={"after" : last_element})
        if ONLY_TEST:
            print(hot_changed, "posts would have been changed via the \"Hot\" queue")
        else:
            print("Changed", hot_changed, "posts via the \"Hot\" queue")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("Exception", e)
# new procedure
def run_new_flair_setting():        
    print("Will now replace link flairs with a text of \"{0}\" and a class of \"{1}\" to have a text of \"{2}\" and a class of \"{3}\" via the \"New\" page".format(OLD_FLAIR_TEXT, OLD_FLAIR_CSS, NEW_FLAIR_TEXT, NEW_FLAIR_CSS)
    try:
        last_new_element = None
        new_posts = sub.get_new(limit=100)
        found_new_new_post = True
        new_changed = 0
        active_new_page = 0
        while found_new_new_post:
            active_new_page += 1
            print("Searching the", active_new_page, "New Page")
            found_new_new_post = False
            for post in new_posts:
                found_new_new_post = True
                if (post.link_flair_css_class == OLD_FLAIR_CSS or not OLD_FLAIR_CSS) and (post.link_flair_text == OLD_FLAIR_TEXT or not OLD_FLAIR_TEXT):
                    if ONLY_TEST:
                        print ("Flair would be changed")
                        new_changed += 1
                    else:
                        print("Changing flair")
                        post.set_flair(NEW_FLAIR_TEXT, NEW_FLAIR_CSS)
                        new_changed += 1
                last_new_element = post.name
            new_posts = sub.get_new(limit=100, params={"after" : last_element})
        if ONLY_TEST:
            print(new_changed, "posts would have been changed via the \"New\" queue")
        else:
            print("Changed", new_changed, "posts via the \"New\" queue")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("Exception", e)
# rising procedure
def run_rising_flair_setting():        
    print("Will now replace link flairs with a text of \"{0}\" and a class of \"{1}\" to have a text of \"{2}\" and a class of \"{3}\" via the \"Rising\" page".format(OLD_FLAIR_TEXT, OLD_FLAIR_CSS, NEW_FLAIR_TEXT, NEW_FLAIR_CSS)
    try:
        last_rising_element = None
        rising_posts = sub.get_rising(limit=100)
        found_new_rising_post = True
        rising_changed = 0
        active_rising_page = 0
        while found_new_rising_post:
            active_rising_page += 1
            print("Searching the", active_rising_page, "New Page")
            found_new_rising_post = False
            for post in new_posts:
                found_new_rising_post = True
                if (post.link_flair_css_class == OLD_FLAIR_CSS or not OLD_FLAIR_CSS) and (post.link_flair_text == OLD_FLAIR_TEXT or not OLD_FLAIR_TEXT):
                    if ONLY_TEST:
                        print ("Flair would be changed")
                        rising_changed += 1
                    else:
                        print("Changing flair")
                        post.set_flair(NEW_FLAIR_TEXT, NEW_FLAIR_CSS)
                        rising_changed += 1
                last_new_element = post.name
            new_posts = sub.get_rising(limit=100, params={"after" : last_element})
        if ONLY_TEST:
            print(rising_changed, "posts would have been changed via the \"Rising\" queue")
        else:
            print("Changed", rising_changed, "posts via the \"Rising\" queue")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("Exception", e)
#
# EXECUTION GROUPING
#
def run_full_script():
    setting_variables()
    o.refresh()
    print("Starting link flair bot for /r/{0}".format(SUBREDDIT))
    run_hot_flair_setting()
# FULL EXECUTION
if __name__ == "__main__":
    if not USERAGENT:
        print("Missing Useragent")
    elif not SUBREDDIT:
        print("Missing Subreddit")
    elif not OLD_FLAIR_CSS and not OLD_FLAIR_TEXT:
        print("Old flair not set")
    else:
        run_full_script()
			