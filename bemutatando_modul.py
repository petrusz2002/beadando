import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class sajat_osztaly:
    def megjelenetes(*args):
        index =honap_cb.current()

        if index in range(2) or index == 11:
            showinfo(
                title='Téli hónapok',
                message=f'Választásod alapján ebben a hónapban születtél: {valasztott_honap.get()}!\n Jó hideg lehetett :,('
            )
        elif index in range(2,5):
            showinfo(
                title='Tavaszi hónapok',
                message=f'Választásod alapján ebben a hónapban születtél: {valasztott_honap.get()}!\n Szépen kinyílhattak a virágok!'
            )
        elif index in range(5,8):
            showinfo(
                title='Nyári hónapok',
                message=f'Választásod alapján ebben a hónapban születtél: {valasztott_honap.get()}!\n Nagyon meleg van ekkor!'
            )
        elif index in range(8,11):
            showinfo(
                title='Őszi hónapok',
                message=f'Választásod alapján ebben a hónapban születtél: {valasztott_honap.get()}!\n Jó kis szüreti időszakok :,)'
            )



root = tk.Tk()


root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox bemutatás')


lbl = ttk.Label(text="Melyik hónapban születtél?:")
lbl.pack(fill=tk.X, padx=5, pady=5)


valasztott_honap = tk.StringVar()
honap_cb = ttk.Combobox(root, textvariable=valasztott_honap)


honap_cb['values'] = ['Január','Február','Március',
                      'Április','Május','Június',
                      'Július','Augusztus','Szeptember',
                      'Október','November','December']


honap_cb['state'] = 'readonly'


honap_cb.pack(fill=tk.X, padx=5, pady=5)



def honap_valtozik(event):
    sajat_osztaly.megjelenetes()


honap_cb.bind('<<ComboboxSelected>>', honap_valtozik)

root.mainloop()