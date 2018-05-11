from goto import with_goto

param = {}
var = {}
variables = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for v in variables:
    var[v] = ""

param["AFAM"] = 10844
param["AFECTOSALUDADIC"] = 10712
param["AFP"] = 199229
param["AFPSEG"] = 57577
param["AFPTASA"] = 2.89
param["AFPTOTAL"] = 228715
param["AGUINALDO"] = 0
param["ALIQ"] = 1781158
param["ANTCLIQCOM"] = 0
param["ANTCOMISIONES"] = 0
param["ANTI"] = 0
param["ANTICIPOAGUINALDO"] = 0
param["APAT"] = 18927
param["ASCCAF"] = 0
param["ASIGRETROACTIVA"] = 0
param["BC"] = 0
param["BI"] = 1992288
param["BONOESP"] = 0
param["BONORESUL"] = 0
param["BPE"] = 0
param["BT"] = 1621870
param["BTUTM"] = 35.0834
param["COMISIONES"] = 0
param["COSE"] = 2267124
param["COTFON"] = 0
param["CTA2"] = 0
param["DAF"] = 30
param["DCM"] = 30
param["DESCANTIC"] = 0
param["DESCTELEFONO"] = 0
param["DESCTOESPECIAL"] = 0
param["DESCVARIOS"] = 0
param["DESCVC"] = 864787
param["DESCVCP"] = 0
param["DGRAT"] = 0
param["DSCTOTARJETA"] = 0
param["DTMES"] = 30
param["DTMES1"] = 0
param["DTMES2"] = 0
param["DTMES3"] = 30
param["FPAFP"] = 228715
param["FPINP"] = 0
param["FS"] = 16016
param["HEXT"] = 0
param["HEXTA"] = 0
param["HEZAHORROCAF"] = 0
param["HREXT"] = 0
param["IP"] = 1.066672
param["IPP"] = 49311
param["MHV"] = 0
param["MHV_Previred"] = 0
param["MHVB"] = 0
param["MONAN"] = 864787
param["MONTOVACACIONES"] = 57664
param["OTRSNIMP"] = 0
param["PAGOVACACIONES"] = 0
param["PREST_CCAF"] = 0
param["PREST_CCAF_C001"] = 0
param["PRESTAMO"] = 0
param["RBONO"] = 0
param["RCOL"] = 85000
param["RGRAT"] = 104500
param["RHEXTA"] = 0
param["RISD"] = 2002057
param["RMOV"] = 85000
param["RSBM"] = 806500
param["RVALORSM"] = 10613
param["RVIATICO"] = 0
param["RVX001"] = 0
param["RVX002"] = 0
param["SALUD_L_MED"] = 0
param["SALUD_L_MEDA"] = 0
param["SALUD_L_MEDB"] = 0
param["SALUDADIC"] = 10712
param["SALUDCODSAFP"] = 0
param["SALUDINP"] = 0
param["SALUDISAPRE"] = 139460
param["SALUDOBLI"] = 139460
param["SALUDTOT"] = 150172
param["SD2"] = 48049
param["SDE"] = 32033
param["SDT"] = 12012
param["SDTE"] = 0
param["SEMCOR"] = 0
param["SG"] = 0
param["SINV_01"] = 28091
param["SINV_02"] = 29486
param["SL"] = 856447
param["TAFAM"] = 0
param["TD"] = 1315610
param["TGRAT"] = 104500
param["TH"] = 2172057
param["THIT"] = 2002057
param["THNINT"] = 170000
param["TI"] = 8
param["TINP"] = 0
param["TLS"] = 390899
param["TOPE_42"] = 139460
param["TOPE90UF"] = 2987117
param["TOPIMP"] = 1992288
param["TOTSALISA"] = 150172
param["TRAMOAFAM"] = "A"
param["TSL"] = 139460
param["VBONO"] = 0
param["VCOMISION"] = 1033393
param["VCPREMIO"] = 0
param["VIATICO"] = 0
param["VX001"] = 0
param["VX002"] = 0

@with_goto
def adic_salud():
    if param["VFCAL"] == 10:
        return
    if param["SALUDTIPO"] == "SI":
        var["A"] = param["SALUDVALOR"] * param["UFMES"]
    if param["SALUDTIPO"] == "PESOS":
        var["A"] = param["SALUDVALOR"]
    if param["SALUD_L_MED"] == "SI":
        var["A"] = var["A"] / 30
        var["A"] = var["A"] * param["DTMES"]
        goto .calculo
    if param["SALUDCODSAFP"] == 2:
        var["A"] = var["A"] / 30
        var["A"] = var["A"] * param["DTMES"]
    label .calculo
    if var["A"] > param["SALUDOBLI"]:
        param["SALUDADIC"] = var["A"] - param["SALUDOBLI"]
    #

