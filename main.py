import tkinter as tk
import data
import sqlite3 as sql
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
con = sql.connect('money.db')
cur = con.cursor()
cur.execute("SELECT * FROM money WHERE id=(SELECT MAX(id) FROM money);")
one_result = cur.fetchall()
db_id = one_result[0][0]

def light_theme_f():
    window['bg'] = "#E8F0F2"
    lab['bg'] = "#E8F0F2"
    lab['fg'] = "#053742"
    lab_title['bg'] = "#E8F0F2"
    lab_title['fg'] = "#053742"
    dop_lab['bg'] = "#E8F0F2"
    dop_lab['fg'] = "#053742"
    ext_lab['bg'] = "#E8F0F2"
    ext_lab['fg'] = "#053742"
    lab_made_by['bg'] = "#E8F0F2"
    lab_made_by['fg'] = "#053742"

def dark_theme_f():
    window['bg'] = "#132C33"
    lab['bg'] = "#132C33"
    lab['fg'] = "#D8E3E7"
    lab_title['bg'] = "#132C33"
    lab_title['fg'] = "#D8E3E7"
    dop_lab['bg'] = "#132C33"
    dop_lab['fg'] = "#D8E3E7"
    ext_lab['bg'] = "#132C33"
    ext_lab['fg'] = "#D8E3E7"
    lab_made_by['bg'] = "#132C33"
    lab_made_by['fg'] = "#D8E3E7"

def btn_3_f():
    cur.execute("SELECT * FROM money WHERE id=(SELECT MAX(id) FROM money);")
    one_result = cur.fetchall()
    db_id = one_result[0][0]
    global today
    new_db_id = db_id + 1
    res = [(new_db_id, 'EUR', data.EUR, today)]
    lab['text'] = f'Текущий курс Евро {data.EUR}'
    cur.execute("SELECT * FROM money WHERE currency='EUR';")
    db_result = cur.fetchall()
    ext_lab['text'] = f'Прошлое значение курса: \n {db_result[len(db_result) - 1][3]} - {db_result[len(db_result) - 1][2]}'
    if data.EUR > db_result[len(db_result) - 1][2]:
        dop_lab['text'] = f"Курс увеличился на {data.EUR - db_result[len(db_result) - 1][2]}"
    elif data.EUR < db_result[len(db_result) - 1][2]:
        dop_lab['text'] = f"Курс уменьшился на {db_result[len(db_result) - 1][2] - data.EUR}"
    else:
        dop_lab['text'] = "Курс не изменился"
    cur.executemany("INSERT INTO money VALUES (?,?,?,?)", res)
    ext_lab.pack(pady=10)
    dop_lab.pack(pady=10)
    con.commit()


def btn_4_f():
    cur.execute("SELECT * FROM money WHERE id=(SELECT MAX(id) FROM money);")
    one_result = cur.fetchall()
    db_id = one_result[0][0]
    global today
    new_db_id = db_id + 1
    res = [(new_db_id, 'USD', data.USD, today)]
    lab['text'] = f'Текущий курс Доллара США {data.USD}'
    cur.execute("SELECT * FROM money WHERE currency='USD';")
    db_result = cur.fetchall()
    ext_lab['text'] = f'Прошлое значение курса: \n {db_result[len(db_result) - 1][3]} - {db_result[len(db_result) - 1][2]}'
    if data.USD > db_result[len(db_result) - 1][2]:
        dop_lab['text'] = f"Курс увеличился на {data.USD - db_result[len(db_result) - 1][2]}"
    elif data.USD < db_result[len(db_result) - 1][2]:
        dop_lab['text'] = f"Курс уменьшился на {db_result[len(db_result) - 1][2] - data.USD}"
    else:
        dop_lab['text'] = "Курс не изменился"
    cur.executemany("INSERT INTO money VALUES (?,?,?,?)", res)
    ext_lab.pack(pady=10)
    dop_lab.pack(pady=10)
    con.commit()


