 # Mensagem 
    if mensagem in ["oi", "olá", "bom dia", "boa tarde", "boa noite"]:
        msg.reply(
            "👋 Olá, seja bem-vindo ao *Atendimento Virtual*!\n\n"
            "Escolha uma das opções abaixo:\n"
            "1️⃣ - Ver nossos produtos\n" 
        )

 # Opções do menu
    elif mensagem == "1":
        msg.reply("📦 Aqui estão nossos produtos:\n- Arroz\n- Feijão\n- Macarrão\n- Leite\n- Pão")
    