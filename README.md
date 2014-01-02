RestoreFontSizeCommand() for Sublime Text
=========================================

_This extension works with Sublime Text 2 or Sublime Text 3 beta._

Use this Sublime Text extension to restore your edit window font size to a default size defined by you! This is useful if you ever use the Ctrl/Command-= and Ctrl-Command-- keystrokes to increase/decrease the size of the font in the edit window (similar to what you can do with most browsers).

This simple Sublime Text extension is a replacement for the default reset_font_size function that is included as part of Sublime Text (but, curiously, not mapped to any keys on the keyboard) in the Packages/Default/font.py file (which appears to be only distributed with Sublime Text 2). This function is meant to be mapped to Ctrl/Command-0 on your keyboard; by default, the increase_font_size and decrease_font_size functions are mapped to the Ctrl/Command-= and Ctrl/Command-- keys.

Installation
------------

_There is no package install script, you have to do all of this by hand._

Why? Because I'm too lazy to figure out how to create a package install script and because this is such a tiny little extension I didn't think it was worth the effort. Maybe over another long holiday break I'll get the time to figure out how to do that. In the meantime, follow these instructions...

1. Copy `restore_font_size.py` to the Sublime `Packages/User` folder.
  * The precise location varies by OS and install type.
  * OS X: `~/Library/Application Support/Sublime Text 3/Packages/User`
  * Windows relocatable: `<sublime-install-dir>\data\Packages\User`
  * Linux: `TBD`

2. Add the following key bindings to your user key preferences file.
  * `{ "keys": ["super+0"], "command": "restore_font_size" },`
  * `{ "keys": ["ctrl+0"], "command": "restore_font_size" }`
  * Note that the last item in your key-map array should *NOT* end with a `,` character!
  * Find this file via the `Preferences > Key Bindings - User` menu.

3. Add the `font_size_default` property to your user settings file. 
  * `"font_size_default": 11`
  * What to use for the default depends on your eyes, your default font, your monitor...
  * Note that the last item in your user settings array should *NOT* end with a `,` character!
  * Find this file via the `Preferences > Settings - User` menu.

Usage
-----

Try using the Ctrl-= and Ctrl-- keys (Command-= and Command-- on Mac) to change the size of the fonts in your edit windows. Use Ctrl-0 (Command-0 on Mac) to restore the font size to the `font_size_default` setting you defined above.

Why is this needed? Because the `font_size` value gets rewritten every time you use the builtin `increase_font_size` and `decrease_font_size` commands (attached to the Ctrl-=/Ctrl-- keys). So there is "no going back!" This little hack provides a way to get back to your preferred settings, quickly and precisely.

Background
----------

An interesting thing to do is open your user settings file (`Preferences > Settings - User` menu) and watch what happens to the value of the `font_size` setting when you increase and decrease the size of your edit window's font. That's why I needed this extra little ditty. 

I could have used the builtin `reset_font_size` function, but it handles the reset using a very brutal method; it deletes the `font_size` setting from your settings file. I figure my little `restore_font_size` function is a "kinder, gentler" approach; plus it gives you more control over what the actual default font size will be!