def btn_5_f():
    cur.execute("SELECT * FROM money WHERE id=(SELECT MAX(id) FROM money);")
    one_result = cur.fetchall()
    db_id = one_result[0][0]
    global today
    new_db_id = db_id + 1
    res = [(new_db_id, 'AUD', data.AUD, today)]
    lab['text'] = f'Текущий курс Австралийского доллара {data.AUD}'
    cur.execute("SELECT * FROM money WHERE currency='AUD';")
    db_result = cur.fetchall()
    ext_lab['text'] = f'Прошлое значение курса: \n {db_result[len(db_result) - 1][3]} - {db_result[len(db_result) - 1][2]}'
    if data.AUD > db_result[len(db_result) - 1][2]:
        dop_lab['text'] = f"Курс увеличился на {data.AUD - db_result[len(db_result) - 1][2]}"
    elif data.AUD < db_result[len(db_result) - 1][2]:
        dop_lab['text'] = f"Курс уменьшился на {db_result[len(db_result) - 1][2] - data.AUD}"
    else:
        dop_lab['text'] = "Курс не изменился"
    cur.executemany("INSERT INTO money VALUES (?,?,?,?)", res)
    ext_lab.pack(pady=10)
    dop_lab.pack(pady=10)
    con.commit()


def btn_20_f():
    cur.execute("SELECT * FROM money WHERE id=(SELECT MAX(id) FROM money);")
    one_result = cur.fetchall()
    db_id = one_result[0][0]
    global today
    new_db_id = db_id + 1
    res = [(new_db_id, 'CNY', data.CNY, today)]
    lab['text'] = f'Текущий курс Китайского Юаня {data.CNY}'
    cur.execute("SELECT * FROM money WHERE currency='CNY';")
    db_result = cur.fetchall()
    ext_lab['text'] = f'Прошлое значение курса: \n {db_result[len(db_result) - 1][3]} - {db_result[len(db_result) - 1][2]}'
    if data.CNY > db_result[len(db_result) - 1][2]:
        dop_lab['text'] = f"Курс увеличился на {data.CNY - db_result[len(db_result) - 1][2]}"
    elif data.CNY < db_result[len(db_result) - 1][2]:
        dop_lab['text'] = f"Курс уменьшился на {db_result[len(db_result) - 1][2] - data.CNY}"
    else:
        dop_lab['text'] = "Курс не изменился"
    cur.executemany("INSERT INTO money VALUES (?,?,?,?)", res)
    ext_lab.pack(pady=10)
    dop_lab.pack(pady=10)
    con.commit()


def btn_6_f():
    lab['text'] = "Введите куда хотите перевести рубль"
    btn_6.pack_forget()
    btn_7.pack_forget()
    btn_25.pack_forget()
    global btn_8
    global btn_9
    global btn_10
    btn_8.pack(pady=10)
    btn_9.pack(pady=10)
    btn_10.pack(pady=10)
    btn_21.pack(pady=10)


def btn_7_f():
    lab['text'] = "Введите что вы хотите перевести в рубль"
    btn_6.pack_forget()
    btn_7.pack_forget()
    btn_25.pack_forget()
    global btn_14
    global btn_15
    global btn_16
    global btn_23
    btn_14.pack(pady=10)
    btn_15.pack(pady=10)
    btn_16.pack(pady=10)
    btn_23.pack(pady=10)

def btn_25_f():
    lab['text'] = "Выберите валюты"
    btn_6.pack_forget()
    btn_7.pack_forget()
    btn_25.pack_forget()
    global btn_26
    global btn_27
    global btn_28
    global btn_29
    global btn_30
    global btn_31
    btn_26.pack(pady=10)
    btn_27.pack(pady=10)
    btn_28.pack(pady=10)
    btn_29.pack(pady=10)
    btn_30.pack(pady=10)
    btn_31.pack(pady=10)

def btn_26_f():
    lab['text'] = "Выберите операцию"
    btn_26.pack_forget()
    btn_27.pack_forget()
    btn_28.pack_forget()
    btn_29.pack_forget()
    btn_30.pack_forget()
    btn_31.pack_forget()
    btn_32.pack(pady=10)
    btn_33.pack(pady=10)

def btn_27_f():
    lab['text'] = "Выберите операцию"
    btn_26.pack_forget()
    btn_27.pack_forget()
    btn_28.pack_forget()
    btn_29.pack_forget()
    btn_30.pack_forget()
    btn_31.pack_forget()
    btn_34.pack(pady=10)
    btn_35.pack(pady=10)

