CORES_VALIDAS = {"azul", "verde"}
PESO_MIN = 95
PESO_MAX = 105
COMPRIMENTO_MIN = 10
COMPRIMENTO_MAX = 20


def avaliar_peca(peso, cor, comprimento):
    motivos = []

    if not (PESO_MIN <= peso <= PESO_MAX):
        motivos.append(f"peso {peso}g fora do intervalo [{PESO_MIN}g, {PESO_MAX}g]")

    if cor.lower() not in CORES_VALIDAS:
        motivos.append(f"cor '{cor}' inválida (permitidas: azul, verde)")

    if not (COMPRIMENTO_MIN <= comprimento <= COMPRIMENTO_MAX):
        motivos.append(f"comprimento {comprimento}cm fora do intervalo [{COMPRIMENTO_MIN}cm, {COMPRIMENTO_MAX}cm]")

    if motivos:
        return "reprovada", "; ".join(motivos)

    return "aprovada", None


def cadastrar_peca(pecas, caixas):
    print("\n--- Cadastrar Nova Peça ---")

    ids_existentes = {p["id"] for p in pecas}

    while True:
        try:
            id_peca = int(input("ID da peça: "))
            if id_peca in ids_existentes:
                print(f"Já existe uma peça com ID {id_peca}. Use outro ID.")
                continue
            break
        except ValueError:
            print("ID inválido. Digite um número inteiro.")

    while True:
        try:
            peso = float(input("Peso (g): "))
            break
        except ValueError:
            print("Peso inválido. Digite um número.")

    cor = input("Cor: ").strip()

    while True:
        try:
            comprimento = float(input("Comprimento (cm): "))
            break
        except ValueError:
            print("Comprimento inválido. Digite um número.")

    status, motivo = avaliar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor.lower(),
        "comprimento": comprimento,
        "status": status,
        "motivo": motivo,
    }

    pecas.append(peca)

    if status == "aprovada":
        from caixas import adicionar_em_caixa
        adicionar_em_caixa(caixas, peca)
        print(f"\nPeca #{id_peca} APROVADA e adicionada a uma caixa.")
    else:
        print(f"\nPeca #{id_peca} REPROVADA. Motivo: {motivo}")


def listar_pecas(pecas):
    print("\n--- Lista de Peças ---")

    aprovadas = [p for p in pecas if p["status"] == "aprovada"]
    reprovadas = [p for p in pecas if p["status"] == "reprovada"]

    print(f"\nAPROVADAS ({len(aprovadas)}):")
    if aprovadas:
        for p in aprovadas:
            print(f"  ID {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
    else:
        print("  Nenhuma peça aprovada.")

    print(f"\nREPROVADAS ({len(reprovadas)}):")
    if reprovadas:
        for p in reprovadas:
            print(f"  ID {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
            print(f"    Motivo: {p['motivo']}")
    else:
        print("  Nenhuma peça reprovada.")


def remover_peca(pecas, caixas):
    print("\n--- Remover Peça ---")

    if not pecas:
        print("Nenhuma peça cadastrada.")
        return

    while True:
        try:
            id_peca = int(input("ID da peça a remover: "))
            break
        except ValueError:
            print("ID inválido. Digite um número inteiro.")

    peca_encontrada = next((p for p in pecas if p["id"] == id_peca), None)

    if not peca_encontrada:
        print(f"Peça com ID {id_peca} não encontrada.")
        return

    pecas.remove(peca_encontrada)

    if peca_encontrada["status"] == "aprovada":
        for caixa in caixas:
            if peca_encontrada in caixa["pecas"]:
                caixa["pecas"].remove(peca_encontrada)
                if caixa["fechada"] and len(caixa["pecas"]) < 10:
                    caixa["fechada"] = False
                break

    print(f"Peça #{id_peca} removida com sucesso.")
