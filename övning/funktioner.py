def fruktpoäng(frukt):
    if frukt.lower()=="äpple":
        return 10
    elif frukt.lower()=="apelsin":
        return 5

äppelpoäng=fruktpoäng("ÄPpLE")
päronpoäng=fruktpoäng("APELSIN")

print(äppelpoäng+päronpoäng)