def btn_28_f():
    lab['text'] = "Выберите операцию"
    btn_26.pack_forget()
    btn_27.pack_forget()
    btn_28.pack_forget()
    btn_29.pack_forget()
    btn_30.pack_forget()
    btn_31.pack_forget()
    btn_36.pack(pady=10)
    btn_37.pack(pady=10)

def btn_29_f():
    lab['text'] = "Выберите операцию"
    btn_26.pack_forget()
    btn_27.pack_forget()
    btn_28.pack_forget()
    btn_29.pack_forget()
    btn_30.pack_forget()
    btn_31.pack_forget()
    btn_38.pack(pady=10)
    btn_39.pack(pady=10)

def btn_30_f():
    lab['text'] = "Выберите операцию"
    btn_26.pack_forget()
    btn_27.pack_forget()
    btn_28.pack_forget()
    btn_29.pack_forget()
    btn_30.pack_forget()
    btn_31.pack_forget()
    btn_40.pack(pady=10)
    btn_41.pack(pady=10)

def btn_31_f():
    lab['text'] = "Выберите операцию"
    btn_26.pack_forget()
    btn_27.pack_forget()
    btn_28.pack_forget()
    btn_29.pack_forget()
    btn_30.pack_forget()
    btn_31.pack_forget()
    btn_42.pack(pady=10)
    btn_43.pack(pady=10)

def btn_32_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_32.pack_forget()
    btn_33.pack_forget()
    btn_32_ent.pack(pady=10)

def btn_32_ent_f():
    lab['text'] = f"{ent.get()} EUR - {float(ent.get())*round((data.EUR/data.USD),2)} USD"

def btn_33_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_32.pack_forget()
    btn_33.pack_forget()
    btn_33_ent.pack(pady=10)

def btn_33_ent_f():
    lab['text'] = f"{ent.get()} USD - {float(ent.get())*round((data.USD/data.EUR),2)} EUR"

def btn_34_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_34.pack_forget()
    btn_35.pack_forget()
    btn_34_ent.pack(pady=10)

def btn_34_ent_f():
    lab['text'] = f"{ent.get()} EUR - {float(ent.get())*round((data.EUR/data.AUD),2)} AUD"

def btn_35_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_34.pack_forget()
    btn_35.pack_forget()
    btn_35_ent.pack(pady=10)

def btn_35_ent_f():
    lab['text'] = f"{ent.get()} AUD - {float(ent.get())*round((data.AUD/data.EUR),2)} EUR"

def btn_36_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_36.pack_forget()
    btn_37.pack_forget()
    btn_36_ent.pack(pady=10)

def btn_36_ent_f():
    lab['text'] = f"{ent.get()} EUR - {float(ent.get())*round((data.EUR/data.CNY),2)} CNY"

def btn_37_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_36.pack_forget()
    btn_37.pack_forget()
    btn_37_ent.pack(pady=10)

def btn_37_ent_f():
    lab['text'] = f"{ent.get()} CNY - {float(ent.get())*round((data.CNY/data.EUR),2)} EUR"

def btn_38_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_38.pack_forget()
    btn_39.pack_forget()
    btn_38_ent.pack(pady=10)

def btn_38_ent_f():
    lab['text'] = f"{ent.get()} USD - {float(ent.get())*round((data.USD/data.AUD),2)} AUD"

def btn_39_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_38.pack_forget()
    btn_39.pack_forget()
    btn_39_ent.pack(pady=10)

def btn_39_ent_f():
    lab['text'] = f"{ent.get()} AUD - {float(ent.get())*round((data.AUD/data.USD),2)} USD"

def btn_40_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_40.pack_forget()
    btn_41.pack_forget()
    btn_40_ent.pack(pady=10)

def btn_40_ent_f():
    lab['text'] = f"{ent.get()} USD - {float(ent.get())*round((data.USD/data.CNY),2)} CNY"

def btn_41_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_40.pack_forget()
    btn_41.pack_forget()
    btn_41_ent.pack(pady=10)

def btn_41_ent_f():
    lab['text'] = f"{ent.get()} CNY - {float(ent.get())*round((data.CNY/data.USD),2)} USD"

def btn_42_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_42.pack_forget()
    btn_43.pack_forget()
    btn_42_ent.pack(pady=10)

