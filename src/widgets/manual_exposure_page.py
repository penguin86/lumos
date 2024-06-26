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

@Gtk.Template(resource_path='/eu/ichibi/Lumos/widgets/manual_exposure_page.ui')
class ManualExposurePage(Gtk.Box):
    __gtype_name__ = 'ManualExposurePage'


    def onValuesChanged(self, isoSpeed: int,  sensorValue: float, sensorUnit: str):
        # Check the unit is absolute ("lux")
        if sensorUnit != "lux":
            return

    def onIsoSpeedChanged(self, isoSpeed: int):
        print("ME: onIsoSpeedChanged {}".format(isoSpeed))
