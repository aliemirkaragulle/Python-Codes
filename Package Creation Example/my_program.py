#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 22:37:23 2022

@author: aliemirkaragulle
"""
# Import from a Module
from my_module import even_or_not

# Import from a Package
from MyMainPackage import main_script

# Import from a Sub-Package
from MyMainPackage.SubPackage import my_sub_script


# Functions
print(even_or_not(4))

print(main_script.report_main())

print(my_sub_script.sub_report())