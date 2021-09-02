import os
from os import path
import tkinter as tk
from tkinter import IntVar
from tkinter import StringVar
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageEnhance
import webbrowser
import requests

__author__ = "Mons (https://blog.mons.ws)"
__copyright__ = "Copyright 2021"
__credits__ = ["Code: Mons (https://github.com/blyamur/)", "TTK Theme: rdbende (https://github.com/rdbende/Sun-Valley-ttk-theme)"]
__license__ = "non-commercial use only, for personal use"
__version__ = "3.1.0"
__maintainer__ = "Mons"
__email__ = "mons@mons.ws"
__status__ = "Production"

Image.MAX_IMAGE_PIXELS = None #disable image size restrictions

class App(ttk.Frame):
	def __init__(self, parent):
		ttk.Frame.__init__(self)
		for index in [0, 1, 2]:
			self.columnconfigure(index=index, weight=1)
			self.rowconfigure(index=index, weight=1)
		self.setup_widgets()

	def setup_widgets(self):
		global delete_im
		global quality_im
		global enhance_im
		global status
		delete_im = IntVar()
		enhance_im = IntVar()
		quality_im = IntVar()
		status = StringVar()
		status.set('')
		self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
		self.widgets_frame.grid(
			row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
		)
		self.widgets_frame.columnconfigure(index=0, weight=1)
		self.label = ttk.Label(
			self.widgets_frame,
			text="Select Images [.JPG,.PNG]",
			justify="center",
			font=("-size", 15, "-weight", "bold"),
		)
		self.label.grid(row=1, column=0,padx=0, pady=25, columnspan=2, sticky="S")
		self.accentbutton = ttk.Button(
			self.widgets_frame, text="Select file (s)", style="Accent.TButton",command=open_file
		)
		self.accentbutton.grid(row=2, column=0, padx=2, pady=10, sticky="nsew")

		self.switch = ttk.Checkbutton(
			self.widgets_frame, text="Overwrite", style="Switch.TCheckbutton", variable=delete_im, onvalue=1, offvalue=0
		)
		self.switch.grid(row=4, column=0, padx=1, pady=1, sticky="w")
		self.switch = ttk.Checkbutton(
			self.widgets_frame, text="Enhance", style="Switch.TCheckbutton", variable=enhance_im, onvalue=1, offvalue=0
		)
		self.switch.grid(row=4, column=0, padx=1, pady=1, sticky="e")
		self.switch = ttk.Checkbutton(
			self.widgets_frame, text="Compress", style="Switch.TCheckbutton", variable=quality_im, onvalue=1, offvalue=0
		)
		self.switch.grid(row=4, column=0, padx=1, pady=1, sticky="s")
		
		
		self.labels = ttk.Label(
			self.widgets_frame,
			textvariable = status,
			foreground="#49B349",
			justify="center",
			font=("-size", 11, "-weight", "bold"),
		)
		self.labels.grid(row=5, column=0, padx=10, pady=11, columnspan=11, sticky="n")
		#Bottom copyright 2 url button
		self.UrlButton = ttk.Button(
			self.widgets_frame, text="© 2021 Mons (blog.mons.ws)", style="Url.TButton",command=openweb
		)
		self.UrlButton.grid(row=7, column=0, padx=0, pady=0, columnspan=11, sticky="n")
		self.UrlButton = ttk.Button(
			self.widgets_frame, text="V:"+currentVersion+" Check Update", style="Url.TButton",command=checkUpdate
		)
		self.UrlButton.grid(row=8, column=0, padx=0, pady=0, columnspan=11, sticky="n")
		
		
def checkUpdate(method='Button'):
	try:
		# checks for latest version available on GitHub README file
		github_page = requests.get('https://raw.githubusercontent.com/blyamur/Feodora/main/README.md')
		github_page_html = str(github_page.content).split()
		
		for i in range(0, 12):
			try:
				index = github_page_html.index(('3.' + str(i)))
				version = github_page_html[index]
			except ValueError:
				pass
			# display popup window if update found
		if float(version) > float(currentVersion):
			updateApp(version)
		else:
			if method == 'Button':
				messagebox.showinfo(title='No update found', message=f'No update found.\nLatest version: {version}')

	# do not check for update if offline
	except requests.exceptions.ConnectionError:
		if method == 'Button':
			messagebox.showwarning(title='You are offline', message='You are offline.\nPlease connect to the internet to check for update.')
		elif method == 'Button':
			pass
def updateApp(version):
	update = messagebox.askyesno(title='Update available', message=f'Version {version} available. Update?')
	if update:
		webbrowser.open_new_tab('https://github.com/blyamur/Feodora')
def open_file():
	try:
		file_open = filedialog.askopenfilenames(parent=root,title='Please select an Image', filetypes=[('Image Files', ['.jpeg', '.jpg', '.png'])])
		files = root.tk.splitlist(file_open)
		for filename in files:
			full_name = path.basename(filename) #Current image name
			status.set(full_name)
			file_dir = os.path.dirname(os.path.abspath(filename)) #source folder path
			dir_name = path.splitext(full_name)[0] #image name
			new_name = 'RSD_'+dir_name #new name
			ext_name = path.splitext(full_name)[1] #extension 
			if ext_name.lower().endswith(('.jpeg', '.jpg', '.png')):
				try:
					img = Image.open(filename)
					if enhance_im.get() == 1: 
						enhancer = ImageEnhance.Sharpness(img)
						img = enhancer.enhance(factor)
						nenhance = 'enhance_'
					else:
						nenhance = ''
					if quality_im.get() == 1: 
						quality_im_set=70 #quality compression ratio
						nquality='compressed_'
					else:
						quality_im_set=99
						nquality=''
					img.save(file_dir + '/' + nenhance + nquality + new_name +'.bmp') #image is saved in bmp format
					imgs = Image.open(file_dir + '/'  + nenhance + nquality + new_name + '.bmp') #image opens in bmp format
					if delete_im.get() == 1:
						os.remove(file_dir + '/' + full_name) #original image is deleted
						imgs.save(file_dir + '/' + full_name, quality=quality_im_set) #image is saved in the original format
						os.remove(file_dir + '/' + nenhance + nquality + new_name +'.bmp')  #deletes the bmp image
					else:
						imgs.save(file_dir + '/' + nenhance + nquality + new_name + ext_name, quality=quality_im_set)  #image is saved in the original format
						os.remove(file_dir + '/' + nenhance + nquality + new_name +'.bmp') #deletes the bmp image
					status.set('Done, we saved everything successfully!')
				except:
					messagebox.showerror(title='Error', message='Oops, Something went wrong!', icon='warning')
			else:
				messagebox.showerror("Error", " You haven't selected a file!")
	except:
		messagebox.showerror("Error", " Something went wrong!")
def openweb():
	webbrowser.open_new_tab('https://blog.mons.ws')

if __name__ == "__main__":
	root = tk.Tk()
	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	w = w//2 
	h = h//2 
	w = w - 200
	h = h - 200
	root.geometry('570x300+{}+{}'.format(w, h)) #window dimensions
	root.resizable(False, False)
	root.title("Feodora: Script for resaving images3.1") #application window title
	root.iconbitmap('icon.ico') #application window icon
	factor = 1.8 #image enhancement factor
	currentVersion = '3.1'
	root.tk.call("source", "spring-noon.tcl") #setting the theme
	root.tk.call("set_theme", "light") #theme style
	app = App(root)
	app.pack(fill="both", expand=True)
	root.update()
	root.mainloop()
