#!/usr/bin/env python3
"""The core functionality of enb is extended by means of plugins and templates. These derive from Installable,
a class that by default copies the Installable's source contents and runs the subclass' build() method.
Python libraries available via pip can be defined for Installables, which are attempted to be satisfied before invoking
the build method.

Plugins are conceived self-contained, python modules that can assume the enb library is installed.

Templates are very similar to plugins, but use jinja to transform `.enbt` template files upon installation.

Please refer to each submodule for further information.
"""
__author__ = "Miguel Hernández-Cabronero <miguel.hernandez@uab.cat>"
__since__ = "01/08/2021"

from .installable import Installable, import_all_installables, list_all_installables
from .plugin import Plugin, PluginMake
from .template import Template
