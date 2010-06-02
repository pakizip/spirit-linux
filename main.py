import gtk
import gtk.glade
import pygtk
import os
import time
home = os.getenv("HOME")+"/"
folder = home+"spirit-linux"
if not os.path.exists(folder):
	os.system("mkdir "+folder)
	if not os.path.exists(folder+"/spirit-log"):
		newfile = open(folder+"/spirit-log", 'wt')
		newfile.close()
def on_button1_clicked(widget, data=None):
		button1.set_sensitive(False)
		button1.set_label(" ")
		time1 = os.stat(folder+"/spirit-log").st_mtime
		os.system("./spirit-output")
		while 0 < 1:
			while os.stat(folder+"/spirit-log").st_mtime != time1:
				list = []
				file = open(folder+"/spirit-log", 'r')
				lettura = file.readlines()
				for riga in lettura:
					list.append(riga)
					while gtk.events_pending() == 1:
						gtk.main_iteration()
					time.sleep(0.1)
				last = list[-1]
				if last[:4] == "INFO":
					if label2.get_text() != last:
						label2.set_text(last)
						while gtk.events_pending() == 1:
							gtk.main_iteration()
							print last
				if last[:5] == "ERROR":
					if label2.get_text() != last:
						label2.set_text(last)
						print last
def on_help_clicked(widget, data=None):
	helpdialog1.show()
	return True
def on_info_clicked(widget, data=None):
	aboutdialog1.show()
	return True
def do_response(dialog, response):
    if response == gtk.RESPONSE_DELETE_EVENT or response == gtk.RESPONSE_CANCEL or response == gtk.RESPONSE_OK:
        dialog.hide()
segnali = {
			'on_button1_clicked': on_button1_clicked,
			'on_info_clicked': on_info_clicked,
			'on_help_clicked': on_help_clicked
}
gladeFile = gtk.glade.XML('ui.glade')
gladeFile.signal_autoconnect(segnali)
window1 = gladeFile.get_widget('window1')
label2 = gladeFile.get_widget('label2')
button1 = gladeFile.get_widget('button1')
aboutdialog1 = gladeFile.get_widget('aboutdialog1')
helpdialog1 = gladeFile.get_widget('helpdialog1')
window1.connect("destroy", exit)
aboutdialog1.connect('delete-event', lambda w, e: w.hide() or True)
aboutdialog1.connect('response', do_response)
helpdialog1.connect('delete-event', lambda w, e: w.hide() or True)
helpdialog1.connect('response', do_response)
label2.set_markup("Please connect device and click on <b>Jailbreak!</b>\nA log file will be created on <b>"+folder+"</b>")
window1.show()
gtk.main()
