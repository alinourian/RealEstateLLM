buy_rent = {
    'name': 'buy/rent',
    'type': 'option',
    'question': 'Do you want to buy or rent?',
    'question-en': 'Do you want to buy or rent?',
    'question-ar': 'هل تريد أن تشتري أو تستأجر؟',
    'question-fa': 'آیا قصد خرید دارید یا اجاره؟',
    'question-ur': 'کیا آپ خریدنا چاہتے ہیں یا کرایہ پر لینا چاہتے ہیں؟',
    'question-zh-CN': '你想买还是租？',
    'question-ru': 'Вы хотите купить или арендовать?',
    'question-hi': 'क्या आप खरीदना या किराये पर लेना चाहते हैं?',
    'valid_response': {0: 'rent', 1: 'buy'},
    'parent': '',
    'children': ['rent__budget', 'buy__budget']
}

rent__budget = {
    'name': 'rent__budget',
    'type': 'scroll',
    'question': 'How much money do you have per month?',
    'question-en': 'How much money do you have per month?',
    'question-ar': 'كم من المال لديك شهريا للإيجار؟',
    'question-fa': 'چه مبلغی برای اجاره یک ماه درنظر دارید؟',
    'question-ur': 'آپ کے پاس کرایہ کے لیے ماہانہ کتنے پیسے ہیں؟',
    'question-zh-CN': '你每个月有多少钱房租？',
    'question-ru': 'Сколько у вас денег в месяц на аренду?',
    'question-hi': 'आपके पास प्रति माह किराए के लिए कितना पैसा है?',
    'valid_response': {0: 1000, 1: 5000},
    'parent': 'buy/rent',
    'children': ['time']
}

buy__budget = {
    'name': 'buy__budget',
    'type': 'scroll',
    'question': 'How much money do you have?',
    'question-en': 'How much money do you have?',
    'question-ar': 'كم من المال لديك؟',
    'question-fa': 'چقدر سرمایه درنظر دارید؟',
    'question-ur': 'تمہارے پاس کتنی رقم ہے؟',
    'question-zh-CN': '你有多少钱？',
    'question-ru': 'Сколько у тебя денег?',
    'question-hi': 'आपके पास कितना पैसा है?',
    'valid_response': {0: 50000, 1: 500000},
    'parent': 'buy/rent',
    'children': ['ready/off-plane']
}

time = {
    'name': 'time',
    'type': 'input',
    'question': 'How long are you looking to rent the property for?',
    'question-en': 'How long are you looking to rent the property for?',
    'question-ar': 'ما هي المدة التي تبحث فيها عن تأجير العقار؟',
    'question-fa': 'برای چه مدت به دنبال اجاره هستنید؟',
    'question-ur': 'آپ کتنے عرصے سے پراپرٹی کرایہ پر لینا چاہتے ہیں؟',
    'question-zh-CN': '您打算租用该房产多久？',
    'question-ru': 'На какой срок вы планируете арендовать недвижимость?',
    'question-hi': 'आप कितने समय के लिए संपत्ति किराए पर लेना चाहते हैं?',
    'valid_response': {0: 'less than 6 month', 1: '6 month', 2: '1 year'},
    'parent': 'rent__budget',
    'children': ['rent__property-type', 'rent__property-type', 'rent__property-type']
}

ready_off_plan = {
    'name': 'ready/off-plane',
    'type': 'option',
    'question': 'Do you want it ready or off-plan?',
    'question-en': 'Do you want it ready or off-plan?',
    'question-ar': '',
    'question-fa': 'آیا قصد پیش‌خرید دارید یا واحد آماده می‌خواهید؟',
    'question-ur': '',
    'question-zh-CN': '',
    'question-ru': '',
    'question-hi': '',
    'valid_response': {0: 'ready', 1: 'off-plan'},
    'parent': 'buy__budget',
    'children': ['buy__property-type', 'buy__property-type']
}

rent__property_type = {
    'name': 'rent__property-type',
    'type': 'option',
    'question': 'What kind of property type do you want?',
    'question-en': 'What kind of property type do you want?',
    'question-ar': 'ما نوع الملكية التي تريدها؟',
    'question-fa': 'چه نوع واحدی در نظر دارید؟',
    'question-ur': 'آپ کس قسم کی پراپرٹی چاہتے ہیں؟',
    'question-zh-CN': '您想要什么样的房产类型？',
    'question-ru': 'Какой тип недвижимости вы хотите?',
    'question-hi': 'आप किस प्रकार की संपत्ति चाहते हैं?',
    'valid_response': {0: 'Apartment', 1: 'vila'},
    'parent': 'time',
    'children': ['rent__square-root', 'rent__square-root']
}

