import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
import asyncio
import logging

API_TOKEN = os.environ.get('TOKEN_BOT')
HR_CHAT_ID = 944196754
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Состояния для анкеты
class ApplyForm(StatesGroup):
    name = State()
    city = State()
    age = State()
    specialization = State()
    experience = State()
    gov_experience = State()
    portfolio = State()
    contact = State()
    confirm = State()
    edit_field = State()


# Состояния для вопросов
class QuestionForm(StatesGroup):
    waiting_question = State()
    confirm_question = State()



# Главное меню
main_menu_buttons = [
    [KeyboardButton(text='ℹ️ Об Connect\'e'), KeyboardButton(text='💼 Connect • Карьера')],
    [KeyboardButton(text='📝 Откликнуться'), KeyboardButton(text='📞 Контакты')],
    [KeyboardButton(text='❓ Задать вопрос')]
]
main_menu = ReplyKeyboardMarkup(keyboard=main_menu_buttons, resize_keyboard=True)

# Кнопка старт
start_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='🚀 Старт')]],
    resize_keyboard=True
)

# Раздел "Об Connect'e"
about_connect_buttons = [[KeyboardButton(text='◀️ В меню')]]
about_connect = ReplyKeyboardMarkup(keyboard=about_connect_buttons, resize_keyboard=True)

# Раздел "Connect • Карьера"
career_info_buttons = [
    [KeyboardButton(text='📝 Откликнуться'), KeyboardButton(text='◀️ В меню')]
]
career_info = ReplyKeyboardMarkup(keyboard=career_info_buttons, resize_keyboard=True)

# Кнопки специализации
specialization_buttons = [
    [KeyboardButton(text='🎨 Дизайнер'), KeyboardButton(text='👔 Менеджер')],
    [KeyboardButton(text='📊 Руководитель'), KeyboardButton(text='🛠️ Продюсер')],
    [KeyboardButton(text='📋 Режиссер'), KeyboardButton(text='📌 Другое')]
]
specialization_keyboard = ReplyKeyboardMarkup(keyboard=specialization_buttons, resize_keyboard=True)

# Кнопки да/нет
yes_no_buttons = [
    [KeyboardButton(text='✅ Да'), KeyboardButton(text='❌ Нет')]
]
yes_no_keyboard = ReplyKeyboardMarkup(keyboard=yes_no_buttons, resize_keyboard=True)

# Кнопки подтверждения анкеты
confirm_buttons = [
    [KeyboardButton(text='✈️ Отправить'), KeyboardButton(text='✏️ Изменить')]
]
confirm_keyboard = ReplyKeyboardMarkup(keyboard=confirm_buttons, resize_keyboard=True)

# Кнопки для выбора поля редактирования
edit_field_buttons = [
    [KeyboardButton(text='📛 Имя'), KeyboardButton(text='🏙️ Город')],
    [KeyboardButton(text='🎂 Возраст'), KeyboardButton(text='🎯 Специализация')],
    [KeyboardButton(text='⏰ Опыт'), KeyboardButton(text='🏛️ Опыт с гос.мероприятиями')],
    [KeyboardButton(text='🗂️ Портфолио'), KeyboardButton(text='📞 Контакты')],
    [KeyboardButton(text='❌ Отмена')]
]
edit_field_keyboard = ReplyKeyboardMarkup(keyboard=edit_field_buttons, resize_keyboard=True)

# Кнопки согласия
consent_buttons = [
    [KeyboardButton(text='✅ Согласен(на)'), KeyboardButton(text='❌ Отмена')]
]
consent_keyboard = ReplyKeyboardMarkup(keyboard=consent_buttons, resize_keyboard=True)

# Кнопки для подтверждения вопроса
question_confirm_buttons = [
    [KeyboardButton(text='✅ Да, отправить HR'), KeyboardButton(text='❌ Нет, отменить')]
]
question_confirm_keyboard = ReplyKeyboardMarkup(keyboard=question_confirm_buttons, resize_keyboard=True)


