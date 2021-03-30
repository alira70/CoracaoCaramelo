# The script of the game goes in this file.

# PERSONAGENS.
define c = Character("Caramelo", color="#FFCA33", image="Caramelo")
define l = Character("Lucimel", color="#FF33F6", image="Lucimel")
define j = Character("Jubileu", color="#FF3333", image="Jubileu")
define rr = Character("Robson Rogério", color="#1C0FDE", image="RR")
define m = Character("Laila", color="#645E2A", image="Laila")
define f = Character("Fateco", color="#4EC9C7", image="Fateco")
define lj = Character("Lucimel e Jubileu", color="#760B0B", image="LJ")
define cjl = Character("Caramelo, Lucimel e Jubileu", color="#0CD3C1", image="CJL")

# IMAGENS DOS PERSONAGENS


    # IMAGENS Caramelo

##image  tag_nomeDoPersonagem  atributo = "nome.extensão"

    # IMAGENS Mel

##image  tag_nomeDoPersonagem  atributo = "nome.extensão"

    # IMAGENS Jubileu
image  side Jubileu normal = im.Scale("images/Jubileu.png", 250, 250, xoffset=40, yoffset=25)
##image  tag_nomeDoPersonagem  atributo = "nome.extensão"

    # IMAGENS Robson Rogério
##image  tag_nomeDoPersonagem  atributo = "nome.extensão"

    # IMAGENS Laila
##image  tag_nomeDoPersonagem  atributo = "nome.extensão"

    # IMAGENS Fateco
##image  tag_nomeDoPersonagem  atributo = "nome.extensão"

#IMAGENS DE CENAS (BACKGROUNDS)

    #IMAGENS DA CASA
##image  casa daLaila = "nome.extensão"
##image  casa fateco = "nome.extensão"

    #IMAGENS DO BECO
##image  beco principal dia = "nome.extensão"
##image  beco principal noite = "nome.extensão"
##image  beco banquete dia = "nome.extensão"
##image  becos banquete noite = "nome.extensão"
##image  beco aleatorio dia = "nome.extensão"
##image  becos aleatorio noite = "nome.extensão"

    #IMAGENS DO GALPÃO
##image  galpao noite = "nome.extensão"

    #IMAGENS DO RUA PRINCIPAL
##image  rua principal dia = "nome.extensão"
##image  rua principal noite = "nome.extensão"

    #IMAGENS DO PRAÇA
##image  praca dia = "nome.extensão"
##image  praca noite = "nome.extensão"

    #IMAGENS DA CLINICA
##image  clinica vet dia = "nome.extensão"

# The game starts here.

label start:

    jump cena01_Abandono

label cena01_Abandono:

    c normal "cena 01"

    scene casa daLaila

    scene beco principal

    jump cena02_Nascimento

label cena02_Nascimento:

    c "cena 02"

    scene beco principal noite

    jump cena03_Cuidados

label cena03_Cuidados:

    c "cena 03"

    scene beco principal dia

    jump cena04_Morte

label cena04_Morte:

    c "cena 04"

    scene beco principal noite

    c "Mãe... mamãe? Acorda mamãe!"

    c "Preciso achar comida eu mesmo, a mamãe deve estar muito cansada"

    c "Mas, pra onde devo ir?"

    menu:

        "PRAÇA":
            jump  cena05_escolha01

        "GALPÃO":
            jump  cena05_escolha02

        "RUA PRINCIPAL":
            jump game_over

label cena05_escolha01:

    c "cena 05"

    scene praca noite

    c "Oi, meu nome é Caramelo."

    l normal "Oi Caramelo, meu nome é Lucimel, você viu meu humano por aí? Me perdi dele e agora não consigo mais encontra-lo."

    c "Eu te ajudo a achar, não se preocupe."

    jump cena06_escolha01

