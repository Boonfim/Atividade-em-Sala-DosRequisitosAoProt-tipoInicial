"""
Requisito 1: o aplicativo deve mostrar as vagas disponiveis no estacionamento
em tempo real, isto e, o mapa exibido sempre reflete o ultimo estado
reportado pelos usuarios (ver requisito 2).
"""

VERDE = "\033[92m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

ROTULO_TIPO = {
    "normal": "N",
    "pcd": "P",
    "idoso": "I",
}


def _formatar_vaga(vaga):
    cor = VERMELHO if vaga["ocupada"] else VERDE
    rotulo = ROTULO_TIPO[vaga["tipo_vaga"]]
    marca_reserva = "*" if vaga["reservada_servidor"] else " "
    return f"{cor}[{vaga['id']:>2}{rotulo}{marca_reserva}]{RESET}"


def _imprimir_em_grade(vagas, por_linha=5):
    for inicio in range(0, len(vagas), por_linha):
        trecho = vagas[inicio:inicio + por_linha]
        print("  ".join(_formatar_vaga(v) for v in trecho))


def exibir_estacionamento(vagas_carro, vagas_moto):
    """Mostra o mapa quadriculado atual das vagas de carro e de moto."""
    print("\n===== ESTACIONAMENTO DO CAMPUS - MAPA ATUAL =====")
    print("verde=livre  vermelho=ocupada  N=normal P=PCD I=idoso  *=reservada servidor (biblioteca)\n")

    print("-- Carros --")
    _imprimir_em_grade(vagas_carro)

    print("\n-- Motos --")
    _imprimir_em_grade(vagas_moto)

    livres_carro = sum(1 for v in vagas_carro if not v["ocupada"])
    livres_moto = sum(1 for v in vagas_moto if not v["ocupada"])
    print(f"\nVagas livres -> carros: {livres_carro}/{len(vagas_carro)}  |  "
          f"motos: {livres_moto}/{len(vagas_moto)}")