# Обработка стартового сообщения
@dp.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Привет! 👋\n\n"
        "Мы №1 в B2G – и переносим надёжность в коммерцию. "
        "Рады вашему интересу к Connect Group. Мы делаем крупные события по всей России и ищем людей, которым близки надёжность процессов и креатив.\n"
        "Готовы познакомиться и понять, где мы можем совпасть по задачам. Нажмите «Старт», чтобы выбрать раздел, отклинуться или задать вопрос.\n\n"
        "Продолжая пользоваться ботом, вы даёте согласие на обработку персональных данных, полученных через Telegram, в соответствии с нашей политикой.",
        reply_markup=start_button
    )


# Обработка кнопки "Старт"
@dp.message(F.text == '🚀 Старт')
async def start_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Выберите раздел или задайте вопрос боту. Если ответа не найдётся – мы передадим его HR.\n\n"
        "Можно написать свой вопрос текстом",
        reply_markup=main_menu
    )


# Главное меню
@dp.message(F.text == 'ℹ️ Об Connect\'e')
async def about_connect_func(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Собираем и реализуем масштабные и коммерческие события по всей стране: форумы, конгрессы, церемонии, фестивали, протокольные мероприятия. Мы №1 в B2G и переносим эту надёжность в коммерческие проекты – с креативом и человеческим теплом.\n"
        "Ключсы, процессы и полезности смотрите в нашем TG-канале: @ConnectEvent\n"
        "Сайт: connect-event.ru\n\n"
        "Если хотите присоединиться – вернитесь в меню и нажмите «Откликнуться».",
        reply_markup=about_connect
    )


@dp.message(F.text == '💼 Connect • Карьера')
async def career_func(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Этот бот – ваш быстрый вход в экосистему Connect: вакансии, проектная занятость и фрилан.\n"
        "Как это работает:\n"
        "1. Вы заполните анкету и делитесь портфолио.\n"
        "2. Если профиль отклика на наши задачам, HR пригласит на беседу – в офисе или онлайн.\n"
        "3. Если после разговора и просмотра ключей случится полный мьстч: то фиксируем формат работы и ставки.\n"
        "Дальше – подключаем к релевантным проектам.\n\n"
        "Готовы познакомиться ближе? Нажмите «Откликнуться».",
        reply_markup=career_info
    )


# Возврат в главное меню
@dp.message(F.text == '◀️ В меню')
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Вы вернулись в главное меню. Выберите раздел или задайте вопрос боту.",
        reply_markup=main_menu
    )


# Обработчик для кнопки "Откликнуться"
@dp.message(F.text == '📝 Откликнуться')
async def apply_func(message: types.Message, state: FSMContext):
    await state.clear()
    await state.set_state(ApplyForm.name)
    await message.answer(
        "Отлично! Всего несколько вопросов – и мы поймём, куда вас пригласить в первую очередь. Можно отвечать текстом или выбирать варианты.",
        reply_markup=types.ReplyKeyboardRemove()
    )
    await message.answer("Как вас зовут? (ФИО или имя и фамилия)")


# Обработчик для кнопки "Контакты"
@dp.message(F.text == '📞 Контакты')
async def contacts_func(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "По вопросам найма и проектной занятости:\n"
        "Елизавета, HR Connect'а – @diosish",
        reply_markup=main_menu
    )


# Обработчик для кнопки "Задать вопрос"
@dp.message(F.text == '❓ Задать вопрос')
async def question_func(message: types.Message, state: FSMContext):
    await state.clear()
    await state.set_state(QuestionForm.waiting_question)
    await message.answer(
        "Напишите ваш вопрос сюда текстом. Бот попробует подобрать ответ. Если не найдём – передадим HR и вернём с ответом.\n\n"
        "Примеры:\n"
        "• Какие у вас проекты в коммерции?\n"
        "• Есть ли вакансии менеджеров в Москве?\n"
        "• Как попасть во фрилан-пул?",
        reply_markup=types.ReplyKeyboardRemove()
    )