label cena05_escolha02:

    c "cena 05"

    scene galpao depoisDaRinha noite

    c "Você está bem? Parece muito machucado, eu sou o Caramelo e vou te ajudar!"
    j normal "Caramelo, eu preciso de curativos, você me ajuda a procurar? A propósito, meu nome é Jubileu. Entendeu?"
    c "Entendi... Ajudo sim Jubileu, vamos encontrar curativos pra te curar!"
    c "Vi uma praça aqui por perto"
    c "Se apoie em mim e vamos lá"

    jump cena06_escolha02

label cena06_escolha01:
    #nt: explorar melhor a mentalidade deles a partir da criação
    scene galpao depoisDaRinha noite

    c "cena 06"

    c "Você parece muito machucado precisa de ajuda?"

    j normal "Preciso de ajuda para achar curativos..."
    j normal "fui obrigado pelos humanos a lutar em uma rinha de cachorros"
    j normal "e acabei perdendo e sendo largado aqui pelo meu humano para morrer"
    j normal "meu nome é Jubileu."

    l normal "Jubileu, Caramelo e eu vamos te ajudar, esqueça que perdeu."
    l normal "Jubileu! Aguenta firme, entendeu?"

    c "Jubileu, consegue andar? Venha aqui, se apoia em um lado meu!"

    c "Mas, onde acharemos curativos a essa hora Luci?"

    menu:

        "PROCURAR NA PRAÇA":
            l normal "Na praça sempre tem algo nas lixeiras!"
            jump  cena07_praca

        "PROCURAR NOS BECOS":
            l normal "Em algum beco deve ter algo... em alguma lixeira!"
            jump  cena07_becos

        "PROCURAR NA RUA PRINCIPAL":
            l normal "Tem de tudo na rua principal!"
            jump game_over

label cena06_escolha02:

    scene praca noite

    c "Oi, eu sou o Caramelo e ele é o Jubileu, nós estamos procurando curativos pq o Jubileu está machucado, você quer vir junto?"
    l normal "Olá Caramelo e Jubileu, eu sou a Lucimel, ele parece bem mal mesmo"
    l normal "Eu estou procurando meu humano, mas vou com vocês, quem sabe não encontro ele pelo caminho."
    c "Mas, onde vamos achar um kit médico?"

    menu:

        "PROCURAR NA PRAÇA":
            l normal "Nas lixeiras dessa praça tem cada coisa inacreditável..."
            l normal "Podemos dar sorte!"
            jump  cena07_praca

        "PROCURAR NOS BECOS":
            l normal "Em algum beco dessa cidade... Vamos rápido!"
            jump  cena07_becos

        "PROCURAR NA RUA PRINCIPAL":
            l normal "Tem de tudo na rua principal!"
            jump game_over

label cena07_praca:

    scene praca noite

    # FUNC VASCULHAM AS LIXEIRAS

    j normal "Já me sinto bem melhor com esses curativos e vejam só como demos sorte, encontramos bastante comida, vamos dividir tudo."
    c "Cuidado Jubileu, minha mamãe comeu uma comida que encontrou em um dos becos, caiu adormecida e não acordou mais."
    l normal "Que triste Caramelo, sinto muito por sua mamãe."
    j normal "Eu também sinto muito Caramelo, mas não temos outra alternativa a não ser comer, estamos com muita fome."
    l normal "Não comam aqui, vamos voltar rapido para o galpao"
    j normal "Por que?! Estou com muita fome já"
    l normal "Explico no caminho, mas confie em mim"

    scene galpao noite

    menu:

        "Comer":
            $ veneno = True
            if veneno:
                jump game_over
            else:
                jump cena08

        "Não comer":
            jump cena08

label cena07_becos:

    scene becos noite

    # FUNC VASCULHAM AS LIXEIRAS

    j normal "Já me sinto bem melhor com esses curativos e vejam só como demos sorte, encontramos bastante comida, vamos dividir tudo."
    c "Cuidado Jubileu, minha mamãe comeu uma comida que encontrou em um dos becos, caiu adormecida e não acordou mais."
    l normal "Que triste Caramelo, sinto muito por sua mamãe."
    j normal "Eu também sinto muito Caramelo, mas não temos outra alternativa a não ser comer, estamos com muita fome."
    l normal "Não comam aqui, vamos voltar rapido para o galpao"
    j normal "Por que?! Estou com muita fome já"
    l normal "Explico no caminho, mas confie em mim"

    scene galpao noite

    menu:

        "Comer":
            $ veneno = True
            if veneno:
                jump game_over
            else:
                jump cena08

        "Não comer":
            jump cena08

