from conexao import conectar

def cadastrar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contatos (nome, telefone) VALUES (%s,%s)", (nome, telefone))
    conn.commit()
    conn.close()
    print("Contato cadastrado!\n")

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos")
    print("\n--- Contatos ---")
    for id, nome, tel in cursor.fetchall():
        print(f"{id} - {nome}: {tel}")
    conn.close()

def main():
    while True:
        op = input("1-Cadastrar 2-Listar 3-Sair: ")
        if op=="1": cadastrar()
        elif op=="2": listar()
        elif op=="3": break

if __name__=="__main__":
    main()
