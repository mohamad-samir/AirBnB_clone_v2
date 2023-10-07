#!/usr/bin/python3
from fabric.api import *

env.hosts = ["100.24.235.23", "3.85.141.52"]

def do_clean(number=0):
    number = 1 if int(number) == 0 else int(number)

    # Clean local versions
    local_archives = sorted(os.listdir("versions"))
    [local_archives.pop() for _ in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in local_archives]

    # Clean remote versions
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        [remote_archives.pop() for _ in range(number)]
        [run("rm -rf ./{}".format(a)) for a in remote_archives]
