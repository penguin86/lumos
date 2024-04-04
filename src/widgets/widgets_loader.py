from gi.repository import GObject

from .time_priority_page import TimePriorityPage
from .aperture_priority_page import AperturePriorityPage

# Register widgets to be used in templates UI
def registerWidgets() -> None:
    GObject.type_ensure(TimePriorityPage)
    GObject.type_ensure(AperturePriorityPage)

