from pecas import cadastrar_peca, listar_pecas, remover_peca
from caixas import listar_caixas_fechadas
from relatorio import gerar_relatorio


def exibir_menu():
    print("\n" + "=" * 42)
    print("   GESTÃO DE PEÇAS — CONTROLE DE QUALIDADE")
    print("=" * 42)
    print("  1. Cadastrar nova peça")
    print("  2. Listar peças aprovadas/reprovadas")
    print("  3. Remover peça cadastrada")
    print("  4. Listar caixas fechadas")
    print("  5. Gerar relatório final")
    print("  0. Sair")
    print("-" * 42)


def main():
    pecas = []
    caixas = []

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca(pecas, caixas)
        elif opcao == "2":
            listar_pecas(pecas)
        elif opcao == "3":
            remover_peca(pecas, caixas)
        elif opcao == "4":
            listar_caixas_fechadas(caixas)
        elif opcao == "5":
            gerar_relatorio(pecas, caixas)
        elif opcao == "0":
            print("\nSistema encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
