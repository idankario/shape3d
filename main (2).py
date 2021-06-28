# This program create ship and give the option to move it on screen
""""**********************************************
    *  Student 1 :  Shani Levi     ID: 302853619
    *  Student 2 :  Idan Kario     ID: 300853751
    *  Student 3 :  Mhmd atamny    ID: 207887720

**********************************************"""

# Import Libraries
from tkinter import Tk, Canvas, Frame, Label, OptionMenu, Button, StringVar, IntVar
from tkinter import Tk, Canvas, messagebox, Frame, Label,Entry, OptionMenu, Button, StringVar, IntVar
from tkinter_custom_button import TkinterCustomButton
from tkinter import colorchooser
from PIL import Image, ImageTk
from collections import namedtuple
from math import sin, cos, radians
from tkinter import filedialog #for open file
import math
import threading 
from multiprocessing import Process
import json
#Pixel
pixel = namedtuple("pixel", ['x1','y1'])
option_figure = ['Line', 'Circle', 'Cerve']
option_curve = [10, 50, 100, 1000]

class DrowingApp:
    data={} 
    fileOpend=""
    def __init__(self, master,WIDTH=1100, HEIGHT=800):
        master.title("GUI HW2 By Shani & Idan & mhmd ")
        self.init_Val()
        self.create_canvas(master, WIDTH, HEIGHT)
        master.attributes("-transparentcolor", "red")
        self.create_upper_menu()
        # lower section
        self.lower_frame = Canvas(self.master, bg='#c9daf8', bd=5)
        self.lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
        self.lower_frame.bind("<ButtonPress-1>", self.clickMove)
        self.reset()
        self.lower_frame.bind("<Button 1>", self.left_click)
        self.lower_frame.bind("<ButtonRelease 1>", self.left_click_release)
 
      
    def updateValueToCurrectForm(self , maxX,maxY) :    
        for  p in points :
            x = p[0]
            y = p[1]
            x= maxX  (x > maxX) 
            y= maxY  (x > maxY) 
            x= 0 (x < 0)
            y= 0 (x < 0) 
        middle.x = (range.maxX + range.minX) / 2
        middle.y = (range.maxY + range.minY) / 2
    
