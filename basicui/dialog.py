from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import dal.dbinit as db

class dialog(StatesGroup):
	registration = State()
	admin = State()
	participant = State()
	calendar = State()
	checkin = State()
	nickname = State()

async def start(message: Message):
	db.cur = db.conn.cursor()
	db.cur.execute(f"SELECT * FROM participant WHERE tg_id = {message.chat.id}")
	result = db.cur.fetchone()
	if result is None:
		await dialog.registration.set()
	elif result["is_admin"] == 1:
		await dialog.admin.set()
	else:
		await dialog.participant.set()

async def admin_registration(message: Message):
	db.cur.execute(f'''INSERT INTO participant VALUES ('{message.from_user.id}', '{message.from_user.first_name}', 'nick','1')''')
	db.conn.commit()
	await message.answer('Вы админ!')
	await dialog.admin.set()

async def participant_registration(message: Message):
	db.cur.execute(f'''INSERT INTO participant VALUES ('{message.from_user.id}', '{message.from_user.first_name}', 'nick','0')''')
	db.conn.commit()
	await message.answer('Вы участник!')
	await dialog.participant.set()

async def start_registration(message: Message, state: FSMContext):
	kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
	kb.add(types.InlineKeyboardButton(text="Сотрудник"))
	kb.add(types.InlineKeyboardButton(text="Учащийся"))
	await message.answer('Привет, я тебя не знаю! Ты сотрудник школы или учащийся?', reply_markup=kb)
