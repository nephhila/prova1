## Ola, prof Jamal :). Infelizmente meu teclado nao tem acentos pq esta habilitado p/ ENG e como era um programa 
## feito por nos eu decidi deixar do meu jeitinho, por isso ta escrito meio zoado kkkkkkk desculpa se nao puder
## eu poderia ter colocado o contador se eu quisesse muito, mas nao achei que ia ornar com o codigo que eu quis
## criar, por isso deixei sem mesmo. a seguir vou explicar meu codigo de forma resumida:
# o codigo funciona como uma especie de formulario curto que deseja conhecer o usuario que o responde, perguntando
# seu nome, sua idade, com qual campeao/personagem voce joga mais no jogo League Of Legends (lol) e qual a sua
# maestria com o campeao Yasuo (o qual muitas pessoas odeiam). tentei tornar o mais interativo possivel sem criar
# muitas variaveis, apenas conversando com os dados que o proprio usuario fornece. 

print ('quero te conhecer melhor, entao vamo la. me fala as seguintes coisas:')

r = 'ja falei que a maestria eh so 0, 4, 5, 6 ou 7 fi, fala de novo pra mim>'

for i in range (1):
    nome = input ('fala teu nome pra mim: ')
    print ('daora,', nome)

    idade = int (input ('agora sua idade: ')) 
    while idade>15:
        print ('voce nao acha que ta muito velho pra jogar esse joguinho de fada com', idade ,'anos, nao?')
        break
    if idade<=15:
        print (nome, 'sai desse jogo e vai ser adolescente direito, virar corote, sei la...')

    main = input ('ta, agora me fala seu main: ')
    print ('analise 🔎🐸 *julgando silenciosamente*')

    m = int (input ('qual sua maestria com yasuo no lol? (apenas 0, 4, 5, 6 ou 7!):'))
    while m != 0 and m != 4 and m != 5 and m != 6 and m != 7:
        print (r)
        m = int (input ('qual sua maestria com yasuo no lol? (apenas 0, 4, 5, 6 ou 7!):'))

    if m == 7:
        print ('simplesmente o cara que toma cafe gelado [voce me da medo, sai daqui seu esquisito]')
    elif m == 6:
        print ('se voce fosse um ser humano qual seria? *pergunta genuina*')
    elif m == 5:
        print ('nao por favor eu to te implorando [cara serio isso pode destruir familias]')
    elif m == 4:
        print ('para agora por favor enquando ha tempo')
    elif m == 0:
        print ('ufa voce ainda e gente :v)')
    else:
        print (r)

    print ('valeu ai meu mano <3, foi bom te conhecer,', nome)