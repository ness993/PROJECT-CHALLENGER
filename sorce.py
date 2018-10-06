import os,subprocess,sys
from tempfile import gettempdir
# region Functions
def priprema_za_extrakciju_stringova_po_prethodno_generiranoj_naredbi(loka, nare):
    """
    Funkcija koja generira  file
    :param loka: Lokacija ps1 scripte koja ce se izvrsavti
    :param nare: puna naredba koja ce biti zapisana u scrpti
    :return: THE file
    """
    lscrypt=loka+'\\scrypt.ps1'
    narediti=nare
    file=open(lscrypt, "w")
    file.write(narediti)
    file.close()


#TODO funkcija pisanja yara pravila
#TODO provjera novih pravila za podudarnost na postojeca goodware and badware
    #TODO ako se podudara spremiti u bedware ako se ne podudara a znamo da je badware spremiti u badraew
    #TODO ako se ne podudara s badware i nemamo idicija da je badware spremiti u goodware
#TODO szcelje za prebacivanje goodware u badware i obratmno

# endregion
# region StartUp
tmp = str(gettempdir())
lokacija_skripte = os.path.dirname(os.path.realpath(__file__))
lokacija_strigs = lokacija_skripte
lokacija_sumljivca =raw_input("Povuci i opali enter za datoteku koju treba analizirati: ")
lista_puta = lokacija_sumljivca.split(os.sep)
ime_sumljivca=lista_puta[-1].replace('"', '')
ime_sumljivca=ime_sumljivca.split(".")
parametri=raw_input("napisi parametre za string ostavi prazo ako zelis standardno: ")

if not parametri:
    parametri = "-a -n 4 -nobanner"
    print parametri
    print("  ")
    odgovor = raw_input("dali zelis da tako ostane Y/N: ")
    if odgovor.lower() == 'n':
        parametri = raw_input("napisi parametre za string : ")
    if odgovor.lower() == 'y':
        print(" ")

finalna_string =".\\strings.exe " + parametri + " " + lokacija_sumljivca
lokacija_spremanja_csv = lokacija_skripte+"\\"+ime_sumljivca[0]+".csv"
final_naredba = "cd "+lokacija_skripte+"; "+finalna_string+" | ConvertFrom-CSV -UseCulture | Export-CSV "+lokacija_spremanja_csv+" -NoTypeInformation"
# endregion


priprema_za_extrakciju_stringova_po_prethodno_generiranoj_naredbi(tmp, final_naredba);

p = subprocess.Popen(["powershell.exe", tmp+'\\scrypt.ps1'], stdout=sys.stdout)




#TODO multi threding ako je moguce
