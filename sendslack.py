#!/usr/bin/env/python
"""
Send a slack message to $SLACK_URL
    usage: python -m sendslack [-h] [--channel CHANNEL] [--username USERNAME]
                     [--icon ICON] [--url URL] [--message MESSAGE | -]
We roll with the webhooks default settings, however each one can be overridden
via command-line option. Due to the sensitive nature of the webhook url we
prefer the url come in over SLACK_URL, but the lazy could just do --url.
"""
import requests
import sys
import os
import argparse


def send(url, message, channel=None, username=None, icon=None):
    """Send a message to a channel via incoming webhook url."""
    data = dict(channel=channel, username=username, text=message,
                icon_emoji=icon)
    requests.post(url, json=data)


def arg_parser():
    desc = 'Send a message to slack via incoming webhook.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--channel')
    parser.add_argument('--username')
    parser.add_argument('--icon')
    parser.add_argument('--url')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--message')
    group.add_argument('infile', type=argparse.FileType('r'), nargs='?')
    return parser


if __name__ == '__main__':
    args = vars(arg_parser().parse_args())
    try:
        url = args.pop('url') or os.environ.get('SLACK_URL')
        if not url:
            raise ValueError('no SLACK_URL set')
        infile, message = args.pop('infile'), args.pop('message')
        if infile:
            message = infile.read().strip()
        send(url, message, **args)
    except Exception as e:
        print('error: ' + str(e), file=sys.stderr)
        sys.exit(1)