def btn_42_ent_f():
    lab['text'] = f"{ent.get()} AUD - {float(ent.get())*round((data.AUD/data.CNY),2)} CNY"

def btn_43_f():
    lab['text'] = "Введите сумму"
    ent.pack(pady=10)
    btn_42.pack_forget()
    btn_43.pack_forget()
    btn_43_ent.pack(pady=10)

def btn_43_ent_f():
    lab['text'] = f"{ent.get()} CNY - {float(ent.get())*round((data.CNY/data.AUD),2)} AUD"

def btn_8_f():
    lab['text'] = "Введите сумму Рублей"
    btn_8.pack_forget()
    btn_9.pack_forget()
    btn_10.pack_forget()
    btn_21.pack_forget()
    global ent
    ent.pack(pady=10)
    btn_11.pack(pady=10)


def btn_9_f():
    lab['text'] = "Введите сумму Рублей"
    btn_8.pack_forget()
    btn_9.pack_forget()
    btn_10.pack_forget()
    btn_21.pack_forget()
    global ent
    ent.pack(pady=10)
    btn_12.pack(pady=10)


def btn_10_f():
    lab['text'] = "Введите сумму Рублей"
    btn_8.pack_forget()
    btn_9.pack_forget()
    btn_10.pack_forget()
    btn_21.pack_forget()
    global ent
    ent.pack(pady=10)
    btn_13.pack(pady=10)


def btn_21_f():
    lab['text'] = "Введите сумму Рублей"
    btn_8.pack_forget()
    btn_9.pack_forget()
    btn_10.pack_forget()
    btn_21.pack_forget()
    global ent
    ent.pack(pady=10)
    btn_22.pack(pady=10)


def btn_11_f():
    lab['text'] = f'{ent.get()} RUB - {round((float(ent.get()) / data.EUR), 2)} EUR'


def btn_12_f():
    lab['text'] = f'{ent.get()} RUB - {round((float(ent.get()) / data.USD), 2)} USD'


def btn_13_f():
    lab['text'] = f'{ent.get()} RUB - {round((float(ent.get()) / data.AUD), 2)} AUD'


def btn_22_f():
    lab['text'] = f'{ent.get()} RUB - {round((float(ent.get()) / data.CNY), 2)} CNY'


def btn_14_f():
    lab['text'] = "Введите сумму Валюты"
    btn_14.destroy()
    btn_15.destroy()
    btn_16.destroy()
    btn_23.destroy()
    global ent
    ent.pack(pady=10)
    btn_17.pack(pady=10)


def btn_15_f():
    lab['text'] = "Введите сумму Валюты"
    btn_14.destroy()
    btn_15.destroy()
    btn_16.destroy()
    btn_23.destroy()
    global ent
    ent.pack(pady=10)
    btn_18.pack(pady=10)


def btn_16_f():
    lab['text'] = "Введите сумму Валюты"
    btn_14.destroy()
    btn_15.destroy()
    btn_16.destroy()
    btn_23.destroy()
    global ent
    ent.pack(pady=10)
    btn_19.pack(pady=10)


def btn_23_f():
    lab['text'] = "Введите сумму Валюты"
    btn_14.destroy()
    btn_15.destroy()
    btn_16.destroy()
    btn_23.destroy()
    global ent
    ent.pack(pady=10)
    btn_19.pack(pady=10)


def btn_17_f():
    lab['text'] = f'{ent.get()} EUR - {round((float(ent.get()) * data.EUR), 2)} RUB'


def btn_18_f():
    lab['text'] = f'{ent.get()} USD - {round((float(ent.get()) * data.USD), 2)} RUB'


def btn_19_f():
    lab['text'] = f'{ent.get()} AUD - {round((float(ent.get()) * data.AUD), 2)} RUB'


def btn_24_f():
    lab['text'] = f'{ent.get()} CNY - {round((float(ent.get()) * data.CNY), 2)} RUB'


def btn_1_f():
    btn_1.pack_forget()
    btn_2.pack_forget()
    ligth_theme.pack_forget()
    dark_theme.pack_forget()
    global btn_3
    global btn_4
    global btn_5
    global btn_20
    btn_3.pack(pady=10)
    btn_4.pack(pady=10)
    btn_5.pack(pady=10)
    btn_20.pack(pady=10)
    global back_1
    back_1.pack(pady=10, side="bottom")


