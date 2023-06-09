import copy

def pocetniParametri():
    print("Unesite m")
    while True:
        m=input()
        try:
            m=int(m)
            break
        except:
            print("Nevalidna vrednost, unesite ceo broj!")
    print("Unesite n")
    while True:
        n=input()
        try:
            n=int(n)
            break
        except:
            print("Nevalidna vrednost, unesite ceo broj!")
    return (m, n)

def unesiKoordinate(matrica, smer, m, n):
    print("Unesite 'pomoc' ako zelite da vidite vase moguce poteze")
    while True:
        print("Unesite x,y")
        koordinate=input()
        if(koordinate == "pomoc"):
            print([potez[0] for potez in proveriMogucaStanja(matrica, smer, m, n)])
            continue
        koordinate=koordinate.split(",")
        try:
            x=int(koordinate[0])
            y=int(ord(koordinate[1].upper()))-64
            break
        except:
            print("Nevalidna vrednost, unesite koordinate kao: broj,slovo")
    return (x,y,smer)

def crtajSlova(n):
    print(" ", end = ' ')
    for i in range(65,65+n):
        print(chr(i), end = ' ')
    print(" ")

def crtajIvicu(n, f):
    print(" ", end = ' ')
    for i in range(n):
        print(f, end = ' ')
    print(" ")

def crtajRed(x,n,red):
    print(str(x)+"ǁ", end= '')
    for i in range(n-1):
        print(red[i] + "|", end='')
    print(red[n-1] + "ǁ"+str(x))

def crtajTablu(a):
    m=a[0]
    n=a[1]
    matrica=a[2]
    crtajSlova(n)
    crtajIvicu(n, "=")
    for x in range(m, 1, -1):
        crtajRed(x,n,matrica[x-1])
        crtajIvicu(n, "-")
    crtajRed(1,n, matrica[0])
    crtajIvicu(n, "=")
    crtajSlova(n)
    return a

def napraviMatricu(a):
    m=a[0]
    n=a[1]
    matrica=[]
    red=[]
    for i in range(m):
        for j in range(n):
            red.append(" ")
        matrica.append(red)
        red=[]
    return (a[0], a[1], matrica)

def proveriPotez(x, y, matrica, smer, m, n):
    if(x < 1 or y < 1 or x > m or y > n):
        print("Van table")
        return False
    if smer==True and x > m - 1:
        print("X je van table")
        return False
    if smer==False and y > n - 1:
        print("Y je van table")
        return False
    x=x-1
    y=y-1
    if smer==True and (matrica[x][y] != " " or matrica[x+1][y] != " "):
        print("Zauzeto X")
        return False
    if smer==False and (matrica[x][y] != " " or matrica[x][y+1] != " "):
        print("Zauzeto O")
        return False
    return True

def igrajPotez(koordinate,matrica,smer, m, n, igrac):
    x=koordinate[0]-1
    y=koordinate[1]-1
    if (proveriPotez(x+1, y+1, matrica, smer, m, n)):
        if smer==True:
            matrica[x][y]="X"
            matrica[x+1][y] = "X"
            smer = not smer
            igrac = not igrac
        else:
            matrica[x][y]="O"
            matrica[x][y+1] = "O"
            smer = not smer
            igrac = not igrac
        return (smer,igrac, pretvoriBrojUPotez(koordinate))
    return (smer,igrac)

def slobodanPotez(matrica, smer, m, n):
    if smer==True:
        for i in range(m-1):
            for j in range(n):
                if(matrica[i][j] == " " and matrica[i+1][j] == " "):
                    return True
    else:
        for i in range(m):
            for j in range(n-1):
                if(matrica[i][j] == " " and matrica[i][j+1] == " "):
                    return True
    return False

def pobednik(smer):
    if smer==True:
        print("Pobedio je O!")
    else:
        print("Pobedio je X!")        

def proveriMogucaStanja(matrica, smer, m, n):
    moguciPotezi=[]
    if smer==True:
        for i in range(m-1):
            for j in range(n):
                if(matrica[i][j] == " " and matrica[i+1][j] == " "):
                    moguciPotezi.append(((i+1,chr(65+j).upper()),(i+2,chr(65+j).upper())))
    else:
        for i in range(m):
            for j in range(n-1):
                if(matrica[i][j] == " " and matrica[i][j+1] == " "):
                    moguciPotezi.append(((i+1,chr(65+j).upper()),(i+1,chr(65+j+1).upper())))
    return moguciPotezi

def prviIgra():
    print("Unesite 'Da' ako želite prvi da igrate, ili 'Ne' ako želite da prvi igra računar.")
    while True:
        m=input()
        if (m.upper()=="DA"):
            print("Prvi igra čovek.")
            return True
        elif(m.upper()=="NE"):
            print("Prvi igra računar.")
            return False
        else:
            print("Nevalidna vrednost!")

