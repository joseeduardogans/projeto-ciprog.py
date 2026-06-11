print ("{}[==============================]{}\n A CULTURA DA PAZ\n {}[==============================]{}")
escolha1 = input (" FASE 1\n Você é apenas um professor de geografia de uma universidade. \n Digite qualquer tecla...")
while escolha1 != "c":
    escolha1 = input("Você acha que teremos a paz no retorno da ditadura neste país?\n \n escolha alhuma das opções\n a) Provavelmente, pois a paz significa a conquista pela homogeanidade\n b) Não, pois o lado mais minoritário trará a paz\n c) Eu simplesmente não creio. A paz surge da cooperação e satisfação do bem comum.\n d) Talvez outros modos de governo trarão a paz\n\n")
    if escolha1 == "a":
        print ("\nNota 0. Antipacífico\n")
    elif escolha1 == "b":
        print ("\nNota 4. Não é exatamente assim, a paz não provém essencialmente da rebelião\n")
    else: print ("\nNota 7! Uma visão sensata, não quis recorrer\n")
if escolha1 == "c":
        print("\nParabéns! Nota 10, porque demonstrou realismo dignidade humana integralmente.\n")
        
        

escolha2 = input("Você acaba encontrando dois grupos de alunos brigando à força física contra o outro por motivos políticos...\n Digite Qualquer telca...")
while escolha2 != "b" :
    escolha2 = input ("O que você faz?\n\n escolha alguma das opções\n a) Agir de forma indiferente e sair \n b) Chame algum aluno mais próximo para conversar \n c) Apoiar totalmente um lado\n\n")
    if escolha2 == "a":
        print("\nNota 4. Você tomou a decisão relativamente comum, mas foi meio imprudente enquanto professor\n")
    else: print("\n Nota 0. Foi antiético e contra a cultura da paz\n")
if escolha2 == "b":
    print("\nParabéns! Nota 10, porque fez a boa atitude por pequenos passos : pelo mais próximo\n")
    
    
escolha3 = input ("FASE 3\n Após toda a confusão, o aluno na qual você dialogou teve uma visão melhor em como se ter postura e firmeza de suas opiniões e argumentações. Mas reconhece a dificuldade de manter um ambiente de diálogo pacífico.\n Digite qualquer letra...")
while escolha3 != "d":
    escolha3 = input ("Ele pergunta: Como eu irei suportar esta violência silenciosa? O que fazemos é o mal para eles, e o que eles fazem é o mal para nós\n escolha alguma das opções\n a) Apenas siga em frente com sua convicção e não se enfraqueça com as visões opostas, o ânimo provém também das batalhas\n b) Quanto mais você luta pelo o que acredita, mais encontrará a própria paz, pois somente ela que importa para você\n c) Você só conseguirá suportar se evitar algum contato com quem você despreza\n d) Criei coragem para as dificuldades da vida, assim também seja com quem é injusto com você. Se valoriza a justiça, execute ela com quem é injusto com você também, com respeito e dialogando cada premissa nas quais concordam e discordam")
    if escolha3 == "a":
        print("4 pontos. Foi motivacional, mas é meio problemático, pois pode se fechar muito das outras visões.")
    elif escolha3 == "b":
        print("2 pontos. Apesar da própria paz ser importante, ela não garante a paz mais universal que é com os outros. Está opção pode cair em soberba.")
    else: print("0 pontos. O mais problemático, já que, mesmo que não esteja incentivando o conflito explicitamente, a desunião pode gerar mais estranheza, preconceitos, preparando para um conflito mais violento.")
if escolha3 == "d":
    print("Nota 10 Parabéns! Escolheu o correto! porque a verdadeira paz está na compreensão e na justiça, mesmo diante do desconforto e do conflito indireto.")
