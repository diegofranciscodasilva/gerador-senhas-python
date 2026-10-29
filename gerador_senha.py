import secrets
import string

def gerar_senha():
    print("\n=== GERADOR DE SENHAS SEGURAS ===")
    try:
        tamanho = int(input("Quantos caracteres você quer na senha? (Mínimo: 16): "))
        if tamanho < 16:
            print("⚠️ A senha deve ter pelo menos 16 caracteres para ser mais segura.")
            return
    except ValueError:
        print("⚠️ Digite apenas números inteiros válidos.")
        return
        
    # Junta letras maiúsculas/minúsculas, números e pontuações
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Sorteia os caracteres e une em uma string única
    senha = "".join(secrets.choice(caracteres) for _ in range(tamanho))
    
    print(f"\n🔒 Sua nova senha gerada é:\n{senha}\n")

if __name__ == "__main__":
    gerar_senha()
    