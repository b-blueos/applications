import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf
import sys
import os


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="BlueOS Hub", application=app)
        self.set_default_size(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_from_file("/blue/assets/logo.png")

        main = Gtk.Box(orientation=1)
        main.pack_start(Gtk.Label(), False, False, 1)

        header = Gtk.Label()
        user = os.getlogin()
        header.set_markup("<b><big><big>Welcome, what would you like to do " + user + "?</big></big></b>")
        main.pack_start(header, False, False, 5)


        help_section = Gtk.Box(orientation=0)

        help_label = Gtk.Label()
        help_label.set_markup("Read the online Documentation?")

        help_page = Gtk.LinkButton(uri="https://blueos.burnyllama.tk")
        help_page.set_label("Official Webpage")

        help_section.pack_start(Gtk.Label(), True, False, 10)
        help_section.pack_start(help_label, False, False, 5)
        help_section.pack_start(help_page, False, False, 5)
        help_section.pack_start(Gtk.Label(), True, False, 10)

        main.pack_start(help_section, False, False, 5)

        self.add(main)

class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.set_decorated(True)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
