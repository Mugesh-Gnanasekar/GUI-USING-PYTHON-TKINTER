from Tkinter import *

#Creating Different Fonts as Global names and we can specify which want we want ot use to display the text in widgets
LARGE_FONT= ("Verdana", 16)
NORMAL_FONT= ("Verdana", 12)
SMALL_FONT= ("Verdana", 8)

class Root_Window(Tk):
    def __init__(self,*args,**kwargs):                               #Initialization function
        Tk.__init__(self,*args,**kwargs)                             #Calling initialization function of Tk() class
                                                                     # which creates the root window

        self.geometry("1280x720")                                    #Setting the geometry of the root window
        self.title("MY FIRST GUI")                                   #Setting the title of the root window

       #Creating the Top container where we can stack the other frames that we want to create
        Top_container=Frame(self)                                    #creating object of 'Frame' class
        Top_container.pack(side="top", fill="both", expand=True)     #Packing the Top container all over the root window
        Top_container.grid_rowconfigure(0,weight=1)                  #Here we are making the rows and columns to expand
        Top_container.grid_columnconfigure(0,weight=1)               #when the window size is resized

       #Creating a Menubar for our GUI
        menubar = Menu(self)
        self.config(menu=menubar)                                    #Displaying the Menubar

        fileMenu =Menu(menubar, tearoff = False)                     #Creating a 'File' Menu with four options
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label='New')
        fileMenu.add_command(label='Open')
        fileMenu.add_command(label='Save')
        fileMenu.add_command(label='Exit', command = quit)


        self.frames = {}

        for F in (Start_Page,Page_One,Page_Two):

            frame = F(Top_container,self)                           #Objects for each frame class created with Top
                                                                    # container as first parent object and also passing
                                                                    # object of Root_window class so that all other frame
                                                                    # classes can access the functions defined here using
                                                                    # that object

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(Start_Page)                             #Bring the Start Page initially

    #Method to pull different frames to the top
    def show_frame(self,cont):
         frame=self.frames[cont]
         frame.tkraise()

class Start_Page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        label =Label(self, text="WELCOME TO MY GUI",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Radio_button_1 = Radiobutton(self,text="GO TO PAGE ONE",command=lambda: controller.show_frame(Page_One))
        Radio_button_1.pack()

        Radio_button_2 = Radiobutton(self,text=" GO TO PAGE TWO",command=lambda: controller.show_frame(Page_Two))
        Radio_button_2.pack()

class Page_One(Frame):

    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        self.label = Label(self, text="YOU HAVE COME TO PAGE ONE",font=LARGE_FONT)
        self.label.pack()

        self.button = Button(self,text="Back to Home",command=lambda: controller.show_frame(Start_Page))
        self.button.pack(side = "bottom")

class Page_Two(Frame):

    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        self.label = Label(self, text="YOU HAVE COME TO PAGE_TWO",font=LARGE_FONT)
        self.label.pack()

        self.button = Button(self,text="Back to Home",command=lambda: controller.show_frame(Start_Page))
        self.button.pack(side = "bottom")



app= Root_Window()
app.mainloop()
