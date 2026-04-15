CAPACIDADE_CAIXA = 10


def _caixa_atual(caixas):
    for caixa in caixas:
        if not caixa["fechada"]:
            return caixa
    return None


def _abrir_nova_caixa(caixas):
    numero = len(caixas) + 1
    nova_caixa = {"numero": numero, "pecas": [], "fechada": False}
    caixas.append(nova_caixa)
    return nova_caixa


def adicionar_em_caixa(caixas, peca):
    caixa = _caixa_atual(caixas)

    if caixa is None:
        caixa = _abrir_nova_caixa(caixas)

    caixa["pecas"].append(peca)

    if len(caixa["pecas"]) >= CAPACIDADE_CAIXA:
        caixa["fechada"] = True
        print(f"Caixa #{caixa['numero']} fechada ({CAPACIDADE_CAIXA} peças).")


def listar_caixas_fechadas(caixas):
    print("\n--- Caixas Fechadas ---")

    fechadas = [c for c in caixas if c["fechada"]]

    if not fechadas:
        print("Nenhuma caixa fechada ainda.")
        return

    for caixa in fechadas:
        ids = [str(p["id"]) for p in caixa["pecas"]]
        print(f"\n  Caixa #{caixa['numero']} | {len(caixa['pecas'])} peças")
        print(f"  Peças: {', '.join(ids)}")
