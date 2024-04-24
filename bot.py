from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


bot = Bot(token='7006550283:AAHBTYapAML05uKHWTtkyEClqiFpsCbg_iM')  # Объект бота
dp = Dispatcher(bot)  # Диспетчер

questions = {
    "Вопрос 1": {
        "question": "Как звали пушкинского Онегина?",
        "answers": ["Александр", "Иван", "Евгений", "Михаил"],
        "correct": "Евгений"
    },
    "Вопрос 2": {
        "question": "Какой город является столицей Франции?",
        "answers": ["Лондон", "Берлин", "Париж", "Рим"],
        "correct": "Париж"
    },
    "Вопрос 3": {
        "question": "Сколько планет в Солнечной системе?",
        "answers": ["7", "9", "8", "10"],
        "correct": "8"
    },
    "Вопрос 4": {
        "question": "Как звали известного физика, автора теории относительности?",
        "answers": ["Ньютон", "Эйнштейн", "Кюри", "Максвелл"],
        "correct": "Эйнштейн"
    },
    "Вопрос 5": {
        "question": "Как называется самая большая планета в Солнечной системе?",
        "answers": ["Марс", "Юпитер", "Венера", "Сатурн"],
        "correct": "Юпитер"
    },
}

current_question_number = 1


@dp.message_handler(commands=['start'])  # Начало викторины
async def start(message: types.Message):
    global current_question_number
    current_question_number = 1
    await message.answer("Добро пожаловать в игру 'Кто хочет стать миллионером?'!")
    await ask_question(message)


async def ask_question(message: types.Message):  # Задаёт вопросы с вариантами
    global current_question_number
    question_key = f"Вопрос {current_question_number}"
    current_question = questions.get(question_key)
    await message.answer(current_question['question'])

    for answer in current_question['answers']:
        await message.answer(answer)


@dp.message_handler()  # Проверка на правильность вопроса
async def check_answer(message: types.Message):
    global current_question_number
    user_answer = message.text
    current_question_key = f"Вопрос {current_question_number}"
    current_question = questions.get(current_question_key)
    correct_answer = current_question['correct']

    if user_answer == correct_answer:
        await message.answer("Правильно!")
        current_question_number += 1
        next_question_key = f"Вопрос {current_question_number}"  # Проверка остались ли ещё вопросы
        if next_question_key in questions:
            await ask_question(message)
        else:
            await message.answer("Поздравляем, вы ответили на все вопросы! Игра окончена.")
    else:
        await message.answer("Неправильно! Наберите /start чтобы начать заново.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
