#!/usr/bin/python3
# Fabfile to delete out-of-date archives.

from fabric.api import env, run
from fabric.operations import sudo

env.hosts = ["54.160.85.72", "35.175.132.106"]

def do_clean(number=0):
    number = int(number)

    # Ensure we keep at least one version
    if number == 0:
        number = 1

    # Delete files in versions
    versions_files = sorted(run('ls -tr versions').split())
    if len(versions_files) > number:
        del versions_files[-number:]  # Leave the last 'number' of files
        for outdated_file in versions_files:
            sudo('rm versions/{}'.format(outdated_file))

    # Delete files in /data/web_static/releases
    releases_files = sorted(run('ls -tr /data/web_static/releases').split())
    if len(releases_files) > number:
        del releases_files[-number:]  # Leave the last 'number' of files
        for outdated_file in releases_files:
            sudo('rm -rf /data/web_static/releases/{}'.format(outdated_file))
