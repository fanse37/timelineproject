#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "timelineproject.settings")

    from django.core.management import execute_from_command_line
	aaaa
    execute_from_command_line(sys.argv)
