"""
### **Exercício: Gerenciador de Arquivos Simples**

**Descrição:**  
Você deve criar um script Python que permita ao usuário realizar as seguintes tarefas:
1. Criar um novo diretório com um nome fornecido pelo usuário.
2. Listar todos os arquivos e diretórios dentro do diretório atual.
3. Verificar se um arquivo ou diretório específico existe no caminho atual.
4. Renomear um arquivo ou diretório existente.

**Requisitos:**
- Use funções da biblioteca `os` para implementar cada uma das operações.
- Interaja com o usuário por meio de entradas (`input`) e saídas (`print`).
- Certifique-se de tratar possíveis erros, como tentar renomear um arquivo que não existe.

**Etapas sugeridas:**
1. Pergunte ao usuário qual operação ele deseja realizar (criar diretório, listar conteúdo, verificar existência ou renomear).
2. Implemente cada operação em uma função separada para manter o código organizado.
3. Ao final de cada operação, pergunte ao usuário se ele deseja realizar outra tarefa ou encerrar o programa.

---

### **Dicas:**
- Use `os.mkdir()` para criar diretórios.
- Use `os.listdir()` para listar arquivos e diretórios.
- Use `os.path.exists()` para verificar a existência de um arquivo ou diretório.
- Use `os.rename()` para renomear arquivos ou diretórios.
- Use `try` e `except` para lidar com possíveis erros, como tentar acessar um diretório inexistente.

---

### **Exemplo de Fluxo do Programa:**
```
Bem-vindo ao Gerenciador de Arquivos!
Escolha uma operação:
1 - Criar diretório
2 - Listar conteúdo do diretório atual
3 - Verificar existência de arquivo/diretório
4 - Renomear arquivo/diretório
Digite sua escolha: 1
Digite o nome do novo diretório: documentos
Diretório 'documentos' criado com sucesso!
Deseja realizar outra operação? (s/n): s
...
```

---

Agora é sua vez! Tente implementar o script sozinho. Se precisar de ajuda ou quiser conferir a solução depois, estou aqui para ajudar. Boa prática! 🚀
"""
import os

# print(os.getcwd())

def criar_dir(nome):
    os.mkdir(nome)
    if not os.path.exists(nome):
        print("Erro na criação do diretorio.")
        return
    else:
        print(f"Diretório '{nome}' criado com sucesso!")

def listar_arquivos(dir_atual):
    if not os.listdir(dir_atual):
        raise ValueError("ERR: O diretório está vazio.")
    for item in os.listdir(dir_atual):
        item_path = os.path.join(dir_atual, item)
        if os.path.isdir(item_path):
            print(f'[DIR] {item}')
        elif os.path.isfile(item_path):
            print(f'[FILE] {item}')

def verificar_existencia(nome_arquivo):
    if not os.path.exists(nome_arquivo):
    # if not os.path.isfile(nome_arquivo): # se fosse para verificar apenas de um arquivo
        print(f'O arquivo "{nome_arquivo} não está no diretorio {os.path.dirname(os.getcwd())}."')
        return
    print(f'O arquivo "{nome_arquivo}" está no diretório {os.path.dirname(os.getcwd())}')
    return

def renomear_arquivo(nome_atual, novo_nome):
    if not os.path.exists(nome_atual):
        print(f'O arquivo "{nome_atual} não está no diretorio {os.getcwd()}."')
        return
    if os.path.isdir(nome_atual):
        os.rename(nome_atual, novo_nome)
        print(f"O diretório foi renomeado com sucesso de '{nome_atual}' para '{novo_nome}.'")
        return

    os.rename(nome_atual, novo_nome)
    print(f"O arquivo foi renomeado com sucesso de '{nome_atual}' para '{novo_nome}.'")
    return

# criar_dir('periferia')
# print(os.path.dirname(os.getcwd()))  # '/caminho/para'


def menu():
    while True:
        try:
            print('-'* 20)
            print('Explorador de arquivos')
            print('1. Criar diretorio')
            print('2. Listar arquivos')
            print('3. Verificar existencia de diretório/arquivo')
            print('4. Renomear arquivo/diretório')
            print('5. Sair')
            escolha = int(input("O que você deseja fazer? "))
        except ValueError as er:
            print(er)
            
        match escolha:
            case 1:
                nome_dir = input("Qual nome do diretório que você deseja criar?")
                criar_dir(nome_dir)
                # return
            case 2:
                listar_arquivos('C:/Users/User/Desktop/python/teste_dir')
                # return
            case 3:
                nome_dir = input("Qual nome do diretório que você deseja verificar se existe?")
                verificar_existencia(nome_dir)
                # return
            case 4:
                nome_atual = input("Qual é o nome atual do arquivo que você deseja renomear?")
                nome_novo = input("Qual novo nome?")
                renomear_arquivo(nome_atual, nome_novo)
                # return
            case 5:
                print("Obrigado por usar o Explorador de arquivos")
                break
            
if __name__ == '__main__':
    os.chdir('C:/Users/User/Desktop/python/teste_dir')
    menu()
