from utils import makePrediction
import re
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class MainWindow(Gtk.Window):
    """
    Class for the main window of the GUI. Uses the file glade_file.glade to build the UI.
    """
    encryptedFilePath = ""
    decryptedFilePath = ""

    def __init__(self):
        """
        Create all the GUI elements from the glade file on initialization.
        """
        self.gladeFile = "res/glade_file.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladeFile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.window.set_size_request(550, 500)
        self.window.connect("destroy", Gtk.main_quit)
        self.header = Gtk.HeaderBar()
        self.header.props.title = "Integrated Approach for Cryptology using Deep Neural Network"
        self.header.set_show_close_button(True)
        self.decryptButton = self.builder.get_object("decrypt")
        self.decryptButton.connect("clicked", self.decrypt)
        self.encryptedText = self.builder.get_object("encrypted_text")
        self.encryptedTextBuffer = self.encryptedText.get_buffer()
        self.decryptedText = self.builder.get_object("decrypted_text")
        self.decryptedTextBuffer = self.decryptedText.get_buffer()
        self.window.set_titlebar(self.header)
        self.window.show_all()

    def decrypt(self, widget):
        """
        Called on clicking the "Decrypt" button. Performs decryption of the encrypted text.
        Displays the output to the decrypted text window and if a text file is selected,
        stores the data to the text file.
        """
        if self.encryptedTextBuffer == "":
            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "ERROR")
            dialog.format_secondary_text("Please write the encrypted data to decrypt or select file!")
            dialog.run()
            dialog.destroy()
        else:
            start_iter = self.encryptedTextBuffer.get_start_iter()
            end_iter = self.encryptedTextBuffer.get_end_iter()
            text = self.encryptedTextBuffer.get_text(start_iter, end_iter, True)
            tokens = text.split('\n')
            output = makePrediction(tokens[:-1])
            self.decryptedTextBuffer.set_text(output)
            if self.decryptedFilePath != "":
                with open(self.decryptedFilePath,"w") as f:
                    f.write(output)




    def encryptedFileSelect(self, widget):
        """
        Called on selecting the encrypted file to decrypt. Reads the file and displays the
        text to the encrypted text window.
        :param widget: The current widget object
        """
        self.encryptedFilePath = widget.get_filename()
        if not re.search('.txt$', self.encryptedFilePath):    #Check to ensure that the input file is of type .txt
            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "ERROR")
            dialog.format_secondary_text("Please select a \"Text\" file!")
            dialog.run()
            dialog.destroy()
            self.encryptedFilePath = ""
            widget.set_filename("None")
        else:
            with open(self.encryptedFilePath) as file:
                data = file.read()
                self.encryptedTextBuffer.set_text(data)

    def decryptedFileSelect(self, widget):
        """
        Called on selecting the file to decrypt to. Stores the path of the file.
        :param widget: The current widget object
        """
        self.decryptedFilePath = widget.get_filename()
        if not re.search('.txt$', self.decryptedFilePath):  #Ensure that the selected file is a text file.
            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "ERROR")
            dialog.format_secondary_text("Please select a \"Text\" file!")
            dialog.run()
            dialog.destroy()
            self.decryptedFilePath = ""
            widget.set_filename("None")
        elif not os.stat(self.decryptedFilePath).st_size == 0:  #Handle case when selected file is not empty.
            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, "WARNING")
            dialog.format_secondary_text("The file where the decrypted data is to be written is not empty."
                                         "\nAre you sure you want to continue?")
            response = dialog.run()
            if response == Gtk.ResponseType.NO:
                dialog1 = Gtk.FileChooserDialog("Please choose a new file", None,
                                                Gtk.FileChooserAction.OPEN, (Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

                response1 = dialog1.run()
                if response1 == Gtk.ResponseType.OK:
                    self.decryptedFilePath = dialog1.get_filename()
                    self.decrypted_file_file_set_cb(self, widget)
                dialog1.destroy()
            dialog.destroy()


window = MainWindow()
Gtk.main()
