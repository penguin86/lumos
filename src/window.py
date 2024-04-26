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

from gi.repository import Adw, Gtk, GObject
from .sensors_polling_timer import SensorsPollingTimer
from .ev_calculator import EVCalculator

@Gtk.Template(resource_path='/eu/ichibi/Lumos/window.ui')
class LumosWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'LumosWindow'

    # Labels
    lux_label = Gtk.Template.Child()
    ev_label = Gtk.Template.Child()
    error_banner = Gtk.Template.Child()
    sensor_unit_error_banner = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.lastError = None

        # Register for window lifecycle events
        self.connect("close-request", self.__on_close_request)

        # Start polling sensors
        self.sensorsPollingTimer = SensorsPollingTimer(0.1, self.onSensorRead)
        self.sensorsPollingTimer.onError = self.onError
        self.sensorsPollingTimer.start()

    def __on_close_request(self, _obj: GObject.Object) -> None:
        # On window destroyed.Stop polling sensors
        self.sensorsPollingTimer.cancel()

    def onSensorRead(self, value: float, unit: str):
        # Called when the light value changed

        if self.lux_label:
            self.lux_label.set_label("{:.0f} {}".format(value, unit))

        # Check the unit is absolute ("lux"), otherwise there's no way to convert to an absolute EV value
        if unit != "lux":
            self.sensor_unit_error_banner.set_revealed(True)
            return

        # Convert lux to EV
        ev = EVCalculator.luxToEV(value)
        if self.ev_label:
            self.ev_label.set_label("{:.1f} EV".format(ev))

    def onError(self, e: Exception):
        self.lastError = e
        self.error_banner.set_revealed(True)

    @Gtk.Template.Callback()
    def showErrorDetails(self, _button: Gtk.Button) -> None:
        # Called by error_banner button click signal
        if "ServiceUnknown" in self.lastError.message or "UnknownMethod" in self.lastError.message:
            dialogTitle = "No light sensor found"
        else:
            dialogTitle = "Unable to access D-Bus"

        dialog = Adw.AlertDialog(
            heading = dialogTitle,
            body = self.lastError,
            close_response="close",
        )
        dialog.add_response("close", "Close")
        dialog.choose(self, None, None)


