

def formatar_produtos(estoque):
    linhas = ["📦 *Produtos disponíveis:*"]
    for produto, qtd in estoque.items():
        linhas.append(f"- {produto}: {qtd} em estoque")
    linhas.append("\nDigite *menu* para voltar.")
    return "\n".join(linhas)

def handle_message(msg):
    raw = getattr(msg, "body", None) or getattr(msg, "text", None)
    if not raw:
        return
    mensagem = raw.strip().lower()
    if mensagem == "1":
        msg.reply(formatar_produtos(estoque))
    elif mensagem == "menu":
        msg.reply("👋 Menu principal:\n\n1️⃣ - Ver nossos produtos")