label cena08:

    scene galpao noite

    j normal "Não falei Caramelo, podemos comer tudo que encontramos sem medo, comigo é assim, Jubileu não leu, o pau comeu!"
    #j normal "Caramelo? Acho que já dormiu..."

    jump dia02_cena01

label dia02_cena01:

    scene rua principal dia

    rr "Olha só... 3 dogs pulguentos."
    c "Quem disse isso? "
    lj normal "Não vejo mais ninguém aqui!"
    rr "Eu disse!"
    j normal "E quem é você?"
    rr "Como assim quem sou eu mano, sou o Robson Rogério, o pombo mais famoso de Osasco."
    c "Nunca ouvi falar."
    rr "Claro, o que 3 dogs pulguentos saberiam pru pru pru pru pru"
    j normal "Seu pombo mal-educado, é melhor calar a boca, pq eu sou o Jubileu não leu, o pau comeu!"
    rr "Jubileu?"
    j normal "SIM!"
    rr "Jubileu, você não sabe e nem eu pru pru pru pru pru"
    j normal "Seu pombo maldito!"
    rr "Pombo maldito não, já falei, Robson Rogério, o pombo mais famoso de Osasco. E se eu fosse você, ficaria esperto, pois posso cagar na sua cabeça pru pru pru pru pru"

    ## FUNC MINIGAME DE DESVIAR DO COCO DO RR

    c "Senhor Robson Rogério, o senhor poderia nos ajudar a encontrar comida? Estamos com muita fome."
    rr "Só pq você e essa cadelinha são bonitinhos, eu vou ajudar."
    rr "Vi um humano jogando uma pizza inteira, só não me lembro se foi no beco, na praça, ou na rua principal."
    rr "Se eu fosse vocês, iria procurar logo antes que mais alguém ache."
    l normal "Muito obrigado senhor Robson Rogério!"
    rr "Pru."
    j normal "Você disse pizza?! Vamos logo galera!"
    c "Mas, pra onde"

    menu:
        "PROCURAR NA PRAÇA":
            l normal "Vamos logo pra praça! Meu humano pode estar me esperando."
            j normal "... Vamos."
            $ cena = "praça"
            jump  dia02_cena02

        "PROCURAR NOS BECOS":
            c "Acho que minha mãe está em um beco..."
            c "Vamos procurar neles e ver se achamos ela também!"
            $ cena = "beco"
            jump  dia02_cena02

        "PROCURAR NA RUA PRINCIPAL":
            j normal "Vamos aproveitar que já estamos aqui e vasculhar os lixos dessa rua!"
            $ cena = "rua"
            jump dia02_cena02

