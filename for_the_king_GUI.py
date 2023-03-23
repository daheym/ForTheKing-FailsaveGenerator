from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

# from PIL import Image, ImageTk

import shutil
import os
import base64
from datetime import datetime

###############################################################
FTK_logo=b'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'
imgdata = base64.b64decode(FTK_logo)
###############################################################

def open_file():
    '''Function which id executed when the "specify FILE" button is pressed.'''
    global target_file
    target_file = fd.askopenfilename(filetypes=[("FTK Savegames", "*.run"),("all files","*.*")], initialdir=f'C:\\Users\\{user}\\AppData\\LocalLow\\IronOak Games\\FTK\\save')
    target_pathlabel.config(text=target_file.split('/')[-1])
    
    if target_file != '':
        FILE.config(state='disabled')
        DIRECTORY.config(state='normal')

def save_file():
    '''Function which is executed when the "specify DIRECTORY" button is pressed.'''
    global destination_dir
    destination_dir = fd.askdirectory(initialdir=f'C:\\Users\\{user}\\AppData\\LocalLow\\IronOak Games\\FTK\\save')
    destination_pathlabel.config(text=destination_dir)
    
    if destination_dir != '':
        DIRECTORY.config(state='disabled')
        minutes.config(state='normal')
        START.config(state='normal')
    
def start():
    '''
    Function which is executed when the "START" button is pressed.
    First, the entry in the timer-window is evaluated. Second, the main function is started.
    '''
    global running
    running = True
    
    def time_evaluation():
        
        global save_time
        
        try: 
            save_time = int(minutes.get())
            
            if save_time > 60:
                save_time = 60*60000
            
            elif save_time >= 1:
                save_time *= 60000
                
            elif save_time == 0:
                save_time = 15*60000
                messagebox.showwarning('Invalid time settings', 'Invalid entry! Timer set to 15 minutes.')
                
            elif save_time < 0:
                save_time = 15*60000
                messagebox.showwarning('Invalid time settings', 'Negative time - really? Invalid entry!\nTimer set to 15 minutes.')
                
            var.set(int(save_time/60000))
            
        except ValueError:
            save_time = 15*60000
            var.set(15)
            messagebox.showwarning('Invalid time settings', 'Invalid entry! Timer set to 15 minutes.')
             
    time_evaluation()
    
    START.config(state='disabled')
    MANUAL.config(state='normal')
    minutes.config(state='disabled')
    
    main_function()
    
def manual_save(): 
    root.after_cancel(THREAD)
    main_function()
    
def stop():
    global running
    running = False
    root.destroy()

#################################################################

def file_saver(target_file,destination_dir):

    # grab the current date and time
    date = datetime.now().strftime("%Y_%m_%d--%H_%M_%S") 

    # define source and target destination
    target = target_file.split('/')[-1]
    destination_file = f'{destination_dir}/{date}_{target}'

    # copy a file from source to target destination
    shutil.copy2(target_file,destination_file)

def main_function():

    # some recursion to let the main function call itself after execution
    # running get set to True by the start.function
    if running:
        file_saver(target_file,destination_dir)
        global THREAD
        THREAD = root.after(save_time, main_function)
        
##################################################################

if __name__ == '__main__':

    root = Tk()
    root.title('For The King: Failsave generator')
    root.resizable(False,False)
    
#     for c in range(4):
#         root.columnconfigure(c, weight=1)

    # get the username for the specific directory
    user = os.environ['USERNAME']

    # select the target file
    FILE = Button(root, text='specify FILE', command=open_file, width=15, state='normal')
    FILE.grid(row=0, column=0, sticky='W')
    target_pathlabel = Label(root)
    target_pathlabel.grid(row=0, column=1, columnspan=2, sticky='W', ipadx=5)

    # select the destination directory
    DIRECTORY = Button(root, text='specify DIRECTORY', command=save_file, width=15, state='disabled')
    DIRECTORY.grid(row=1, column=0, sticky='W')
    destination_pathlabel = Label(root)
    destination_pathlabel.grid(row=1, column=1, columnspan=2, sticky='W', ipadx=5)
    
    # insert the FTK-logo
    logo = PhotoImage(data=imgdata, format='gif')
    LOGO = Label(root, image=logo)
    LOGO.grid(row=0, column=3, rowspan=4)

    # label for entry box
    LABEL = Label(root, text='how often do you want to save (in minutes?)')
    LABEL.grid(row=2, column=0, columnspan=2, sticky='W', ipady=10, ipadx=5)

    # entry box for time with default value
    var = IntVar(root)
    var.set(15)
    minutes = Spinbox(root, from_=1, to=60, increment=1, state='disabled', textvariable=var, width=15)
    minutes.grid(row=2, column=2, sticky='W')

    # start/stop-buttons with their initial states
    START = Button(root, text='START', command=start, background='#05e365', activebackground='darkgreen' ,state='disabled', width=15)
    START.grid(row=3, column=0, sticky='W')
    MANUAL = Button(root, text='SAVE NOW', command=manual_save, background='#edda02', state='disabled', width=15)
    MANUAL.grid(row=3, column=1, sticky='E')
    STOP = Button(root, text='QUIT', command=stop, background='#f22727', state='normal', width=15)
    STOP.grid(row=3, column=2, sticky='E')

    root.mainloop()