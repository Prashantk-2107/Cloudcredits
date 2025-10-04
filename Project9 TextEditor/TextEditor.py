import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

class TextEditor:
    def __init__(self, root):
        self.root = root #Define Root of the program   
        self.root.title("Text Editor") #Define name of The Editor
        self.root.geometry("800x600") #Default oprning size

        # Current open file path
        self.file_path = None #Currently opened path

        # Create text area
        self.text_area = ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Create menu bar
        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.exit_editor)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

        # Bind keyboard shortcuts
        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-q>", lambda event: self.exit_editor())

    def new_file(self):
        if self.confirm_unsaved_changes():
            self.text_area.delete(1.0, tk.END)
            self.file_path = None
            self.root.title("Untitled - Text Editor 📝")

    def open_file(self):
        if self.confirm_unsaved_changes():
            file_path = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
                    self.file_path = file_path
                    self.root.title(f"{file_path} - Text Editor 📝")
                except Exception as e:
                    messagebox.showerror("Error", f"Could not open file:\n{e}")

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, "w", encoding="utf-8") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
                messagebox.showinfo("Success", "File saved successfully ✅")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
                self.file_path = file_path
                self.root.title(f"{file_path} - Text Editor 📝")
                messagebox.showinfo("Success", "File saved successfully ✅")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")

    def exit_editor(self):
        if self.confirm_unsaved_changes():
            self.root.quit()

    def confirm_unsaved_changes(self):
        if self.text_area.edit_modified():
            answer = messagebox.askyesnocancel("Unsaved Changes", "Do you want to save changes before exiting?")
            if answer:  # Yes
                self.save_file()
                return True
            elif answer is None:  # Cancel
                return False
        return True

    def show_about(self):
        messagebox.showinfo("About", "Simple Text Editor\nCreated using Python Tkinter.\n\nHave a Nice Day")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
