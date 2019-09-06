def main():
    
    regels = ""
    teller = 0
    lengte = 0.0

    bestand =  'atgcatgctagctagcctagctagcatcgta' #open('README.md')
    for line in bestand:
        regels = regels + line
        
    for letter in regels:
        print (letter)
        if letter == "g" or letter == "c":
            teller += 1
        if letter == "g" or letter == "c" or letter == "a" or letter == "t":
            lengte += 1
    
    gcperc =  (teller/lengte)*100
    
    print ("het GC-percentage is" , gcperc , "%. ")
    htmlrapport(gcperc, bestand)

def htmlrapport(gcperc, bestand):
    html_file = open("rapport.html", "w")
    gcperc = str(gcperc)
    html_file.write(gcperc)
    html_file.write(bestand)
    html_file.close()
    
main()
