import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    welcome_message = """🧸 به DiDi TOYS خوش آمدید! 🎉

📋 منوی ربات:
/products - مشاهده محصولات"""
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """🔧 دستورات موجود:

/start - پیام خوش‌آمدگویی
/products - مشاهده محصولات
/dolls - کوسن‌های عروسکی
/cans - بطری‌های فانتزی
/help - نمایش این منو

🧸 DiDi TOYS در خدمت شماست! ✨"""
    await update.message.reply_text(help_text)

async def products(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show main product categories."""
    products_text = """🛍️ محصولات DiDi TOYS:

🧸 DiDi Dolls - کوسن‌های عروسکی
🍼 DiDi Cans - بطری‌های فانتزی

برای مشاهده زیرمجموعه‌ها:
/dolls - کوسن‌های عروسکی  
/cans - بطری‌های فانتزی"""
    await update.message.reply_text(products_text)

async def dolls(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show dolls subcategories."""
    dolls_text = """🧸 DiDi Dolls - کوسن‌های عروسکی:

• کوسن عروسک دختر
• کوسن عروسک پسر  
• کوسن حیوانات
• کوسن شخصیت‌های کارتونی

برای سفارش با ما تماس بگیرید."""
    await update.message.reply_text(dolls_text)

async def cans(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show cans subcategories."""
    cans_text = """🍼 DiDi Cans - بطری‌های فانتزی:

• بطری فانتزی دختر
• بطری فانتزی پسر
• بطری حیوانات  
• بطری شخصیت‌های کارتونی

برای سفارش با ما تماس بگیرید."""
    await update.message.reply_text(cans_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle non-command messages."""
    user_message = update.message.text.lower()
    
    # Simple keyword responses in Persian
    if any(word in user_message for word in ['سلام', 'درود', 'های']):
        await update.message.reply_text("سلام! 👋 به DiDi TOYS خوش آمدید! چطور می‌تونم کمکتون کنم؟")
    elif any(word in user_message for word in ['قیمت', 'هزینه', 'خرید', 'سفارش']):
        await update.message.reply_text("برای اطلاعات قیمت و سفارش لطفاً با ما تماس بگیرید! 📞")
    elif any(word in user_message for word in ['محصول', 'عروسک', 'کوسن', 'بطری']):
        await update.message.reply_text("محصولات زیبای ما را با دستور /products ببینید! 🧸")
    elif any(word in user_message for word in ['ممنون', 'متشکرم', 'مرسی']):
        await update.message.reply_text("خواهش می‌کنم! 😊 خوشحالیم که به DiDi TOYS اعتماد کردید!")
    else:
        await update.message.reply_text("سلام! من ربات DiDi TOYS هستم 🤖\nبرای مشاهده دستورات /help را بزنید!")

def main() -> None:
    """Start the bot."""
    if not TOKEN:
        logger.error("No TELEGRAM_BOT_TOKEN found in environment variables")
        return
    
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("products", products))
    application.add_handler(CommandHandler("dolls", dolls))
    application.add_handler(CommandHandler("cans", cans))
    
    # Add message handler for non-command messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    port = int(os.environ.get('PORT', 8000))
    application.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=TOKEN,
        webhook_url=f"https://your-app-name.herokuapp.com/{TOKEN}"
    )

if __name__ == '__main__':
    main()
