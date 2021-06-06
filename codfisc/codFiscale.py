from datetime import date as dt


class CodFiscale:

    def __init__(self, cognome, nome, sesso, dataNascita,  luogoNascita='', nazioneNascita='ITALIA'):
        """Costruttore delle clase CodFiscale"""

        self.__cognome = cognome.upper()
        self.__nome = nome.upper()
        self.__sesso = sesso
        self.__dataNascita = dataNascita
        self.__nazioneNascita = nazioneNascita
        self.__luogoNascita = luogoNascita

    def __dividiConsVoc(self, cogNom):
        """Metodo private per separare consonanti e vocali in Cognoeme / Nome"""

        VOCALI = 'AEIOU'
        parteV = ''
        parteC = ''
        cogNom = cogNom.replace(" ", "")
        cogNom = cogNom.replace("'", "")

        for c in cogNom:
            if c not in VOCALI:
                parteC += c
            else:
                parteV += c
        return parteC, parteV

    def __restaParte(self, consonanti, vocali):
        """Metodo private per unire Consonanti +Vocali"""

        parte = consonanti + vocali
        parte = (parte.ljust(3, 'X'))[0:3]
        return parte

    def creaParteCognome(self):
        """Metodo public che restituisce Parte Cognome"""

        parteC, parteV = self.__dividiConsVoc(self.__cognome)
        return self.__restaParte(parteC, parteV)

    def creaParteNome(self):
        """Metodo public che restituisce Parte Nome"""

        parteC, parteV = self.__dividiConsVoc(self.__nome)
        lun = len(parteC)

        if lun >= 4:
            parteC = parteC[0:1] + parteC[2:3] + parteC[3:4]
            return parteC

        return self.__restaParte(parteC, parteV)

    def creaParteData(self):
        """Metodo public che restituisce Parte Data"""

        tbMese = {'gen': 'A', 'feb': 'B', 'mar': 'C', 'apr': 'D', 'mag': 'E', 'giu': 'H', 'lug': 'L', 'ago': 'M',
                  'set': 'P', 'ott': 'R', 'nov': 'S', 'dic': 'T'}

        if self.__sesso == 'F':
            gg = 40
        elif self.__sesso == 'M':
            gg = 0

        giorno = int(self.__dataNascita.strftime('%d')) + gg
        parteData = self.__dataNascita.strftime('%y') + tbMese[self.__dataNascita.strftime('%b')] + str(giorno).rjust(2, '0')

        return parteData

    def __cercaLuogo(self, file, luogo, indice):
        """Metodo privato per ricerca del codice Luogo o Nazione"""

        try:
            with open(file, encoding="ISO-8859-1") as fileLuogo:
                listaLuogo = fileLuogo.readlines()
                for ln in listaLuogo:
                    if ";" + luogo + ";" in ln:
                        codiceLuogo = ln.split(';')[indice]
                        return codiceLuogo
            return f"\033[91m Luogo {luogo} non trovato. Calcolo del CF sospeso \033[0m"

        except FileNotFoundError:
            mes = f"\033[91m File {file} non esistente. Calcolo del CF sospeso \033[0m. Verificare"
            print(mes)
            return mes  # Ritorna eventuale messaggio di errore per file listacomuni.txt o listaesteri.txt non esistente

    def creaParteLuogo(self):
        """Metodo public che restituisce codice Luogo"""

        if self.__nazioneNascita == 'ITALIA':
            return self.__cercaLuogo("data//listacomuni.txt", self.__luogoNascita, 6)
        else:
            return self.__cercaLuogo("data//listaesteri.txt", self.__nazioneNascita, 9)

    def __partePariDisp(self, car, p):
        """Metodo private che ricava la somma dei codici delle posizioni Pari e Dispari dei primi 15 caratteri del CF"""

        cf = f"{self.creaParteCognome()}{self.creaParteNome()+self.creaParteData()+self.creaParteLuogo()}"

        parametro = 0

        for i in range(p, len(cf), 2):
            for d in car:
                if cf[i] + ';' in d:
                    parametro += int(d.split(';')[1])
        return parametro  # Restitusce la somma dei codici dei caratteri in posizione Pari (p=1) e Dispari (p=0)

    def creaCin(self):
        """Metodo Public per calcolare il CIN del CF"""

        try:
            with open("data//CaratAlfaDispari.txt", encoding="ISO-8859-1") as fileDis:
                carDis = fileDis.readlines()
            with open("data//CaratAlfaPari.txt", encoding="ISO-8859-1") as filePar:
                carPar = filePar.readlines()
            with open("data//Resto.txt", encoding="ISO-8859-1") as fileRes:
                resto = fileRes.readlines()
        except FileNotFoundError as e:
            mes = f"\033[91m {str(e)} Calcolo del CF sospeso \033[0m. Verificare"
            print (mes)
            return mes

        codCin = (self.__partePariDisp(carPar, 1) + self.__partePariDisp(carDis, 0)) % 26

        dizResto={}

        for ln in resto:
            (key, val) = ln.split(';')
            dizResto[int(key)] = val
        return dizResto[codCin][:1]

    def stampaCF(self):
        """Metodo che ritorna il CF completo"""

        return f"{self.creaParteCognome()}{self.creaParteNome()}{self.creaParteData()}{self.creaParteLuogo()}{self.creaCin()}"
