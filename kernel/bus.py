from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message

import basicui.dialog as dial

async def handle_all(dp: Dispatcher):

	@dp.message_handler(commands=['start'])
	async def start(message: Message):
		await dial.start(message)

	@dp.message_handler(content_types=['text'], text='Сотрудник', state=dial.dialog.registration)
	async def admin_registration(message: Message):
		await dial.admin_registration(message)

	@dp.message_handler(content_types=['text'], text='Учащийся', state=dial.dialog.registration)
	async def participant_registration(message: Message):
		await dial.participant_registration(message)


	@dp.message_handler(state=dial.dialog.registration)
	async def start_registration(message: Message, state: FSMContext):
		await dial.start_registration(message, state)

	await dp.start_polling()


# @main.dp.message_handler(commands=['start'])
# async def start(message: Message):
# 	dialog.start(message)

# @main.dp.message_handler(content_types=['text'], text='Сотрудник', state=dialog.dialog.registration)
# async def admin_registration(message: Message):
# 	dialog.admin_registration(message)

# @main.dp.message_handler(content_types=['text'], text='Учащийся', state=dialog.registration)
# async def participant_registration(message: Message):
# 	dialog.participant_registration(message)


# @main.dp.message_handler(state=dialog.registration)
# async def start_registration(message: Message, state: FSMContext):
# 	dialog.admin_registration(message, state)



# @dp.message_handler(state=dialog.spam)
# async def start_spam(message: Message, state: FSMContext):
#   if message.text == 'Назад':
#     await message.answer('Главное меню', reply_markup=kb)
#     await state.finish()
#   else:
#     cur = conn.cursor()
#     cur.execute(f'''SELECT user_id FROM users''')
#     spam_base = cur.fetchall()
#     for z in range(len(spam_base)):
#         await bot.send_message(spam_base[z][0], message.text)
#         await message.answer('Рассылка завершена', reply_markup=kb)
#         await state.finish()

# @dp.message_handler(content_types=['text'], text='Добавить в ЧС')
# async def hanadler(message: types.Message, state: FSMContext):
#   if message.chat.id == ADMIN:
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(types.InlineKeyboardButton(text="Назад"))
#     await message.answer('Введите id пользователя, которого нужно заблокировать.\nДля отмены нажмите кнопку ниже', reply_markup=keyboard)
#     await dialog.blacklist.set()

# @dp.message_handler(state=dialog.blacklist)
# async def proce(message: types.Message, state: FSMContext):
#   if message.text == 'Назад':
#     await message.answer('Отмена! Возвращаю назад.', reply_markup=kb)
#     await state.finish()
#   else:
#     if message.text.isdigit():
#       cur = conn.cursor()
#       cur.execute(f"SELECT block FROM users WHERE user_id = {message.text}")
#       result = cur.fetchall()
#       if len(result) == 0:
#         await message.answer('Такой пользователь не найден в базе данных.', reply_markup=kb)
#         await state.finish()
#       else:
#         a = result[0]
#         id = a[0]
#         if id == 0:
#           cur.execute(f"UPDATE users SET block = 1 WHERE user_id = {message.text}")
#           conn.commit()
#           await message.answer('Пользователь успешно добавлен в ЧС.', reply_markup=kb)
#           await state.finish()
#           await bot.send_message(message.text, 'Ты был забанен Администрацией')
#         else:
#           await message.answer('Данный пользователь уже получил бан', reply_markup=kb)
#           await state.finish()
#     else:
#       await message.answer('Ты вводишь буквы...\n\nВведи ID')

# @dp.message_handler(content_types=['text'], text='Убрать из ЧС')
# async def hfandler(message: types.Message, state: FSMContext):
#   cur = conn.cursor()
#   cur.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
#   result = cur.fetchone()
#   if result is None:
#     if message.chat.id == ADMIN:
#       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#       keyboard.add(types.InlineKeyboardButton(text="Назад"))
#       await message.answer('Введите id пользователя, которого нужно разблокировать.\nДля отмены нажмите кнопку ниже', reply_markup=keyboard)
#       await dialog.whitelist.set()

# @dp.message_handler(state=dialog.whitelist)
# async def proc(message: types.Message, state: FSMContext):
#   if message.text == 'Отмена':
#     await message.answer('Отмена! Возвращаю назад.', reply_markup=kb)
#     await state.finish()
#   else:
#     if message.text.isdigit():
#       cur = conn.cursor()
#       cur.execute(f"SELECT block FROM users WHERE user_id = {message.text}")
#       result = cur.fetchall()
#       conn.commit()
#       if len(result) == 0:
#         await message.answer('Такой пользователь не найден в базе данных.', reply_markup=kb)
#         await state.finish()
#       else:
#         a = result[0]
#         id = a[0]
#         if id == 1:
#           cur = conn.cursor()
#           cur.execute(f"UPDATE users SET block = 0 WHERE user_id = {message.text}")
#           conn.commit()
#           await message.answer('Пользователь успешно разбанен.', reply_markup=kb)
#           await state.finish()
#           await bot.send_message(message.text, 'Вы были разблокированы администрацией.')
#         else:
#           await message.answer('Данный пользователь не получал бан.', reply_markup=kb)
#           await state.finish()
#     else:
#       await message.answer('Ты вводишь буквы...\n\nВведи ID')

# @dp.message_handler(content_types=['text'], text='Статистика')
# async def hfandler(message: types.Message, state: FSMContext):
# 	cur = conn.cursor()
# 	cur.execute('''select * from users''')
# 	results = cur.fetchall()
# 	await message.answer(f'Людей которые когда либо заходили в бота: {len(results)}')
