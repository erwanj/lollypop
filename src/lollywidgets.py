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

from gi.repository import Gtk, Gdk

"""
	Custom Event Box: just change mouse cursor type on enter/leave event
"""
class LollyEventBox(Gtk.EventBox):

	__gtype_name__ = 'LollyEventBox'

	def __init__(self):
		Gtk.EventBox.__init__(self)

	"""
		Change mouse pointer to Hand
	"""
	def do_enter_notify_event(self, event):
		print("event")
		gdk_window = self.get_root_window()
		gdk_window.set_cursor(Gdk.Cursor(Gdk.CursorType.HAND1))

	"""
		Change mouse pointer to left ptr
	"""
	def do_leave_notify_event(self, event):
		gdk_window = self.get_root_window()
		gdk_window.set_cursor(Gdk.Cursor(Gdk.CursorType.LEFT_PTR))

