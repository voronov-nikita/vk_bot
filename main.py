import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random



vk_session = vk_api.VkApi(token = 'c8b8b2da7fa103783485c3917543234b3893e1f619a8d791ce53c4523c1f6260018bf7300ca488a62cc8e')
session_api= vk_session.get_api()


longpool = VkLongPoll(vk_session)
vocabulary = ['спасибо', 'нет', "да", "что", "незнаю", "согласен", "хочу в Геленжик", "!","ок", "хрю", "он виноват" , '.']
Bot=True
k=0
admin = False



set_word = ['Кто прочитал, тот гей', "Лучшее оружие - дикобраз", "Корма не надо?","Есть женщины, а есть люди", "НЕГР - Наилучший Еврейский Граненный Рубин" ]

def send_some_message(id, some_text):
    vk_session.method("messages.send", {"user_id": id, "message": some_text, "random_id":0})


for event in longpool.listen():
    if event.type==VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id


            if msg =='привет' or msg=='Привет'or msg=='hi'or msg=='hello'or msg=='Hello':
                send_some_message(id, 'Привет')

            elif msg=='/шутка':
                send_some_message(id, str(random.choice(set_word)))

            elif msg=='/слова'or msg=='/Слова':
                send_some_message(id, str(random.choice(vocabulary)))

            elif msg=='/все слова' and admin==True:
                f = '; '.join(vocabulary)
                send_some_message(id, f)

            elif (msg=='/stop'or msg=='/Stop'or msg=='/Стоп'or msg=='/стоп') and Bot==True:
                send_some_message(id, 'Пока')
                Bot=False
                if msg== 'привет' or msg=='Привет' or msg=='hi'or msg=='hello'or msg=='Hello':
                    Bot=True

            elif msg=='//':
                send_some_message(id, 'Настройки:')
                f= open('settings.txt').read()
                for i in f:
                    if i=='1':
                        send_some_message(id, str(f))

            elif msg=='/login admin admin' or msg=='/логин admin admin':
                send_some_message(id, 'Доступ разрешенн')
                admin = True

            elif (msg=='/clear'or msg=='/сбросить') and admin==True:
                vocabulary = ['спасибо', 'нет', "да", "что", "незнаю", "согласен", "хочу в Геленжик", "!","ок", "хрю", "он виноват"]
                send_some_message(id, 'Успешно')

            else:
                for symbvoly in msg:
                    if symbvoly=='/':
                        send_some_message(id, "Мы друг друга не понимаем, попробуй иначе")
                    else:
                        if len(vocabulary)<10:
                            break
                            send_some_message(id, 'Мой словарный запас не такой уж и большой')
                vocabulary.insert(1, msg)
                send_some_message(id, random.choice(vocabulary))


