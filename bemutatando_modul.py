import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class Kerdoiv:
    def megjelenetes(*args):
        showinfo(
            title='Eredmény',
            message=f'Ezt a hónapot választottad {valasztott_honap.get()}!'
        )



root = tk.Tk()

# képernyő létrehozása
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox bemutatás')

# label létrehozása
lbl = ttk.Label(text="Kérlek válassz egy hónapot:")
lbl.pack(fill=tk.X, padx=5, pady=5)

# combobox létrehozása
valasztott_honap = tk.StringVar()
honap_cb = ttk.Combobox(root, textvariable=valasztott_honap)


honap_cb['values'] = ["Január","Február","Március",
                      "Április","Május","Június",""
                      "Július","Augusztus","Szeptember",
                      "Október","November","December"]


honap_cb['state'] = 'readonly'

# elehelyezzük
honap_cb.pack(fill=tk.X, padx=5, pady=5)


# esemény amikor változik az érték
def month_changed(event):
    Kerdoiv.megjelenetes()


honap_cb.bind('<<ComboboxSelected>>', month_changed)

root.mainloop()