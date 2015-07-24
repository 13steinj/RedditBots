import sys
import os
import time
import platform
import urllib
import pip
import shutil
import urllib.request

def maindownload(file_name):
    url = "https://raw.githubusercontent.com/13steinj/RedditBots/master/ChangeFlairBot/{0}".format(file_name)
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print("Downloading: {0} {1} Bytes: {2}".format(file_name, "(the main script)", file_size))
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status)
    f.close()
if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    if not os.path.exists("ChangeFlairBotBak"):
        os.makedirs("ChangeFlairBotBak")
    try:
        import script
    except ImportError:
        maindownload("script.py")
        import script
    script.script_version_update()
    reload(script)
    version_check()
