from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

school_types_buttons = {"school": "🏫 Школа", "lyceum": "🏫 Лицей", "gymnasium": "🏫 Гимназия"}


def pupil_age_keyboard():
    pupil_age_keyboard_builder = ReplyKeyboardBuilder()
    for age in range(7, 20):
        button = KeyboardButton(text=str(age))
        if age in [11, 16]:
            pupil_age_keyboard_builder.row(button)
        else:
            pupil_age_keyboard_builder.add(button)
    return pupil_age_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


def pupil_school_type_keyboard():
    pupil_school_type_keyboard_builder = ReplyKeyboardBuilder()
    for school_type in school_types_buttons:
        button = KeyboardButton(text=school_types_buttons[school_type])
        pupil_school_type_keyboard_builder.row(button)
    return pupil_school_type_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


lyceum_buttons = (
    "⬅️ Назад",
    "Лицей «Бизнес и информационные технологии»",
    "Инженерно-технологический лицей № 25",
    "Лицей № 29",
    "Лицей № 54",
    "Лицей № 64",
    "Лицей № 66",
    "Лицей № 74",
    "Лицей № 92",
    "Лицей № 137",
    "Лицей № 143",
    "Лицей № 145",
    "Лицей № 149",
    "Лицей № 166"
)

def lyceum_keyboard():
    lyceum_keyboard_builder = ReplyKeyboardBuilder()
    for lyceum in lyceum_buttons:
        button = KeyboardButton(text=lyceum)
        lyceum_keyboard_builder.row(button)
    return lyceum_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)

gymnasium_buttons = (
    "⬅️ Назад",
    "Гимназия № 9",
    "Гимназия № 12 имени Героя Советского Союза В.П. Горячева",
    "Гимназия № 19",
    "Гимназия № 26",
    "Гимназия № 43",
    "Гимназия № 62",
    "Гимназия № 69 им. И.М. Чередова",
    "Гимназия № 75",
    "Гимназия № 76",
    "Гимназия № 84",
    "Гимназия № 85",
    "Гимназия № 88",
    "Гимназия № 115",
    "Гимназия № 123 с углубленным изучением отдельных предметов им. О.И. Охрименко",
    "Гимназия № 139",
    "Гимназия № 140",
    "Гимназия № 146",
    "Гимназия № 147",
    "Гимназия № 150",
    "Гимназия № 159"
)

def gymnasium_keyboard():
    gymnasium_keyboard_builder = ReplyKeyboardBuilder()
    for gymnasium in gymnasium_buttons:
        button = KeyboardButton(text=gymnasium)
        gymnasium_keyboard_builder.row(button)
    return gymnasium_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


school_buttons = (
    "⬅️ Назад",
    "Школа № 1",
    "Школа № 2",
    "Школа № 3",
    "Школа № 4 имени И.И. Стрельникова",
    "Школа № 5",
    "Школа № 6",
    "Школа № 7 имени Героя Советского Союза М.М. Кузьмина",
    "Школа № 8 имени Героя Советского Союза М.Я. Лаптева",
    "Школа № 10",
    "Школа № 11",
    "Школа № 13 имени А.С. Пушкина",
    "Школа № 14 с углубленным изучением отдельных предметов",
    "Школа № 15",
    "Школа № 16",
    "Школа № 17",
    "Школа № 18 с углубленным изучением отдельных предметов",
    "Школа № 21",
    "Школа № 23",
    "Школа № 24",
    "Школа № 27",
    "Школа № 28 с углубленным изучением отдельных предметов",
    "Школа № 30",
    "Школа № 31 с углубленным изучением отдельных предметов",
    "Школа № 32",
    "Школа № 33",
    "Школа № 34",
    "Начальная Школа № 35",
    "Школа № 36",
    "Школа № 37",
    "Школа № 38 с углубленным изучением отдельных предметов",
    "Школа № 39 с углубленным изучением отдельных предметов",
    "Школа № 40 с углубленным изучением отдельных предметов имени Героя Советского Союза И.В. Панфилова",
    "Школа № 41",
    "Школа № 42",
    "Школа № 44",
    "Школа № 45",
    "Школа № 46",
    "Школа № 47 с углубленным изучением отдельных предметов",
    "Школа № 48",
    "Школа № 49",
    "Школа № 50",
    "Школа № 51",
    "Школа № 53",
    "Школа № 55 имени Л.Я. Кичигиной и В.И. Кичигина",
    "Школа № 56 с углубленным изучением отдельных предметов",
    "Школа № 58",
    "Школа № 59 имени Героя Российской Федерации И.А. Мишина",
    "Школа № 60",
    "Школа № 61",
    "Школа № 63",
    "Школа № 65",
    "Школа № 67",
    "Школа № 68",
    "Школа № 70",
    "Школа № 71",
    "Школа № 72 с углубленным изучением отдельных предметов",
    "Школа № 73 с углубленным изучением отдельных предметов",
    "Школа № 77",
    "Школа № 78",
    "Школа № 79",
    "Школа № 80",
    "Школа № 81",
    "Школа № 82",
    "Школа № 83",
    "Школа № 86",
    "Школа № 87",
    "Школа № 89",
    "Школа № 90 имени Д.М. Карбышева",
    "Школа № 91",
    "Школа № 93",
    "Школа № 94",
    "Школа № 95 с углубленным изучением отдельных предметов",
    "Школа № 96",
    "Школа № 97",
    "Школа № 98",
    "Школа № 99 с углубленным изучением отдельных предметов",
    "Школа № 100",
    "Школа № 101",
    "Школа № 103",
    "Школа № 104",
    "Школа № 105 имени Героя Советского Союза Н.П. Бударина",
    "Школа № 106",
    "Школа № 107",
    "Школа № 108",
    "Школа № 109 с углубленным изучением отдельных предметов",
    "Школа № 110",
    "Школа № 111",
    "Школа № 112",
    "Школа № 113",
    "Школа № 114",
    "Школа № 116",
    "Школа № 118",
    "Школа № 119",
    "Школа № 120",
    "Школа № 122",
    "Школа № 124",
    "Школа № 126",
    "Школа № 127",
    "Школа № 129",
    "Школа № 130",
    "Школа № 131",
    "Школа № 132",
    "Школа № 133",
    "Школа № 134",
    "Школа № 135 имени Героя Советского Союза Алексея Петровича Дмитриева",
    "Школа № 138",
    "Школа № 141",
    "Школа № 142",
    "Школа № 144",
    "Школа № 148",
    "Школа № 151",
    "Школа № 152",
    "Школа № 160",
    "Школа № 161",
    "Школа № 162"
)


