import requests
from lxml import html
import urllib.parse
import webbrowser

svilinkovi= []
pravilinkovi = []
jezici = ["Python","C", "C#", "C++", "Cpp", "Ruby", "Html", "Css", "Javascript", "Go"]
linkovisvihstranica = []

def googlesearch():
    r = requests.get("https://www.google.com/search?q=" + pinp)
    webpage = html.fromstring(r.content)

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
        print(link)


def programming():
    linkovisvihstranica.clear()
    stranice = ["https://www.google.com/search?q=site:geeksforgeeks.org " + pinp, "https://www.google.com/search?q=site:stackoverflow.com " + pinp, "https://www.google.com/search?q=site:w3schools.com " + pinp]
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
    google = "https://www.google.com/search?q=" + pinp
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
    print("Odgovori: ")
    for link in linkovisvihstranica:
        nula += 1
        if nula == 1:
            print("")
            print("geeksforgeeks.org")
        if "https://www.geeksforgeeks.org/" in link:
            if nula <=10:
                link1 = link.replace("https://www.geeksforgeeks.org/", "")
                link2 = link1.replace(link1[-1], "")
                for c in link2:
                    if c == "-":
                        link3 = link2.replace(c, " ")
                print(str(nula) + ": " + link3)
        if nula == 10:
            print("")
            print("stackoverflow.com")
        if "https://stackoverflow.com/questions/" in link:
            if nula <=20:
                link1 = link.replace("https://stackoverflow.com/questions/", "")
                link2 = link1.split("/")
                for c in link2[1]:
                    if c == "-":
                        link3 = link2[1].replace(c, " ")
                print(str(nula) + ": " + link3)
        if nula == 20:
            print("")
            print("w3schools.com")
        if "https://www.w3schools.com/" in link:
            if nula <= 30:
                link1 = link.replace("https://www.w3schools.com/", "")
                print(str(nula) + ": "+ link1)
        if nula == 30:
            print("")
            print("Google")
        if "w3schools" not in link:
            if nula >= 30:
                print(str(nula) + ": " + link)
    while True:
        try:
            otvori = input("Unesi broj (0): ")
            if otvori == "0":
                break
            brotvori = int(otvori) - 1
            webbrowser.open_new_tab(linkovisvihstranica[brotvori])
        except ValueError:
            print("mora da bude broj...")


if __name__ == '__main__':
    while True:
        inp = input("Pitaj: ")
        spl = inp.split()
        pinp = urllib.parse.quote(inp, safe='')
        if spl[0] == "potrazi":
            googlesearch()
        for j in jezici:
            for rec in spl:
                if rec == j:
                    programming()