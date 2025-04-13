#give creadit if u are creating new version or using code ,,, github:- github.com/nixxcom , ig:- @o978x
import subprocess
import sys
import platform
from tkinter import Tk, Label, Button, filedialog, messagebox, Frame
from PIL import Image, ImageTk
import os


def req():
    os_type = platform.system().lower()
    try:
        import pip
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "ensurepip"])
    if os_type == 'windows' or os_type == 'linux':
        print(f"Detected {os_type.capitalize()} OS. Installing requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    else:
        print(f"Unsupported OS: {os_type}. Please install Pillow .")
        sys.exit(1)


req()


def tp(input_image):

    directory = os.path.dirname(os.path.abspath(__file__))

    file_name = os.path.basename(input_image)

    output_image_path = os.path.join(directory, f"{os.path.splitext(file_name)[0]}_transparent.png")

    image = Image.open(input_image).convert("RGBA")
    width, height = image.size

    transparent_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))  

    transparent_image.save(output_image_path)

    return output_image_path


def select_file():
    file_path = filedialog.askopenfilename(

        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")]
    )
    if file_path:
        try:
            output_path = tp(file_path)
            messagebox.showinfo("Success", f"Invisible image saved at:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image:\n{str(e)}")



app = Tk()

app.title("Transparent Image Creator")


app.geometry("600x500")

app.configure(bg="#000000")


logo_frame = Frame(app, width=600, height=200, bg="#000000")
logo_frame.pack_propagate(False)
logo_frame.pack(fill='x', side='top')

try:
    logo_image = Image.open("xx.png")

    
    max_logo_width = 600 - 2 * 30   
    max_logo_height = 200 - 2 * 25 

   
    logo_image.thumbnail((max_logo_width, max_logo_height), Image.LANCZOS)


    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_inner_frame = Frame(logo_frame, bg="#000000")
    logo_inner_frame.pack(padx=30, pady=25)

    logo_label = Label(logo_inner_frame, image=logo_photo, bg="#4CAF50")
    logo_label.pack()
except Exception as e:
    print("Logo image could not be loaded:", e)



Label(
    app,
    text="Select an image.(github:- github.com/nixxcop)",
    font=("Helvetica", 17),
    bg="#000000",
    fg="#4CAF50",
    justify="center",
    pady=7

).pack()

def on_hover(e): styled_button.config(bg="#45a049")


def on_leave(e): styled_button.config(bg="#4CAF50")

styled_button = Button(
    app,
    text="Select Image",
    command=select_file,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 12, "bold"),
    padx=20,
    pady=10,
    bd=0,
    relief="flat",
    highlightthickness=0,
    cursor="hand2"
)
styled_button.configure(width=15, height=2)

styled_button.bind("<Enter>", on_hover)


styled_button.bind("<Leave>", on_leave)

styled_button.pack(pady=30)


app.mainloop()
