from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5920367606:AAHs9Z8vj6_Pib94H5H2E2w3sjT8krTEHhI").build()

app.add_handler(CommandHandler("hello", hello))
print('server start')
app.run_polling()



# # Fixing random state for reproducibility
# np.random.seed(19680801)

# dt = 0.01
# t = np.arange(0, 30, dt)
# nse1 = np.random.randn(len(t))                 # white noise 1
# nse2 = np.random.randn(len(t))                 # white noise 2

# # Two signals with a coherent part at 10 Hz and a random part
# s1 = np.sin(2 * np.pi * 10 * t) + nse1
# s2 = np.sin(2 * np.pi * 10 * t) + nse2

# fig, axs = plt.subplots(2, 1)
# axs[0].plot(t, s1, t, s2)
# axs[0].set_xlim(0, 2)
# axs[0].set_xlabel('Time')
# axs[0].set_ylabel('s1 and s2')
# axs[0].grid(True)

# cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
# axs[1].set_ylabel('Coherence')

# fig.tight_layout()
plt.show()


# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))


# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()


# from isOdd import isOdd
# print(isOdd(1)) 
# print(isOdd(4))
