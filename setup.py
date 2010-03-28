#!/usr/bin/python
# apt-forktracer - a utility for managing package versions
# Copyright (C) 2008,2010 Marcin Owsiany <porridge@debian.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from distutils.core import setup
setup(name = 'apt-forktracer',
	version = '0.3',
	description = 'Debian packages version tracing utility',
	author = 'Marcin Owsiany',
	author_email = 'marcin@owsiany.pl',
	packages = ['apt_forktracer'],
	package_dir = {'': 'lib'},
	scripts = ['apt-forktracer']
	)

