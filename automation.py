import os
import subprocess
from datetime import datetime
import logging
import sys


def current_date():
    file_path = "date.txt"
    content = f"File updated on {datetime.now()}"
    with open(file_path, 'w') as file:
        file.write(content)

current_date()
