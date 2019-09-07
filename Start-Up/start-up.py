import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf
import sys
import os


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="", application=app)
        self.set_default_size(800, 100)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_from_file("/blue/assets/logo.png")

        welcome = Gtk.Label()
        welcome.set_markup("<big><big><b>Welcome to BlueOS!</b></big></big>")

        info = Gtk.Label()
        info.set_markup("This message will only show up the first time you boot the OS. \n"
                        "(Unless of course.... Bugs.....) \n"
                        "Do you want to start a quick guide? (Not yet implemented implemented...)")
        info.set_line_wrap(True)
        info.set_justify(Gtk.Justification.CENTER)

        logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("/blue/assets/logo.png", 300, 300, True)
        logo = Gtk.Image()
        logo.set_from_pixbuf(logo_pixbuf)
        logo.set_hexpand(False)

        webpageLink = Gtk.LinkButton(uri="https://blueos.burnyllama.tk")
        webpageLink.set_label("Official Webpage")
        webpage = Gtk.Box(orientation=0, spacing=50)
        webpage.pack_start(Gtk.Label(), True, False, 10)
        webpage.pack_start(webpageLink, False, False, 10)
        webpage.pack_start(Gtk.Label(), True, False, 10)

        button_info = Gtk.Button()
        button_info.set_label("Start Guide!")
        button_info.connect("clicked", self.do_guide)

        button_exit = Gtk.Button()
        button_exit.set_label("Skip Guide")
        button_exit.connect("clicked", self.do_exit)

        buttons = Gtk.Box(orientation=0, spacing=20)

        box = Gtk.Box(spacing=10, orientation=1)
        box.pack_start(Gtk.Label(), True, True, 5)
        box.pack_start(logo, False, True, 5)
        box.pack_start(welcome, False, True, 5)
        box.pack_start(webpage, False, True, 5)
        box.pack_start(info, False, True, 5)

        box.pack_end(Gtk.Label(), True, True, 5)
        box.pack_end(buttons, True, True, 10)
        buttons.pack_start(Gtk.Label(), True, True, 5)
        buttons.pack_start(button_info, True, True, 5)
        buttons.pack_start(button_exit, True, True, 5)
        buttons.pack_start(Gtk.Label(), True, True, 5)


        self.add(box)

    def do_guide(self, button):
        # Initialize guide!
        sys.exit("Guide-Mode")
    def do_exit(self, button):
        sys.exit("Close-Down")

class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.set_decorated(False)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
