"""
Requisito 3: o sistema deve ajudar a evitar que alunos estacionem em vagas
reservadas para servidores, especialmente as vagas proximas a biblioteca.
"""


def validar_acesso(vaga, tipo_usuario):
    """Retorna (permitido: bool, motivo: str) para tipo_usuario ocupar a vaga."""
    if vaga["reservada_servidor"] and tipo_usuario == "aluno":
        motivo = (
            f"vaga {vaga['id']} e reservada para servidores (proxima a biblioteca)."
        )
        return False, motivo
    return True, ""
