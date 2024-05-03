# time_priority_page.py
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

@Gtk.Template(resource_path='/eu/ichibi/Lumos/widgets/time_priority_page.ui')
class TimePriorityPage(Gtk.Box):
    __gtype_name__ = 'TimePriorityPage'

    # Values of time dropdown entries defined in the .ui file
    time_priority_speed_dropdown_values = [
        1/4000,
        1/2000,
        1/1000,
        1/500,
        1/250,
        1/125,
        1/60,
        1/30,
        1/15,
        1/8,
        1/4,
        1/2,
        1,
        2,
        4,
        8,
        15,
        30
    ]

    # Widgets
    time_priority_speed_dropdown = Gtk.Template.Child()
    time_priority_aperture_label = Gtk.Template.Child()

    lastSensorValue = None

    def onValuesChanged(self, isoSpeed: int, sensorValue: float, sensorUnit: str):
        # Check the unit is absolute ("lux")
        if sensorUnit != "lux":
            return

        self.lastSensorValue = sensorValue
        self.updateView(isoSpeed, sensorValue)

    def onIsoSpeedChanged(self, isoSpeed: int):
        if self.lastSensorValue:
            self.updateView(isoSpeed, self.lastSensorValue)

    def updateView(self, isoSpeed: int, sensorValue: float):
        shutterSpeed = self.time_priority_speed_dropdown_values[self.time_priority_speed_dropdown.get_selected()]
        apertureValue = EVCalculator.calcAperture(isoSpeed, sensorValue, shutterSpeed)
        # TODO: Round aperture value to nearest existing value and set label color to red if outside 1 stop range
        self.time_priority_aperture_label.set_label("f/ {:.2f}".format(apertureValue))
