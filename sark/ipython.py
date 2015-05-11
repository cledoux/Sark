from IPython import display

from .qt import capture_widget, get_window, get_widget

def snap(title=None):
    if title:
        w = get_widget(title)
    else:
        w = get_window()

    return display.Image(data=capture_widget(w))