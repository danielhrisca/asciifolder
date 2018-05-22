# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys

from colorama import Fore, init
from natsort import natsorted

init()


def folder2ascii(path, prefix=''):
    """ converts folder structure to list of strings

    Parameters
    ----------
    path : str
        root folder
    prefix : str
        prefix for current subfolder; default is empty str for the root folder

    Returns
    -------
    lines : list
        list of strings that compose the folder structure as text

    """
    name = os.path.basename(path)
    yield '{}{}{}{}/'.format(prefix, Fore.GREEN, name, Fore.RESET)

    items = list(os.listdir(path))

    if items:

        dim = len(items)


        folders = natsorted(
            [
                item
                for item in items
                if os.path.isdir(os.path.join(path, item))
            ]
        )

        files = natsorted(
            item
            for item in items
            if os.path.isfile(os.path.join(path, item))
        )

        cntr = 1

        if prefix:
            if prefix[0] not in  '└ ':
                char = '│'
            else:
                char = ' '

            clean_prefix = char + prefix[1:].replace('─', ' ').replace('├', '│').replace('└', ' ')
        else:
            clean_prefix = ''

        for folder in folders:

            if cntr == dim:
                prefix_ = clean_prefix + '└── '
            else:
                prefix_ = clean_prefix + '├── '

            for line in folder2ascii(
                    os.path.join(path, folder),
                    prefix_):
                yield line
            cntr += 1

        for file in files:
            if cntr == dim:
                prefix_ = clean_prefix + '└── '
            else:
                prefix_ = clean_prefix + '├── '
            yield '{}{}'.format(prefix_, file)

            cntr += 1


def main(path):
    for line in folder2ascii(path):
        print(line)


if __name__ == '__main__':
    main(sys.argv[1])
