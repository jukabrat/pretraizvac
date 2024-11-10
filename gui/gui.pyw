import requests
from lxml import html
import urllib.parse
import webbrowser
from customtkinter import *
import customtkinter as tk

svilinkovi= []
pravilinkovi = []
jezici = ["Python" , "C", "C#", "C++", "Cpp", "Ruby", "Html", "Css", "Javascript", "Go", "Php", "Sql", "Java", "Ruby"]
linkovisvihstranica = []

def googlesearch(result):
    r = requests.get("https://www.google.com/search?q=" + result)
    webpage = html.fromstring(r.content)
    x = 0
    y = 0
    a = webpage.xpath('//a/@href')

    for link in a:
        lstr = str(link)
        if "https" in lstr:
            novistr = lstr.replace("/url?q=", "")
            svilinkovi.append(novistr)

    for link in svilinkovi:
        if "google.com" not in link:
            pravilinkovi.append(link)
            if "youtube.com" in link:
                pravilinkovi.remove(link)
            else:
                result = str(link).split("&", 1)[0]
                pravilinkovi.remove(link)
                pravilinkovi.append(result)
    for link in pravilinkovi:
        def otvori_link(text):
            webbrowser.open_new_tab(text)
        kutija = CTkFrame(second_frame, 300, 300, corner_radius=15, fg_color="white", border_color="black", border_width=2)
        kutija.grid(row= 1 + x, column = 0 + y,sticky="nsew", padx = 20, pady = 10)
        labela = CTkLabel(kutija, text=link, text_color="black", font=Font_tuple, wraplength=250, fg_color="lightblue")
        labela.place(rely = 0.1, relx = 0.1)
        otvori = CTkButton(kutija, 100, 30, text="Otvori", fg_color="white",bg_color="white",text_color="black", border_color="black", border_width=2, hover_color="white", cursor = "hand2", command= lambda link = link: otvori_link(link))
        otvori.place(rely = 0.8, relx = 0.5, anchor = "center")
        y += 1
        if y > 5:
            x += 1
            y = 0
        

        
