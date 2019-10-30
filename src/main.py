from tkinter import *
from tkinter.messagebox import *
import json
from PIL import ImageTk, Image
from PIL import *
import pyglet
import playsound
import time
import random
from random import randrange as rnd, choice
from pyglet import *
from multiprocessing import Process


#главное окно
root = Tk()
root.geometry('1500x1000')
bg_color = "#B0E0E6"
root['bg'] = bg_color
w, h = root.winfo_screenwidth(), root.winfo_screenheight()


#фреймы
frame1 = Frame(root, width=100, height=100, background=bg_color)
frame2 = Frame(root, width=1000, height=1500, background=bg_color)
frame3 = Frame(root, width=1000, height=100, background=bg_color)
frame4 = Frame(root, width=500, height=100, background=bg_color)
frame5 = Frame(root, width=w, height=h, background=bg_color)
frame6 = Frame(root, width=w, height=h, background=bg_color)



#переменные объектов окна
var_mode = IntVar()
var_mode.set(1000)
var_count_of_approaches = IntVar()
var_background_color = StringVar()
var_text_color = StringVar()
var_text_size = IntVar()
var_voice_helper = StringVar()
var_voice_helper.set("OFF")


    
def stop_sound():
    if (p_sound1.is_alive()):
        p_sound1.terminate()
    if (p1.is_alive()):
        p1.terminate()
    if (p2.is_alive()):
        p2.terminate()
    if (p3.is_alive()):
        p3.terminate()
    if (p4.is_alive()):
        p4.terminate()
    if (p5.is_alive()):
        p5.terminate()
    root['bg'] = bg_color
    frame5.place_forget()
    start_train()

def width_alignment(text, width):
    paragraphs = [paragraph.splitlines() for paragraph in text.split('\n\n')]

    for paragraph in paragraphs:
        for i, line in enumerate(paragraph[:-1]):
            words = line.split()
            s = width - sum(map(len, words))
            cs = len(words) - 1
            spw, mod = divmod(s, cs)
            spw = spw if spw > 0 else 1
            ws = [' ' * spw] * (cs - mod) + [' ' * (spw + 1) for _ in range(mod)] + ['']
            paragraph[i] = ''.join(w + s for w, s in zip(words, ws))

    poet = '\n\n'.join('\n'.join(paragraph) for paragraph in paragraphs)
    return poet

    
def my_table(data):
  
    frame1.place_forget()
    frame2.place_forget()
    frame3.place_forget()
    frame4.place_forget()
    frame5.pack(fill="both", expand=True, padx=0, pady=0)
    frame5.place(in_=root, anchor="c", relx=.5, rely=.5)
    txt_c = '#000000'
    bg_c = '#FFFFFF'

    if (data['bg_color'] == 'персиковый'):
        bg_c = '#FFDAB9'
    if (data['bg_color'] == 'лимонный'):
        bg_c = '#FFFACD'
    if (data['bg_color'] == 'светло-розовый'):
        bg_c = '#DDA0DD'
    if (data['bg_color'] == 'белый'):
        bg_c = '#FFFFFF'
    if (data['bg_color'] == 'бирюзовый'):
        bg_c = '#7FFFD4'
    if (data['bg_color'] == 'ночной режим'):
        bg_c = '#000000'

    if (data['txt_color'] == 'тёмно-красный'):
        txt_c = '#8B0000'
    if (data['txt_color'] == 'цвет морской волны'):
        txt_c = '#006400'
    if (data['txt_color'] == 'зелёный'):
        txt_c = '#008080'
    if (data['txt_color'] == 'синий'):
        txt_c = '#191970'
    if (data['txt_color'] == 'ночной режим'):
        txt_c = '#FFFFFF'
    if (data['txt_color'] == 'чёрный'):
        txt_c = '#000000'
   
    frame5['bg'] = bg_c
    root['bg'] = bg_c
    mas = ['Н', 'Б', 'Л', 'Ш', 'Щ', 'Ц', 'Ы', 'М', 'В', 'К', 'Ф', 'Р', 'И', 'Ч', 'Я', 'Д', 'У', 'Г', 'Ъ', 'Ь', 'П']
    
    for i in range(15):
        label = Label(frame5, text=mas[random.randrange(0, 20, 1)],
                      font="Arial " + str(data['txt_size']), bg=bg_c, fg=txt_c, width=int(7*15/data['txt_size']), height = 2)
        label.grid(row=1, column=i)
    for i in range(15):
        label = Label(frame5, text=mas[random.randrange(0, 20, 1)],
                       font="Arial " + str(data['txt_size']-3),bg=bg_c, fg=txt_c, width=int(7*15/data['txt_size']), height = 2)
        label.grid(row=2, column=i)
    for i in range(15):
        label = Label(frame5, text=mas[random.randrange(0, 20, 1)],
                    font="Arial " + str(data['txt_size']-6),bg=bg_c,fg=txt_c, width=int(7*15/data['txt_size']), height = 2)
        label.grid(row=3, column=i)
    for i in range(15):
        label = Label(frame5, text=mas[random.randrange(0, 20, 1)], 
                      font="Arial " + str(data['txt_size']-9),bg=bg_c,fg=txt_c, width=int(7*15/data['txt_size']), height = 2)
        label.grid(row=4, column=i)
    
    lab = Label(frame5, text="", font="Arial 15",bg=bg_c, fg=txt_c, width=7, height = int(20*15/data['txt_size']))
    lab.grid(row=5, column=1, columnspan=500)
    b_start = Button(frame5, text="НАЧАТЬ", width=50, height=5, bg="#B0C4DE", border=0, command=start_audio1)
    b_start.grid(row=6, column=1, columnspan=7)
    b_stop = Button(frame5, text="CТОП", width=50, height=5, bg="#B0C4DE", border=0, command=stop_sound)
    b_stop.grid(row=6, column=8, columnspan=7)
    

