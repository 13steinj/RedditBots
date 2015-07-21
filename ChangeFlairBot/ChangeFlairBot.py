"""
A bot to change the flair of all posts in a subreddit
Written by /u/SmBe19
Modified by /u/13steinj to be an all in one script and search for flairs with a better method
"""

import sys, os, time, platform
import pip

if (sys.version_info < (3, 0, 0)):
    if (sys.version_info < (2, 6, 0)):
        try:
            print "You are using Python ", platform.python_version()
            print "This version is incompatible with the script."
            print "You must use Python 3.0.0 or higher.\nPython 3.4.3 is recommended."
            print "The script shall now close."
            sys.exit()
        except SyntaxError:
            pass
    else:
        print("You are using Python ", platform.python_version())
        print("This version is incompatible with the script.")
        print("You must use Python 3.0.0 or higher.\nPython 3.4.3 is recommended.")
        print("The script shall now close.")
        sys.exit()
elif (sys.version_info >= (3, 0, 0)):
    print("You are using Python ", platform.python_version())
    print("This version is compatible with the script.")
    if (sys.version_info < (3, 4, 3)):
        print("Python 3.4.3 or higher is recommended.")
        print("If you would like exit the script now to change the python version you are using, do so now.\nOtherwise please wait 2 seconds.")
        time.sleep(2)
    else:
        pass
    print("The script shall now start.")

# MOVE TO SCRIPT DIRECTORY AND CREATE / APPEND TO LOGFILE

os.chdir(os.path.dirname(os.path.realpath(__file__)))


print("Logging started. You will be able to view an indepth log either when the script finishes,\nor when you choose to later on by opening either the \"ChangeFlairBot.log\" or \"ChangeFlairBot.log.md\" files.")

def PrintLog(Statement):
    print(Statement)
    StatementLog = Statement + "\n"
    LogFile.write(StatementLog)
    MdLogFile.write(StatementLog)

LogFile = open("ChangeFlairBot.log", "r")
MdLogFile = open("ChangeFlairBot.log.md", "r")

# ### PRELIMINARY PREREQUISITE PACKAGE CHECK, INSTALLATION, AND UPGRADE ### #

packages = sorted(["%s" % (i.key) for i in pip.get_installed_distributions()])
package_versions = sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])

if ((("PRAW has been installed." not in LogFile.read()) or ("PRAW has been installed." not in MdLogFile.read())) or (("PRAW has had an attempt to have been updated." not in LogFile.read()) or ("PRAW has had an attempt to have been updated." not in MdLogFile.read()))):
    LogFile.close()
    MdLogFile.close()
    LogFile = open("ChangeFlairBot.log", "a")
    MdLogFile = open("ChangeFlairBot.log.md", "a")
    print("Checking if prerequisite packages are installed...")
    LogFile.write("Checking if prerequisite packages are installed...\n")
    MdLogFile.write("Checking if prerequisite packages are installed...\n")
    if ('praw' not in packages):
        print("You do not have the necessarry prerequisite PRAW. Will install in two seconds.")
        LogFile.write("You do not have the necessarry prerequisite PRAW. Will install in two seconds.\n")
        MdLogFile.write("You do not have the necessarry prerequisite PRAW. Will install in two seconds.\n")
        time.sleep(2)
        pip.main(['install', 'praw'])
        print("PRAW has been installed.")
        LogFile.write("PRAW has been installed.\n")
        MdLogFile.write("PRAW has been installed.\n")
    else:
        print("You have the necessarry prerequisite PRAW.")
        print("However, it may not be the latest version. An update will be attempted in two seconds.")
        print("If you recieve an output that the requirement is already up-to-date,\nignore it and let the script continue as normal.")
        LogFile.write("You have the necessarry prerequisite PRAW.")
        MdLogFile.write("You have the necessarry prerequisite PRAW.")
        time.sleep(2)
        pip.main(['install', 'praw', '--upgrade'])
        print("PRAW has had an attempt to have been updated.")
        LogFile.write("PRAW has had an attempt to have been updated.\n")
        MdLogFile.write("PRAW has had an attempt to have been updated.\n")
    if ('praw-oauth2util' not in packages):
        print("You do not have the necessarry prerequisite PRAW-Oauth2Util. Will install in two seconds")
        time.sleep(2)
        pip.main(['install', 'praw-oauth2util'])
    else:
        print("You have the necessarry prerequisite PRAW.")
        print("However, it may not be the latest version. An update will be attempted in two seconds.")
        print("If you recieve an output that the requirement is already up-to-date,\nignore it and let the script continue as normal.")
        time.sleep(2)
        pip.main(['install', 'praw-oauth2util', '--upgrade'])
