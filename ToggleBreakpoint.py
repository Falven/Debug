import sublime, sublime_plugin

def plugin_loaded():
    global pluginLoaded;

    pluginLoaded = True;

class ToggleBreakpointCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global pluginLoaded;

        if pluginLoaded:
            print("Toggled A Breakpoint.")
