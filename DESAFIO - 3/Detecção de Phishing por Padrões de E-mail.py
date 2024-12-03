# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click", "promoção"]
    
    mensagem = mensagem.lower() # Converte a mensagem para minúsculas para evitar problemas de caixa alta
    
    # Verifica se alguma palavra suspeita está presente no corpo do e-mail
    for palavra in palavras_suspeitas:
        if palavra in mensagem:
            return "Phishing"  # Se encontrar uma palavra suspeita, classifica como phishing
    
    return "Seguro"  # Se não encontrar nenhuma palavra suspeita, classifica como seguro

email_usuario = input()

email_usuario = email_usuario.strip()

resultado = verificar_phishing(email_usuario)

print(f"Classificação: {resultado}")