# Обработчик получения вопроса
@dp.message(QuestionForm.waiting_question)
async def receive_question(message: types.Message, state: FSMContext):
    await state.update_data(question=message.text)
    await state.set_state(QuestionForm.confirm_question)
    await message.answer(
        f"Ваш вопрос:\n\n{message.text}\n\n"
        "Не получилось найти точный ответ. Хотите отправить этот вопрос HR Connect?",
        reply_markup=question_confirm_keyboard
    )


# Подтверждение отправки вопроса
@dp.message(QuestionForm.confirm_question, F.text == '✅ Да, отправить HR')
async def confirm_send_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    question = data.get('question', '')

    user_tag = f"@{message.from_user.username}" if message.from_user.username else "Нет тега"
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    # Отправляем вопрос HR
    await bot.send_message(
        HR_CHAT_ID,
        f"❓ Новый вопрос от пользователя:\n\n"
        f"Пользователь: {user_name}\n"
        f"Telegram: {user_tag}\n"
        f"ID: {user_id}\n\n"
        f"Вопрос:\n{question}"
    )

    await message.answer(
        "Ваш вопрос передан HR Connect. Если потребуется уточнение – свяжемся с вами.\n"
        "Если хотите ускорить процесс – напишите @diosish.",
        reply_markup=main_menu
    )
    await state.clear()


# Отмена отправки вопроса
@dp.message(QuestionForm.confirm_question, F.text == '❌ Нет, отменить')
async def cancel_send_question(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Вопрос не отправлен. Вы вернулись в главное меню.",
        reply_markup=main_menu
    )


# Обработчик для имени
@dp.message(ApplyForm.name)
async def process_name(message: types.Message, state: FSMContext):
    if message.text == '◀️ В меню':
        await back_to_main_menu(message, state)
        return

    data = await state.get_data()
    if 'editing_field' in data:
        await state.update_data(name=message.text, editing_field=None)
        await show_confirmation(message, state)
    else:
        await state.update_data(name=message.text)
        await state.set_state(ApplyForm.city)
        await message.answer("В каком городе вы живёте?")


# Обработчик для города
@dp.message(ApplyForm.city)
async def process_city(message: types.Message, state: FSMContext):
    if message.text == '◀️ В меню':
        await back_to_main_menu(message, state)
        return

    data = await state.get_data()
    if 'editing_field' in data:
        await state.update_data(city=message.text, editing_field=None)
        await show_confirmation(message, state)
    else:
        await state.update_data(city=message.text)
        await state.set_state(ApplyForm.age)
        await message.answer("Сколько вам лет? (можно число)")


# Обработчик для возраста
@dp.message(ApplyForm.age)
async def process_age(message: types.Message, state: FSMContext):
    if message.text == '◀️ В меню':
        await back_to_main_menu(message, state)
        return

    data = await state.get_data()
    if 'editing_field' in data:
        await state.update_data(age=message.text, editing_field=None)
        await show_confirmation(message, state)
    else:
        await state.update_data(age=message.text)
        await state.set_state(ApplyForm.specialization)
        await message.answer(
            "Укажите вашу специализацию (можно несколько):",
            reply_markup=specialization_keyboard
        )


# Обработчик для специализации
@dp.message(ApplyForm.specialization)
async def process_specialization(message: types.Message, state: FSMContext):
    if message.text == '◀️ В меню':
        await back_to_main_menu(message, state)
        return

    if message.text == '📌 Другое':
        await message.answer("Напишите свою роль:", reply_markup=types.ReplyKeyboardRemove())
        return

    data = await state.get_data()
    if 'editing_field' in data:
        await state.update_data(specialization=message.text, editing_field=None)
        await show_confirmation(message, state)
    else:
        await state.update_data(specialization=message.text)
        await state.set_state(ApplyForm.experience)
        await message.answer(
            "Сколько лет вы в ивенте и какие типы мероприятий делали?\n"
            "(кратко: «5 лет – форумы, конгрессы, концерты»)",
            reply_markup=types.ReplyKeyboardRemove()
        )