label dia02_cena02:

    if cena == "praca":
        scene praca dia
    elif cena == "beco":
        scene beco dia
    elif cena == "rua":
        scene rua principal dia

    l normal "Agora sim vamos comer muito bem!"
    c "Lucimel, como foi que você se perdeu do seu humano?"
    l normal "Ele me chamou para um passeio de carro, fique tão feliz."
    l normal "Paramos na praça para brincar de bolinha, ele então jogou a bolinha para mim ir buscar."
    l normal "Mas, quando voltei, ele tinha sumido, só deu tempo de ver o carro indo embora sem mim, tentei correr atrás..."
    l normal "Porém, não consegui correr tão rápido assim."
    l normal "Claro que ele deve ter me esquecido aqui."
    j normal "Lucimel, sinto muito em te dizer isso, mas... você foi abandonada."
    l normal "Não fui não!"
    j normal "Existem humanos maus, eles nos tratam como se não tivéssemos sentimentos."
    j normal "Vejam o meu caso, fui obrigado a lutar em rinhas e quando perdi..."
    j normal "Fui largado para trás!"
    j normal "O seu humano te abandonou naquela praça Mel, mas não se preocupe,"
    j normal "Agora você tem a mim e ao Caramelo"
    j normal "Somos uma família"
    j normal "Ninguém irá nos separar nunca mais."
    l normal "Sim, somos uma família, não quero mais saber de humanos. Caramelo, qual a sua história?"
    c "Eu nasci no beco, só tinha minha mamãe, vivemos muito felizes por um tempo, até que um dia ela comeu uma comida estranha, dormiu e nunca mais acordou."
    j normal "Como eu disse garoto, existem humanos maus, sua mãe comeu comida envenenada. Alguns humanos deixam comidas envenenadas pelas ruas, para matar todos cachorros."
    c "Que malvados... minha mamãe também me contou que foi expulsa de casa sem motivo algum."
    l normal "Qual era o nome dela, Caramelo?"
    c "Laila..."
    j normal "Laila? Eu conheci uma Laila... por acaso sua mãe era a Laila Caramelo?"
    c "Sim, você conhecia ela?"
    j normal "Sim garoto, sua mãe foi o grande amor da minha vida. Éramos vizinhos, conversávamos o dia todo. As vezes nossos humanos deixavam a gente brincar juntos... até que de uma amizade, nos apaixonamos... um dia resolvemos fugir para viver nosso amor, mas nossos humanos nos pegaram e ficaram muitos bravos... não deixavam mais a gente se ver..."
    l normal "E o que aconteceu depois Jubileu?"
    j normal "Fui abandonado no galpão, até que um humano mal me achou e me obrigou a entrar na rinha e o resto, vocês já sabem..."
    c "Mas pq você foi abandonado? Só pq vc fugiu junto com a minha mamãe?"
    j normal "Não garoto, foi pq a Laila acabou ficando grávida e... espere, se você Caramelo é filho da Laila... você é meu filho, o filho que eu pensei que nunca iria conhecer!"
    rr "Dogs pulguentos, a carrocinha vem vindo pegar vocês, corre que é cilada bino pru!"

    # FUNC MINIGAME PERSEGUIÇÃO DA CARROCINHA

    $ win = True
    if win:
        jump dia02_cena03
    else:
        jump game_over



label dia02_cena03:

    scene rua principal dia

    c "Conseguimos fugir, estão todos bem?"
    j normal "CARAMELO!! OLHA A LUCIMEL!"
    l normal "O que tem eu?"
    #Lucimel é atropelada
    c "Lucimel!! Não faz isso com a gente..."
    c "Vamo! Se mexe!"
    c "Alguém ajuda!!"
    c "Jubileu, me ajuda a carregar ela para ali, ela ainda não morreu"
    j normal "Isso é hora pra fazer rima com meu nome? Ajudo sim"

    scene clinica vet dia
    f "Vejam só, cachorrinhos, eu sou o doutor Fateco e vocês quem são?"
    c "Por favor, nos ajude, nossa amiga se machucou e precisa de ajuda!"
    f "AUAUAUAUAU"
    j normal "Chamou minha mãe do quê?"
    f "Essa cadelinha parece machucada..."
    f "AUAUAUAUAU"
    f "Quer dizer... ENFERMEIRA PRECISAMOS LEVA-LA PARA A SALA DE OPERAÇÃO!"
    f "Podem ficar tranquilos, a amiga de vocês está bem!"
    c "Graças a Scoby-Doo, a Lucimel está bem!"
    f "Eu não costumo fazer isso... mas vocês me parecem cachorros de rua e sem donos. Senti uma ligação com vocês... será que vocês não gostariam de ser adotados por mim?"
    cjl "SIM."
    f "Não entendi o que vocês disseram, mas vou considerar como um sim! AU?"
    cjl "Esse cara é maluco..."

    jump dia03

label dia03:

    scene casa fateco

    l normal "Finalmente encontramos um humano que irá cuidar de nós."
    c "Sim, tivemos muita sorte em encontrar ele."
    j normal "Sim meu filho, agora mais do que nunca... somos uma família!"

    return

label game_over:

    c "GAME OVER"

    return
