""" A simple logging module for Pythonista.

Logs are saved in to './logs' where '.' is the 'slog.py' parent's parent (i.e. slog.py/../../logs/) directory

Requires Python3.6+
Copyright (c) 2021 Aareon Sullivan
"""
from datetime import datetime as dt
import os
from pathlib import Path
import sys
import traceback as tb

_pyfile_ = __file__.split("/")[-1]
DEFAULT_LOGS_DIR = Path(__file__).parent.parent / 'logs'

if not DEFAULT_LOGS_DIR.exists():
    DEFAULT_LOGS_DIR.mkdir(parents=True, exist_ok=True)

LN = '\n'
CR = '\r'

_print = print


def slog(msg, level='debug', datetime=True, print=True, write=True, logs_dir=DEFAULT_LOGS_DIR, NL=True, log_file=None):
    if log_file is None:
        log_file = 'slog.log'

    if datetime:
        now = dt.now()
        s = f'[{now.strftime("%m/%d/%y %H:%M:%S")}]'
    s = f'{s}[{level}] {msg}'
    
    if print:
        _print(f'{CR}{s}{LN if NL else ""}', end='')
    if write:
        try:
            with open(Path(logs_dir) / log_file, 'a+') as f:
                f.write(f'{s}{LN}')
        except Exception as exc:
            err = tb.something(exc)
            with open(DEFAULT_LOGS_DIR / 'errors.log', 'a+') as f:
                f.write(f'error when attempting to log:{LN}"{s}"{LN}{CR}{slog(trace, write=False, print=False)}')

    return s


if __name__ == '__main__':
    try:
        _stash = globals()['_stash']
        STASHLOG = os.environ.get('STASHLOG')
    except KeyError:
        print("Error. Try doing that in StaSH.")
