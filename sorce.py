import os,subprocess,sys
from tempfile import gettempdir

tmp = str(gettempdir())
def priprema_skripte(loka,nare):
    lscrypt=loka+'scrypt.os1'
    file=open(lscrypt, "w+")
    file.write(nare)
    file.close()

lokacija_skripte=os.path.dirname(os.path.realpath(__file__))
lokacija_strigs=lokacija_skripte
lokacija_sumljivca=raw_input("Povuci i opali enter za datoteku koju treba analizirati:  ")
lista_puta = lokacija_sumljivca.split(os.sep)
ime_sumljivca=lista_puta[-1].replace('"', '')
ime_sumljivca=ime_sumljivca.split(".")
parametri=raw_input("napisi parametre za string ostavi prazo ako zelis standardno  :    ")

if not parametri:
    parametri = "-a -n 4 -nobanner"
    print parametri
    print( )
    odgovor = raw_input("dali zelis da tako ostane Y/N: ")
    if odgovor.lower() == 'n':
        parametri = raw_input("napisi parametre za string :    ")
    if odgovor.lower() == 'y':
        print(" ")

finalna_string =".\\strings.exe " + parametri + " " + lokacija_sumljivca
lokacija_spremanja_csv = lokacija_skripte+"\\"+ime_sumljivca[0]+".csv"
final_naredba = "cd "+lokacija_skripte+"; "+finalna_string+" | ConvertFrom-CSV -UseCulture | Export-CSV "+lokacija_spremanja_csv+" -NoTypeInformation"

#print(final_naredba)

priprema_skripte(lokacija_skripte, final_naredba)


lscrypt=tmp+'\\scrypt.ps1'
file=open(lscrypt, "w+")
file.write(final_naredba)
file.close()

p = subprocess.Popen(["powershell.exe", lscrypt], stdout=sys.stdout)