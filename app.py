import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk

def resize_image(img, percentage):
    
    width, height = img.size
    new_width = int(width * (percentage / 100))
    new_height = int(height * (percentage / 100))
    return img.resize((new_width, new_height), Image.Resampling.LANCZOS)

def handle_drop(event):
    
    file_path = event.data.strip()
    input_path.set(file_path)
    show_image(file_path)

def select_file():
    
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
    )
    if file_path:
        input_path.set(file_path)
        show_image(file_path)

def show_image(file_path):
    
    try:
        img = Image.open(file_path)
        img.thumbnail((200, 200))  
        tk_img = ImageTk.PhotoImage(img)
        preview_label.config(image=tk_img)
        preview_label.image = tk_img
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

def compress_image():
 
    try:
        percentage = int(size_var.get())
        img = Image.open(input_path.get())
        resized_img = resize_image(img, percentage)

      
        if resized_img.mode == "RGBA":
            resized_img = resized_img.convert("RGB")
        
        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if save_path:
            resized_img.save(save_path, "JPEG", quality=85)
            messagebox.showinfo("Success", "Image compressed successfully!")
            app.destroy()  
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



app = TkinterDnD.Tk()
app.title("Image Compressor with Drag and Drop")
app.geometry("400x400")

input_path = tk.StringVar()
size_var = tk.IntVar(value=100)

tk.Label(app, text="Drag and drop an image or select one:").pack(pady=10)
tk.Entry(app, textvariable=input_path, width=40).pack(pady=5)
tk.Button(app, text="Browse", command=select_file).pack(pady=5)


preview_label = tk.Label(app, text="No image selected", width=30, height=15, bg="gray")
preview_label.pack(pady=10)


tk.Label(app, text="Reduce size by percentage:").pack(pady=10)
tk.Scale(app, from_=10, to=100, orient="horizontal", variable=size_var).pack(pady=5)


tk.Button(app, text="Compress", command=compress_image).pack(pady=10)


app.drop_target_register(DND_FILES)
app.dnd_bind('<<Drop>>', handle_drop)

app.mainloop()