def btn_2_f():
    btn_1.pack_forget()
    btn_2.pack_forget()
    ligth_theme.pack_forget()
    dark_theme.pack_forget()
    lab['text'] = 'Введите способ конвертации'
    global btn_6
    global btn_7
    btn_6.pack(pady=10)
    btn_7.pack(pady=10)
    btn_25.pack(pady=10)
    back_1.pack(pady=10, side="bottom")


def back_1_f():
    btn_3.pack_forget()
    btn_4.pack_forget()
    btn_5.pack_forget()
    btn_6.pack_forget()
    btn_7.pack_forget()
    btn_8.pack_forget()
    btn_9.pack_forget()
    btn_10.pack_forget()
    btn_11.pack_forget()
    btn_12.pack_forget()
    btn_13.pack_forget()
    btn_14.pack_forget()
    btn_15.pack_forget()
    btn_16.pack_forget()
    btn_17.pack_forget()
    btn_18.pack_forget()
    btn_19.pack_forget()
    btn_20.pack_forget()
    btn_21.pack_forget()
    btn_22.pack_forget()
    btn_23.pack_forget()
    btn_24.pack_forget()
    btn_25.pack_forget()
    btn_26.pack_forget()
    btn_27.pack_forget()
    btn_28.pack_forget()
    btn_29.pack_forget()
    btn_30.pack_forget()
    btn_31.pack_forget()
    btn_32.pack_forget()
    btn_32_ent.pack_forget()
    btn_33.pack_forget()
    btn_33_ent.pack_forget()
    btn_34.pack_forget()
    btn_34_ent.pack_forget()
    btn_35.pack_forget()
    btn_35_ent.pack_forget()
    btn_36.pack_forget()
    btn_36_ent.pack_forget()
    btn_37.pack_forget()
    btn_37_ent.pack_forget()
    btn_38.pack_forget()
    btn_38_ent.pack_forget()
    btn_39.pack_forget()
    btn_39_ent.pack_forget()
    btn_40.pack_forget()
    btn_40_ent.pack_forget()
    btn_41.pack_forget()
    btn_41_ent.pack_forget()
    btn_42.pack_forget()
    btn_42_ent.pack_forget()
    btn_43.pack_forget()
    btn_43_ent.pack_forget()
    ent.pack_forget()
    back_1.pack_forget()
    ext_lab.pack_forget()
    dop_lab.pack_forget()
    btn_1.pack(pady=10)
    btn_2.pack(pady=10)
    ligth_theme.pack(pady=10)
    dark_theme.pack(pady=10)
    lab['text'] = 'Что вам нужно?'


window = tk.Tk()
window.title("Конвертер Валют")
window.geometry("500x750")
window['bg'] = "#E8F0F2"

