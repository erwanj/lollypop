#!/usr/bin/python
# Copyright (c) 2014 Cedric Bellegarde <gnumdk@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from gettext import gettext as _
from gi.repository import Gdk

"""
	Return formated artist name
	@param str
"""
def format_artist_name(name):
	# Handle language ordering
	# Translators: Add here words that shoud be ignored for artist sort order
	for special in _("The the").split():
		if name.startswith(special+" "):
				strlen = len(special+" ")
				name = name[strlen:]+"@@@@"+special
	return name

"""
	Return translate formated artist name
	@param str
"""
def translate_artist_name(name):
	split = name.split("@@@@")
	if len(split) == 2:
		name = split[1]+" "+split[0]
	return name
	
"""
	Return current monitor size
	@return (monitor width as int, monitor height as int)
"""
def get_monitor_size():	
		s = Gdk.Screen.get_default()
		m = s.get_monitor_at_window(s.get_active_window())
		monitor = s.get_monitor_geometry(m)
		return (monitor.width, monitor.height)