else:
    print("Checking if prerequisite packages are installed...")
    print("All prerequisite packages have been installed previously!")

# IMPORT INSTALLED / UPDATED PACKAGES

import praw, OAuth2Util

# ### USER CONFIGURATION ### #

# The old and new flair text and css class. Set to None to use a wildcard.
# Setting the flairs via search will only work if OLD_FLAIR_TEXT is not set to None.
OLD_FLAIR_CSS = ""
NEW_FLAIR_TEXT = ""
NEW_FLAIR_CSS = ""
# Set to True if you only want to see how many posts would be altered. No flairs will be altered with this set to True.


# ### END USER CONFIGURATION ### #
def setting_variables():
    if (os.path.exists("oauth.txt") and os.path.isfile("oauth.txt")):
        pass
    else:
        print("You do not have the necessary oauth.txt file.\n This is a one time set-up process.\n")
        app_key = input("Input your app id and then hit the \'Enter\' or \'return\' key on your keyboard:\n")
        app_secret = input("Input your app secret and then hit the \'Enter\' or \'return\' key on your keyboard.\nRemember to never share your app secret:\n")
        print("Writing to file \"oauth.txt\", please wait.")
        oauth_file = open("oauth.txt", "w")
        oauth_file.write("# This is yout oauth.txt\n\n# Config:\nscope=modflair\nrefreshable=True\n\n# App Info\n")
        oauth_file.write("app_key=", app_key, "\n")
        oauth_file.write("app_secret=", app_secret, "\n\n")
        oauth_file.write("# Token\ntoken=None\nrefresh_token=none\n")
        oauth_file.close()
        print("Done.")
    yesnoprompt = True
        while yesnoprompt:
            is_this_a_test: input('Would you like to do a test run instead of actually changing anything\(Y/n\)?\n')
            if (is_this_a_test == "Y" or is_this_a_test == "yes" or is_this_a_test == "y" or is_this_a_test == "YES")
                ONLY_TEST = True
                yesnoprompt = False
                print("This will be a test run. Nothing will be changed.")
            elif (is_this_a_test == "N" or is_this_a_test == "no" or is_this_a_test == "n" or is_this_a_test == "NO"):
                ONLY_TEST = False
                yesnoprompt = False
                print("This will NOT be a test run. Flairs will be changed.")
            else:
                print("You did not input an accepted value.\nPlease input 'Y' for \"yes\" or 'n' for \"no\" (or 'yes' and 'no', respectively) next time.")
    USERAGENT = input('Please input your useragent and then hit the \'Enter\' or \'return\' key on your keyboard.\nIt should contain a short description of what it does and yout username. E.g. RSS Bot by /u/SmBe19:\n')
    print("Your user agent is now", USERAGENT)
    SUBREDDIT = input('Please input the subreddit that you are working on and then hit the \'Enter\' or \'return\' key on your keyboard:\n')
    print("The subreddit you have selected is /r/{0}".format(SUBREDDIT))
    print("Now you must set the text and css class of the flair you want to change, as well as the text and class you want it to become.\nInput \"*\" to use a wildcard\n")
    OLD_FLAIR_TEXT = input('Please input the text of the flair that you want to change and then hit the \'Enter\' or \'return\' key on your keyboard:\nWARNING: This script will not use the search method if this is a wildcard\n')
        
    r = praw.Reddit(USERAGENT)
    o = OAuth2Util.OAuth2Util(r)
    sub = r.get_subreddit(SUBREDDIT)
    FLAIR_QUERY = "flair:'{0}'".format(OLD_FLAIR_TEXT)

def run_hot_flair_setting():
    print("Will now replace link flairs with a text of \"{0}\" and a class of \"{1}\" to have a text of \"{2}\" and a class of \"{3}\" via the \"Hot\" page".format(OLD_FLAIR_TEXT, OLD_FLAIR_CSS, NEW_FLAIR_TEXT, NEW_FLAIR_CSS))
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
    print("Will now replace link flairs with a text of \"{0}\" and a class of \"{1}\" to have a text of \"{2}\" and a class of \"{3}\" via the \"New\" page".format(OLD_FLAIR_TEXT, OLD_FLAIR_CSS, NEW_FLAIR_TEXT, NEW_FLAIR_CSS))
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
    print("Will now replace link flairs with a text of \"{0}\" and a class of \"{1}\" to have a text of \"{2}\" and a class of \"{3}\" via the \"Rising\" page".format(OLD_FLAIR_TEXT, OLD_FLAIR_CSS, NEW_FLAIR_TEXT, NEW_FLAIR_CSS))
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
    elif not OLD_FLAIR_CSS and not OLD_FLAIR_TEXT:
        print("Old flair not set")
    else:
        run_full_script()
			