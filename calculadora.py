#!/usr/bin/python

import webapp
import random


class otroServidor(webapp.webApp):

    def parse(self, request):
    
        act = request.split()[0]
        rec = request.split()[1]
        if act == "GET":
            cuerpo = ''
        else:
            cuerpo = request.split()[-1]
        resp = (act, rec, cuerpo)
        return resp

    def process(self, parsedRequest):

        (act, rec, cuerpo) = parsedRequest
        if act == "GET":
            htmlCode = "200 OK"
            htmlAnswer = self.operacion + "=" + str(self.resultado)
        elif act == "PUT":
            rec = rec[1:]
            operandos = cuerpo.split(',')
            htmlCode = "200 OK"
            htmlAnswer = "Tu operacion se ha realizado correctamente./n"
            htmlAnswer = htmlAnswer + "Puedes consultarla haciendo un GET"
            if len(operandos) == 2:
                if rec == "suma":
                    try:
                        self.operacion = operandos[0] + "+" + operandos[1]
                        self.resultado = int(operandos[0])+int(operandos[1])
                    except ValueError:
                        htmlCode = "400 Bad Request"
                        htmlAnswer = "Operandos invalidos"
                elif rec == "resta":
                    try:
                        self.operacion = operandos[0] + "-" + operandos[1]
                        self.resultado = int(operandos[0])-int(operandos[1])
                    except ValueError:
                        htmlCode = "400 Bad Request"
                        htmlAnswer = "Operandos invalidos"                
                elif rec == "multiplicacion":
                    try:
                        self.operacion = operandos[0] + "*" + operandos[1]
                        self.resultado = int(operandos[0])*int(operandos[1])
                    except ValueError:
                        htmlCode = "400 Bad Request"
                        htmlAnswer = "Operandos invalidos"               
                elif rec == "division":
                    try:
                        self.operacion = operandos[0] + "/" + operandos[1]
                        self.resultado = int(operandos[0])/int(operandos[1])
                    except ValueError:
                        htmlCode = "400 Bad Request"
                        htmlAnswer = "Operandos invalidos"                    
                else:
                    htmlCode = "400 Bad Request"
                    htmlAnswer = "Solo se admiten las operaciones:/n/nsuma/n"
                    htmlAnswer = htmlAnswer + "resta/nmultiplicacion/ndivision"                    
            else:
                htmlCode = "400 Bad Request"
                htmlAnswer = "Solo se admiten dos operandos"
        else:
            htmlCode = "400 Bad Request"
            htmlAnswer = "Solo se admiten operaciones PUT y GET"
            
        return(htmlCode, htmlAnswer)


if __name__ == "__main__":
    serv = otroServidor("localhost", 1234)
