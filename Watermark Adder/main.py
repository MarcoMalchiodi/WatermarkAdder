from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

watermark = Image.open('watermark.png')
my_watermark = watermark.resize((50,50))

window = Tk()
window.title('Watermark Adder')
window.geometry("400x300")
window.config(padx=20,pady=20) #padding can also be applied to rows and columns

my_font=('times', 18, 'bold')
my_label = Label(text='Upload Your File Here', font=my_font)
my_label.grid(column=1,row=1)

def download_file():
    # Ask the user to specify the save location and filename
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])

    if file_path:
        # Save the image to the selected location
        image_with_watermark.save(file_path)

def button_clicked():
    global img
    global image_with_watermark
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((600,300)) # new width & height
    
    # Create a copy of the uploaded image to avoid modifying the original
    image_with_watermark = img_resized.copy()
    
    # Calculate the position to place the watermark (e.g., bottom right corner)
    watermark_width, watermark_height = my_watermark.size
    image_width, image_height = img_resized.size
    position = (image_width - watermark_width, image_height - watermark_height)
    
    # Paste the watermark onto the image
    image_with_watermark.paste(my_watermark, position, my_watermark)
    
    img = ImageTk.PhotoImage(image_with_watermark)
    b2 = Button(image=img)
    b2.image = img  # Keep a reference to prevent garbage collection
    b2.grid(row=3, column=1)
    
    download_button = Button(text='Download Image', command=download_file)
    download_button.grid(row=4,column=1)

upload_button = Button(text='Upload File', command=button_clicked, width=16)
upload_button.grid(row=2,column=1)







window.mainloop()