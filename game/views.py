import random
from django.shortcuts import render, redirect

def iniciar_jogo(request):
    """
    Inicializa o jogo e gera um número aleatório.
    """
    numero_aleatorio = random.randint(1, 100)  # Número a ser adivinhado
    tentativas = 0  # Inicializa o número de tentativas
    mensagem = "Tente adivinhar o número entre 1 e 100!"
    
    return render(request, 'game/jogar.html', {
        'numero_aleatorio': numero_aleatorio,
        'tentativas': tentativas,
        'mensagem': mensagem
    })


def jogar(request):
    """
    Processa o palpite do jogador e retorna a resposta.
    """
    if request.method == "POST":
        try:
            # Captura o palpite e os valores ocultos do formulário
            palpite = int(request.POST.get('palpite'))
            numero_aleatorio = int(request.POST.get('numero_aleatorio'))
            tentativas = int(request.POST.get('tentativas')) + 1  # Incrementa as tentativas

            print('palpite: ', palpite,'/', 'Correto: ', numero_aleatorio)

            # Verifica se o palpite está correto, muito alto ou muito baixo
            if palpite < numero_aleatorio:
                mensagem = "Muito baixo! Tente novamente."
            elif palpite > numero_aleatorio:
                mensagem = "Muito alto! Tente novamente."
            else:
                return render(request, 'game/vitoria.html', {
                    'numero_aleatorio': numero_aleatorio,
                    'tentativas': tentativas,
                })

        except (ValueError, TypeError):
            # Caso ocorra algum erro na conversão dos valores
            mensagem = "Por favor, insira um valor válido!"
            numero_aleatorio = random.randint(1, 100)
            tentativas = 0

        # Retorna os dados para o template com as tentativas atualizadas
        return render(request, 'game/jogar.html', {
            'numero_aleatorio': numero_aleatorio,
            'tentativas': tentativas,
            'mensagem': mensagem
        })

    # Se não for POST, redireciona para iniciar o jogo
    return redirect('iniciar_jogo')