def change_settings():
    data = {}
    data['t1'] = int(frame2.nametowidget('ent1').get())
    data['t2'] = int(frame2.nametowidget('ent2').get())
    data['voice_helper'] = var_voice_helper.get()
    data["count_approaches"] = var_count_of_approaches.get()
    data["bg_color"] = var_background_color.get()
    data["txt_color"] = var_text_color.get()
    data["txt_size"] = var_text_size.get()
    save_data_to_file(data, "user.json")


def check_settings():
    t1 = frame2.nametowidget('ent1').get()
    t2 = frame2.nametowidget('ent2').get()
    if (t1.isdigit() == False or int(t1) > 60 or int(t1) < 30):
        frame2.nametowidget('ent1').delete(0, END)
        showerror("Ошибка", "Неправильно введены данные")
        return False
    if (t2.isdigit() == False or int(t2) > 120 or int(t2) < 60):
        frame2.nametowidget('ent2').delete(0, END)
        showerror("Ошибка", "Неправильно введены данные")
        return False
    return True

def start_sound():
     playsound.playsound('start.mp3', True)
def finish_sound():
     playsound.playsound('finish.mp3', True)
def lefty_sound():
     playsound.playsound('LeftY.mp3', True)
def righty_sound():
     playsound.playsound('RightY.mp3', True)
def untitled111_sound():
     playsound.playsound('Untitled111.mp3', True)
def audio_sound2():
     playsound.playsound('5min.mp3', True)


def start_audio1():
    global p_sound1
    p_sound1 = Process(name="p_sound",target=setting_audio_mode1)
    p_sound1.start()

def start_audio2():
    global p_sound2
    p_sound2 = Process(name="p_sound",target=setting_audio_mode2)
    p_sound2.start()


def setting_audio_mode2():
    time.sleep(5)
    global p6
    p6 = Process(name ='p6', target=audio_sound2)
    p6.start()
    


def setting_audio_mode1():
    dictionary = from_file_to_dict()
    t1 = dictionary.get("t1")
    t2 = dictionary.get("t2")
    count_approaches = dictionary.get("count_approaches")
    global p1, p2, p3, p4, p5
    p1 = Process(name="p1",target=start_sound)
    p2 = Process(name="p2",target=finish_sound)
    p3 = Process(name="p3",target=lefty_sound)
    p4 = Process(name="p4",target=righty_sound)
    p5 = Process(name="p5",target=untitled111_sound)
    p1.start()
    time.sleep(5)
    for approach in range(count_approaches):
        p3.start()
        time.sleep(t1)
        p5.start()
        time.sleep(t2)

    for approach in range(count_approaches):
        p4.start()
        time.sleep(t1)
        p5.start()
        time.sleep(t2)
    p2.start()

    

def start():
    if (check_settings() == False):
        return
    change_settings()
    if (var_mode.get() == 1):
        data = from_file_to_dict()
        my_table(data)


