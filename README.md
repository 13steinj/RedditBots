# RedditBots

## Prerequisites
To run any of those bots you need:

### Software

[Python 2 or Python 3](https://www.python.org/downloads/).  
The version required will be mentioned in the bot's READMEs.
The latest of each (your OS is automatically detected) are available at first sight as shown here:

You can download specific versions by selecting a Python version from here and clicking `Download`:

From there, you can also download versions for 32/64-bit, as well as for different OS's then automatically detected (if for whatever reason needed (`Source Release` is for Linux/UNIX)):

### Packages
* [PRAW](https://github.com/praw-dev/praw/blob/master/) (`pip install praw`)
* [OAuth2Util](https://github.com/SmBe19/praw/blob/master/) (`pip install praw-oauth2util`) *or* prawoauth2 (`pip install praw-oauth2util`)

Note: Most of the bots install / update the ones needed for you if they detect they are not there / not the version they need
Note: Special syntax:  
* `pip install packagename --upgrade` ~ updates the package called `packagename` if already installed to it's latest version.
* `pip install packagename==x.y.z` ~ installs the package called `packagename`'s specified version `x.y.z`.
* `pip install 'packagename>=x.y.z'` ~ installs the package called `packagename`'s specified version `x.y.z` or greater.
* `pip install packagename -r "SOMEPATH/filename.txt"` ~ Installs / updates packages from a file with the name `filename.txt` that is in the location of `SOMEPATH`, these files must be in the [correct format](https://pip.pypa.io/en/latest/reference/pip_install.html#requirements-file-format).

If the bot uses OAuth2, you have to [register an app on Reddit](https://www.reddit.com/prefs/apps/), using `script` as app type and `http://127.0.0.1:65010/authorize_callback` as redirect uri. You then have to create a file called `oauth.txt` in the folder and paste the app id on the first line and the app secret on the second line.

In the source code of the bots you will find 

    try:
        import bot
        variable = bot.variable
    except ImportError:
        variable = input("Please input your <variable>:\n")

The term `variable` will be one of the following. There may be

 - `SUBREDDIT` ~ The subreddit you're working on
 - `USERAGENT` ~ Your user-agent, it should be descriptive and include your username.
  Sometimes this is automatically specified in the script; and a `USERNAME` is instead asked for, which will be appended to the given `USERAGENT`
 - `USERNAME` ~ Your username used for the user-agent (or log in if not using Oauth2)
  Note: Oauth2 will soon be mandated. By this time (supposedly August 3rd), this variable will no longer be used for logging in
 - `PASSWORD` ~ Your password
 - `APP_KEY` 
. In the `USER CONFIGURATION` section you should fill out every variable as they describe detailed what and where the bot should do (e.g. User Name, Subreddit to operate in, duration of sleep). The `BOT CONFIGURATION` section defines variables that you don't really have to change, but if you really have to, they are there. They are mostly constants for the bot (e.g. Name of config files).

##List of Bots

 * **ChangeFlairBot** ~ a bot to change link flairs in a subreddit
