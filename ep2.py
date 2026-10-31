GRAVIDADE = 9.81
PI = 3.14159265358979323846

def ConvertAngulo(graus,PI):
    rad = (graus * (PI/180))
    return rad

def fatorial(x):
    return 1 if (x==1 or x==0) else x * fatorial(x - 1)

def ElevaFatorial(valor,indice):
    num = valor ** indice
    den = fatorial(indice)
    eq = num/den
    return eq
    
def seno(theta):
    '''
    Esta função aproxima o valor da função seno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do seno do ângulo theta.
    '''
    ang = ConvertAngulo(theta,PI)
    a = ang
    b = 3
    c = 1
    while ElevaFatorial(ang,b) > ((10)**(-10)): 
        c = (c)*(-1)
        u = (c) * ElevaFatorial(ang,b)
        a += u
        b += 2
    return a


def cosseno(theta):
    '''
    Esta função aproxima o valor da função cosseno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do cosseno do ângulo theta.
    '''
    ang = ConvertAngulo(theta,PI)
    a = 1
    b = 2
    c = 1
    while ElevaFatorial(ang,b) > ((10)**(-10)):
        c = (c)*(-1)
        u = (c) * ElevaFatorial(ang,b)
        a += u
        b += 2
    return a


def raizQuadrada(x):
    '''
    Esta função aproxima o valor da raiz quadrada de x, através da
    fórmula de recorrência r_0 = x e r_{n+1} = 1/2 (r_n+ x/r_n)
    enquanto o módulo da diferença entre os dois últimos valores
    calculados for maior que 1e-10.
    Entrada: O valor de x
    Saída: A aproximação da raiz quadrada de x.
    '''
    i = 1
    while abs(x - (i * i)) > ((10)**(-10)):
        p = (1/2)*(i + (x / i))
        i = p
    return i


def atualizaPosicao(x, y, vx, vy, dt):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    g = GRAVIDADE
    
    YA = y + vy * dt - (((g)*((dt)**2))/2)
    XA = x + vx * dt
    
    return XA, YA


def atualizaVelocidade(vx, vy, dt):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    g = GRAVIDADE
    
    VYA = ((vy) - (g)*(dt))
    VXA = vx
    
    return VXA, VYA


def distanciaPontos(x1, y1, x2, y2):
    '''
    Esta função calcula a distância entre dois pontos (x1, y1) e (x2, y2).
    Entrada: As coordenadas dos pontos do plano (x1, y1) e (x2, y2).
    Saída: A distância entre (x1, y1) e (x2, y2).
    '''
    DP = raizQuadrada(((x2 - x1)**2)+(y2 - y1)**2)
    
    return DP



def simulaLancamento (xpokebola, ypokebola, rb,
                      vlancamento, angulolancamento,
                      xpokemon, ypokemon, rp,
                      delta_t):
    '''
    Esta função simula o lançamento da bola até que ela capture o
    pokemon, ou atinja o chão.
    Entrada: Posição inicial da pokebola (xpokebola e ypokebola), em metros;
    Posição do pokemon (xpokemon e ypokemon), em metros;
    Velocidade escalar, em metros por segundo;
    e ângulo de lançamento, em graus;
    Os raios rb e rp, em metros;
    a granularidade de tempo delta_t usada na simulação, em segundos.
    Saída: Um booleano (True se o lançamento teve sucesso e acertou o 
    pokémon, ou False caso contrário), a menor distância do pokémon à
    pokébola e as coordenadas x e y da pokébola nesta posição mais próxima.
    '''
    
    
    VY = (vlancamento) * (seno(angulolancamento))
    VX = (vlancamento) * (cosseno(angulolancamento))
    PY = ypokebola
    PX = xpokebola
    captura = False

    db = distanciaPontos(xpokebola, ypokebola, xpokemon, ypokemon) - (rb+rp)
    
    menorX = 0
    menorY = 0
    
    DI = db
    
    while (not captura or DI > 0) and PY >=0:
        PX, PY = atualizaPosicao(PX, PY, VX, VY, delta_t)
        VX, VY = atualizaVelocidade(VX, VY, delta_t)
        DI = distanciaPontos(PX, PY, xpokemon, ypokemon) - (rb+rp)
        captura = DI <= rb + rp
        if DI < db:
            db = 0
            menorX = PX
            menorY = PY
    
    return captura, db, menorX, menorY





def main():
    xp = float(input("Digite a coordenada x do pokemon: "))
    yp = float(input("Digite a coordenada y do pokemon: "))
    #Complete o código da função principal.
    rp = float(input("Digite o raio do pokemon (> 0) em metros: "))
    rb = float(input("Digite o raio da pokebola (> 0) em metros: "))
    d = float(input("Digite a granularidade de tempo da simulacao em segundos: "))
    print("")
   
    
# Não altere o código abaixo:
if __name__ == "__main__":
    main()
