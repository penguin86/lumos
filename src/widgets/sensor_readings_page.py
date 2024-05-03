# sensor_readings_page.py
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

from gi.repository import Adw
from gi.repository import Gtk
from .ev_calculator import EVCalculator

@Gtk.Template(resource_path='/eu/ichibi/Lumos/widgets/sensor_readings_page.ui')
class SensorReadingsPage(Gtk.Box):
    __gtype_name__ = 'SensorReadingsPage'

    # Labels
    lux_label = Gtk.Template.Child()
    ev_label = Gtk.Template.Child()

    def onValuesChanged(self, isoSpeed: int,  sensorValue: float, sensorUnit: str):
        # Called when the light value changed

        if self.lux_label:
            self.lux_label.set_label("{:.0f} {}".format(sensorValue, sensorUnit))

        # Check the unit is absolute ("lux"), otherwise there's no way to convert to an absolute EV value
        if sensorUnit != "lux":
            return

        # Convert lux to EV
        ev = EVCalculator.luxToEV(sensorValue)
        if self.ev_label:
            self.ev_label.set_label("{:.1f} EV".format(ev))

    def onIsoSpeedChanged(self, isoSpeed: int):
        print("SR: onIsoSpeedChanged {}".format(isoSpeed))
