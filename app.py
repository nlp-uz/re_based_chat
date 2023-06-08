from Chat import Chat
import gradio as gr
import time
pairs = (
    (
        r"M[ea]nga (.*) kerak",
        (
            " %1? Nimaga kerak?",
            "Manimcha shu %1? sizga hozirgi vaqtda zarilmasdir",
            "Aniq shu %1 kerakmi?",
        ),
    ),
    (
        r"(.*) Albatta",
        (
            "Shashtingiz yaxshi, shu shashtingizni susaytirmang!",

        ),
    ),
    (
        r"(.*) oting (.*)",
        (
            "Mening ismim ElizaUz!",

        ),

    ),
    (
        r"(.*) isming (.*)",
        (
            "Mening ismim ElizaUz!",

        ),
        
    ),
    (
        r"isming (.*)",
        (
            "Mening ismim ElizaUz!",

        ),
        
    ),
    (
        r"Hop",
        (
            "Yana ubu narsa haqida gaplashsak nima deysiz?",
            "Davom ettiramizmi?"

        ),
    ),
    (
        r"Nimani?",
        (
            "Rostdan tushunmadingmi?",
            "Mmm, siz nimani deb o'ylaysiz?"

        ),
    ),
    (
        r"[Bb]uni kim yasadi",
        (
            "Mohirdev jamoasi tomonidan tuzilgan, yana qanaqa savollaringiz bor",

        ),
    ),
    (
        r"Nimaga s[ae]n (.*)",
        (
            " %1 ? Biroz o'ylab ko'rsam",
            " %1 deb nima dimoqchisiz",
            "Kengi safar endi",
        ),
    ),
    (
        r"Nimaga man (.*)",
        (
            "Boshqalardan ham shu savolni so'rab ko'rganmisiz?",
            "Keling siz bilan boshqa mavzuda suhbatlashsak.",
            "Bilmasam yaxshilab o'ylab ko'rishim uchun qo'shimcha vaqt berasizmi?",

        ),
    ),

    (
        r"Man (.*)",
        (
            "Buni eshitganimdan xursandman",
            "Siz haqingizda ko'proq ma'lumot olganimdan xursandman",
            "Ajoyib-ku?",
        ),
    ),

    (
        r"Chunki (.*)",
        (
            "Shu sabab bo'la oladimi sizningcha?",
            "Yana nima qo'shimcha qilsa bo'ladi",
            "Manimcha shoshmasdan yana o'ylab ko'rish kerak!",

        ),
    ),

    (
        r"Salom(.*)",
        (
            "Assalomu alaykum!",
            "Salom!",
            "Salom, Salom!",
        ),
    ),

    (r"Xa", ("Chunarli!", "Ha yaxshi unda")),
  


    (
        r"NLP (.*)",
        (
            "Ajoyib, NLP ni o'rganib o'zbek tiliga o'z xissangizni qo'shishingiz mumkun bo'ladi",
            "NLP bo'yicha sizga yordam berishim mumkun",
            "NLP %1 ? to'g'ri tushundimi?",
        ),
    ),

    (
        r"San (.*)",
        (
            "Ne unaqa o'yladingiz",
            "Rahmat rahmat",
            "Endi shunaqa ekande",
            
        ),
    ),
    (
        r"mohirdevda (.*) kurslar (.*)",
        (
            "mohirdev.uz -Onlayn Dasturlash kurslari, sitega kirib batafsil ma'lumot olishingiz mumkin ",
            "Mohirdev haqida qiziqishingiz juda ajoyib! Mohirdev.uz site dan kurslarni ko'rishingiz mumkin",

        ),
    ),

    (
        r"(.*) mohirdev (.*)",
        (
            "mohirdev.uz -Onlayn Dasturlash kurslari, sitega kirib batafsil ma'lumot olishingiz mumkin ",
            "Mohirdev haqida qiziqishingiz juda ajoyib! Mohirdev.uz site dan kurslarni ko'rishingiz mumkin",
            "Mohirdev haqida fikr bildirganingizdan hursand bo'ldim.",

        ),
    ),
      (
        r"mohirdev (.*)",
        (
            "mohirdev.uz orqali siz dasturlashni o'rganishingiz mumkun ",
            "Mohirdev haqida qiziqishingiz juda ajoyib! Biz bilan dasturlashni o'rganing",
            "Mohirdev haqida so'raganingiz uchun hursand bo'ldim.",

        ),
    ),
    

    (
        r"(.*)\?",
        (
            "Nega bunaqa savol berdingiz?",
            "Siz bu savolni javobini bilasizmi?",
            "%1 bu savolingizdan tashqari yana boshqa savolingiz ham bormi?",
        ),
    ),
    (
        r"xayr",
        (
            "Rahmat salomat bo'ling.",
            "Xayr, Xayr",
            "Ko'rishguncha",
        ),
    ),
    (
        r"(.*)",
        (
            "Anqiroq yozib ko'rinchi.",
            "Savolni sal o'zgartirib beringchi.",
            "To'liqro ayting", 
            "Nimaga bu savolni so'ravosiz?",
            "O'ylab ko'rish kerak",
            "Qiziq!",
        ),
    ),
)




chat = Chat(pairs)


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        bot_message = chat.respond(message)
        chat_history.append((message, bot_message))
        time.sleep(1)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(share= True)