# Обработчик для опыта
@dp.message(ApplyForm.experience)
async def process_experience(message: types.Message, state: FSMContext):
    if message.text == '◀️ В меню':
        await back_to_main_menu(message, state)
        return

    data = await state.get_data()
    if 'editing_field' in data:
        await state.update_data(experience=message.text, editing_field=None)
        await show_confirmation(message, state)
    else:
        await state.update_data(experience=message.text)
        await state.set_state(ApplyForm.gov_experience)
        await message.answer(
            "Есть ли опыт с государственными мероприятиями?",
            reply_markup=yes_no_keyboard
        )


# Обработчик для опыта с гос. мероприятиями
@dp.message(ApplyForm.gov_experience)
async def process_gov_experience(message: types.Message, state: FSMContext):
    if message.text == '◀️ В меню':
        await back_to_main_menu(message, state)
        return

    data = await state.get_data()

    if message.text == '✅ Да' and 'editing_field' not in data:
        await state.update_data(gov_experience_answer='✅ Да')
        await message.answer(
            "Уточните, с какими (уровень/роль/регион):",
            reply_markup=types.ReplyKeyboardRemove()
        )
        return

    if 'editing_field' in data:
        if message.text == '✅ Да':
            await state.update_data(gov_experience_answer='✅ Да')
            await message.answer("Уточните, с какими (уровень/роль/регион):")
            return
        await state.update_data(gov_experience=message.text, editing_field=None)
        await show_confirmation(message, state)
    else:
        gov_exp = message.text
        if data.get('gov_experience_answer') == '✅ Да':
            gov_exp = f"✅ Да ({message.text})"

        await state.update_data(gov_experience=gov_exp)
        await state.set_state(ApplyForm.portfolio)
        await message.answer(
            "Портфолио или резюме – дайте, пожалуйста, ссылку.\n"
            "(можно прикрепить файл или написать «нет»)",
            reply_markup=types.ReplyKeyboardRemove()
        )


# Обработчик для портфолио (текст)
@dp.message(ApplyForm.portfolio, F.text)
async def process_portfolio_text(message: types.Message, state: FSMContext):
    if message.text == '◀️ В меню':
        await back_to_main_menu(message, state)
        return

    data = await state.get_data()
    if 'editing_field' in data:
        await state.update_data(portfolio=message.text, portfolio_file=None, editing_field=None)
        await show_confirmation(message, state)
    else:
        await state.update_data(portfolio=message.text, portfolio_file=None)
        await state.set_state(ApplyForm.contact)
        await message.answer("Ваши контакты для связи (телеграм @, e-mail, телефон).")


# Обработчик для портфолио (документ)
@dp.message(ApplyForm.portfolio, F.document)
async def process_portfolio_document(message: types.Message, state: FSMContext):
    document = message.document
    file_info = {
        'type': 'document',
        'file_id': document.file_id,
        'file_name': document.file_name,
        'caption': message.caption or 'Файл портфолио/резюме'
    }

    data = await state.get_data()
    if 'editing_field' in data:
        await state.update_data(
            portfolio=f"Файл: {document.file_name}",
            portfolio_file=file_info,
            editing_field=None
        )
        await show_confirmation(message, state)
    else:
        await state.update_data(
            portfolio=f"Файл: {document.file_name}",
            portfolio_file=file_info
        )
        await state.set_state(ApplyForm.contact)
        await message.answer("Отлично! Файл получен.\n\nВаши контакты для связи (телеграм @, e-mail, телефон).")


