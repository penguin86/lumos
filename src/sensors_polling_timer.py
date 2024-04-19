from gi.repository import Gio, GLib
from threading import Timer

# window.py
#
# Copyright 2024 Daniele Verducci
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


# A timer for polling the light sensor via DBus.
# Checks the sensor at a specific interval and runs a callback only when an update is detected.
#
# Usage:
# Instantiate it, then call run(interval_in_seconds, callback_function)
# To stop it, call cancel()
class SensorsPollingTimer(Timer):
	def run(self):
		# Setup
		bus = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)
		self.proxy = Gio.DBusProxy.new_sync(bus,Gio.DBusProxyFlags.NONE,None,'net.hadess.SensorProxy','/net/hadess/SensorProxy','org.freedesktop.DBus.Properties', None)
		self.oldValue = None

		# Loop
		while not self.finished.wait(self.interval):
			value = self.proxy.Get('(ss)', 'net.hadess.SensorProxy', 'LightLevel')
			if (self.oldValue != value):
				self.oldValue = value
				unit = self.proxy.Get('(ss)', 'net.hadess.SensorProxy', 'LightLevelUnit')
				self.function(value, unit)    # Invoke callback

