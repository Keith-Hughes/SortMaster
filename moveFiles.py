import gi
import shutil
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
class MoveFiles(Gtk.Window):
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

    def on_submit_button_clicked(self, widget):
        # Retrieve user input
        target_directory = self.target_entry.get_text()
        destination_directory = self.destination_entry.get_text()
        pattern_string = self.pattern_entry.get_text()
        spinner.start()
        move_files_with_pattern(target_directory, destination_directory, pattern_string)
    
        

        

def update_progress(progress_bar, value):
        progress = value / size  # declaring size of list as steps in the processing
        progress_bar.set_fraction(progress)

def move_files_with_pattern(src_folder, dest_folder, pattern):
        global size
        # Create the destination folder if it doesn't exist
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        list_of_files = os.listdir(src_folder)
            
        size = len(list_of_files)
        # Iterate over files in the source folder    
        for index in range(size):
            src_filepath = os.path.join(src_folder, list_of_files[index])
                
                # Check if the file name contains "S02"
            if pattern in list_of_files[index]:
                dest_filepath = os.path.join(dest_folder, list_of_files[index])

                    # Move the file to the destination folder
                shutil.move(src_filepath, dest_filepath)
                print(f"Moved: {list_of_files[index]} to {dest_folder}")
            Gtk.main_iteration_do(False)
            GLib.idle_add(update_progress, progress_bar, index+1)
            GLib.usleep(10000) 
        spinner.stop()

if __name__ == "__main__":
    win = MoveFiles()
    win.show_all()
    Gtk.main()




