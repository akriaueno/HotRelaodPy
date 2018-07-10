#!/usr/bin/env python

import sys
import os
from pathlib import Path
from subprocess import Popen

watch_dir = sys.argv[1]
cmd = sys.argv[2:]
watch_files = [os.fspath(py) for py in Path(watch_dir).glob('**/*.py')]
file_mtimes = {f: os.stat(f).st_mtime for f in watch_files}
p = Popen(cmd)
while True:
    for (f, mt) in file_mtimes.items():
        new_mt = os.stat(f).st_mtime
        if new_mt != mt:
            file_mtimes[f] = new_mt
            print('[changed] ', f)
            p.terminate()
            p = Popen(cmd)
