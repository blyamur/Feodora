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

Image.MAX_IMAGE_PIXELS = None #отключение ограничений по размеру изображений

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
			text="Выберите Изображения [.JPG,.PNG]",
			justify="center",
			font=("-size", 15, "-weight", "bold"),
		)
		self.label.grid(row=1, column=0,padx=0, pady=25, columnspan=2, sticky="S")
		self.accentbutton = ttk.Button(
			self.widgets_frame, text="Выбрать файл(ы)", style="Accent.TButton",command=open_file
		)
		self.accentbutton.grid(row=2, column=0, padx=2, pady=10, sticky="nsew")

		self.switch = ttk.Checkbutton(
			self.widgets_frame, text="Перезаписать", style="Switch.TCheckbutton", variable=delete_im, onvalue=1, offvalue=0
		)
		self.switch.grid(row=4, column=0, padx=1, pady=1, sticky="w")
		self.switch = ttk.Checkbutton(
			self.widgets_frame, text="Улучшить", style="Switch.TCheckbutton", variable=enhance_im, onvalue=1, offvalue=0
		)
		self.switch.grid(row=4, column=0, padx=1, pady=1, sticky="e")
		self.switch = ttk.Checkbutton(
			self.widgets_frame, text="Сжать", style="Switch.TCheckbutton", variable=quality_im, onvalue=1, offvalue=0
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
			self.widgets_frame, text="V:"+currentVersion+" Проверить Обновления", style="Url.TButton",command=checkUpdate
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
				messagebox.showinfo(title='Обновления не найдены', message=f'Обновления не найдены.\nТекущая версия: {version}')

	# do not check for update if offline
	except requests.exceptions.ConnectionError:
		if method == 'Button':
			messagebox.showwarning(title='Нет доступа к сети', message='Нет доступа к сети.\nПроверьте подключение к интернету.')
		elif method == 'Button':
			pass

def updateApp(version):
	update = messagebox.askyesno(title='Найдено обновление', message=f'Доступна новая версия {version} . Обновимся?')
	if update:
		webbrowser.open_new_tab('https://github.com/blyamur/Feodora')

def open_file():
	try:
		file_open = filedialog.askopenfilenames(parent=root,title='Пожалуйста выберите Изображение', filetypes=[('Image Files', ['.jpeg', '.jpg', '.png'])])
		files = root.tk.splitlist(file_open)
		for filename in files:
			full_name = path.basename(filename) #Текущее название изображения
			status.set(full_name)
			file_dir = os.path.dirname(os.path.abspath(filename)) #путь к папке источнику
			dir_name = path.splitext(full_name)[0] #название изображения
			new_name = 'RSD_'+dir_name #новое название
			ext_name = path.splitext(full_name)[1] #расширение 
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
						quality_im_set=70 # степень сжатия качества
						nquality='compressed_'
					else:
						quality_im_set=99
						nquality=''
					img.save(file_dir + '/' + nenhance + nquality + new_name +'.bmp') #изображение сохраняется в формате bmp
					imgs = Image.open(file_dir + '/'  + nenhance + nquality + new_name + '.bmp') #изображение открывается в формате bmp
					if delete_im.get() == 1:
						os.remove(file_dir + '/' + full_name) #удаляется оригинал изображения
						imgs.save(file_dir + '/' + full_name, quality=quality_im_set) #изображение сохраняется в формате оригинала 
						os.remove(file_dir + '/' + nenhance + nquality + new_name +'.bmp')  #удаляется изображение  в формате bmp
					else:
						imgs.save(file_dir + '/' + nenhance + nquality + new_name + ext_name, quality=quality_im_set)  #изображение сохраняется в формате оригинала
						os.remove(file_dir + '/' + nenhance + nquality + new_name +'.bmp') #удаляется изображение  в формате bmp
					status.set('Готово, мы все успешно пересохранили!')
				except:
					messagebox.showerror(title='Ошибка', message='Ой, Что-то пошло не так!', icon='warning')
			else:
				messagebox.showerror("Ошибка", " Вы не выбрали файл!")
	except:
		messagebox.showerror("Ошибка", "Что-то пошло не так!")
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
	root.geometry('570x300+{}+{}'.format(w, h)) #размеры окна
	root.resizable(False, False)
	root.title("Феодора: Скрипт для пересохранения изображений 3.1") # заголовок окна приложения
	root.iconbitmap('icon.ico') # иконка окна приложения
	factor = 1.8 #степень улучшения изображения
	currentVersion = '3.1'
	root.tk.call("source", "spring-noon.tcl") #установка темы оформления
	root.tk.call("set_theme", "light") #стиль темы оформления
	app = App(root)
	app.pack(fill="both", expand=True)
	root.update()
	root.mainloop()
