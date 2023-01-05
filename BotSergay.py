import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
import random

stick_orange_cat = ['66', '89', '63', '75', '71', '86', '50', '68', '58', '65','59', '83', '70', '77','88', '87','49','54', '56', '67','73', '51',
             '55', '57','72', '61', '60', '64', '81', '84', '79', '96', '74', '78', '80', '52', '62', '82', '53','69', '94', '90','91',
                    '85', '92', '93', '95', '76', '19657']
stick_vk_dog = ['26', '45', '24','7', '23','44','41', '40', '20','33', '31','4','17','38','42','9', '34','13','5','14','8','39',
                '47','11','19','27','43','6','30','16','15','32','25','12','46','48','10','35','18','2','28','29','22','21','3',
                '36','37','1','19633']
stick_vk_fruit = ['134','140','145','136','143','151','148','144','133','135','137','142','153','150','156','138','159',
                  '141','147','149','164','161','130','132','139','152','146','160','129','162','165','157','167','154',
                  '131','155','163','158','166','168']
stick_vk_smile = ['9008','9009','9010','9011','9012','9015','9014','9013','9019','9018','9017', '9016','9023','9020','9022',
                  '9021','9020','9027','9026','9025','9024','9031','9030','9029','9028','9035','9034''9033','9032','9039','9038',
                  '9037','9036','9040','9041','9042','9043','9047','9046','9045','9044']


stickers = stick_orange_cat+stick_vk_dog+stick_vk_fruit+stick_vk_smile

vk_session = vk_api.VkApi(token = 'dade50ad48694c109de26e521e4ec0bcf4a4a6ad58ba0ab2a285981aded485e95db7d35beb869830b4637')#Филлософия СергеяДА
vk= vk_session.get_api()


url_image = ['photo-212782725_457239018', 'photo-30026037_457292858', 'photo-189432042_457241678','photo-147286578_457643067',
             'photo-212782725_457239020','photo-212782725_457239022','photo-212782725_457239025','photo-212782725_457239021','photo-212782725_457239022',
             'photo-212782725_457239023','photo-45045130_458032024','photo-45045130_458032006','photo-45045130_458032009','photo-169357618_457239557',
             'photo707919211_457239026','photo707919211_457239027','photo707919211_457239028','photo707919211_457239029','photo707919211_457239030',
             'photo707919211_457239031','photo707919211_457239032','photo707919211_457239033']

vocabulary = ['спасибо', 'нет', "да", "что", "не знаю", "согласен", "хочу в Геленжик", "!","ок", "хрю", "он виноват" ,'Подожди, у меня инфаркт.',
              'Мои мысли открыты тебе','не согласен','.']

bad_words = ['бля', 'хуй','блять','пизда','пиздец','ебать',"епт","сука","сучара","хуевый","пиздабол","ебаный","ебаный рот"]

Bot=True
k=0
admin = False
golos = True
koll_xru= 1


class MyLongPool(VkLongPoll):
    def listen(self):
        while True:
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                print(e)

longpool = MyLongPool(vk_session)

set_word = ['Кто прочитал, тот гей', "Лучшее оружие - дикобраз", "Корма не надо?","Есть женщины, а есть люди", "НЕГР - Наилучший Еврейский Граненный Рубин", 'Беслодие не передается по наследству',
            'Я подавился от того, что вздохнул','Ok', 'У тебя не хрустит тазобедренный сустав? А вот у меня хрустит!',
            'Меня даже ислам опроверг','Дикари, Животные, Дебилы!', 'Что значит кит не питается лисами? Где доказательства? Мне плевать, что там в Интернете!',
            'Если сьесть 150 кг бананов, то ты умрешь...', 'Дай нож, мне скучно...','Я чуть не устроился работать на стройку, я всего лишь хотел посмотреть статью.',
            'Я люблю, но не люблю, когда она ведет себя как животное', 'Доширак - лучше изоленты','Кто забрал мою челюсть?','Поищи саморез в своем пинале',
            'У меня пенсия ассоциируется с пеной.','Подожди, у меня инфаркт.','Я чуть не устроился работать на стройку.','Я это Дошираком заделаю.','Кто грустит - тот негр.',
            'Зимбабве!','Мои мысли открыты тебе']

