import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import sorting

class Gui(Gtk.Window):
    def __init__(self):
        global spinner, progress_bar
        Gtk.Window.__init__(self, title="SortMaster")
        self.set_border_width(2)
        self.connect("destroy", Gtk.main_quit)

        # Create a grid to organize the form
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(5)
        self.add(grid)

        # Create labels and input fields for target directory, destination directory, and pattern string
        target_label = Gtk.Label(label="Target Directory:")
        destination_label = Gtk.Label(label="Destination Folder:")
        pattern_label = Gtk.Label(label="Pattern String:")

        self.target_entry = Gtk.Entry()
        self.target_entry.set_placeholder_text("eg. /home/test/")
        self.destination_entry = Gtk.Entry()
        self.destination_entry.set_placeholder_text("Enter Destination folder")
        self.pattern_entry = Gtk.Entry()
        self.pattern_entry.set_placeholder_text("Enter Pattern")

        # Create a submit button
        submit_button = Gtk.Button(label="Sort")
        submit_button.connect("clicked", self.on_submit_button_clicked)
        quit_btn = Gtk.Button(label="Quit")
        quit_btn.connect("clicked", self.on_quit_click)

        spinner = Gtk.Spinner()
        progress_bar = Gtk.ProgressBar()
        # Attach widgets to the grid
        grid.attach(target_label, 0, 0, 1, 1)
        grid.attach(self.target_entry, 1, 0, 1, 1)
        grid.attach(destination_label, 0, 1, 1, 1)
        grid.attach(self.destination_entry, 1, 1, 1, 1)
        grid.attach(pattern_label, 0, 2, 1, 1)
        grid.attach(self.pattern_entry, 1, 2, 1, 1)
        grid.attach(submit_button, 0, 3, 2, 1)
        grid.attach(spinner, 2, 3, 1, 1)
        grid.attach(progress_bar, 0, 4, 2, 1)


    def on_quit_click(self, widget):
         self.close()

    def on_submit_button_clicked(self, widget):
        # Retrieve user input
        target_directory = self.target_entry.get_text()
        destination_directory = self.destination_entry.get_text()
        pattern_string = self.pattern_entry.get_text()
        spinner.start()
        sorting.move_files_with_pattern(target_directory, destination_directory, pattern_string)
    
        

def update_progress(value, file_size):
    progress = value / file_size  # declaring size of list as steps in the processing
    progress_bar.set_fraction(progress)     

    


def stop_spinner():
        spinner.stop()
    
def progress_animation(step:float, total_steps:int):
        Gtk.main_iteration_do(False)
        GLib.idle_add(update_progress, step+1, total_steps)
        GLib.usleep(10000) 

   

        