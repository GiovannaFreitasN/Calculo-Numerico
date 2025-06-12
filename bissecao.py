import numpy as np
from matplotlib import pyplot 
import main
print("===========================Método da Bisseção===========================")
print("========================================================================")
# Definição do intervalo [a, b] e parâmetros de precisão

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
if a >= b:
    print("Erro! O valor de a deve ser menor que o valor de b.")
    exit()
if a == b:
    print("Erro! O valor de a não pode ser igual ao valor de b.")
    exit()
if a < 0 or b < 0:
    print("Erro! O valor de a e b devem ser maiores que zero.")
    exit()
epsilon = abs(float(input("Digite o valor de epsilon (precisão): ")))
maxIter = int(input("Digite o número máximo de iterações: "))

f_expr = input("Digite a função f(x) (use 'x' como variável): ")

## Método da Bisseção

def f(x):
    return eval(f_expr)

def bissecao(f, a, b, epsilon, maxIter = 50):
    """Executa o método da bisseção para achar o zero de f no intervalo 
       [a,b] com precisão epsilon. O método executa no máximo maxIter
       iterações.
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    ## Inicializa as variáveis Fa e Fb com os valores de f(a) e f(b), 
    ## respectivamente.
    Fa = f(a)
    Fb = f(b)
    
    ## Teste para saber se a função muda de sinal. Se não mudar, mostrar
    ## mensagem de erro
    if Fa * Fb > 0:
        ## Mostrar mensagem
        print("Erro! A função não muda de sinal, ou seja não há raiz no intervalo [%e, %e]." % (a, b))
        return (True, None)
    
    ## Mostra na tela cabeçalho da tabela
    print("k\t  a\t\t  fa\t\t  b\t\t  fb\t\t  x\t\t  fx\t\tintervX")
    
    ## Inicializa tamanho do intervalo intervX usando a função abs, x e Fx
    intervX = abs(b - a)
    x = (a + b) / 2
    Fx = f(x)
    
    ## Mostra dados de inicialização
    print("-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (a, Fa, b, Fb, x, Fx, intervX))
    
    ## Teste se intervalo já é do tamanho da precisão e retorna a raiz sem erros
    if intervX <= epsilon:
        print("Intervalo já é menor que a precisão.")
        return (False, x)
    
    ## Iniciliza o k
    k = 1
    
    ## laço
    while k <= maxIter:
        ## Se a função não mudar de sinal entre a e x, então atualiza o a e Fa. 
        ## Senão, atualiza o b e Fb
        if Fa * Fx < 0:
            a = x
            Fb = Fx
        else:
            b = x
            Fa = Fx
        ## Atualiza intervX, x, e Fx
        
        intervX = abs(b - a)
        x = (a + b) / 2
        Fx = f(x)

        ## Mostra valores na tela
        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(k, a, Fa, b, Fb, x, Fx, intervX))
        
        ## Teste do critério de parada (usando apenas o tamanho do intervalo)
        
        if (intervX <= epsilon):
            ## Se o intervalo já é menor que a precisão, retorna a raiz
            print("Intervalo já é menor que a precisão.")
            return (False, x)

        ## Incrementa o k
        k = k+1
    ## Se chegar aqui é porque o número máximo de iterações foi atingido
    ## Mostrar uma mensagem de erro e retorna que houve erro e a última raiz encontrada
    print("ERRO! número máximo de iterações atingido.")
    return (True, x)

(houveErro, raiz) = bissecao(f, a, b, epsilon, maxIter)

if houveErro:
    print("Houve erro na execução do método da bisseção.")
else:
    print("Raiz encontrada: %e" % (raiz))
    print("Valor da função na raiz: %e" % (f(raiz)))
    print("Número de iterações: %d" % (maxIter))
    print("Intervalo final: [%e, %e]" % (a, b))

"""
# Plotando o gráfico da função
x_values = np.linspace(a - 1, b + 1, 100)
y_values = f(x_values)
pyplot.plot(x_values, y_values, label='f(x)')
pyplot.axhline(0, color='black', lw=0.5, ls='--')
pyplot.axvline(raiz, color='red', lw=0.5, ls='--', label='Raiz encontrada')
pyplot.title('Gráfico da Função f(x)')
pyplot.xlabel('x')
pyplot.ylabel('f(x)')
pyplot.legend()
pyplot.grid()
pyplot.show()
"""

print("========================================================================")
# Retornando ao menu principal

main.menu()

# O código acima implementa o método da bisseção para encontrar raízes de uma função
# definida pelo usuário em um intervalo [a, b]. Ele inclui verificações de erro para garantir que o intervalo seja válido e que a função mude de sinal.
# Após a execução, o programa exibe uma tabela com os resultados de cada iteração e plota o gráfico da função com a raiz encontrada.
# O usuário pode escolher sair do programa ou retornar ao menu principal.