def get_but(text, color):
    return{
            "action":{
                "type": "text",
                "label": f"{text}"
            },
        "color": f"{color}"
    }

keyboard = {
    "one_time":False,
    "buttons":[
        [get_but('/орел', 'primary'), get_but('/решка', 'primary')],
        [get_but('/шутка', 'primary'), get_but('/фото', 'primary')]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

def send_some_message(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message':text, 'random_id' :0})

def send_stick(id, number):
    vk.messages.send(user_id =id, sticker_id = number, random_id = 0)

def send_image(id, url):
    vk.messages.send(user_id =id, attachment = url, random_id = 0)


def play_orel_and_reshka(id):
    otv= ''
    if msg =='/орел':
        wins = 1
    elif msg =='/решка':
        wins =2
    r = random.randint(1, 2)
    if wins==r:
        send_some_message(id, 'Вы выйграли')
        otv = msg
    else:
        send_some_message(id, 'Вы проиграли, выйграл я')
    if otv==msg:
        send_image(id, 'photo707919211_457239025')

def send_or(id, msg):
    l1 = []
    name1 = ''
    name2 = ''
    for i in msg:
        l1.insert(0, i)
    l1.reverse()
    s = l1.index(' ')
    for i in range(s):
        name1 += l1[i]
    for i in range(5):
        del l1[s]
    for i in range(len(name1)):
        del l1[0]
    for i in range(len(l1)):
        name2 += l1[i]

    r = random.randint(0, 2)
    if r==1:
        send_some_message(id, name1)
    else:
        send_some_message(id, name2)


for event in longpool.listen():
    if event.type==VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id

            if msg =='привет' or msg=='hi'or msg=='hello':
                send_some_message(id, 'Привет')
                f= random.randint(-1, 5)
                if f==0:
                    send_stick(id, 66)
                elif f==1:
                    send_stick(id, 134)
                elif f==2:
                    send_stick(id, 134)
                else:
                    send_stick(id, 21)

            elif msg=='что ты умеешь'or msg=='что ты умеешь?' or msg== '/команды':
                send_some_message(id, 'Я умее многое, хотя, нет, не очень много, для полного ознакомления напишите //')

            elif msg=='/шутка':
                send_some_message(id, str(random.choice(set_word)))
                f = random.randint(0, 5)
                if f == 1 or f == 2:
                    send_stick(id, 140)
                elif f == 3:
                    send_stick(id, 1)
                else:
                    send_stick(id, 89)

            elif msg=='согласен' or msg=='подтверждаю':
                send_some_message(id, 'А то, мои мысли=мысли Сергея')

            elif msg=='/орел'or msg=='/решка':
                play_orel_and_reshka(id)

            elif msg=='как дела' or msg=='как дела?' or msg=='как дела ?':
                send_some_message(id, 'Все круто!')
                f = random.randint(0, 5)
                if f==1 or f==2:
                    send_stick(id, 63)
                elif f==3:
                    send_stick(id, 37)
                else:
                    send_stick(id, 153)

            elif msg=='хрюкни' or msg=='хрюндель' or msg=='хрю':
                for i in range(koll_xru):
                    send_some_message(id, 'Хрю-хрю')
                if koll_xru==6:
                    koll_xru=1
                    send_some_message(id, 'Хрю-хрю ууиииии')
                else:
                    koll_xru+=1

            elif msg=='/photo'or msg=='/фото':
                url = str(random.choice(url_image))
                if url=='photo-212782725_457239020':
                    send_image(id, 'photo-212782725_457239020')
                    send_some_message(id, 'Угадай, где сидел индивидум')

                elif url=='photo-147286578_457643067':
                    send_image(id, 'photo-147286578_457643067')
                    send_some_message(id, 'Лучший день рождения')

                elif url=='photo707919211_457239027':
                    send_image(id, 'photo707919211_457239027')
                    send_some_message(id, 'Почему так всегда?')

                elif url=='photo707919211_457239028':
                    send_image(id, 'photo707919211_457239028')
                    send_some_message(id, 'Ритуал поклонения МНЕ.')

                elif url=='photo707919211_457239029':
                    send_image(id, 'photo707919211_457239029')
                    send_some_message(id, 'Тупо моя собака.')

                elif url=='photo707919211_457239032' or url=='photo707919211_457239031':
                    send_image(id, url)
                    send_some_message(id, 'Без комментариев')

                elif url=='photo-169357618_457239557':
                    send_image(id, 'photo-169357618_457239557')
                    send_some_message(id, 'Большой хрю-хрю')
                    send_some_message(id, 'Хрю-хрю')

                elif url=='photo-189432042_457241678' or url=='photo707919211_457239026':
                    send_image(id, url)
                    send_some_message(id, 'Наш лидер, согласен?')

                elif url=='photo-212782725_457239018':
                    send_image(id, 'photo-212782725_457239018')
                    send_some_message(id, 'Это мой прародитель')

                else:
                    send_image(id, url)
                    send_some_message(id, 'Мудрость так и плещет')

            elif msg=='/stick' or msg=='/стикер':
                send_stick(id, int(random.choice(stickers)))

            elif msg=='/слова':
                send_some_message(id, str(random.choice(vocabulary)))

            elif msg=='/все слова' and admin==True:
                f = '; '.join(vocabulary)
                send_some_message(id, f)

            elif (msg=='/stop'or msg=='/стоп') and Bot==True:
                send_some_message(id, 'Пока')
                Bot=False

            elif msg=='/кнопки':
                vk_session.method('messages.send',{'user_id': id, 'message': 'Возможности быстрого доступа', 'random_id': 0, 'keyboard': keyboard})

            elif msg=='//':
                send_some_message(id, 'Настройки и команды:')
                f= open('settings.txt', encoding='utf-8').read()
                for i in f:
                    if i=='1':
                        send_some_message(id, str(f))

            elif msg=='/login admin admin' or msg=='/логин admin admin':
                send_some_message(id, 'Доступ разрешенн')
                admin = True

            elif msg=='/close admin admin':
                send_some_message(id, 'Защищено')
                admin=False

            elif (msg=='/clear'or msg=='/сбросить') and admin==True:
                vocabulary = ['спасибо', 'нет', "да", "что", "не знаю", "согласен", "хочу в Геленжик", "!", "ок", "хрю",
                              "он виноват", 'Подожди, у меня инфаркт.',
                              'Мои мысли открыты тебе', 'не согласен', '.']
                send_some_message(id, 'Успешно')

            elif msg=='молодец':
                send_stick(id, 31)

            else:
                if msg not in bad_words:
                    if 'или' not in msg:
                        for symbvoly in msg:
                            if symbvoly=='/':
                                send_some_message(id, "Мы друг друга не понимаем, попробуй иначе\n Для получения одробной информации введи //")
                            else:
                                if len(vocabulary)<10:
                                    break
                                    send_some_message(id, 'Мой словарный запас не такой уж и большой')
                        vocabulary.insert(1, msg)

                        if golos == True:
                            g = random.choice(vocabulary)
                            print(g)
                            send_some_message(id, str(g))
                            if g=='нет' or g=='не согласен':
                                f = random.randint(0, 8)
                                if f == 1:
                                    send_stick(id, 150)
                                elif f==2:
                                    send_stick(id, 35)
                                else:
                                    send_stick(id, 70)

                            elif g=='да'or g=='хорошо' or g=='ок':
                                f = random.randint(0, 12)
                                if f == 1:
                                    send_stick(id, 63)
                                elif f == 2:
                                    send_stick(id, 145)
                                elif f== 3:
                                    send_stick(id, 9046)
                                elif f== 4:
                                    send_stick(id, 9045)
                                else:
                                    send_stick(id, 37)

                            elif g=='не знаю':
                                f = random.randint(0, 7)
                                if f == 1:
                                    send_stick(id, 9032)
                                elif f == 2:
                                    send_stick(id, 133)
                                elif f == 3:
                                    send_stick(id, 65)
                                else:
                                    send_stick(id, 46)

                    else:
                        one=True
                        for i in msg:
                            if i == ' ' and one == True:
                                one = False
                                send_or(id, msg)
                else:
                    send_some_message(id, 'Материться не хорошо')
                    f = random.randint(0, 4)
                    if f == 1:
                        send_stick(id, 10)
                    elif f == 2:
                        send_stick(id, 156)
                    else:
                        send_stick(id, 51)

