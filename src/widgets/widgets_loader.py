from gi.repository import GObject

from .time_priority_page import TimePriorityPage
from .aperture_priority_page import AperturePriorityPage
from .manual_exposure_page  import ManualExposurePage
from .sensor_readings_page  import SensorReadingsPage

# Register widgets to be used in templates UI
def registerWidgets() -> None:
    GObject.type_ensure(TimePriorityPage)
    GObject.type_ensure(AperturePriorityPage)
    GObject.type_ensure(ManualExposurePage)
    GObject.type_ensure(SensorReadingsPage)

