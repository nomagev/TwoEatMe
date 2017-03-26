# Testing for Issue 13:
# Handling Proper CHCP setup on Shell
# https://github.com/nomagev/TwoEatMe/issues/13

import os

# pylint: disable=C0103
# -*- coding: utf-8 -*-

subprocess.check_output(['cmd.com'])
print table(['chcp.com'])

#end