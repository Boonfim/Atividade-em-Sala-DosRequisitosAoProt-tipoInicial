"""
Requisito 2: para o sistema inicialmente, alunos e servidores devem reportar
as vagas manualmente (ocupando ou liberando), informando tipo de usuario,
tipo de veiculo e numero da vaga.
"""

from requisito3_validar_acesso import validar_acesso


def _escolher(mensagem, opcoes):
    opcoes_fmt = "/".join(opcoes)
    while True:
        escolha = input(f"{mensagem} ({opcoes_fmt}): ").strip().lower()
        if escolha in opcoes:
            return escolha
        print("Opcao invalida, tente novamente.")


def _buscar_vaga(vagas, numero):
    for vaga in vagas:
        if vaga["id"] == numero:
            return vaga
    return None


def reportar_vaga(vagas_carro, vagas_moto):
    """Fluxo interativo para reportar uma vaga como ocupada ou livre."""
    tipo_usuario = _escolher("Voce e", ["aluno", "servidor"])
    tipo_veiculo = _escolher("Tipo de veiculo", ["carro", "moto"])
    vagas = vagas_carro if tipo_veiculo == "carro" else vagas_moto

    try:
        numero = int(input(f"Numero da vaga de {tipo_veiculo}: ").strip())
    except ValueError:
        print("Numero invalido.")
        return

    vaga = _buscar_vaga(vagas, numero)
    if vaga is None:
        print("Vaga inexistente.")
        return

    acao = _escolher("Deseja", ["ocupar", "liberar"])

    if acao == "liberar":
        vaga["ocupada"] = False
        print(f"Vaga {numero} de {tipo_veiculo} liberada.")
        return

    if vaga["ocupada"]:
        print("Vaga ja esta ocupada.")
        return

    permitido, motivo = validar_acesso(vaga, tipo_usuario)
    if not permitido:
        print(f"BLOQUEADO: {motivo}")
        return

    vaga["ocupada"] = True
    print(f"Vaga {numero} de {tipo_veiculo} ocupada por {tipo_usuario}.")
