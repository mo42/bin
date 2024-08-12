#!/usr/bin/python3

import argparse
import getpass
import pysftp
import posixpath
import stat

def rmtree(sftp, remote_path):
    for file in sftp.listdir_attr(remote_path):
        path = posixpath.join(remote_path, file.filename)
        if stat.S_ISDIR(file.st_mode):
            rmtree(sftp, path)
        else:
            path = posixpath.join(remote_path, file.filename)
            sftp.remove(path)
    sftp.rmdir(remote_path)

def main():
    parser = argparse.ArgumentParser(description='Recursively delete all files on an SFTP server.')
    parser.add_argument('host', type=str, help='The host to connect to')
    parser.add_argument('username', type=str, help='The username for login')
    args = parser.parse_args()
    password = getpass.getpass(prompt=f'{args.username}@{args.host}\'s password: ')
    with pysftp.Connection(args.host, username=args.username, password=password) as sftp:
        rmtree(sftp, './')

if __name__ == '__main__':
    main()
