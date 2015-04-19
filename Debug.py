import sublime, sublime_plugin

class DebugCommand(sublime_plugin.WindowCommand):
    def run(self):
        print("run")

def plugin_loaded():
    print("plugin_loaded")
    region = sublime.Region(0, self.view.size())
    lines = self.view.lines(region)
    print(len(lines))
