class linea_funcion(object):

    def __init__(self, db):
        self.id = db["IDFormula"]
        self.linea = db["Linea"]
        self.sentencia = db["Sentencia"]
        self.tipo_param1 = db["TipoParam1"]
        self.param1 = db["Param1"]
        self.tipo_param2 = db["TipoParam2"]
        self.param2 = db["Param2"]
        self.tipo_param3 = db["TipoParam3"]
        self.param3 = db["Param3"]
        self.operador = db["Operador"]
        self.linea_destino = db["LineaDestino"]
        self.identicacion = db["Indentacion"]
        self.param_hist1 = db["ParaHis1"]
        self.param_hist2 = db["ParaHis2"]
        self.param_hist3 = db["ParaHis3"]
        # self.IDFormula = db.IDFormula
        # self.Linea = db.Linea
        # self.Sentencia = db.Sentencia
        # self.TipoParam1 = db.TipoParam1
        # self.Param1 = db.Param1
        # self.TipoParam2 = db.TipoParam2
        # self.Param2 = db.Param2
        # self.TipoParam3 = db.TipoParam3
        # self.Param3 = db.Param3
        # self.Operador = db.Operador
        # self.LineaDestino = db.LineaDestino
        # self.Indentacion = db.Indentacion
        # self.ParaHis1 = db.ParaHis1
        # self.ParaHis2 = db.ParaHis2
        # self.ParaHis3 = db.ParaHis3
    
    def __repr__(self):
        return self.methods[self.sentencia](self)

    def ETI(self):
        """
        ETIQUETA PARA EJECUTAR UN GOTO
        """
        sentencia = "label .{param1}".format(param1=self.param1)
        return sentencia

    def FIN(self):
        """
        FIN BLOQUE SI
        """
        return ""

    def HAC(self):
        """
        HACER ASIGNACION DE VALOR SEGUN OPERADOR
        """
        tipo_param = {
            "P":"param['{v}']",
            "V":"var['{v}']",
            "A":"{v}",
            "":""
        }

        param1 = tipo_param[self.tipo_param1].format(v=self.param1)
        param2 = tipo_param[self.tipo_param2].format(v=self.param2)
        param3 = tipo_param[self.tipo_param3].format(v=self.param3)

        sentencia = "{param1} = {param2} {operador} {param3}".format(
            param1=param1,
            param2=param2,
            param3=param3,
            operador=self.operador)

        return sentencia

    def IRA(self):
        """
        GOTO ALGUNA ETIQUETA PREVIAMENTE DEFINIDA
        """
        sentencia = "goto .{param1}".format(param1=self.param1)
        return sentencia

    def NUL(self):
        """
        COMENTARIO
        """
        sentencia = "# {param1}".format(param1=self.param1)
        return sentencia

    def SAL(self):
        """
        FINALIZA LA EJECUCIÓN DE LA FUNCIÓN
        """
        return "return"

    def SI(self):
        """
        SENTENCIA SI
        """
        tipo_param = {
            "P":"param['{v}']",
            "V":"var['{v}']",
            "A":"{v}",
            "":""
        }

        tipo_operador = {
            "=":"==",
            "<>":"!=",
            "<":"<",
            "<=":"<=",
            ">":">",
            ">=":">=",
            "":""
        }

        param1 = tipo_param[self.tipo_param1].format(v=self.param1)
        param2 = tipo_param[self.tipo_param2].format(v=self.param2)
        operador = tipo_operador[self.operador]

        sentencia = "if {param1} {operador} {param2}:".format(param1=param1, param2=param2, operador=operador)
        return sentencia

    methods = {
        "ETI":ETI,
        "FIN":FIN,
        "HAC":HAC,
        "IRA":IRA,
        "NUL":NUL,
        "SAL":SAL,
        "SI":SI
    }
