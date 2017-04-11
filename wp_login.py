#!/usr/bin/env python

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.exceptions import *
from wordpress_xmlrpc.methods import *
import argparse

def main(args):
    wp_url = args.url
    wp_user = args.user
    wp_pass = args.pwd

    try:
        wp_site = Client(wp_url, wp_user, wp_pass)
        siteurl = wp_site.call(options.GetOptions(['home_url']))[0].value
        if siteurl:
            print("[+] login successfully: " + wp_user + ":" + wp_pass)
    except InvalidCredentialsError as e:
        print("[!] login failed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url',  help="url + xmlrpc.php path (required)", required=True)
    parser.add_argument('--user', help="username (required)", required=True)
    parser.add_argument('--pwd', help="password (required)", required=True)
    args = parser.parse_args()
    main(args)