import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def show_image():
    """
    Displays the image in the label when the button is clicked.
    """
    img_label.config(image=photo)
    img_label.image = photo
    print("Image displayed successfully!")

# Create the main window
root = tk.Tk()
root.title("Favorite Video Answer")

# Create a label with a question
question_label = ttk.Label(root, text="What is your favorite movie?", font=("Arial", 16))
question_label.pack(pady=10)

# Create a button that calls the show_image function when clicked
answer_button = ttk.Button(root, text="Show Answer", command=show_image)
answer_button.pack(pady=10)

# Create an empty label for displaying the image later
img_label = ttk.Label(root)
img_label.pack(pady=10)

# Load the image using Pillow
try:
    image_path = "answer.png"  # Ensure the path is correct
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    print(f"Image loaded successfully from {image_path}")
except Exception as e:
    print(f"Failed to load image: {e}")

# Start the main loop of tkinter
root.mainloop()