import random

materia = [
    "Método dos Nós e Método das Barras\nEm uma estrutura com barras de treliça, usando o fato de que cada uma dessas barras corresponde a uma única incógnita (o escalar que dá o módulo e o sentido do par de forças), não adianta isolar uma barra e escrever suas equações de equilíbrio – elas já serão identicamente satisfeitas. Para essas estruturas há duas técnicas de abordagem. No chamado Método dos nós, as equações são obtidas impondo-se o equilíbrio dos nós (pontos de conexão das barras). No chamado Método das barras, a estrutura é seccionada (cortada) em subestruturas, impondo-se o equilíbrio de cada parte.",
    "Atrito seco de escorregamento\nLei estabelecida por Coulomb (modelo - caráterpuramente experimental): |F| ≤ μ|N|",
    "Lei fundamental da Hidrostática:\n“A pressão exercida por um líquido perfeito num ponto a uma profundidade h, sendo γ o peso específico desse líquido, é dada por:\np = p0 + γh\ncom p0 = pressão atuante na superfície do líquido”.",
    "Um sistema de forças distribuídas paralelas, aplicadas a uma superfície plana normal a elas, é equivalente a uma única força (a resultante) aplicada num ponto dessa superfície, que é a projeção normal do centro do volume das pressões sobre a mesma superfície.",
    
    "Forças distribuídas: são aquelas aplicadas a todos os pontos de um sistema material, ou parte dele (caso contínuo).\nPodem ser distribuídas sobre uma linha (modelo de fio sob a ação do vento), uma superfície (pressão de líquido) ou de um voluma (peso, forças eletromagnéticas).\nNote-se que não são, necessariamente, paralelas.",
    "Definição de equilíbrio:\nDizemos que um sistema está em equilíbrio em relação a um referencial (ou que as forças que nele atuam estão equilibradas) quando a ação total dessas forças é tal a manter o corpo em repouso, isto é, não produz no corpo, a partir do repouso, nenhuma variação de posição.", 
    "Momento: se considerarmos várias forças aplicadas em diversos pontos de um corpo, e outro ponto (polo) qualquer, ou eixo (reta orientada) qualquer, este sistema pode ter a tendência de fazer o corpo girar em torno daquele polo ou daquele eixo. O momento é a medida dessa tendência.",
    "Como já mencionado, a Mecânica como ciência se propõe a estudar o comportamento de corpos sob a ação de forças. Na Estática, o foco se dá nas situações de equilíbrio, ou seja, quando não há variações no tempo. Em geral, os problemas se referem a determinar esforços numa dada configuração do sistema, ou determinar a configuração num dado conjunto de esforços.",
]

def handleResponse(message) -> str:
    processedMessage = message.lower()
    
    if processedMessage == "!r insulto":
        return "Isso não é relatório!!!! Vc se acha muito espertinho?"
    
    if processedMessage == "!r roll":
        return "You rolled a " + str(random.randint(1, 6))
    
    if processedMessage == "!r bom_dia":
        return "Bom dia."
    
    if processedMessage == "!r motive":
        return "Você pode fazer melhor do que isso!!"
    
    if processedMessage == "!r materia":
        return materia[random.randint(0, len(materia) - 1)]
    
    if processedMessage == "!r help":
        return "Todos os comandos começam com !r. Os comandos são: \ninsulto \nbom_dia \nmotive \nmateria" 
    
    
    
    