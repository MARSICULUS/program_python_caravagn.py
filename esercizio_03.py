class Date():
    def __init__(self, giorno, mese, anno):
        self.dd = giorno
        self.mm = mese
        self.yy = anno
    
    def __str__(self):
        return '{}/{}/{}'.format(self.dd, self.mm, self.yy)
    
    def __iter__(self):
        return self

    def __next__(self):
        #giorno corrente = copia

        #se sono all'ultimo mese
            #se sono all'ultimo giorno
                #aggiorno tutto
            #else aggirno il giorno
        #se sono a un mese di trenta giorni
            #se sono all'ultimo giorno
                #aggiorno mese e giorno
            #else aggiorno giorno
        #se sono in febbrario
            #se sono all'ultimo giorno
                #aggiorno mese e giorno
            #else aggiorno giorno
        #se sono a un mese di 31 giorni
            #se sono all'ultimo giorno
                #aggiorno mese e giorno
            #else aggiorno giorno

        #titorno il gioro corrente (copia)