#################### Create Ship ###################### 
    def createShip(self,lines,circels,bezier):
        thread_list = []
        for  line in lines:
            thread=threading.Thread(target=self.myLine, args=(line[0],line[1],line[2],line[3]))
            thread_list.append(thread) 
        for  circle in circels:
            thread=threading.Thread(target=self.myCircle, args=(circle[0],circle[1],circle[2],circle[3]))
            thread_list.append(thread) 
        thread=threading.Thread(target=self.myCurve, args=(bezier[0],bezier[1],bezier[2],bezier[3],bezier[4],bezier[5],bezier[6],bezier[7]))
        thread_list.append(thread) 

        for thread in thread_list:
            thread.start()

    def create_upper_menu(self):
        # Uper section 1
        frame = Frame(self.master, bg='#a0dbd1', bd=4)
        frame.place(relx=0.5, rely=0.04, relwidth=0.50, relheight=0.1, anchor='n')
        # Set curve and figure variable and trace changes
        openfile = TkinterCustomButton(master=frame, height=52, text="Open File", command=self.openfile)
        openfile.place(relx=0)

        derivative = TkinterCustomButton(master=frame, height=52, text="cutting",command=self.derived)
        derivative.place(relx=0.25)

        reset = TkinterCustomButton(master=frame, height=52, text="Reset", command=self.reset)
        reset.place(relx=0.50)

        reset = TkinterCustomButton(master=frame, height=52, text="Help", command=self.help)
        reset.place(relx=0.75)

        # Uper section 2
        self.frame2 = Frame(self.master, bg='#a0dbd1', bd=4)
        self.frame2.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.1, anchor='n')
        move = TkinterCustomButton(master=self.frame2, height=52, text="Move", command=self.move)
        move.place(relx=0.05)
        zoomIn = TkinterCustomButton(master=self.frame2, height=52, text="zoomIn +", command=self.zoomIn)
        zoomIn.place(relx=0.20)
        zoomOut = TkinterCustomButton(master=self.frame2, height=52, text="zoomOut -", command=self.zoomOut)
        zoomOut.place(relx=0.35)
        MirorX = TkinterCustomButton(master=self.frame2, height=52, text="Rotat to X", command=self.rotate_X)
        MirorX.place(relx=0.50)
        MirorY = TkinterCustomButton(master=self.frame2, height=52, text="Miror to Y", command=self.reset)
        MirorY.place(relx=0.65)
        button1 = TkinterCustomButton(master=self.frame2, height=52, text="routat input",  command=self.setAmountRotation)
        button1.place(relx=0.80)

        labal1 = Label(text='Amount of Rotatio:')
        labal1.place(relx=0.80, rely=0.05)
        self.entty1 = Entry(width=15)
        self.entty1.place(relx=0.90, rely=0.05)

        labal2 = Label(text='Amount of 2:')
        labal2.place(relx=0.80, rely=0.1)
        entty2 = Entry(width=15)
        entty2.place(relx=0.90, rely=0.1)

    def setAmountRotation(self):
        try:
            if self.entty1.get()=='':
                messagebox.showinfo("empty", "plese set rotate angle")
                return
            if int(self.entty1.get()) :
                messagebox.showinfo("ok", "rotate ok")
        except ValueError:
            messagebox.showinfo("not ok", "only a number betwen 1 to 9")

    def openfile(self):
        tf = filedialog. askopenfilename(initialdir="../Path/For/JSON_file",
                           filetypes=((".json", "*.json"), ("All Files", "*.*")),
                           title="Choose a file.")
        try:
            if tf:
                with open(tf) as f:
                    self.data = json.load(f)
                    self.fileOpend = f          
                self.createShip( self.data['lines'],self.data['circles'],self.data['bezier'])

                # tf.close()
            elif tf=='':
                messagebox.showinfo("cencel", "file not selcted")
        except IOError:
            messagebox.showinfo("Error", "erorr")

    def help(self):
        with open('help.txt', 'r') as help_file:
            # help_file.read()
            messagebox.showinfo('help', help_file.read())

    #drag ship with click on bord
    def left_click(self, event):
        self.x_start = event.x
        self.y_start = event.y
    def left_click_release(self, event):
        self.x_end = event.x
        self.y_end = event.y
        self.canvas.delete('all')
        self.dragShip()
    def dragShip(self):
        x = self.x_end - self.x_start
        y = self.y_end - self.y_start

        if self.x_start !=-1 and self.x_end !=-1:
            # set to -1
            self.x_start = -1
            self.y_start = -1
            self.x_end = -1
            self.y_end = -1
            # clear
            self.lower_frame.delete("all")

            # # set new ship
            index = 0
            for item in self.data["lines"]:
                x1 = self.data["lines"][index][0] + x
                y1 = self.data["lines"][index][1] + y
                x2 = self.data["lines"][index][2] + x
                y2 = self.data["lines"][index][3] + y
                self.myLine(x1, y1, x2, y2)
                index = index + 1

            index = 0
            for item in self.data["circles"]:
                x1 = self.data["circles"][index][0] + x
                y1 = self.data["circles"][index][1] + y
                x2 = self.data["circles"][index][2] + x
                y2 = self.data["circles"][index][3] + y
                self.myCircle(x1, y1, x2, y2)
                index = index + 1

            index = 0
            for item in self.data["star"]:
                x1 = self.data["star"][index][0] + x
                y1 = self.data["star"][index][1] + y
                x2 = self.data["star"][index][2] + x
                y2 = self.data["star"][index][3] + y
                self.ceate_star(x1, y1, x2, y2)
                index = index + 1

            index = 0
            for item in self.data["bezier"]:
                x1 = self.data["bezier"][index][0] + x
                y1 = self.data["bezier"][index][1] + y
                x2 = self.data["bezier"][index][2] + x
                y2 = self.data["bezier"][index][3] + y
                self.myCurve(x1, y1, x2, y2)
                index = index + 1
    #end drag logic

    def reset(self):
        if self.fileOpend == "":
            with open('./ship.json') as f:
                self.data = json.load(f)  
        else:    
            with open(self.fileOpend) as f:
                self.lower_frame.delete("all")
                self.data = json.load(f)  
        self.lower_frame.delete("all")
        self.createShip( self.data['lines'],self.data['circles'],self.data['bezier'])

    def init_Val(self):
        self.my_color = "Black"
        # Holds the selected point
        self.x = [0, 0, 0, 0]
        self.y = [0, 0, 0, 0]
        self.x_start = -1
        self.y_start = -1
        self.x_end = -1
        self.y_end = -1
        self.rotationInput=-1

    def create_canvas(self, master, WIDTH, HEIGHT):
        self.master = master
        self.rootgeometry(WIDTH, HEIGHT)
        self.canvas = Canvas(self.master)
        self.canvas.pack()
        self.background_image = Image.open('bg.PNG')
        self.image_copy = self.background_image.copy()
        self.background = ImageTk.PhotoImage(self.background_image)
        self.loadbackground()

    def color_option(self):
        # variable to store hexadecimal code of color
        color = colorchooser.askcolor()[1]
        if color != None:
            self.my_color = color

    def putPixel(self, x_, y_):
        self.lower_frame.create_line(x_, y_, x_ + 1, y_ + 1, fill=self.my_color)

    # Bersenheim
    def myLine(self,x1,y1,x2,y2):
        #Bresenham's Line Algorithm
        # Determine how steep the line is
        direction =abs(y2-y1)> abs(x2-x1)
        # Rotate line
        if direction:
            x1, y1,x2, y2 = y1, x1,  y2, x2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Recalculate differentials
        dx = x2 - x1
        dy = y2 - y1
        # Calculate error
        errp = 2*dx 
        direcx=1 if x2-x1>=0 else -1
        direcy=1 if y2-y1>=0 else -1
        # Iterate over bounding box generating points between start and end
        y,x = round(y1),round(x1)
        steps=int(max(dx,dy))
        for i in range(steps):
            self.putPixel(y,x) if direction else self.putPixel(x,y)
            errp -= 2*abs(dy)
            if errp < 0:
                y += direcy
                errp += 2*abs(dx)
            x+=direcx    

    def plotCiclePoints(self, xc, yc, x, y):
        self.putPixel(xc + x, yc + y)
        self.putPixel(xc - x, yc + y)
        self.putPixel(xc + x, yc - y)
        self.putPixel(xc - x, yc - y)
        self.putPixel(xc + y, yc + x)
        self.putPixel(xc - y, yc + x)
        self.putPixel(xc + y, yc - x)
        self.putPixel(xc - y, yc - x)

    def myCircle(self, xc,yc,x2,y2):
        radius= math.sqrt( (x2 - xc)**2 + (y2 - yc)**2 )
        "Bresenham complete circle algorithm in Python"
        p = 3 - (2 * radius)
        x = 0
        y = radius
        while x < y:
            self.plotCiclePoints(xc,yc,x,y)
            if p < 0:
                p = p + (4 * x) + 6
            else:
                self.plotCiclePoints(xc,yc,x,y)
                p = p + (4 * (x - y)) + 10
                y -=1
            x+=1
        if(x==y):
            self.plotCiclePoints(xc,yc,x,y)

    def bezier(self, x1, x2, x3, x4, t):
        ax = -x1 + 3 * x2 - 3 * x3 + x4
        bx = 3 * x1 - 6 * x2 + 3 * x3
        cx = -3 * x1 + 3 * x2
        dx = x1
        res = ax * t ** 3 + bx * t ** 2 + cx * t + dx
        return round(res)

    def myCurve(self, x1,y1,x2,y2,x3,y3,x4,y4):        
        xt1 = x1
        yt1 = y1
        path_resolution=1000
        for t in range(0, path_resolution + 1):
            pointx = self.bezier(x1, x2, x3, x4, t / path_resolution)
            pointy = self.bezier(y1, y2, y3, y4, t / path_resolution)
            self.myLine(xt1, yt1, pointx, pointy)
            xt1 = pointx
            yt1 = pointy
        return

    def loadbackground(self):
        self.label = Label(self.canvas, image=self.background)
        self.label.bind('<Configure>', self.resizeimage)
        self.label.pack(fill='both', expand='yes')

    def rootgeometry(self, WIDTH, HEIGHT):
        self.master.geometry(str(WIDTH) + 'x' + str(HEIGHT))

    def zoomToFile(self,shape,zoom):
        if(zoom):
            for i in range(len(shape)):
                if i % 2 == 0:
                    shape[i] =int(1.1*shape[i])
                else:
                    shape[i] =int(1.1*shape[i])
        else:          
            for i in range(len(shape)):
                if i % 2 == 0:
                    shape[i] =int(0.9*shape[i])
                else:
                    shape[i] =int(0.9*shape[i])
    def zoomIn(self):
        self.lower_frame.delete("all")
        for  line in self.data["lines"]:
            self.zoomToFile(line,1)
        for  circle in self.data["circles"]:
            self.zoomToFile(circle,1)
        self.zoomToFile(self.data["bezier"],1)
        self.createShip( self.data['lines'],self.data['circles'],self.data['bezier'])
    def zoomOut(self):
        self.lower_frame.delete("all")
        for  line in self.data["lines"]:
            self.zoomToFile(line,0)
        for  circle in self.data["circles"]:
            self.zoomToFile(circle,0)
        self.zoomToFile(self.data["bezier"],0)
        self.createShip( self.data['lines'],self.data['circles'],self.data['bezier'])
    def resizeimage(self, event):
        image = self.image_copy.resize((self.master.winfo_width(), self.master.winfo_height()))
        self.image1 = ImageTk.PhotoImage(image)
        self.label.config(image=self.image1)

   
    """Rotates a point around center_point(origin by default)
    Angle is in degrees.+*-
    Rotation is counter-clockwise
    """

    # rotation logic
    def rotate_X(self):
        self.lower_frame.delete("all")
        self.rotate_point(90)

    def rotate_point(self,angle):
            for  line in self.data["lines"]:
                self.rotate_shape(line,angle)
            for  circle in self.data["circles"]:
                self.rotate_shape(circle,angle)
            self.rotate_shape(self.data["bezier"],angle)
            self.createShip( self.data['lines'],self.data['circles'],self.data['bezier'])
    def moveShape(self,shape,stepx,stepy):
        for i in range(len(shape)):
                if i % 2 == 0:
                    shape[i] +=stepx
                else:
                    shape[i] +=stepy
    def rotate_shape(self,shape,angle):
        x,y=shape[0],shape[1]
        self.moveShape(shape,0-x, 0-y)
        for i in range(len(shape)):
            if i % 2 == 0:
                shape[i] = round(shape[i] * math.cos(angle)-shape[i+1]* math.sin(angle))
            else:
                shape[i] = round(shape[i-1] * math.sin(angle)+shape[i]* math.cos(angle))
        self.moveShape(shape,x, y)
            
    def clickMove(self, event):
        if self.my_point == 0:
            # Get first x,y
            self.x[0] = event.x
            self.y[0] = event.y
            self.my_point = 1
        if self.action == 'move' and self.my_point == 1:
            #clear
            self.lower_frame.delete("all")
            self.my_point = 0
            #set new ship
            stepx= self.x[0]-self.data["lines"][0][0]
            stepy= self.y[0]-self.data["lines"][0][1]
            for line in self.data["lines"]:
                self.moveShape(line,stepx,stepy)
            for  circle in self.data["circles"]:
                self.moveShape(circle,stepx,stepy)
            self.moveShape(self.data["bezier"],stepx,stepy)
            self.createShip( self.data['lines'],self.data['circles'],self.data['bezier'])
    def move(self):
        #reset clicks
        self.my_point =0
        #lisinigs for 2 clicks
        self.action ='move'
    def derivedShape(self,shape,derive):
        for i in range(len(shape)):
            if i % 2 == 0:
                shape[i]=  shape[i] +shape[i+1]*derive
        
    def derived(self):
        self.lower_frame.delete("all")
        for  line in self.data["lines"]:
            self.derivedShape(line,0.1)
        for  circle in self.data["circles"]:
            self.derivedShape(circle,0.1)
        self.derivedShape(self.data["bezier"],0.1)
        self.createShip( self.data['lines'],self.data['circles'],self.data['bezier'])





if __name__ == '__main__':
    root = Tk()
    my_gui = DrowingApp(root)
    root.mainloop()

