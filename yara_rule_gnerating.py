import csv

def yaraGenerate(nizIzCsva, nazivPravila, tag, writer,thretlevle,description):
    """

    :param nizIzCsva: Lokacija csv datoteke
    :param nazivPravila: naziv pravila koje čemo generirati
    :param tag: tag malwera ako se korisiti ako ne nemoj pisati :<tag>
    :param wroter: ime pisca ili github luink
    :param thretlevle: od DEFCON 5(nije opsno) fp DEFCON 1(Tera Opasno)
    :return: File with yara rule
    rule <nameofrule>:tag{

        meta:
            $writer="Neno Horvat"
            $description = <some discription>
            $thretLvl=3
        strings:
            $string<number> = <stringFromNizIzCsva> ascii
            ...
            ...
            ...
        condition:
            all_of_them
    }
    """

    #todo rulewriter
    file=open(gde_spremiti_pravilo,'w+')
    prva_linija="rule "+nazivPravila+" "
    taG=": "+tag
    if tag:
        prva_linija=prva_linija+tag+" {"
    else:
        prva_linija=prva_linija+" {"
    file.write(prva_linija)
    file.write("")
    file.write("    meta:")
    file.write('        $writer ="'+writer+'"')
    file.write('        $descryption ="'+description+'"')
    file.write('        $thret_levle ="'+thretlevle+'"')
    file.write('    strings:')
    for x in range(0, len(nizIzCsva)):
        file.write('        $string'+x+' ="'+str(nizIzCsva[x]).replace("['","").replace("']", "").encode('hex')+' ascii')
    file.write('    condition:')
    file.write('        all of them ')



def yaraGenerate(lokacija_spremanja_csv, nazivpravila,tagmalwera,myName,ThretLevel):
    my_list=[]
    with open(lokacija_spremanja_csv, 'rb') as f:
        reader = csv.reader(f)
        my_list = list(reader)

    yaraGenerate(my_list,nazivpravila,tagmalwera,myName,ThretLevel)

   # file =open(lokacija_spremanja_csv,"r")


    #todo generiranje pravila po array upisivanja  i piasnje u datoteku