lab_title = tk.Label(text="Конвертер Валют", bg="#E8F0F2", fg="#053742", font=(("Montserat"), 20))
lab = tk.Label(text="Что вам нужно?", bg="#E8F0F2", fg="#053742", font=(("Montserat"), 17))
ext_lab = tk.Label(text="", bg="#E8F0F2", fg="#053742", font=(("Montserat"), 12))
dop_lab = tk.Label(text="", bg="#E8F0F2", fg="#053742", font=(("Montserat"), 12))
ent = tk.Entry(bd=0, bg="#8FD6E1", fg="#053742", width=46)
ligth_theme = tk.Button(text="Светлая тема", command=light_theme_f, bg="#51C4D3", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
dark_theme = tk.Button(text="Темная тема", command=dark_theme_f, bg="#126E82", fg="#D8E3E7", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
btn_1 = tk.Button(text="Узнать курс валюты", command=btn_1_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
btn_2 = tk.Button(text="Конвертировать валюту", command=btn_2_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)

btn_3 = tk.Button(text="Евро", command=btn_3_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
btn_4 = tk.Button(text="Доллар США", command=btn_4_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
btn_5 = tk.Button(text="Австралийский доллар", command=btn_5_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
btn_20 = tk.Button(text="Китайский Юань", command=btn_20_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)

btn_6 = tk.Button(text="Рубль -> Валюта", command=btn_6_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
btn_7 = tk.Button(text="Валюта -> Рубль", command=btn_7_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
btn_25= tk.Button(text="Валюта -> Валюта", command=btn_25_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)

btn_8 = tk.Button(text="Евро", command=btn_8_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
btn_9 = tk.Button(text="Доллар США", command=btn_9_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                  borderwidth=0, width=25, height=2)
btn_10 = tk.Button(text="Австралийский доллар", command=btn_10_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_21 = tk.Button(text="Китайский Юань", command=btn_21_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)

btn_11 = tk.Button(text="Ввод", command=btn_11_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_12 = tk.Button(text="Ввод", command=btn_12_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_13 = tk.Button(text="Ввод", command=btn_13_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_22 = tk.Button(text="Ввод", command=btn_22_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)

btn_14 = tk.Button(text="Евро", command=btn_14_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_15 = tk.Button(text="Доллар США", command=btn_15_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_16 = tk.Button(text="Австралийский доллар", command=btn_16_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_23 = tk.Button(text="Китайский Юань", command=btn_23_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)



btn_17 = tk.Button(text="Ввод", command=btn_17_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_18 = tk.Button(text="Ввод", command=btn_18_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_19 = tk.Button(text="Ввод", command=btn_19_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)
btn_24 = tk.Button(text="Ввод", command=btn_24_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)

btn_26 = tk.Button(text="Евро / Доллар", command=btn_26_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_27 = tk.Button(text="Евро / Ав.доллар", command=btn_27_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_28 = tk.Button(text="Евро / Юань", command=btn_28_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_29 = tk.Button(text="Доллар / Ав.доллар", command=btn_29_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_30 = tk.Button(text="Доллар / Юань", command=btn_30_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_31 = tk.Button(text="Ав.доллар/ Юань", command=btn_31_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)


btn_32 = tk.Button(text="Евро -> Доллар", command=btn_32_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_32_ent = tk.Button(text="Ввод", command=btn_32_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_33 = tk.Button(text="Доллар -> Евро", command=btn_33_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_33_ent = tk.Button(text="Ввод", command=btn_33_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)

btn_34 = tk.Button(text="Евро -> Ав.Доллар", command=btn_34_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_34_ent = tk.Button(text="Ввод", command=btn_34_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_35 = tk.Button(text="Ав.Доллар -> Евро", command=btn_35_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_35_ent = tk.Button(text="Ввод", command=btn_35_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)

btn_36 = tk.Button(text="Евро -> Юань", command=btn_36_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_36_ent = tk.Button(text="Ввод", command=btn_36_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_37 = tk.Button(text="Юань -> Евро", command=btn_37_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_37_ent = tk.Button(text="Ввод", command=btn_37_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)

btn_38 = tk.Button(text="Доллар -> Ав.доллар", command=btn_38_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_38_ent = tk.Button(text="Ввод", command=btn_38_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_39 = tk.Button(text="Ав.доллар -> Доллар", command=btn_39_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_39_ent = tk.Button(text="Ввод", command=btn_39_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)

btn_40 = tk.Button(text="Доллар -> Юань", command=btn_40_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_40_ent = tk.Button(text="Ввод", command=btn_40_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_41 = tk.Button(text="Юань -> Доллар", command=btn_41_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_41_ent = tk.Button(text="Ввод", command=btn_41_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)

btn_42 = tk.Button(text="Ав.доллар -> Юань", command=btn_42_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_42_ent = tk.Button(text="Ввод", command=btn_42_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_43 = tk.Button(text="Юань -> Ав.доллар", command=btn_43_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)
btn_43_ent = tk.Button(text="Ввод", command=btn_43_ent_f, bg="#A2DBFA", fg="#053742", font=(("Montserat"), 11),
                   borderwidth=0, width=25, height=2)


back_1 = tk.Button(text="Назад", command=back_1_f, bg="#344FA1", fg="#A2DBFA", font=(("Montserat"), 14),
                   borderwidth=0, width=25, height=2)

lab_made_by = tk.Label(text="Made by Kozyrev Petr", bg="#E8F0F2", fg="#053742", font=(("Montserat"), 9))


lab_title.pack(pady=30)
lab.pack(pady=25)
btn_1.pack(pady=10)
btn_2.pack(pady=10)
ligth_theme.pack(pady=10)
dark_theme.pack(pady=10)
lab_made_by.pack(pady=10,side="bottom")

window.mainloop()
