import os
import random
import time
import logging

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ========== 基础配置 ==========
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# ========== 菜单 ==========
def main_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🌤 Início do Dia", callback_data="menu_day")],
        [
            InlineKeyboardButton("✅ Hábitos & Pequenas Metas", callback_data="menu_habit"),
            InlineKeyboardButton("😊 Emoções & Humor", callback_data="menu_mood"),
        ],
        [
            InlineKeyboardButton("🧠 Quiz & Perguntas", callback_data="menu_quiz"),
            InlineKeyboardButton("📚 Leitura Leve & Frases", callback_data="menu_read"),
        ],
        [
            InlineKeyboardButton("🎲 Funções Aleatórias", callback_data="menu_random"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def day_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📅 Frase de Hoje", callback_data="day_sentence"),
            InlineKeyboardButton("📋 Dica de Hoje", callback_data="day_tip"),
        ],
        [
            InlineKeyboardButton("🧭 Direção do Dia", callback_data="day_direction"),
        ],
        [InlineKeyboardButton("⬅ Voltar ao Início", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def habit_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("✅ Gerar Pequena Meta", callback_data="habit_goal"),
            InlineKeyboardButton("🔁 Micro Hábito", callback_data="habit_action"),
        ],
        [
            InlineKeyboardButton("🧹 Pequena Organização", callback_data="habit_clean"),
            InlineKeyboardButton("🚶 Movimento Leve", callback_data="habit_move"),
        ],
        [InlineKeyboardButton("⬅ Voltar ao Início", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def mood_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("💬 Frase de Humor", callback_data="mood_text"),
            InlineKeyboardButton("🎨 Cor do Humor", callback_data="mood_color"),
        ],
        [
            InlineKeyboardButton("🧘 Relaxamento Simples", callback_data="mood_relax"),
            InlineKeyboardButton("❤️ Autocuidado", callback_data="mood_selfcare"),
        ],
        [InlineKeyboardButton("⬅ Voltar ao Início", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def quiz_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🧠 Pergunta Reflexiva", callback_data="quiz_think"),
            InlineKeyboardButton("🔢 Teste Numérico", callback_data="quiz_number"),
        ],
        [
            InlineKeyboardButton("👀 Tempo de Reação", callback_data="quiz_reaction"),
        ],
        [InlineKeyboardButton("⬅ Voltar ao Início", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def read_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📖 Frase Suave", callback_data="read_soft"),
            InlineKeyboardButton("💡 Faísca de Ideia", callback_data="read_idea"),
        ],
        [
            InlineKeyboardButton("📝 Pergunta de Reflexão", callback_data="read_question"),
        ],
        [InlineKeyboardButton("⬅ Voltar ao Início", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def random_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🎲 Número Aleatório", callback_data="rand_number"),
            InlineKeyboardButton("😊 Emoji Aleatório", callback_data="rand_emoji"),
        ],
        [
            InlineKeyboardButton("📌 Pequena Tarefa", callback_data="rand_task"),
            InlineKeyboardButton("✨ Inspiração Aleatória", callback_data="rand_inspire"),
        ],
        [InlineKeyboardButton("⬅ Voltar ao Início", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


# ========== /start /help /about ==========
START_TEXT = (
    "👋 Bem-vindo ao **Momento Leve · Espaço de Vida**!\n\n"
    "Este é um bot em português focado em *pequenas metas diárias, cuidado emocional, quizzes leves e inspiração aleatória*.\n\n"
    "Aqui você pode:\n"
    "🌤 Ver dicas para começar o dia\n"
    "✅ Gerar pequenas metas e micro hábitos\n"
    "😊 Expressar seu humor com frases ou cores\n"
    "🧠 Fazer quizzes leves e pequenos testes\n"
    "📚 Ler frases suaves e perguntas reflexivas\n"
    "🎲 Obter números, emojis, tarefas ou inspirações aleatórias\n\n"
    "Este bot oferece apenas interações textuais leves e saudáveis, sem envolver dinheiro, recompensas, apostas, investimentos ou conteúdos sensíveis.\n\n"
    "👇 Use os botões abaixo para escolher o que deseja explorar agora:"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            START_TEXT, reply_markup=main_menu(), parse_mode="Markdown"
        )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📝 Como usar\n\n"
        "• Envie /start para abrir o menu principal\n"
        "• Use os botões para acessar: Início do Dia / Hábitos / Emoções / Quiz / Leitura / Funções Aleatórias\n"
        "• Cada botão oferece conteúdo ou interação textual\n"
        "• Se a interface travar, envie /start novamente\n"
    )
    await update.message.reply_text(text)


async def about_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "ℹ️ Sobre o **Momento Leve · Espaço de Vida**\n\n"
        "Um pequeno bot para relaxar nos momentos livres:\n"
        "• Pequenas metas e micro tarefas para mudanças graduais\n"
        "• Ferramentas emocionais para cuidar do humor\n"
        "• Quizzes leves e leituras para estimular a mente\n"
        "Todo o conteúdo é saudável, não comercial e sem informações sensíveis."
    )
    await update.message.reply_text(text)


# ========== 按钮总路由 ==========
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "menu_main":
        await query.edit_message_text("🏠 Você voltou ao início:", reply_markup=main_menu())
        return
    if data == "menu_day":
        await query.edit_message_text("🌤 Início do Dia:", reply_markup=day_menu())
        return
    if data == "menu_habit":
        await query.edit_message_text("✅ Hábitos & Pequenas Metas:", reply_markup=habit_menu())
        return
    if data == "menu_mood":
        await query.edit_message_text("😊 Emoções & Humor:", reply_markup=mood_menu())
        return
    if data == "menu_quiz":
        await query.edit_message_text("🧠 Quiz & Perguntas:", reply_markup=quiz_menu())
        return
    if data == "menu_read":
        await query.edit_message_text("📚 Leitura Leve & Frases:", reply_markup=read_menu())
        return
    if data == "menu_random":
        await query.edit_message_text("🎲 Funções Aleatórias:", reply_markup=random_menu())
        return

    # ===== Início do Dia =====
    if data == "day_sentence":
        sentences = [
            "Você pode ir devagar hoje, mas não precisa parar.",
            "Definir uma meta bem pequena hoje já é suficiente.",
            "Mesmo cuidar bem de uma refeição é viver com atenção.",
        ]
        await query.edit_message_text(
            "📅 Frase de Hoje:\n\n" + random.choice(sentences),
            reply_markup=day_menu(),
        )
        return

    if data == "day_tip":
        tips = [
            "Que tal usar um pouco menos o celular hoje e guardar tempo para você?",
            "Escolha um pequeno canto para organizar por apenas 3 minutos.",
            "Se o dia estiver cheio, separe tarefas em “necessárias” e “podem esperar”.",
        ]
        await query.edit_message_text(
            "📋 Dica de Hoje:\n\n" + random.choice(tips),
            reply_markup=day_menu(),
        )
        return

    if data == "day_direction":
        directions = [
            "Trate hoje como um dia de base: faça pequenas coisas úteis a longo prazo.",
            "Considere hoje um dia de ajuste e permita-se desacelerar.",
            "Hoje pode ser um dia para tentar algo novo, mesmo que pequeno.",
        ]
        await query.edit_message_text(
            "🧭 Direção do Dia:\n\n" + random.choice(directions),
            reply_markup=day_menu(),
        )
        return

    # ===== Hábitos & Pequenas Metas =====
    if data == "habit_goal":
        goals = [
            "Conclua hoje uma meta que leve apenas 5 minutos.",
            "Foque em apenas uma pequena coisa que seja importante para você.",
            "Defina uma meta simples: fazer já é suficiente.",
        ]
        await query.edit_message_text(
            "✅ Sugestão de Meta:\n\n" + random.choice(goals),
            reply_markup=habit_menu(),
        )
        return

    if data == "habit_action":
        actions = [
            "Beba um copo de água e diga a si mesmo: “bom trabalho”.",
            "Levante-se e alongue os ombros por 30 segundos.",
            "Guarde um objeto que não usa com frequência.",
        ]
        await query.edit_message_text(
            "🔁 Micro Hábito:\n\n" + random.choice(actions),
            reply_markup=habit_menu(),
        )
        return

    if data == "habit_clean":
        texts = [
            "Escolha uma gaveta ou pasta e descarte algo em apenas 2 minutos.",
            "Organize levemente o que está à vista para deixar o ambiente mais leve.",
        ]
        await query.edit_message_text(
            "🧹 Pequena Organização:\n\n" + random.choice(texts),
            reply_markup=habit_menu(),
        )
        return

    if data == "habit_move":
        moves = [
            "Caminhe no lugar por 30 segundos para ativar o corpo.",
            "Faça 10 respirações profundas com movimentos de ombro.",
            "Levante-se e caminhe até outro cômodo como uma mini caminhada.",
        ]
        await query.edit_message_text(
            "🚶 Movimento Leve:\n\n" + random.choice(moves),
            reply_markup=habit_menu(),
        )
        return

    # ===== Emoções & Humor =====
    if data == "mood_text":
        moods = [
            "Sentir-se cansado também é sinal de esforço.",
            "As emoções variam, mas você sempre merece cuidado.",
            "Está tudo bem não estar no seu melhor hoje.",
        ]
        await query.edit_message_text(
            "💬 Frase de Humor:\n\n" + random.choice(moods),
            reply_markup=mood_menu(),
        )
        return

    if data == "mood_color":
        colors = [
            "🔵 Azul: bom para acalmar e organizar pensamentos.",
            "🟢 Verde: ideal para relaxar e ouvir música.",
            "🟡 Amarelo: ótimo para conversar com alguém.",
            "🟣 Roxo: bom para escrever ou criar ideias.",
        ]
        await query.edit_message_text(
            "🎨 Sugestão de Cor:\n\n" + random.choice(colors),
            reply_markup=mood_menu(),
        )
        return

    if data == "mood_relax":
        text = (
            "🧘 Exercício de Relaxamento:\n\n"
            "1️⃣ Sente-se de forma confortável\n"
            "2️⃣ Faça 5 respirações profundas\n"
            "3️⃣ Ao expirar, solte um pouco da tensão\n"
        )
        await query.edit_message_text(text, reply_markup=mood_menu())
        return

    if data == "mood_selfcare":
        texts = [
            "Você pode ser um pouco mais gentil consigo mesmo.",
            "Reconheça seu esforço hoje, mesmo que pequeno.",
        ]
        await query.edit_message_text(
            "❤️ Autocuidado:\n\n" + random.choice(texts),
            reply_markup=mood_menu(),
        )
        return

    # ===== Quiz & Perguntas =====
    if data == "quiz_think":
        qs = [
            "🧠 Reflexão:\n\nSe hoje tivesse um título, qual seria?",
            "🧠 Reflexão:\n\nQual pequeno progresso recente te deixou satisfeito?",
        ]
        await query.edit_message_text(
            random.choice(qs),
            reply_markup=quiz_menu(),
        )
        return

    if data == "quiz_number":
        number = random.randint(10, 99)
        text = (
            f"🔢 Teste:\n\nComece pelo número {number} e vá subtraindo 3 mentalmente."
        )
        await query.edit_message_text(text, reply_markup=quiz_menu())
        return

    if data == "quiz_reaction":
        context.user_data["reaction_start"] = time.time()
        keyboard = [
            [InlineKeyboardButton("⚡ Clique agora!", callback_data="quiz_reaction_click")],
            [InlineKeyboardButton("⬅ Voltar", callback_data="menu_quiz")],
        ]
        await query.edit_message_text(
            "Clique assim que vir o botão para testar sua reação:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    if data == "quiz_reaction_click":
        start = context.user_data.get("reaction_start")
        if not start:
            msg = "Os dados expiraram. Inicie o teste novamente."
        else:
            ms = int((time.time() - start) * 1000)
            msg = f"🎯 Seu tempo de reação foi: {ms} ms."
        await query.edit_message_text(msg, reply_markup=quiz_menu())
        return

    # ===== Leitura Leve & Frases =====
    if data == "read_soft":
        sentences = [
            "Você não precisa ser perfeito, só lembrar de se gostar.",
            "Muitas coisas podem ser feitas aos poucos.",
        ]
        await query.edit_message_text(
            "📖 Frase Suave:\n\n" + random.choice(sentences),
            reply_markup=read_menu(),
        )
        return

    if data == "read_idea":
        ideas = [
            "Anote hoje uma pequena coisa boa que aconteceu.",
            "Escreva uma frase para você daqui a um mês.",
        ]
        await query.edit_message_text(
            "💡 Faísca de Ideia:\n\n" + random.choice(ideas),
            reply_markup=read_menu(),
        )
        return

    if data == "read_question":
        qs = [
            "📝 Reflexão:\n\nSe a última semana fosse um clima, qual seria?",
            "📝 Reflexão:\n\nEm que aspecto você já melhorou mais do que imagina?",
        ]
        await query.edit_message_text(
            random.choice(qs),
            reply_markup=read_menu(),
        )
        return

    # ===== Funções Aleatórias =====
    if data == "rand_number":
        n = random.randint(0, 100)
        await query.edit_message_text(
            f"🎲 Número Aleatório (0~100): {n}",
            reply_markup=random_menu(),
        )
        return

    if data == "rand_emoji":
        emojis = ["😀", "😆", "😎", "🥳", "🤩", "🤗", "🙌", "🌈", "⭐", "✨", "🍀"]
        seq = " ".join(random.sample(emojis, 5))
        await query.edit_message_text(
            "😊 Emojis Aleatórios:\n\n" + seq,
            reply_markup=random_menu(),
        )
        return

    if data == "rand_task":
        tasks = [
            "Tire uma foto de algo que você acha agradável agora.",
            "Conclua uma pequena tarefa em até 3 minutos.",
            "Deixe o celular de lado por 2 minutos e apenas respire.",
        ]
        await query.edit_message_text(
            "📌 Pequena Tarefa:\n\n" + random.choice(tasks),
            reply_markup=random_menu(),
        )
        return

    if data == "rand_inspire":
        ins = [
            "Escolha uma palavra-tema para hoje, como: leve / ajuste / calma.",
            "Pense em algo simples que possa te fazer sentir melhor em 5 minutos.",
        ]
        await query.edit_message_text(
            "✨ Inspiração Aleatória:\n\n" + random.choice(ins),
            reply_markup=random_menu(),
        )
        return

    await query.edit_message_text(
        "Função não suportada. Envie /start para voltar ao início.", reply_markup=main_menu()
    )


# ========== 主入口 ==========
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN não está definido!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Momento Leve · Espaço de Vida Bot iniciado")
    app.run_polling()


if __name__ == "__main__":
    main()
