from model import model_lead
import control

def add_lead():
    nome = input("Nome: ")
    email = input("Email: ")
    stage = input("Etapa no funil: ")

    print(model_lead(nome, email, stage))

    control.create_lead(model_lead(nome, email, stage))

def list_leads():
    leads = control.list_leads()
    print(leads)


def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Saindo")
            break
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()

