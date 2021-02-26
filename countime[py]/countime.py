import gi
import time
gi.require_version('Gtk','3.0')
from gi.repository import Gtk,GObject,Pango
import threading
import datetime
class timec(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='countime')
        self.set_default_size(700,200)
        self.fixed = Gtk.Fixed()
        self.clock = '00:00:00'
        #label
        self.l1 = Gtk.Label('CountDown')
        self.l2 = Gtk.Label()
        self.l2.set_text(self.clock)
        font = Pango.FontDescription("Tahoma 48")
        self.l2.override_font(font)
        self.lh = Gtk.Label('Hour')
        self.lm = Gtk.Label('Min')
        self.ls = Gtk.Label('Sec')
        #button
        self.btn = Gtk.Button('start')
        self.btn.connect('clicked',self.start)
        #SpinButton
        adj = Gtk.Adjustment(0.0,0.0,60.0,1.0,5.0,1.0)
        adj2 = Gtk.Adjustment(0.0,0.0,60.0,1.0,5.0,1.0)
        adj3 = Gtk.Adjustment(0.0,0.0,60.0,1.0,5.0,1.0)
        self.sb = Gtk.SpinButton()
        self.sb2 = Gtk.SpinButton()
        self.sb3 = Gtk.SpinButton()
        self.sb.set_adjustment(adj)
        self.sb2.set_adjustment(adj2)
        self.sb3.set_adjustment(adj3)
        #fixed
        self.fixed.put(self.btn,600,0)
        self.fixed.put(self.sb3,450,0)
        self.fixed.put(self.sb2,300,0)
        self.fixed.put(self.sb,150,0)
        self.fixed.put(self.l1,10,5)
        self.fixed.put(self.l2,210,70)
        self.fixed.put(self.lh,150,30)
        self.fixed.put(self.lm,300,30)
        self.fixed.put(self.ls,450,30)
        self.add(self.fixed)
    def countime(self):
        h = int(self.sb.get_text())
        m = int(self.sb2.get_text())
        s = int(self.sb3.get_text())
        while not self.event.is_set():
            while h > -1:
                while m > -1:
                    while s > 0:
                        s -= 1
                        time.sleep(1)
                        hs = ''
                        ms = ''
                        ss = ''
                        if h < 10:
                            hs = '0'
                        else:
                            hs = ''
                        if m < 10:
                            ms = '0'
                        else:
                            ms = ''
                        if s < 10:
                            ss = '0'
                        else:
                            ss = ''
                        self.l2.set_label(hs+str(h)+':'+ms+str(m)+':'+ss+str(s))
                    m -= 1
                    s = 60
                h -= 1
                m = 60
 
    def start(self,button):
        self.timer = threading.Thread(target=self.countime)
        self.event = threading.Event()
        self.timer.daemon=True
        self.timer.start()
            
        
    
                    
call = timec()
call.connect('destroy',Gtk.main_quit)
call.show_all()
#call.start()
Gtk.main()
#3label hour min sec
