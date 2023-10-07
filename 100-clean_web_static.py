#!/usr/bin/python3
from fabric.api import *

# List of hosts to connect to
env.hosts = ['54.160.85.72', '35.175.132.106']

def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    # Get a list of local archives, sorted in ascending order
    local_archives = sorted(os.listdir("versions"))

    # Remove the 'number' most recent archives from the list
    for _ in range(number):
        if local_archives:
            local_archives.pop()

    # Delete the remaining archives in the 'versions' directory
    with lcd("versions"):
        for archive in local_archives:
            local("rm ./{}".format(archive))

    # On the remote servers, delete all but the 'number' most recent
    # archives in the '/data/web_static/releases' directory
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]

        for _ in range(number):
            if remote_archives:
                remote_archives.pop()

        for archive in remote_archives:
            run("rm -rf ./{}".format(archive))
