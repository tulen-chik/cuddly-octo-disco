import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os


def get_data():
    raw_data = os.listdir('assets')
    txt_file = [file for file in raw_data if file[-4:] == '.txt']
    img_file = [file for file in raw_data if file[-4:] != '.txt' and file != 'sys']
    return txt_file, img_file


def get_text(file_path):
    with open(file_path, 'r') as file:
        return [line if line[-1:] != '\n' else line[:-1] for line in file]


class App:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.geometry('600x500')
        self.root.resizable(False, False)
        self.data = data
        self.data_len = len(self.data)
        self.txt = get_data()[0]
        self.img = get_data()[1]

        self.main_frame = tk.Frame(self.root)

        self.new_scene_button = tk.Button(self.main_frame, text='добавить новую сцену', command=self.__add_scene)
        self.new_scene_button.grid(row=0, column=0)

        self.save_scene_button = tk.Button(self.main_frame, text='сохранить файл')
        self.save_scene_button.grid(row=0, column=1)

        self.all_scenes = tk.Frame(self.main_frame)

        for scene in range(self.data_len):
            self.scene_frame = tk.Frame(self.all_scenes)

            self.bg_label = tk.Label(self.scene_frame, text='задний фон')
            self.bg_label.grid(row=0, column=0, pady=10)

            self.bg_listbox = ttk.Combobox(self.scene_frame, values=self.img)
            self.bg_listbox.insert(0, self.data[scene]['bg'][7:])
            self.bg_listbox.grid(row=1, column=0, pady=10)

            self.char_label = tk.Label(self.scene_frame, text='персонаж')
            self.char_label.grid(row=0, column=1, pady=10)

            self.char_listbox = ttk.Combobox(self.scene_frame, values=self.img)
            self.char_listbox.insert(0, self.data[scene]['char'][7:])
            self.char_listbox.grid(row=1, column=1, padx=20)

            self.text_label = tk.Label(self.scene_frame, text='текст')
            self.text_label.grid(row=0, column=2)

            self.text_listbox = ttk.Combobox(self.scene_frame, values=self.txt)
            self.text_listbox.insert(0, self.data[scene]['text'][7:])
            self.text_listbox.grid(row=1, column=2)

            self.scene_frame.grid(row=scene, column=0, padx=20)

        self.all_scenes.grid(row=1, column=0)

        self.main_frame.pack()

        #self.message_enter = messagebox.showinfo(title='добро пожаловать', message='для начала работы, вам необходимо '
        #                                                                           'переместить весь текст с сюжетом '
        #                                                                           'вашей игры и картинки в папку '
        #                                                                           'assets')

        self.root.mainloop()

    def __make_scene(self):
        for scene in range(self.data_len):
            self.scene_frame = tk.Frame(self.all_scenes)

            self.bg_label = tk.Label(self.scene_frame, text='задний фон')
            self.bg_label.grid(row=0, column=0, pady=10)

            self.bg_listbox = ttk.Combobox(self.scene_frame, values=self.img)
            self.bg_listbox.insert(0, self.data[scene]['bg'][7:])
            self.bg_listbox.grid(row=1, column=0, pady=10)

            self.char_label = tk.Label(self.scene_frame, text='персонаж')
            self.char_label.grid(row=0, column=1, pady=10)

            self.char_listbox = ttk.Combobox(self.scene_frame, values=self.img)
            self.char_listbox.insert(0, self.data[scene]['char'][7:])
            self.char_listbox.grid(row=1, column=1, padx=20)

            self.text_label = tk.Label(self.scene_frame, text='текст')
            self.text_label.grid(row=0, column=2)

            self.text_listbox = ttk.Combobox(self.scene_frame, values=self.txt)
            self.text_listbox.insert(0, self.data[scene]['text'][7:])
            self.text_listbox.grid(row=1, column=2)

            self.scene_frame.grid(row=scene, column=0, padx=20)

    def __del_scene(self):
        for scene in range(self.data_len-1):
            self.scene_frame.destroy()
            self.bg_label.destroy()
            self.bg_listbox.destroy()
            self.char_label.destroy()
            self.text_label.destroy()
            self.text_listbox.destroy()

    def __add_scene(self):
        self.data.append({'bg': '', 'char': '', 'text': []})
        self.data_len += 1
        self.__del_scene()
        self.__make_scene()


app = App([
        {"bg": "assets/kbp.jfif", "char": "assets/amogus.png", "text": "assets/first_scene.txt"},
        {"bg": "assets/kbp.jfif", "char": "assets/amogus_green.png", "text": "assets/second_scene.txt"},
    ])