# Обработчик для портфолио (фото)
@dp.message(ApplyForm.portfolio, F.photo)
async def process_portfolio_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    file_info = {
        'type': 'photo',
        'file_id': photo.file_id,
        'caption': message.caption or 'Фото портфолио'
    }

    data = await state.get_data()
    if 'editing_field' in data:
        await state.update_data(
            portfolio="Фото портфолио",
            portfolio_file=file_info,
            editing_field=None
        )
        await show_confirmation(message, state)
    else:
        await state.update_data(
            portfolio="Фото портфолио",
            portfolio_file=file_info
        )
        await state.set_state(ApplyForm.contact)
        await message.answer("Отлично! Фото получено.\n\nВаши контакты для связи (телеграм @, e-mail, телефон).")


# Обработчик для контактов
@dp.message(ApplyForm.contact)
async def process_contact(message: types.Message, state: FSMContext):
    if message.text == '◀️ В меню':
        await back_to_main_menu(message, state)
        return

    data = await state.get_data()
    if 'editing_field' in data:
        await state.update_data(contact=message.text, editing_field=None)
        await show_confirmation(message, state)
    else:
        await state.update_data(contact=message.text)
        await show_confirmation(message, state)


# Функция показа подтверждения
async def show_confirmation(message: types.Message, state: FSMContext):
    user_data = await state.get_data()

    portfolio_text = user_data.get('portfolio', 'не указано')
    portfolio_file = user_data.get('portfolio_file')
    if portfolio_file:
        portfolio_text += " (файл прикреплен)"

    await state.set_state(ApplyForm.confirm)
    await message.answer(
        f"Спасибо! Проверьте, всё ли верно?🔍\n\n"
        f"• Имя: {user_data.get('name', 'не указано')}\n"
        f"• Город: {user_data.get('city', 'не указано')}\n"
        f"• Возраст: {user_data.get('age', 'не указано')}\n"
        f"• Специализация: {user_data.get('specialization', 'не указано')}\n"
        f"• Опыт и типы событий: {user_data.get('experience', 'не указано')}\n"
        f"• Опыт с гос.мероприятиями: {user_data.get('gov_experience', 'не указано')}\n"
        f"• Портфолио/резюме: {portfolio_text}\n"
        f"• Контакты: {user_data.get('contact', 'не указано')}\n\n"
        "Если всё верно, нажмите «Отправить», чтобы отправить анкету HR.",
        reply_markup=confirm_keyboard
    )


# Обработчик для кнопки "Отправить"
@dp.message(ApplyForm.confirm, F.text == "✈️ Отправить")
async def confirm_application(message: types.Message, state: FSMContext):
    await message.answer(
        "Подтверждаю, что предоставил(а) данные добровольно и согласен(на) на их обработку для целей найма и проектного взаимодействия с Connect Group.",
        reply_markup=consent_keyboard
    )


# Обработчик согласия на обработку данных
@dp.message(ApplyForm.confirm, F.text == "✅ Согласен(на)")
async def send_application(message: types.Message, state: FSMContext):
    user_data = await state.get_data()

    user_tag = f"@{message.from_user.username}" if message.from_user.username else "Нет тега"
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    application_text = (
        f"📋 Новая анкета:\n\n"
        f"👤 Пользователь Telegram: {user_name}\n"
        f"🔗 Тег: {user_tag}\n"
        f"🆔 ID чата: {user_id}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"Имя: {user_data.get('name', 'не указано')}\n"
        f"Город: {user_data.get('city', 'не указано')}\n"
        f"Возраст: {user_data.get('age', 'не указано')}\n"
        f"Специализация: {user_data.get('specialization', 'не указано')}\n"
        f"Опыт: {user_data.get('experience', 'не указано')}\n"
        f"Опыт с гос.мероприятиями: {user_data.get('gov_experience', 'не указано')}\n"
        f"Портфолио/резюме: {user_data.get('portfolio', 'не указано')}\n"
        f"Контакты: {user_data.get('contact', 'не указано')}"
    )

    await bot.send_message(HR_CHAT_ID, application_text)

    portfolio_file = user_data.get('portfolio_file')
    if portfolio_file:
        try:
            if portfolio_file['type'] == 'document':
                await bot.send_document(
                    HR_CHAT_ID,
                    document=portfolio_file['file_id'],
                    caption=f"📎 Портфолио/резюме от {user_data.get('name', 'кандидата')}"
                )
            elif portfolio_file['type'] == 'photo':
                await bot.send_photo(
                    HR_CHAT_ID,
                    photo=portfolio_file['file_id'],
                    caption=f"📎 Портфолио от {user_data.get('name', 'кандидата')}"
                )
        except Exception as e:
            logging.error(f"Ошибка при отправке файла HR: {e}")

    await message.answer(
        "Анкета отправлена HR Connect'а. Если будет мьстч с ближайшими задачам – свяжемся с вами.\n"
        "Пока ждёте – загляните в наш канал @ConnectEvent: там наши ключсы и все внутренние процессы.",
        reply_markup=main_menu
    )
    await state.clear()


