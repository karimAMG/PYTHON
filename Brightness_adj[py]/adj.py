import gi
import os
import gtk
gi.require_version('Gtk','3.0')
from gi.repository import Gtk , GdkPixbuf

class data(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Brightness')
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_from_file('gauge.png')
        #windows size
        self.set_default_size(260,110)
        self.fixed = Gtk.Fixed()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename='gauge.png',width=230,height=230,preserve_aspect_ratio=True)
        self.img = Gtk.Image.new_from_pixbuf(pixbuf)
        
        self.adj = Gtk.Adjustment(value=0.8,lower=0.0,upper=0.9,step_incr=1,page_incr=10,page_size=0)
        self.adj.connect('value_changed',self.adj_action)
        self.adj.emit('value_changed')
        self.scale = Gtk.HScale(adjustment=self.adj)
        self.scale.show()
        self.scale.set_property("width-request",238)
        self.fixed.put(self.img,15,-50)
        self.fixed.put(self.scale,10,130)
        self.add(self.fixed)
    def adj_action(self,adj):
        cmd = 'xrandr --output LVDS1 --brightness '+str(self.adj.get_value())
        os.system(cmd)
        
call = data()
# On Exit
call.connect('destroy',Gtk.main_quit)
# on display
call.show_all()
Gtk.main()