def start_train():
    frame1.place_forget()
    frame6.place_forget()
    frame5.place_forget()
    frame1.place_forget()
    frame2.pack(fill="both", expand=True, padx=0, pady=0)
    frame2.place(in_=root,  x=100, y=200)
    frame4.pack(fill="both", expand=True, padx=0, pady=0)
    frame4.place(in_=root,  x=100, y=50)
    label_mode = Label(frame4, text="ВЫБЕРИ РЕЖИМ: ", font="Arial 15",bg=bg_color, width=16, height = 2 , pady=3)
    rbut1_mode = Radiobutton(frame4,text='РЕЖИМ 1', variable=var_mode, width=12,value=1,command=change_mode,bg="#B0C4DE",font='Arial 15')
    rbut2_mode = Radiobutton(frame4,text='РЕЖИМ 2', variable=var_mode, width=12, value=2,command=change_mode,bg="#B0C4DE",font='Arial 15')
    
    label_mode.grid(row=1,column=1,columnspan=1,sticky=W)
    rbut1_mode.grid(row=2,column=1,columnspan=1,sticky=W)
    rbut2_mode.grid(row=3,column=1,columnspan=1,sticky=W)

    ent1 = Entry(frame2,width=10,font="Arial 20")
    ent2 = Entry(frame2,width=10,font="Arial 20")

def from_file_to_dict():
    # распарсить словарь
    with open("user.json", "r") as read_file:
        data = json.load(read_file)
        return data


def save_data_to_file(data, filename):
    # сохранить словарь в файл
    with open(filename, "w") as write_file:
        json.dump(data, write_file)

 
def open_main_window():
    frame6.place_forget()
    frame5.place_forget()
    frame4.place_forget()
    frame2.place_forget()
    frame3.place_forget()
    frame1.pack(fill="both", expand=True, padx=0, pady=0)
    frame1.place(in_=root, anchor="c", relx=.5, rely=.5)

    photo = ImageTk.PhotoImage(file="Снимок.png")
    b0 = Button(frame1, width=800, height=400, image=photo, border=0)
    b0.grid(row=0, column=2)

    # Кнопочки
    b1 = Button(frame1, text="ПЕРЕЙТИ К ТРЕНИРОВКЕ", width=100, height=5, bg="#ADD8E6", border=0, command=start_train)
    b1.grid(row=2, column=2)

    b2 = Button(frame1, text="РЕКОМЕНДАЦИИ", width=100, height=5, bg="#87CEEB", border=0, command=open_decription_window)
    b2.grid(row=3, column=2)

    b2 = Button(frame1, text="ВЫХОД", width=100, height=5, bg="#B0C4DE", border=0, command=root.destroy)
    b2.grid(row=4, column=2)

    # show
    root.mainloop()


def to_main_win(root):
    root.destroy()
    #open_main_window()

def start_mode1():
    frame6.place_forget()
    frame2.pack(fill="both", expand=True, padx=0, pady=0)
    frame2.place(in_=root,  x=100, y=200)

    listbox_img = ImageTk.PhotoImage(file="Снимок.png", width=100, height=5)
     

    but_start = Button(frame2, text="ПЕРЕЙТИ К ТРЕНИРОВКE", width=65, height=5, bg="#87CEEB", border=0, command=start)
    bb = Button(frame2, text="ВЕРНУТЬСЯ В ГЛАВОЕ МЕНЮ", width=65, height=5, bg="#B0C4DE", border=0, command=open_main_window)

    lab1 = Label(frame2, text="НАСТРОЙКИ", font="Arial 15",bg=bg_color, height=3)
    lab2 = Label(frame2, text="Время тренировки (в секундах): ", font="Arial 15",bg=bg_color)
    lab3 = Label(frame2, text="Время релаксации (в секундах): ", font="Arial 15",bg=bg_color)
    lab4 = Label(frame2, text="Количество подходов: ", font="Arial 15",bg=bg_color,)
    lab6 = Label(frame2, text="Цвет фона: ", font="Arial 15",bg=bg_color)
    lab7 = Label(frame2, text="Цвет текста: ", font="Arial 15",bg=bg_color)
    lab8 = Label(frame2, text="Размер текста: ", font="Arial 15",bg=bg_color)
    lab9 = Label(frame2, text="", font="Arial 15",bg=bg_color, height=2)
    ent1 = Entry(frame2, width=20, font="Arial 15", bd=0,  name='ent1')
    ent2 = Entry(frame2, width=20, font="Arial 15", bd=0, name='ent2')
    listbox1 = OptionMenu(frame2,  var_count_of_approaches,  3,4,5,6,7)
    listbox1.config(bg="#B0C4DE", width=17, bd = 0,font="Arial 15")
    listbox1["highlightthickness"] = 0


    listbox2 = OptionMenu(frame2, var_background_color, 'персиковый','лимонный','светло-розовый','белый','бирюзовый', 'ночной режим')
    listbox2.config(bg="#87CEEB", width=17, bd = 0,font="Arial 15")
    listbox2["highlightthickness"] = 0
    listbox3 = OptionMenu(frame2, var_text_color, 'тёмно-красный','зелёный','цвет морской волны','синий','чёрный', 'ночной режим')
    listbox3.config(bg="#B0C4DE", width=17, bd = 0,font="Arial 15")
    listbox3["highlightthickness"] = 0
    listbox4 = OptionMenu(frame2, var_text_size, 15,20,25,30,35)
    listbox4.config(bg="#87CEEB", width=17, bd = 0,font="Arial 15")
    listbox4["highlightthickness"] = 0
    
    
    lab1.grid(row=5,column=1,columnspan=1, sticky=W)
    lab2.grid(row=6,column=1,columnspan=1, sticky=W)
    lab3.grid(row=7,column=1,columnspan=1, sticky=W)
    lab4.grid(row=8,column=1,columnspan=1, sticky=W)
    lab6.grid(row=10,column=1,columnspan=1, sticky=W)
    lab7.grid(row=11,column=1,columnspan=1, sticky=W)
    lab8.grid(row=12,column=1,columnspan=1, sticky=W)
    lab9.grid(row=13,column=1,columnspan=1, sticky=W)
    ent1.grid(row=6,column=2)
    ent2.grid(row=7,column=2)
    listbox1.grid(row=8,column=2)
    listbox2.grid(row=10,column=2)
    listbox3.grid(row=11,column=2)
    listbox4.grid(row=12,column=2)
    but_start.grid(row=14,column=1,columnspan=2)
    bb.grid(row=15,column=1,columnspan=2)

    data = from_file_to_dict()
    ent1.insert(0, data.get("t1"))
    ent2.insert(0, data.get("t2"))
    var_voice_helper.set(data.get("voice_helper"))
    var_count_of_approaches.set(data.get("count_approaches"))
    var_background_color.set(data.get("bg_color"))
    var_text_color.set(data.get("txt_color"))
    var_text_size.set(data.get("txt_size"))
    
 


