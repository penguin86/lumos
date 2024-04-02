from gi.repository import GObject

from .time_priority_page import TimePriorityPage

# Register widgets to be used in templates UI
def registerWidgets() -> None:
    GObject.type_ensure(TimePriorityPage)

