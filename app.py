import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")
        self.main_screen()

    def main_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main screen widgets
        label = tk.Label(self.root, text="What would you like to do?", font=("Arial", 16))
        label.pack(pady=20)

        compress_button = tk.Button(self.root, text="Compress Image", font=("Arial", 12), command=self.compression_screen)
        compress_button.pack(pady=10)

        convert_button = tk.Button(self.root, text="Convert Image Format", font=("Arial", 12), command=self.conversion_screen)
        convert_button.pack(pady=10)

    def compression_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Compression screen widgets
        label = tk.Label(self.root, text="Compress Image", font=("Arial", 16))
        label.pack(pady=20)

        upload_button = tk.Button(self.root, text="Upload Image", font=("Arial", 12), command=self.upload_image_compress)
        upload_button.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), command=self.main_screen)
        back_button.pack(pady=20)

    def conversion_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Conversion screen widgets
        label = tk.Label(self.root, text="Convert Image Format", font=("Arial", 16))
        label.pack(pady=20)

        upload_button = tk.Button(self.root, text="Upload Image", font=("Arial", 12), command=self.upload_image_convert)
        upload_button.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), command=self.main_screen)
        back_button.pack(pady=20)

    def upload_image_compress(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            compress_percentage = tk.simpledialog.askinteger("Compression", "Enter compression percentage (10-90):", minvalue=10, maxvalue=90)
            if compress_percentage:
                try:
                    self.compress_image(file_path, compress_percentage)
                    messagebox.showinfo("Success", "Image successfully compressed!")
                except Exception as e:
                    messagebox.showerror("Error", f"Compression failed: {e}")

    def upload_image_convert(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            target_format = tk.simpledialog.askstring("Convert Format", "Enter target format (png, jpeg, bmp):")
            if target_format:
                try:
                    self.convert_image_format(file_path, target_format)
                    messagebox.showinfo("Success", f"Image successfully converted to {target_format} format!")
                except Exception as e:
                    messagebox.showerror("Error", f"Conversion failed: {e}")

    def compress_image(self, file_path, compress_percentage):
        # Open the image and compress it
        image = Image.open(file_path)
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg")])
        if output_path:
            quality = 100 - compress_percentage
            image.save(output_path, quality=quality, optimize=True)

    def convert_image_format(self, file_path, target_format):
        # Open the image and convert its format
        image = Image.open(file_path)
        output_path = filedialog.asksaveasfilename(defaultextension=f".{target_format}", filetypes=[(target_format.upper(), f"*.{target_format}")])
        if output_path:
            image.save(output_path, format=target_format.upper())

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
