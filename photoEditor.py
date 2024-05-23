import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageEnhance, ImageFilter, WebPImagePlugin, ImageTk
import os

path = './imgs'
pathOut = '/editedImgs'

# def submit():
#     imagename = entry.get()
#     return imagename


# class imgName:
#     def __init__(self, image, name) -> None:
#         self.image = image
#         self.name = name
#         pass

#     submit = Button(window,text="Submit",command=submit)
#     window = Tk()
#     window.geometry("750x450")
#     entry = Entry()
#     entry.config(font=('Name',50))
#     entry.pack()
#     entry.insert(0,"Name Image")
#     window.mainloop()

# window = Tk()
# window.geometry("750x450")
# entry = Entry()
# entry.config(font=('Name',50))
# entry.pack()
# window.mainloop()


# for filename in os.listdir(path):
#     img = Image.open(f"{path}/{filename}")
    
#     edit = img.filter(ImageFilter.SHARPEN).convert("RGB")

#     # clean_name = os.path.splitext(filename)[0]

#     window = Tk()
   
#     def new_name():
#         newName = entry.get()
#         return newName
    
#     def nextImg():
#         window.quit

#     submit = Button(window,text="Submit",command=lambda: [new_name(),nextImg()])
#     submit.pack(side = RIGHT)


#     window.geometry("750x450")
#     entry = Entry()
#     entry.config(font=('Name',50))
#     entry.pack()
#     entry.insert(0,"Name Image")
#     window.mainloop()
 

#    # clean_name = input(submit)


#     imgName = submit(new_name(return))

#     edit.save(f'.{pathOut}/{new_name}_edited.jpg')

window = tk.Tk()

# class imgWindow:            

#         def __init__(self, window):
#             self.window = window
#             self.user_input = ""
#             self.entry = tk.Entry(window)
#             self.entry.pack()
#             #self.selected = ""

#            # self.button = tk.Button(window, text="Submit", command=lambda: [self.new_name, window.quit])
#             self.button = tk.Button(window, text="Submit", command=self.new_name)
#             self.button.pack(pady=10)

#             self.button = tk.Button(window, text="Quit", command=window.quit)
#             self.button.pack(pady=100)

#             self.canvas = tk.Canvas(window)
#             self.canvas.pack(pady=10)

#             image = Image.open(f"{path}/{self.selected}")
#             #image = image.resize((400, 400))  # Resize the image to fit the canvas
#             self.photo = ImageTk.PhotoImage(image)
#             self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)


           

#             self.count = 0
#             self.total = len(os.listdir(path))

#             print("The current count",self.count)
#             print("Total amount of images",self.total)
          


#             #print(int(os.listdir(path)))     
           

#         def new_name(self):
#             if self.count <= self.total:
#                 self.user_input = self.entry.get()
#                 self.nameImage()
#                 print("current amount just before button",self.count)
#                 self.count +=1
#                 print("current amount just after button",self.count)
                
#             print(self.count)

#             if self.count == self.total:
#                 self.window.quit()
           
                

        
            
#         # def nameImage(self):
                        
#         #     img = Image.open(f"{path}/{self.selected}")
#         #     edit = img.filter(ImageFilter.SHARPEN).convert("RGB")
#         #     edit.save(f'.{pathOut}/{self.user_input}_edited.jpg')
            

