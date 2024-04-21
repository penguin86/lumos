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

from gi.repository import Adw
from gi.repository import Gtk
from .sensors_polling_timer import SensorsPollingTimer
from .ev_calculator import EVCalculator

@Gtk.Template(resource_path='/eu/ichibi/Lumos/window.ui')
class LumosWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'LumosWindow'

    lux_label = Gtk.Template.Child()
    ev_label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Start polling sensors
        self.sensorsPollingTimer = SensorsPollingTimer(0.1, self.onSensorRead)
        self.sensorsPollingTimer.start()

    def onSensorRead(self, value: float, unit: str):
        # Called when the light value changed
        print("Read {} {}".format(value, unit))

        if self.lux_label:
            self.lux_label.set_label("{:.0f} {}".format(value, unit))

        # Convert lux to EV
        ev = EVCalculator.luxToEV(value)
        if self.ev_label:
            self.ev_label.set_label("{:.1f} EV".format(ev))