def school_keyboard():
    school_keyboard_builder = ReplyKeyboardBuilder()
    for school in school_buttons:
        button = KeyboardButton(text=school)
        school_keyboard_builder.row(button)
    return school_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


def grade_keyboard():
    grade_keyboard_builder = ReplyKeyboardBuilder()
    for grade in range(1, 12):
        button = KeyboardButton(text=str(grade))
        if grade in [6]:
            grade_keyboard_builder.row(button)
        else:
            grade_keyboard_builder.add(button)
    return grade_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


answer_buttons = ["✅ Да", "❌ Нет"]


def request_keyboard():
    request_keyboard_builder = ReplyKeyboardBuilder()
    for request in answer_buttons:
        button = KeyboardButton(text=request)
        request_keyboard_builder.add(button)
    return request_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


university_list = [
    "Омский государственный технический университет",  # ОмГТУ
    "Омский государственный университет им. Ф.М. Достоевского",  # ОмГУ
    "Омский государственный педагогический университет",  # ОмГПУ
    "Сибирский государственный автомобильно-дорожный университет",  # СибАДИ
    "Омский государственный аграрный университет им. П.А. Столыпина",  # ОмГАУ
    "Омский государственный медицинский университет",  # ОмГМУ
    "Омский государственный университет путей сообщения",  # ОмГУПС
    "Сибирский государственный университет физической культуры и спорта",  # СибГУФК
    "Омская юридическая академия",  # ОмЮА
    "Омская гуманитарная академия",  # ОмГА
    "Омский авиационный колледж им. Н.Е. Жуковского",
    "Омский колледж отраслевых технологий строительства и транспорта",
    "Сибирский профессиональный колледж",
    "Омский технологический колледж",
    "Омский музыкально-педагогический колледж",
    "Сибирский многопрофильный колледж «Перспектива»",
    "Международный технологический колледж Российского биотехнологического университета",
    "Омский филиал Московского международного колледжа цифровых технологий «Академия ТОП»",
    "Колледж инновационных технологий, экономики и коммерции",
    "Омский колледж профессиональных технологий",
    "Нет в списке"
]

next_button = {"next": "➡️ Продолжить"}


def university_keyboard(check_list):
    university_keyboard_builder = InlineKeyboardBuilder()
    for n in range(len(university_list)):
        if n in check_list:
            button = InlineKeyboardButton(text="✅ " + university_list[n], callback_data=str(n))
            university_keyboard_builder.row(button)
        else:
            button = InlineKeyboardButton(text=university_list[n], callback_data=str(n))
            university_keyboard_builder.row(button)
    button = InlineKeyboardButton(text=next_button["next"], callback_data="next")
    university_keyboard_builder.row(button)
    return university_keyboard_builder.as_markup(resize_keyboard=True)


answer_q3 = ["Очень часто", "Иногда", "Редко", "Не интересуюсь"]


def keyboard_q3():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in answer_q3:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


# Функция для создания клавиатуры для вопроса 2
answer_q4 = ["Да, с удовольствием", "Если будет интересно", "Скорее нет", "Нет"]


def keyboard_q4():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in answer_q4:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


# Функция для создания клавиатуры для вопроса 5 (любимый язык программирования)
answer_q5 = [
    "Python",
    "JavaScript",
    "C++",
    "Scratch",
    "У меня пока нет любимого языка"
]


def keyboard_q5():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in answer_q5:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


answer_q6 = [
    "Создание игры",
    "Разработка мобильного приложения",
    "Разработка робота",
    "Создание веб-сайта",
    "Не знаю, но хотел(а) бы научиться"
]


def keyboard_q6():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in answer_q6:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)