def programming(potrazi):
    x = 0
    y = 0
    def pravi_kocke(link3,link,stranica,x,y,boja):
        def otvori_link(text):
            webbrowser.open_new_tab(text)
        kutija = CTkFrame(second_frame, 300, 300, corner_radius=15, fg_color="white", border_color="black", border_width=2)
        kutija.grid(row= 1 + x, column = 0 + y,sticky="nsew", padx = 20, pady = 10)

        labela = CTkLabel(kutija, text=stranica, text_color="black", font=Font_tuple, wraplength=250, fg_color=boja, width=300)
        labela.place(rely = 0.1, relx = 0.5, anchor="center")
        labela2 = CTkLabel(kutija, text=link3, text_color="black", font=Font_tuple, wraplength=250)
        labela2.place(rely = 0.3, relx = 0.1)

        otvori = CTkButton(kutija, 100, 30, text="Otvori", fg_color="white",bg_color="white",text_color="black", border_color="black", border_width=2, hover_color="white", cursor = "hand2", command= lambda link = link: otvori_link(link))
        otvori.place(rely = 0.8, relx = 0.5, anchor = "center")
        
    linkovisvihstranica.clear()
    stranice = ["https://www.google.com/search?q=site:geeksforgeeks.org " + potrazi, "https://www.google.com/search?q=site:stackoverflow.com " + potrazi, "https://www.google.com/search?q=site:w3schools.com " + potrazi]
    for s in stranice:
        r = requests.get(s)
        webpage = html.fromstring(r.content)
        a = webpage.xpath('//a/@href')
        w3 = 0
        for link in a:
            w3 += 1
            if "google" not in link:
                if "ie=UTF-8&" not in link:
                    result = str(link).split("&", 1)[0]
                    link1 = result.replace("/url?q=", "")
                    linkovisvihstranica.append(link1)
                    if link == "/advanced_search":
                        linkovisvihstranica.remove(link)
                    if link1 == "/?sa=X":
                        linkovisvihstranica.remove(link1)
    google = "https://www.google.com/search?q=" + potrazi
    r = requests.get(google) 
    webpage = html.fromstring(r.content)
    a = webpage.xpath('//a/@href') 
    for link in a:
        if "/url?q=" in link:
            if "google.com" not in link:
                link1 = link.replace("/url?q=", "")
                result = str(link1).split("&", 1)[0]
                linkovisvihstranica.append(result)

    nula = 0
    for link in linkovisvihstranica:
        nula += 1
        if nula == 1:
            stranica = "geeksforgeeks.org"
        if "https://www.geeksforgeeks.org/" in link:
            if nula <=10:
                link1 = link.replace("https://www.geeksforgeeks.org/", "")
                link2 = link1.replace(link1[-1], "")
                for c in link2:
                    if c == "-":
                        link3 = link2.replace(c, " ")
                boja = "darkgreen"
                pravi_kocke(link3,link,stranica,x,y,boja)
                y += 1
                if y > 5:
                    x += 1
                    y = 0

        if nula == 10:
            stranica = "stackoverflow.com"
        if "https://stackoverflow.com/questions/" in link:
            if nula <=20:
                link1 = link.replace("https://stackoverflow.com/questions/", "")
                link2 = link1.split("/")
                for c in link2[1]:
                    if c == "-":
                        link3 = link2[1].replace(c, " ")
                boja = "orange"
                pravi_kocke(link3,link,stranica,x,y,boja)
                y += 1
                if y > 5:
                    x += 1
                    y = 0

        if nula == 20:
            stranica = "w3schools.com"
        if "https://www.w3schools.com/" in link:
            if nula <= 30:
                link1 = link.replace("https://www.w3schools.com/", "")
                boja = "green"
                pravi_kocke(link1,link,stranica,x,y,boja)
                y += 1
                if y > 5:
                    x += 1
                    y = 0
        if nula == 30:
            stranica = "Google search"
        if "w3schools" not in link:
            if nula >= 30:
                boja = "yellow"
                pravi_kocke(link,link,stranica,x,y,boja)
                y += 1
                if y > 5:
                    x += 1
                    y = 0


if __name__ == '__main__':
    root = CTk(fg_color="lightblue")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(str(width)+'x'+str(height))

    Font_tuple = ("Arial", 15, "normal") 
    main_frame = CTkFrame(root, fg_color="lightblue", bg_color="lightblue")
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = CTkCanvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = CTkScrollbar(main_frame, orientation="VERTICAL", command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    
    second_frame = CTkFrame(my_canvas, width = width, height=height, fg_color="lightblue")

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    my_canvas.bind(
    '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
)
    def razlaganje():
        for widget in second_frame.winfo_children():
            if str(widget) == ".!ctkframe.!ctkcanvas2.!ctkframe.!ctkentry" or str(widget) == ".!ctkframe.!ctkcanvas2.!ctkframe.!ctkbutton":
                pass
            else:
                widget.destroy()
        linkovisvihstranica.clear()
        pravilinkovi.clear()
        svilinkovi.clear()
        potrazi = str(user_input.get())
        spl = potrazi.split()
        if spl[0] == "potrazi":
            spl.remove("potrazi")
            result = ''.join(spl)
            googlesearch(result)
        else:
            for j in jezici:
                for rec in spl:
                    if rec == j:
                        programming(potrazi)

    user_input = tk.StringVar(second_frame)
    search = CTkEntry(second_frame, 300, 40, 5, textvariable=user_input)
    search.grid(column= 0, row = 0)

    potvrdi = CTkButton(second_frame, 120, 40, 5, text = "Search", command=razlaganje)
    potvrdi.grid(column = 1, row = 0)

    root.mainloop()