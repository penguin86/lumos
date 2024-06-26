# aperture_priority_page.py
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

@Gtk.Template(resource_path='/eu/ichibi/Lumos/widgets/aperture_priority_page.ui')
class AperturePriorityPage(Gtk.Box):
    __gtype_name__ = 'AperturePriorityPage'

    # Values of aperture dropdown entries defined in the .ui file
    # TODO: Load dropdown strings from APERTURE_VALUES.values()
    __aperture_priority_speed_dropdown_values = list(EVCalculator.APERTURE_VALUES.keys())

    # Widgets
    aperture_priority_aperture_dropdown = Gtk.Template.Child()
    aperture_priority_time_label = Gtk.Template.Child()

    __sensorValue = None
    __isoSpeed = EVCalculator.DEFAULT_ISO_SPEED

    def onValuesChanged(self, isoSpeed: int, sensorValue: float, sensorUnit: str):
        # Check the unit is absolute ("lux")
        if sensorUnit != "lux":
            return

        self.__sensorValue = sensorValue
        self.__isoSpeed = isoSpeed
        self.updateView()


    def onIsoSpeedChanged(self, isoSpeed: int):
        self.__isoSpeed = isoSpeed
        if self.__sensorValue:
            self.updateView()

    def updateView(self):
        apertureValue = self.__aperture_priority_speed_dropdown_values[self.aperture_priority_aperture_dropdown.get_selected()]
        shutterSpeed = EVCalculator.calcShutterSpeed(self.__isoSpeed, self.__sensorValue, apertureValue)

        # Round shutter speed value to nearest existing value and set label color to red if outside 1 stop range
        [nearestValue, isInsideRange] = EVCalculator.toNearestStr(shutterSpeed, EVCalculator.SHUTTER_SPEED_VALUES)

        if isInsideRange:
            self.aperture_priority_time_label.set_label(nearestValue)
        else:
            self.aperture_priority_time_label.set_label("<span foreground=\"red\">{}</span>".format(nearestValue))

    @Gtk.Template.Callback()
    def onApertureChanged(self, dropDown: Gtk.DropDown, _: any):
        self.updateView()

