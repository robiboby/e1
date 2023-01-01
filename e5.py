import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
    entry = Gtk.Entry()

    def __init__(self):
        Gtk.Window.__init__(self, title="Taschenrechner")

        grid = Gtk.Grid()
        
        # entry field
        grid.attach(self.entry,0,0,4,1)

        # operations
        for i,op in enumerate(["+", "-", "*", "/"]):
            op_button = Gtk.Button(label=op)
            grid.attach(op_button,3,i+1,1,1)
            op_button.connect("clicked", self.op_button_clicked)

        # numbers
        for n in range(10):
            num_button = Gtk.Button(label=str(n))
            if n == 0:
                pos = (1,4,1,1)
            else:
                pos = ((n-1)%3,(n-1)//3+1,1,1)
            grid.attach(num_button,*pos)
            num_button.connect("clicked", self.num_button_clicked)

        show_result = Gtk.Button(label="Res")
        clear = Gtk.Button(label="Clear")
        grid.attach(show_result, 2,4,1,1)
        show_result.connect("clicked", self.res_button_clicked)
        grid.attach(clear, 0, 4, 1, 1)
        clear.connect("clicked", self.clear_clicked)

        self.add(grid)

    def num_button_clicked(self, widget):
        self.entry.set_text(self.entry.get_text() + widget.get_label())

    def op_button_clicked(self, widget):
        self.entry.set_text(self.entry.get_text() + widget.get_label())
        pass

    def res_button_clicked(self,widget):
        num = eval(self.entry.get_text())
        print("NUM == ", num)
        self.entry.set_text(str(num))

    def clear_clicked(self, widget):
        self.entry.set_text("")

window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()