# Обработчик для кнопки "Изменить"
@dp.message(ApplyForm.confirm, F.text == "✏️ Изменить")
async def edit_application(message: types.Message, state: FSMContext):
    await state.set_state(ApplyForm.edit_field)
    await message.answer(
        "Выберите поле для редактирования:",
        reply_markup=edit_field_keyboard
    )


# Обработчик выбора поля для редактирования
@dp.message(ApplyForm.edit_field)
async def select_field_to_edit(message: types.Message, state: FSMContext):
    if message.text == '❌ Отмена':
        await show_confirmation(message, state)
        return

    field_mapping = {
        '📛 Имя': ('name', ApplyForm.name, 'Введите новое имя:'),
        '🏙️ Город': ('city', ApplyForm.city, 'Введите новый город:'),
        '🎂 Возраст': ('age', ApplyForm.age, 'Введите новый возраст:'),
        '🎯 Специализация': ('specialization', ApplyForm.specialization, 'Укажите новую специализацию:'),
        '⏰ Опыт': ('experience', ApplyForm.experience, 'Опишите опыт заново:'),
        '🏛️ Опыт с гос.мероприятиями': ('gov_experience', ApplyForm.gov_experience,
                                     'Есть ли опыт с государственными мероприятиями?'),
        '🗂️ Портфолио': ('portfolio', ApplyForm.portfolio, 'Укажите новое портфолио (ссылку, файл или фото):'),
        '📞 Контакты': ('contact', ApplyForm.contact, 'Введите новые контакты:')
    }

    if message.text in field_mapping:
        field_key, next_state, prompt = field_mapping[message.text]
        await state.update_data(editing_field=field_key)
        await state.set_state(next_state)

        if field_key == 'specialization':
            await message.answer(prompt, reply_markup=specialization_keyboard)
        elif field_key == 'gov_experience':
            await message.answer(prompt, reply_markup=yes_no_keyboard)
        else:
            await message.answer(prompt, reply_markup=types.ReplyKeyboardRemove())


# Обработка отмены при согласии
@dp.message(ApplyForm.confirm, F.text == "❌ Отмена")
async def cancel_consent(message: types.Message, state: FSMContext):
    await show_confirmation(message, state)


# Обработчик нераспознанных сообщений (должен быть последним)
@dp.message()
async def handle_unrecognized(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    # Если пользователь в процессе заполнения формы - игнорируем
    if current_state in [ApplyForm.name, ApplyForm.city, ApplyForm.age,
                         ApplyForm.specialization, ApplyForm.experience,
                         ApplyForm.gov_experience, ApplyForm.portfolio,
                         ApplyForm.contact, ApplyForm.confirm, ApplyForm.edit_field,
                         QuestionForm.waiting_question, QuestionForm.confirm_question]:
        return

    # Сохраняем нераспознанное сообщение
    await state.update_data(question=message.text)
    await state.set_state(QuestionForm.confirm_question)

    await message.answer(
        f"Ваше сообщение:\n\n{message.text}\n\n"
        "Не получилось найти точный ответ. Хотите отправить это сообщение HR Connect?",
        reply_markup=question_confirm_keyboard
    )


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':

    asyncio.run(main())