def start_mode2():
    frame1.place_forget()
    frame2.place_forget()
    frame3.place_forget()
    frame6.pack(fill="both", expand=True, padx=0, pady=0)
    frame6.place(in_=root, anchor="c", relx=.5, rely=.5)
    b_start = Button(frame6, text="НАЧАТЬ", width=50, height=5, bg="#B0C4DE", border=0, command=start_audio2)
    b_start.grid(row=6, column=1, columnspan=7)
    b_stop = Button(frame6, text="CТОП", width=50, height=5, bg="#B0C4DE", border=0, command=stop_sound)
    b_stop.grid(row=6, column=8, columnspan=7)
    

def change_mode():
    if var_mode.get() == 1:
        start_mode1()
    elif var_mode.get() == 2:
        start_mode2()


def open_decription_window():

    frame3.pack(fill="both", expand=True, padx=0, pady=0)
    frame3.place(in_=root, anchor="c", relx=.5, rely=.5)

    poetry = "Режим 1:\nЕсли у вас близорукость — пользуйтесь таблицей на расстоянии не менее 2 метров. \n Если дальнозоркость — вблизи, на расстоянии чтения. \n Тренировка заключается в вождении глаз слево направо по строке, которую вы видите хуже всего. \n"
    poetry = poetry + " \n Режим 2:\n В данном режиме необходимо следовать аудиоинструкциям голосового помощника. \n Если упражение кажется вам непонятным, посмотрите на сопровождающую его картинку. \n Старайтесь не злоупотреблять подсказками на мониторе \n"
    text = Label(frame3, text=poetry, width=100, height=20, bg="#B0E0E6", fg='#2F4F4F', font="Courier 18")

    bb = Button(frame3, text="ВЕРНУТЬСЯ В ГЛАВОЕ МЕНЮ", width=100, height=5, bg="#B0C4DE", border=0, command=open_main_window)

    text.grid(row=1,column=1,columnspan=1)
    bb.grid(row=2,column=1,columnspan=1)



#процессы 
p_sound1 = Process(name="p_sound1",target=setting_audio_mode1)
p_sound2 = Process(name="p_sound2",target=setting_audio_mode2)
p1 = Process(name="p1",target=start_sound)
p2 = Process(name="p2",target=finish_sound)
p3 = Process(name="p3",target=lefty_sound)
p4 = Process(name="p4",target=righty_sound)
p5 = Process(name="p5",target=untitled111_sound)
p6 = Process(name ='p6', target=audio_sound2)

open_main_window()