buy__property_type = {
    'name': 'buy__property-type',
    'type': 'option',
    'question': 'What kind of property type do you want?',
    'question-en': 'What kind of property type do you want?',
    'question-ar': 'ما نوع الملكية التي تريدها؟',
    'question-fa': 'چه نوع واحدی در نظر دارید؟',
    'question-ur': 'آپ کس قسم کی پراپرٹی چاہتے ہیں؟',
    'question-zh-CN': '您想要什么样的房产类型？',
    'question-ru': 'Какой тип недвижимости вы хотите?',
    'question-hi': 'आप किस प्रकार की संपत्ति चाहते हैं?',
    'valid_response': {0: 'Apartment', 1: 'vila'},
    'parent': 'ready/off-plane',
    'children': ['buy__square-root', 'buy__square-root']
}

rent__square = {
    'name': 'rent__square-root',
    'type': 'scroll',
    'question': 'What is the square footage of the house you are interested in?',
    'question-en': 'What is the square footage of the house you are interested in?',
    'question-ar': 'ما هي المساحة المربعة للمنزل الذي تهتم به؟',
    'question-fa': 'چه متراژی برایتان مناسب است؟',
    'question-ur': 'آپ جس گھر میں دلچسپی رکھتے ہیں اس کا مربع فوٹیج کیا ہے؟',
    'question-zh-CN': '您感兴趣的房子的面积是多少？',
    'question-ru': 'Какая площадь интересующего вас дома?',
    'question-hi': 'जिस घर में आपकी रुचि है उसका वर्गाकार फ़ुटेज क्या है?',
    'valid_response': {0: 30, 1: 300},
    'parent': 'rent__property-type',
    'children': ['rent__room']
}

buy__square = {
    'name': 'buy__square-root',
    'type': 'scroll',
    'question': 'What is the square footage of the house you are interested in?',
    'question-en': 'What is the square footage of the house you are interested in?',
    'question-ar': 'ما هي المساحة المربعة للمنزل الذي تهتم به؟',
    'question-fa': 'چه متراژی برایتان مناسب است؟',
    'question-ur': 'آپ جس گھر میں دلچسپی رکھتے ہیں اس کا مربع فوٹیج کیا ہے؟',
    'question-zh-CN': '您感兴趣的房子的面积是多少？',
    'question-ru': 'Какая площадь интересующего вас дома?',
    'question-hi': 'जिस घर में आपकी रुचि है उसका वर्गाकार फ़ुटेज क्या है?',
    'valid_response': {0: 30, 1: 300},
    'parent': 'buy__property-type',
    'children': ['buy__room']
}

rent__room = {
    'name': 'rent__room',
    'type': 'option',
    'question': 'How many bedrooms do you want?',
    'question-en': 'How many bedrooms do you want?',
    'question-ar': 'كم غرفة نوم تريد؟',
    'question-fa': 'چند اتاق خواب برایتان مناسب است؟',
    'question-ur': 'آپ کتنے بیڈروم چاہتے ہیں؟',
    'question-zh-CN': '您想要几间卧室？',
    'question-ru': 'Сколько спален вы хотите?',
    'question-hi': 'आप कितने शयनकक्ष चाहते हैं?',
    'valid_response': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
    'parent': 'rent__square-root',
    'children': [None] * 5
}

buy__room = {
    'name': 'buy__room',
    'type': 'input',
    'question': 'How many bedrooms do you want?',
    'question-en': 'How many bedrooms do you want?',
    'question-ar': 'كم غرفة نوم تريد؟',
    'question-fa': 'چند اتاق خواب برایتان مناسب است؟',
    'question-ur': 'آپ کتنے بیڈروم چاہتے ہیں؟',
    'question-zh-CN': '您想要几间卧室？',
    'question-ru': 'Сколько спален вы хотите?',
    'question-hi': 'आप कितने शयनकक्ष चाहते हैं?',
    'valid_response': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
    'parent': 'buy__square-root',
    'children': [None] * 5
}

menus = {
    buy_rent['name']: buy_rent,
    buy__budget['name']: buy__budget,
    rent__budget['name']: rent__budget,
    time['name']: time,
    ready_off_plan['name']: ready_off_plan,
    rent__property_type['name']: rent__property_type,
    buy__property_type['name']: buy__property_type,
    rent__square['name']: rent__square,
    buy__square['name']: buy__square,
    rent__room['name']: rent__room,
    buy__room['name']: buy__room
}
