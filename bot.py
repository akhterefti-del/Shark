from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8237387201:AAFI98932KS3M5uJDLaTbu27FCFOJ40wwxI"
WEB_APP_URL = "https://shark-silk-two.vercel.app/"  # Replace with your actual URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Check if there's a referral parameter
    if context.args:
        referral_code = context.args[0]
        # The web app will handle the referral processing
        web_app_url = f"{WEB_APP_URL}?tgWebAppStartParam={referral_code}"
    else:
        web_app_url = WEB_APP_URL
    
    keyboard = [[{
        "text": "🦈 Open Shark Bounty",
        "web_app": {"url": web_app_url}
    }]]
    
    await update.message.reply_text(
        f"🦈 Welcome to Shark Bounty!\n\n"
        f"Tap the button below to start earning SHB tokens!\n\n"
        f"💰 Earn 5000 SHB for each friend you refer!",
        reply_markup={"inline_keyboard": keyboard}
    )

async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    referral_link = f"https://t.me/SharkBountybot?start=r{user_id}"
    
    await update.message.reply_text(
        f"🎁 Your Referral Link:\n\n"
        f"{referral_link}\n\n"
        f"Share this link with friends and earn 5000 SHB for each referral!"
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[{
        "text": "💰 Check Balance",
        "web_app": {"url": WEB_APP_URL}
    }]]
    
    await update.message.reply_text(
        "Tap the button below to check your balance:",
        reply_markup={"inline_keyboard": keyboard}
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("referral", referral))
    app.add_handler(CommandHandler("balance", balance))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
