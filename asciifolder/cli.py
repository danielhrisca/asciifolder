# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys

from natsort import natsorted


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
    lines = []
    name = os.path.basename(path)
    lines.append('{}{}/'.format(prefix, name))

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

            lines.extend(
                folder2ascii(
                    os.path.join(path, folder), 
                    prefix_,
                )
            )
            cntr += 1

        for file in files:
            if cntr == dim:
                prefix_ = clean_prefix + '└── '
            else:
                prefix_ = clean_prefix + '├── '
            lines.append('{}{}'.format(prefix_, file))

            cntr += 1

    return lines

def main(path):
    print(*folder2ascii(path), sep='\n')

if __name__ == '__main__':
    #main(sys.argv[1])
    main(r'd:\WinPython-64bit-3.6.4.0Qt5b5\python-3.6.4.amd64\Lib\concurrent')
