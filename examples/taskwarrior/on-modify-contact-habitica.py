#!/usr/bin/env python3
"""Checks off a task as done on habitica when it's done with taskwarrior."""

import os
import sys
import json
import subprocess as sp
import logging


logger = logging.getLogger("__main__")
# A bit of an ugly hack, but this is a little hook script
if os.getenv('DEBUG'):
    logging.basicConfig(level=logging.DEBUG)


def habash(command, task_text):
    """Runs habash in an unsanitized shell.

    This command is equivalent running the following in the underlying shell:
        $ habash <command> <task_text>
    """
    # NOTE: possible Heisenbug here! Be careful when debugging!
    if os.getenv('DEBUG'):
        return sp.check_call("habash {} {} & ".format(
            command, task_text), shell=True)
    else:
        return sp.check_call("(habash {} \"{}\" >& /dev/null) & ".format(
            command, task_text), shell=True)


def habash_up(task_text):
    """Upvotes habitica task."""
    return habash("up", task_text)


def main():
    # Unmodified task can be read in and ignored.
    sys.stdin.readline()

    # Modified task as raw string is needed later
    modified_task_string = sys.stdin.readline()
    modified_task = json.loads(modified_task_string)

    # Now to contact habitica
    if modified_task['status'] == 'completed':
        logger.debug("Task description: {}".format(modified_task['description']))
        habash_up(modified_task['description'])

    # habash expects the modified task to be written to stdout.
    sys.stdout.write(modified_task_string)


if __name__ == '__main__':
    main()
