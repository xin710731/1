import os
import logging
from datetime import datetime
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

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ================= MENU =================

def main_menu():
    keyboard = [
        [InlineKeyboardButton("Fokus Hari Ini", callback_data="focus")],
        [InlineKeyboardButton("Target Pribadi", callback_data="target")],
        [InlineKeyboardButton("Panduan Fokus 25 Menit", callback_data="guide")],
        [InlineKeyboardButton("Refleksi Suasana Hati", callback_data="mood")],
    ]
    return InlineKeyboardMarkup(keyboard)


# ================= COMMANDS =================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Daily Focus Assistant\n\n"
        "Alat sederhana untuk membantu produktivitas pribadi.\n\n"
        "Silakan pilih salah satu fitur di bawah."
    )
    await update.message.reply_text(text, reply_markup=main_menu())


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Tentang Bot\n\n"
        "Bot ini adalah alat bantu produktivitas pribadi.\n\n"
        "Tidak menyediakan:\n"
        "- Hadiah\n"
        "- Sistem poin\n"
        "- Uang\n"
        "- Investasi\n"
        "- Permainan\n\n"
        "Hanya panduan fokus dan refleksi pribadi."
    )
    await update.message.reply_text(text)


async def privacy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Kebijakan Privasi\n\n"
        "Bot ini tidak meminta data pribadi tambahan.\n"
        "Tidak ada sistem pembayaran.\n"
        "Tidak ada integrasi pihak ketiga."
    )
    await update.message.reply_text(text)


# ================= BUTTON HANDLER =================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "focus":
        today = datetime.now().strftime("%d %B %Y")
        text = (
            f"Fokus Hari Ini ({today})\n\n"
            "Tentukan satu prioritas utama.\n"
            "Kerjakan secara bertahap dan tanpa gangguan."
        )
        await query.edit_message_text(text, reply_markup=main_menu())

    elif query.data == "target":
        text = (
            "Target Pribadi\n\n"
            "Tulis satu tujuan sederhana yang ingin kamu capai minggu ini.\n"
            "Pastikan realistis dan terukur."
        )
        await query.edit_message_text(text, reply_markup=main_menu())

    elif query.data == "guide":
        text = (
            "Panduan Fokus 25 Menit\n\n"
            "1. Pilih satu tugas.\n"
            "2. Fokus tanpa gangguan selama 25 menit.\n"
            "3. Istirahat singkat setelah selesai.\n\n"
            "Ulangi sesuai kebutuhan."
        )
        await query.edit_message_text(text, reply_markup=main_menu())

    elif query.data == "mood":
        text = (
            "Refleksi Suasana Hati\n\n"
            "Luangkan waktu sejenak.\n"
            "Tanyakan pada diri sendiri:\n"
            "- Bagaimana kondisi saya hari ini?\n"
            "- Apa yang bisa saya perbaiki besok?"
        )
        await query.edit_message_text(text, reply_markup=main_menu())


# ================= MAIN =================

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN belum diatur")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("privacy", privacy))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Daily Focus Assistant aktif")
    app.run_polling()


if __name__ == "__main__":
    main()