class ImageCovertor:
    def __init__(self,window):
        self.window = window
        self.quit  = window
        self.count = 0
        self.entry = tk.Entry(window)
        self.entry.pack(pady=20)
       # self.entry.config = (0,"Enter Name")
        self.entry.config(font=('Name',50))
        self.entry.insert(0,"Name Image")
   

        self.button = tk.Button(window, text="Submit", command=self.changeName)
        self.button.pack(pady=0)

        self.button = tk.Button(window, text="Quit", command=self.close)
        self.button.pack(pady=0)

        self.button = tk.Button(window, text="Convert all with no name changes", command=self.convertAllNoNameChange)
        self.button.pack(pady=0)

        self.canvas = tk.Canvas(window, width=400, height=400)
        self.canvas.pack(pady=10)

        self.next_button = tk.Button(window, text="Next Image", command=self.show_next_image)
        self.next_button.pack(pady=0)

        self.next_button = tk.Button(window, text="Previous Image", command=self.show_previous_image)
        self.next_button.pack(pady=0)

                
        folder_path = path
        try: # displays the first image on screen and checks for images
            self.image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('webp','.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
                       
            if not self.image_paths:
                #self.result_label.config(text="No images found in the folder.")
                return
            
            image_path = self.image_paths[self.count]
            image = Image.open(image_path)
            image = image.resize((400, 400))  # Resize the image to fit the canvas
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        except Exception as e:
            print("oops")
    
    def show_next_image(self): #Displays the image in the window            
        print(self.count)  
        if self.count >= 0:
            self.count += 1

        if self.count >= len(self.image_paths):
            self.count = 0
        
        print(self.count) 


        image_path = self.image_paths[self.count]   
        try:
            image = Image.open(image_path)
            image = image.resize((400, 400))  # Resize the image to fit the canvas
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

           # self.result_label.config(text=f"Displaying image {self.count + 1} of {len(self.image_paths)}")
           # self.count += 1
        except Exception as e:
            print("oops daisy")
        #    messagebox.showerror("Error", f"An error occurred while loading the image: {e}")

    def show_previous_image(self): #changes to previous image
        print(self.count)  
        if self.count >= 0:
            self.count += -1

        if self.count < 0:
            self.count = len(self.image_paths)-1
        
        print(self.count) 


        image_path = self.image_paths[self.count]   
        try:
            image = Image.open(image_path)
            image = image.resize((400, 400))  # Resize the image to fit the canvas
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

           # self.result_label.config(text=f"Displaying image {self.count + 1} of {len(self.image_paths)}")
           # self.count += 1
        except Exception as e:
            print("oops daisy")
        #    messagebox.showerror("Error", f"An error occurred while loading the image: {e}")      

    def close(self):
        response=messagebox.askyesno('Exit','Are you sure you want to exit?')
        if response:
            self.window.destroy()
            
            
    def complete(self):
        response=messagebox.askyesno('Exit','Converted images saved too' " " + "\n "+ str(pathOut) + " "+ "\nDo you want to quit?") 
        if response:
            self.window.destroy()     

   
    
    def changeName(self):  # changes the name of the image before converting
        newName=self.entry.get()
        print(newName)
        print(self.count)
        image_path = self.image_paths[self.count]
        img = Image.open(image_path)
        edit = img.filter(ImageFilter.SHARPEN).convert("RGB")
        edit.save(f'.{pathOut}/{newName}.jpg')
        self.entry.insert = "Enter Name"
        self.show_next_image()


    def convertAllNoNameChange(self):
        AllCount = 0
        for filename in os.listdir(path):
            
            print(filename)
            image_path = self.image_paths[AllCount]
            clean_name = os.path.splitext(filename)
            img = Image.open(image_path)
            edit = img.filter(ImageFilter.SHARPEN).convert("RGB")
            edit.save(f'.{pathOut}/{clean_name}.jpg')
            print(f'.{pathOut}/{clean_name}.jpg') 
            #doesnt work without the .jpg for some reason
            AllCount += 1
        
        self.complete()

        
        
# for filename in os.listdir(path):
#     img = Image.open(f"{path}/{filename}")
    
#     edit = img.filter(ImageFilter.SHARPEN).convert("RGB")

#      clean_name = os.path.splitext(filename)[0]

#     window = Tk()
   
#     def new_name():
#         newName = entry.get()
#         return newName
    
#     def nextImg():
#         window.quit

#     submit = Button(window,text="Submit",command=lambda: [new_name(),nextImg()])
#     submit.pack(side = RIGHT)


#     window.geometry("750x450")
#     entry = Entry()
#     entry.config(font=('Name',50))
#     entry.pack()
#     entry.insert(0,"Name Image")
#     window.mainloop()
 

#    # clean_name = input(submit)


#     imgName = submit(new_name(return))

#     edit.save(f'.{pathOut}/{new_name}_edited.jpg')

    


    


#     def clicked(self):
#         self.entry.configure(state="normal")
#         self.entry.delete(0, tk.END)
#         self.entry.unbind('<Button-1', self.clicked)
    

    


window.title("AI Webmp to Jpg Convertor")
window.geometry("750x750")

app = ImageCovertor(window)


window.mainloop()

