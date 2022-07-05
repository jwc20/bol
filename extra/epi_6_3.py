

def f(s: str) -> int:
    d = {"A":1, "B":2, "C":3, "D":4,"E":5,"F":6,"G":7,"H":8,
            "I": 9,"J": 10,"K": 11,"L": 12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,
            "S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,
            "AA":27, "BB":53, "CC":79, "DD":102,"EE":128,"FF":154,"GG":180,"HH":206,"II":230}
    #"JJ":256,"KK":282,"LL":308,"MM":334,"NN":360,"OO":386,"PP","QQ","RR","SS","TT","UU","VV","WW","XX","YY","ZZ"}

alph = ["AA", "BB", "CC", "DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO","PP","QQ","RR","SS","TT","UU","VV","WW","XX","YY","ZZ"]


for val, alphabet in enumerate(alph):
    val * 26
    print(val, alphabet)