def koJePobednik(smer):
    if smer == True:
        return 100
    return -100

def oceniPotez(matrica, potezi, m, n):
    pomMatrica = copy.deepcopy(matrica)
    i, j, smer = pretvoriPotezUBroj(potezi[0])
    i=i-1
    j=j-1
    for potez in potezi:
        ii, jj, smerr = pretvoriPotezUBroj(potez)
        ii=ii-1
        jj=jj-1

        if smerr:
            pomMatrica[int(ii)][int(jj)]=" "
            pomMatrica[int(ii+1)][int(jj)]=" "
        else:
            pomMatrica[int(ii)][int(jj)]=" "
            pomMatrica[int(ii)][int(jj+1)]=" "

    razlika = oceniStanje(pomMatrica, not smer, m, n) - oceniStanje(matrica, not smer, m, n)   
    sigurniPotezi = 0
    vrednostSigurnogPoteza = 1

    if smer:
        # ovo je ako je drugi sa leve strane
        if (j==1):
            if (matrica[i][j-1] == " " and matrica[i+1][j-1] == " "):
                sigurniPotezi += vrednostSigurnogPoteza
            if (n == 3):
                if (matrica[i][j+1] == " " and matrica[i+1][j+1] == " "):
                    sigurniPotezi += vrednostSigurnogPoteza
            elif (n>3):
                if (matrica[i][j+2] != " " and matrica[i+1][j+2] != " "):
                    if (matrica[i][j+1] == " " and matrica[i+1][j+1] == " "):
                        sigurniPotezi+=vrednostSigurnogPoteza    
        # ovo je ako je drugi od pozadi
        if (n > 3 and j == n-2):
            if (matrica[i][j+1] == " " and matrica[i+1][j+1] == " "):
                sigurniPotezi += vrednostSigurnogPoteza
            if (matrica[i][j-2] != " " and matrica[i+1][j-2] != " "):
                if (matrica[i][j-1] == " " and matrica[i+1][j-1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza
        #ovo je ako je u sredinu
        if ( j > 2 and j < n-2):
            if (matrica[i][j-2] != " " and matrica[i+1][j-2] != " "):
                if (matrica[i][j-1] == " " and matrica[i+1][j-1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza
            if (matrica[i][j+2] != " " and matrica[i+1][j+2] != " "):
                if (matrica[i][j+1] == " " and matrica[i+1][j+1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza   
        #ovo je ako je prvi
        if (j==0):
            if (matrica[i][j+2] != " " and matrica[i+1][j+2] != " "):
                if (matrica[i][j+1] == " " and matrica[i+1][j+1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza
        #ovo je ako je poslednji
        if (j==n-1):
            if (matrica[i][j-2] != " " and matrica[i+1][j-2] != " "):
                if (matrica[i][j-1] == " " and matrica[i+1][j-1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza
    else:
        #ovo je ako drugi
        if (i==1):
            if (matrica[i-1][j] == " " and matrica[i-1][j+1] == " "):
                sigurniPotezi += vrednostSigurnogPoteza
            if (m == 3):
                if (matrica[i+1][j] == " " and matrica[i+1][j+1] == " "):
                    sigurniPotezi += vrednostSigurnogPoteza
            elif (m>3):
                if (matrica[i+2][j] != " " and matrica[i+2][j+1] != " "):
                    if (matrica[i+1][j] == " " and matrica[i+1][j+1] == " "):
                        sigurniPotezi+=vrednostSigurnogPoteza    
        # ovo je ako je drugi od pozadi
        if (m > 3 and i == m-2):
            if (matrica[i+1][j] == " " and matrica[i+1][j+1] == " "):
                sigurniPotezi += vrednostSigurnogPoteza
            if (matrica[i-2][j] != " " and matrica[i-2][j+1] != " "):
                if (matrica[i-1][j] == " " and matrica[i-1][j+1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza
        #ovo je ako je u sredinu
        if ( i > 2 and i < m-2):
            if (matrica[i-2][j] != " " and matrica[i-2][j+1] != " "):
                if (matrica[i-1][j] == " " and matrica[i-1][j+1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza
            if (matrica[i+2][j] != " " and matrica[i+2][j+1] != " "):
                if (matrica[i+1][j] == " " and matrica[i+1][j+1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza     
        #ovo je ako je prvi
        if (i==0):
            if (matrica[i+2][j] != " " and matrica[i+2][j+1] != " "):
                if (matrica[i+1][j] == " " and matrica[i+1][j+1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza
        #ovo je ako je poslednji
        if (i==m-1):
            if (matrica[i-2][j] != " " and matrica[i-2][j+1] != " "):
                if (matrica[i-1][j] == " " and matrica[i-1][j+1] == " "):
                    sigurniPotezi+=vrednostSigurnogPoteza
    return razlika + sigurniPotezi 

def igrajMinMax(potez, matrica, m, n, smer, igrac):
    pomMatrica = copy.deepcopy(matrica)
    igrajPotez(pretvoriPotezUBroj(potez), pomMatrica, smer, m, n, igrac)
    return pomMatrica

def max_value(matrica, dubina, alpha, beta, smer, igrac, m, n, potezi = [], potez=None):
    if not slobodanPotez(matrica, smer, m, n):
        return (potez, koJePobednik(smer), smer)
    lista_poteza = proveriMogucaStanja(matrica, smer, m, n)
    if dubina == 0 or len(lista_poteza) == 0:
        return (potez, oceniPotez(matrica, potezi, m, n), smer)
    for s in lista_poteza:
        trenutniPotez = (s[0][0], s[0][1], smer)
        potezi.append(trenutniPotez)
        alpha = max(alpha, min_value(igrajMinMax(trenutniPotez, matrica, m, n, smer, igrac), dubina - 1, alpha, beta, not smer, igrac, m, n, potezi, (s[0][0], s[0][1], smer) if potez is None else potez), key = lambda x: x[1])
        potezi.remove(trenutniPotez)
        if alpha[1] >= beta[1]:
            return beta
    return alpha

def min_value(matrica, dubina, alpha, beta, smer, igrac, m, n, potezi = [], potez=None):
    if not slobodanPotez(matrica, smer, m, n):
        return (potez, koJePobednik(smer), smer)
    lista_poteza = proveriMogucaStanja(matrica, smer, m, n)
    if dubina == 0 or len(lista_poteza) == 0:
        return (potez, oceniPotez(matrica, potezi, m, n), smer)
    for s in lista_poteza:
        trenutniPotez = (s[0][0], s[0][1], smer)
        potezi.append(trenutniPotez)
        beta = min(beta, max_value(igrajMinMax(trenutniPotez, matrica, m, n, smer, igrac), dubina - 1, alpha, beta, not smer, igrac, m, n, potezi, (s[0][0], s[0][1], smer) if potez is None else potez), key = lambda x: x[1])
        potezi.remove(trenutniPotez)
        if beta[1] <= alpha[1]:
            return alpha
    return beta

def minimax_alpha_beta(matrica, dubina, igrac, smer, m, n, alpha=(None, -1000), beta=(None, 1000)):
    if not igrac:
        return max_value(matrica, dubina, alpha, beta, smer, igrac, m, n)
    else:
        return min_value(matrica, dubina, alpha, beta, smer, igrac, m, n)

def oceniStanje(matrica, smer, m, n):
    return len(proveriMogucaStanja(matrica, smer, m, n))

def pretvoriPotezUBroj(potez):
    return (int(potez[0]), int(ord(potez[1]))-64, potez[2])

def pretvoriBrojUPotez(broj):   
    return (int(broj[0]), chr(64 + broj[1]), broj[2])

def CovekCovek():
    print("Unesite 'Da' ako želite da igrate covek-covek, ili 'Ne' ako želite covek-racunar/racunar-covek.")
    while True:
        m=input()
        if (m.upper()=="DA"):
            print("Covek-covek.")
            return True
        elif(m.upper()=="NE"):
            print("Covek-racunar/racunar-covek.")
            return False
        else:
            print("Nevalidna vrednost!")

def igrajIgru():
    parametri=crtajTablu(napraviMatricu(pocetniParametri()))
    m=parametri[0]
    n=parametri[1]
    matrica=parametri[2]
    covekCovek = CovekCovek()
    if(not covekCovek):
        igrac=prviIgra()
    smer=True
    while slobodanPotez(matrica, smer, m, n):
        if(not covekCovek):
            SmerIgrac=igrajPotez(unesiKoordinate(matrica, smer, m, n) if igrac else pretvoriPotezUBroj(minimax_alpha_beta(matrica, 3, igrac, smer, m, n)[0]), matrica, smer, m, n, igrac)
        else:
            SmerIgrac=igrajPotez(unesiKoordinate(matrica, smer, m, n), matrica, smer, m, n, True)
        smer=SmerIgrac[0]
        igrac=SmerIgrac[1]
        crtajTablu((m,n,matrica))
        if len(SmerIgrac) > 2:
            print("Odigran je potez od strane " +  ("coveka: " if not igrac else "racunara: "), end="")
            print((SmerIgrac[2][0], SmerIgrac[2][1]))
    pobednik(smer)
    
igrajIgru()
