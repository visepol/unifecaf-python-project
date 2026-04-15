def gerar_relatorio(pecas, caixas):
    print("\n" + "=" * 42)
    print("         RELATÓRIO FINAL DO SISTEMA")
    print("=" * 42)

    aprovadas = [p for p in pecas if p["status"] == "aprovada"]
    reprovadas = [p for p in pecas if p["status"] == "reprovada"]
    caixas_fechadas = [c for c in caixas if c["fechada"]]
    caixa_aberta = next((c for c in caixas if not c["fechada"]), None)

    print(f"\nTotal de peças cadastradas : {len(pecas)}")
    print(f"Total de peças aprovadas   : {len(aprovadas)}")
    print(f"Total de peças reprovadas  : {len(reprovadas)}")

    print(f"\nCaixas fechadas            : {len(caixas_fechadas)}")
    if caixa_aberta:
        print(f"Caixa em aberto            : #{caixa_aberta['numero']} ({len(caixa_aberta['pecas'])}/10 peças)")
    else:
        print("Caixa em aberto            : nenhuma")

    if reprovadas:
        print("\n--- Detalhes das Reprovações ---")
        for p in reprovadas:
            print(f"  ID {p['id']} | Motivo: {p['motivo']}")

    if caixas_fechadas:
        print("\n--- Detalhes das Caixas Fechadas ---")
        for caixa in caixas_fechadas:
            ids = [str(p["id"]) for p in caixa["pecas"]]
            print(f"  Caixa #{caixa['numero']}: peças {', '.join(ids)}")

    print("\n" + "=" * 42)
