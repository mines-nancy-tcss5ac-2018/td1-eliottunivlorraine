#Exercice16

def solve16(n):
    somme  = 0
    Nbr  = 2**n
    for x in str(Nbr):
        somme += int(x)
    return somme

assert solve16(15) == 26
print(solve16(1000))

#Exercice22

def solve22():
    f = open('p022_names.txt', 'r')
    texte = f.read()
    Liste = texte.split(',')
    Liste_triée = sorted(Liste)
    for i in range(len(Liste_triée)):
        Somme = 0
        for x in Liste_triée[i][1:-1]:
            Somme += ord(x)-64
        Liste_triée[i] = Somme*(i+1)
    return sum(Liste_triée)

assert solve22() == 871198282
print(solve22())

#Exercice55    

def reverse(s):
    '''revoie "l'inverse" d'un nombre'''
    s_inv = ''
    for i in range(len(str(s))):
        s_inv  = s_inv + str(s)[-i-1]
    return s_inv

def pal(s):
    '''test si un nombre est un palindrome'''
    for i in range(len(str(s))):
        if str(s)[i] != str(reverse(s))[i]:
            return False
    return True

def Test(s):
    '''réalise le test du palindrome 50 fois'''
    for j in  range(50):
            if pal(s):
                return True
            else:
                s = str(int(s) + int(reverse(s)))
    return False

def solve55(n):
    '''test chaque nombre de 0 à n-1 pour savoir si c'est un nombre de Lychrel'''
    c = 0
    for i in range(n):
        a = str(i)
        if Test(a) == True:
            c = c + 1
    return 10000-c

print(solve55(10000))               
            

            
