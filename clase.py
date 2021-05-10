
class FechaHora:
    __año : ''
    __mes = ''
    __dia = ''
    __minuto = ''
    __hora = ''
    __segundos = ''

    def __init__(self,año = '2020', mes = '1', dia = '1', hora = '0', minuto = '0', segundo = '0'):
       if int(año) < 2022:
        self.__año = año
       else:
         self.__año = 2020
       if int(mes) <= 12:
         self.__mes = mes
       else:
        self.__mes = 1
       if int(dia) <= 31:
        self.__dia = dia
       else:
        self.__dia = 1
       if int(hora) <= 24:
        self.__hora = hora
       else:
         self.__hora = 0
       if int(minuto) <= 60:
        self.__minuto = minuto
       else:
        self.__minuto = 0
       if int(segundo) <= 60:
        self.__segundos = segundo
       else:
         self.__segundos = 0
       if mes == 2 and dia > 28:
         if not año % 4 and (año % 100 or  not año % 400):
           self.__dia = 29
         else:
             self.__dia = 28
       if mes == 4 and dia == 31:
         self.__dia = 30
       if mes == 6 and dia == 31:
         self.__dia = 30
       if mes == 9 and dia == 31:
         self.__dia = 30
       if mes == 11 and dia == 31:
         self.__dia = 30


    def Mostrar(self):
     print(  'fecha :' + str(self.__dia)  + '/' + str(self.__mes) + '/' + str(self.__año) + '  hora :' + str(self.__hora) + 'h '+ str(self.__minuto) + 'm ' + str(self.__segundos) + 's' )
    def PonerEnHora(self,hora = 25, minuto = 61, segundo = 61):
        if int(hora) <= 24:
            self.__hora = hora
        if int(minuto) <= 60:
           self.__minuto = minuto
        if int(segundo) <= 60:
           self.__segundos = segundo
    def AdelantarHora(self, hora = 0, minuto = 0):
        self.__hora = int(self.__hora) + int(hora)
        self.__minuto = int(self.__minuto) + int(minuto)
        if self.__minuto > 60:
          self.__minuto =  self.__minuto - 60
          self.__hora = self.__hora + 1
          if self.__hora > 24:
            self.__hora =   self.__hora - 24
            self.__hora = self.__hora - 1
            self.__dia = self.__dia +1
            if self.__mes == 12:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
                if self.__mes > 12:
                  self.__mes =  self.__mes  - 12
                  self.__año = self.__año + 1
            elif self.__mes == 1:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 3:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 5:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 7:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 8:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 10:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 4:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 6:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 9:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 11:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 2:
              if self.__dia > 28:
                if not self.__año % 4 and (self.__año % 100 or not self.__año % 400):
                   if self.__dia == 29:
                     self.__mes = 2
                     self.__dia = 29
                   else:
                     self.__mes = 3
                     self.__dia = 1
                else:
                  self.__dia = self.__dia - 28
                  self.__mes = self.__mes + 1


    def __Add__(self, FechaHora):
        seg = FechaHora.__segundos + self.__segundos
        sumseg = 0
        if seg > 60:
          seg = seg - 60
          sumseg = 1
          self.__segundos = seg
        else:
          self.__segundos = seg
        summinu = 0
        minu = FechaHora.__minuto + self.__minuto + sumseg
        if minu > 60:
         minu = minu - 60
         summinu = 1
         self.__minuto = minu
        else:
         self.__minuto = minu
        horasuma = 0
        hora = FechaHora.__hora + self.__hora + summinu
        if hora > 24:
          horasuma = 1
          hora = hora - 24
          self.__hora = hora - 1
        else:
          self.__hora = hora
        sumames = 0
        mes = FechaHora.__mes + self.__mes
        if mes > 12:
          mes = mes - 12
          self.__mes = mes
          sumames = 1
        else:
          self.__mes = mes
        diasuma = 0
        dia = FechaHora.__dia + self.__dia + horasuma
        if mes == 1 and dia > 31:
          dia = dia - 31
          self.__dia = dia
          diasuma = 1
        else:
          self.__dia = dia
        if mes == 2 and dia > 28:
            if not self.__año % 4 and (self.__año % 100 or not self.__año % 400):
             dia = dia - 29
             self.__dia = dia
             diasuma = 1
            else:
             dia = dia - 28
             self.__dia = dia
             diasuma = 1
        else:
          self.__dia = dia
        if mes == 3 and dia > 31:
         dia = dia - 31
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        if mes == 4 and dia > 30:
         dia = dia - 30
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        if mes == 5 and dia > 31:
         dia = dia - 31
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        if mes == 6 and dia > 30:
         dia = dia - 30
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        if mes == 7 and dia > 31:
         dia = dia - 31
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        if mes == 8 and dia > 31:
         dia = dia - 31
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        if mes == 9 and dia > 30:
         dia = dia - 30
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        if mes == 10 and dia > 31:
         dia = dia - 31
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        if mes == 11 and dia > 30:
         dia = dia - 30
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        if mes == 12 and dia > 31:
         dia = dia - 31
         self.__dia = dia
         diasuma = 1
        else:
          self.__dia = dia
        suma = FechaHora.__año + self.__año
        self.__año = suma + sumames
        self.__mes = self.__mes + diasuma

    def __sub__(self, FechaHora):
      if self.__gt__(FechaHora) == 1:
       if self.__segundos >= FechaHora.__segundos:
           self.__segundos = self.__segundos - FechaHora.__segundos
       else:
        self.__segundos = (self.__segundos + 60) - FechaHora.__segundos
        self.__minuto = self.__minuto - 1
       if self.__minuto >= FechaHora.__minuto:
           self.__minuto = self.__minuto - FechaHora.__minuto
       else:
         self.__minuto = (self.__minuto + 60) - FechaHora.__minuto
         self.__hora = self.__hora - 1
       if self.__hora >= FechaHora.__hora:
         self.__hora = self.__hora - FechaHora.__hora
       else:
         self.__hora = (self.__hora + 24) - FechaHora.__hora
         self.__dia = self.__dia - 1
       if self.__dia >= FechaHora.__dia:
         self.__dia = self.__dia - FechaHora.__dia
       else:
         self.__dia = (self.__dia + 31) - FechaHora.__dia
         self.__mes = self.__mes - 1
       if self.__mes >= FechaHora.__mes:
         self.__mes = self.__mes - FechaHora.__mes
       else:
         self.__mes = (self.__mes + 12) - FechaHora.__mes
         self.__año = self.__año - 1
       if self.__año >= FechaHora.__año:
         self.__año = self.__año - FechaHora.__año

      else:
       print(' no se puede la fecha segunda es mayor a la primera, no existe fecha negativa ')

    def __gt__(self, FechaHora):
        mayor = 0
        if self.__año > FechaHora.__año:
            mayor = 1
        elif   self.__año == FechaHora.__año:
          if self.__mes > FechaHora.__mes:
              mayor = 1
          elif self.__mes == FechaHora.__mes:
              if self.__dia > FechaHora.__dia:
                  mayor = 1
              elif self.__dia == FechaHora.__dia:
                if self.__hora > FechaHora.__hora:
                   mayor = 1
                elif self.__hora == FechaHora.__hora:
                  if self.__minuto > FechaHora.__minuto:
                    mayor = 1
                  elif self.__minuto == FechaHora.__minuto:
                    if self.__segundos > FechaHora.__segundos:
                      mayor = 1
        return mayor
