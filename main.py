"""
PLANO (passo 1 da atividade)
Requisitos escolhidos, na ordem em que serao implementados:
  1. Exibir o mapa de vagas do estacionamento (carro/moto, normal/PCD/idoso).
     Base visual para testar os proximos dois. 
  2. Reportar vaga manualmente (aluno/servidor escolhe veiculo, numero da
     vaga e ocupa ou libera). 
  3. Bloquear aluno de ocupar vaga reservada para servidor perto da
     biblioteca. Depende do requisito 2 ja funcionando. 
Uso de IA: <tive que usar parar fazer todo o codigo, nao deu tempo de codar do jeito que queria, por conta do tempo>.
"""

from requisito1_exibir_vagas import exibir_estacionamento
from requisito2_reportar_vaga import reportar_vaga


def criar_vagas_carro():
    vagas = []
    for i in range(1, 11):
        vaga = {"id": i, "ocupada": False, "tipo_vaga": "normal", "reservada_servidor": False}
        if i in (1, 2):
            vaga["reservada_servidor"] = True
        elif i == 3:
            vaga["tipo_vaga"] = "pcd"
        elif i == 4:
            vaga["tipo_vaga"] = "idoso"
        vagas.append(vaga)
    return vagas


def criar_vagas_moto():
    vagas = []
    for i in range(1, 6):
        vaga = {"id": i, "ocupada": False, "tipo_vaga": "normal", "reservada_servidor": False}
        if i == 1:
            vaga["reservada_servidor"] = True
        elif i == 2:
            vaga["tipo_vaga"] = "pcd"
        vagas.append(vaga)
    return vagas


def demonstrar_bloqueio(vagas_carro):
    """Comprova o requisito 3 sem exigir interacao: mostra o mesmo pedido de
    vaga reservada sendo negado para aluno e aceito para servidor."""
    from requisito3_validar_acesso import validar_acesso

    vaga_reservada = next(v for v in vagas_carro if v["reservada_servidor"])
    permitido, motivo = validar_acesso(vaga_reservada, "aluno")
    resultado = "permitido" if permitido else f"BLOQUEADO -> {motivo}"
    print(f"\n[Demonstracao requisito 3] Aluno pede vaga {vaga_reservada['id']} (reservada): {resultado}")

    permitido, _ = validar_acesso(vaga_reservada, "servidor")
    resultado = "permitido" if permitido else "bloqueado"
    print(f"[Demonstracao requisito 3] Servidor pede vaga {vaga_reservada['id']} (reservada): {resultado}")


def menu():
    vagas_carro = criar_vagas_carro()
    vagas_moto = criar_vagas_moto()

    exibir_estacionamento(vagas_carro, vagas_moto)
    demonstrar_bloqueio(vagas_carro)

    while True:
        print("\n1) Ver mapa do estacionamento")
        print("2) Reportar vaga (ocupar/liberar)")
        print("3) Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            exibir_estacionamento(vagas_carro, vagas_moto)
        elif opcao == "2":
            reportar_vaga(vagas_carro, vagas_moto)
            exibir_estacionamento(vagas_carro, vagas_moto)
        elif opcao == "3":
            print("Encerrando.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu()


