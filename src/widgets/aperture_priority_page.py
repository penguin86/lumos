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
    aperture_priority_speed_dropdown_values = [
        1/32,
        1/22,
        1/16,
        1/11,
        1/8,
        1/5.6,
        1/4,
        1/2.8,
        1/2,
        1/1.4
    ]

    # Widgets
    aperture_priority_aperture_dropdown = Gtk.Template.Child()
    aperture_priority_time_label = Gtk.Template.Child()

    def onValuesChanged(self, isoSpeed: int,  sensorValue: float, sensorUnit: str):
        # Check the unit is absolute ("lux")
        if sensorUnit != "lux":
            return

        apertureValue = self.aperture_priority_speed_dropdown_values[self.aperture_priority_aperture_dropdown.get_selected()]
        shutterSpeed = EVCalculator.calcShutterSpeed(isoSpeed, sensorValue, apertureValue)
        # TODO: Round shutter speed value to nearest existing value and set label color to red if outside 1 stop range
        self.aperture_priority_time_label.set_label("f/ {:.2f}".format(shutterSpeed))

