import sublime
import sublime_plugin

# Function to restore the default font size using Ctrl/Command-0 keystroke.
# Meant to repair the work of Ctrl/Command-+ and Ctrl/Command-- keystrokes
# that cause the font settings to move up and down in the user preferences.

class RestoreFontSizeCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        s = sublime.load_settings("Preferences.sublime-settings")
        default_font = s.get('font_size_default', 11)

        if default_font < 8:
            default_font = 8
        if default_font > 64:
            default_font = 64

        s.set('font_size', default_font)
        s.set('font_size_default', default_font)
        sublime.save_settings("Preferences.sublime-settings")
