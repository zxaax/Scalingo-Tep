import re

from telethon import Button, events
from telethon.events import CallbackQuery
from ..core import check_owner, pool

from zthon import zedub

from ..Config import Config
from . import mention
HELP = f"**🧑🏻‍💻┊مـرحباً عـزيـزي {mention}**\n**🛂┊في قائمـة المسـاعـده والشـروحـات\n🛃┊من هنـا يمكنـك ايجـاد شـرح لكـل اوامـر السـورس**\n\n[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 ♥️](https://t.me/S_EG_P)\n\n"


if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    @check_owner
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await zedub.get_me()
        if query.startswith("مساعده") and event.query.user_id == zedub.uid:
            buttons = [
                [Button.inline("𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴", data="MMM")],
                [
                    Button.inline("البـوت 🤖", data="botvr"),
                    Button.inline("الحساب🎗", data="acccount"),
                ],
                [
                    Button.inline("البـحـث والتحميـل 🪄", data="zdownload"),
                ],
                [
                    Button.inline("المجمـوعـة 🛗", data="groupvr"),
                    Button.inline(" الفـارات 🛂", data="varszed"),
                ],
                [
                    Button.inline("التسليـه والتحشيش 🎃", data="funzed"),
                ],
                [
                    Button.inline("المرفقـات 🪁", data="extras"),
                    Button.inline("الادوات 💡", data="toolzed"),
                ],
            ]
            result = builder.article(
                title="zedub",
                text=HELP,
                buttons=buttons,
                link_preview=False,
            )
        await event.answer([result] if result else None)


@zedub.zed_cmd(pattern="مساعده")
async def help(event):
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await zedub.inline_query(Config.TG_BOT_USERNAME, "مساعده")
    await response[0].click(event.chat_id)
    await event.delete()


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ZEDHELP")))
@check_owner
async def _(event):
    butze = [
        [Button.inline("𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴", data="MMM")],
        [
            Button.inline("البـوت 🤖", data="botvr"),
            Button.inline("الحساب🎗", data="acccount"),
        ],
        [
            Button.inline("البـحـث والتحميـل 🪄", data="zdownload"),
        ],

        [
            Button.inline("المجمـوعـة 🛗", data="groupvr"),
            Button.inline(" الفـارات 🛂", data="varszed"),
        ],
        [
            Button.inline("التسليـه والتحشيش 🎃", data="funzed"),
        ],
        [
            Button.inline("المرفقـات 🪁", data="extras"),
            Button.inline("الادوات 💡", data="toolzed"),
        ],
    ]
    await event.edit(HELP, buttons=butze, link_preview=False)


############ البوت ############
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"botvr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر البـوت المسـاعد :**\n\n",
        buttons=[
            [
                Button.inline("تحديث", data="updatevr"),
            ],
            [
                Button.inline("اعاده تشغيل", data="resitvr"),
                Button.inline("ايقاف البوت", data="stopvr"),
            ],
            [
                Button.inline("الفحص", data="alivzed"),
            ],
            [
                Button.inline("السليب (النوم)", data="sleep"),
                Button.inline("سرعة الانترنت", data="netzed"),
            ],
            [
                Button.inline("سورس", data="sourcevr"),
                Button.inline("تنصيب", data="zedvr"),
            ],
            [
                Button.inline("الاذاعه", data="ethaavr"),
            ],
            [
                Button.inline("المطور المساعد", data="devvr"),
            ],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"updatevr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تحديث`

**- الوصـف :**
لـ تحديث البوت في حال كان هناك تحديثات جديده للسورس او في حال نزول تحديثات في قناة السورس
هناك امرين للتحديث الاول :

**⪼** `.تحديث الان`
هذا الامر للتحديث البسيط والسريع وهو المطلوب 

**⪼** `.تحديث البوت`
هذا الامر للتحديث الجذري للبوت وهو بمثابة اعاده التنصيب من اول عمليه بعد المربعات وهو امر غير مطلوب الا في حال نزلت تحديثات جذريه وتم التنويه عليها بقناة السورس

**- الاستخـدام :**
ارسـل الامـر   `.تحديث`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"resitvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اعاده تشغيل`

**- الوصـف :**
لترسيت واعاده تشغيل البوت في حال حدوث اخطاء نادراً او في حال كنت تريد ايقاف عمليه جاريه لا تستجيب ل امـر الايقاف الخاص بها

**- ملاحظـه هامـه :**
لا تقم بتكرار هذا الامر اكثر من مره باليوم الواحد والا سوف يسبب توقف البوت الخاص بك

**- الاستخـدام :**
ارسـل الامـر   `.اعاده تشغيل`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"stopvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.ايقاف البوت`

**- الوصـف :**
لـ ايقاف البوت عن العمل نهائياً والغاء تنصيبك .. في حال استخدمت الامر وتريد اعاده تشغيل البوت كل ماعليك هو التشغيل اليدوي من هيروكو عبر الذهاب لحساب هيروكو والضغط على  veiw ثم خيار Reset ثم الزر الاحمـر وانتظر التنصيب

**- الاستخـدام :**
ارسـل الامـر   `.ايقاف البوت`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"alivzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.فحص`

**- الوصـف :**
لـ فحص قاعدة البيانات وعـرض اصـدار السورس ولغة بايثـون واصـدار مكتبة تيليثون

**- الاستخـدام :**
ارسـل الامـر   `.فحص`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"sleep")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.سليب`
**⪼** `.سليب_ميديا`

**- الوصـف :**
لـ جعل الحساب في وضع النـوم او الإسبات ويتم ايقافه عند ارسالك لـ اي رسالة

**- الاستخـدام :**
`.سليب`  **او**  `.سليب` + سبب

`.سليب_ميديا`  **او**  `.سليب_ميديا` + سبب
**بالـرد ع صـورة او ميديـا**""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"netzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.الانترنت`
**⪼** `.الانترنت صورة`

**- الوصـف :**
لـ عرض سرعة الانترنت في البوت الخاص بك

**- الاستخـدام :**
ارسـل الامـر   `.الانترنت صورة`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"sourcevr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.سورس`

**- الوصـف :**
لـ عـرض اصـدار السـورس ومعـرف البوت المساعد واسم تطبيق التنصيب

**- الاستخـدام :**
ارسـل الامـر   `.سورس`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zedvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تنصيب`

**- الوصـف :**
لـ عـرض قنـوات السـورس

**- الاستخـدام :**
ارسـل الامـر   `.تنصيب`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ethaavr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.الاذاعه`

**- الوصـف :**
لـ عـرض اوامـر الاذاعـه الخاصـه بسـورس كرستين

**- الاستخـدام :**
ارسـل الامـر   `.الاذاعه`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"devvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البـــوت 🦾🤖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.رفع مطور`
**لـ رفـع شخـص مطـور مسـاعـد معـك بالبـوت**

**⪼** `.تنزيل مطور`
**- لـ تنزيـل الشخـص مطـور مسـاعـد مـن البـوت**

**⪼** `.المطورين`
**- لـ عـرض قائمـة بمطـورين البـوت الخـاص بـك 🧑🏻‍💻📑**

**⪼** `.وضع المطور تفعيل`
**لـ تفعيـل وضـع المطـورين المسـاعدين**

**⪼** `.وضع المطور تعطيل`
**لـ تعطيـل وضـع المطـورين المسـاعدين**

**⪼** `.تحكم كامل`
**- اعطـاء المطـورين المرفـوعيـن صلاحيـة التحكـم الكـاملـه بالاوامــر ✓**

**⪼** `.تحكم آمن`
**- اعطـاء المطـورين المرفـوعيـن صلاحيـة التحكـم الآمـن لـ الاوامــر الامنـه فقـط ✓**

**⪼** `.تحكم` + اسم الامـر
**اعطـاء المطـورين المرفـوعيـن صلاحيـة التحكـم بأمـر واحـد فقـط او عـدة اوامـر معينـه ✓ .. مثـال (.تحكم ايدي) او (.تحكم ايدي فحص كتم)**

**⪼** `.ايقاف تحكم كامل`
**- ايقـاف صلاحيـة التحكـم الكـاملـه بالاوامــر للمطـورين المرفـوعيـن ✓**

**⪼** `.ايقاف تحكم آمن`
**- ايقـاف صلاحيـة التحكـم الآمـن لـ الاوامــر الآمنـه للمطـورين المرفـوعيـن ✓**

**⪼** `.ايقاف تحكم` + اسم الامـر
**- ايقـاف صلاحيـة التحكـم المعطـاه لـ امـر واحـد فقـط او عـدة اوامـر للمطـورين المرفـوعيـن ✓ .. مثـال (.ايقاف تحكم ايدي) او (.ايقاف تحكم ايدي فحص كتم)**

**⪼** `.التحكم`  /  `.التحكم المعطل`



**- الوصـف :**
لـ رفـع واضافة شخص متحكم معك بالبوت حيث يستطيع استخدام الاوامر مثلك تماماً

**- ملاحظـه هـامه :**
لا تقم برفع احد انت غير واثق فيه لان المتحكم يستطيع استخدام الاوامر في شي ماراح يرضيك او يسبب لك احراج اذا استخدم امر مثل اوامر التوجيه ... الخ

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"groupvr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه 🛗](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر المجمــوعــه :**\n\n",
        buttons=[
            [
                Button.inline("اوامــر المجمــوعــه¹", data="group1vr"),
            ],
            [
                Button.inline("اوامــر المجمــوعــه²", data="group2vr"),
            ],
            [
                Button.inline("اوامــر المجمــوعــه³", data="group3vr"),
            ],
            [
                Button.inline("مكافح التكرار", data="nospam"),
                Button.inline("المنـع", data="noway"),
            ],
            [
                Button.inline("الاضـافه والتفليـش", data="group0vr"),
            ],
            [
                Button.inline("التحذيرات", data="warnzed"),
                Button.inline("الترحيبـات", data="group4vr"),
            ],
            [
                Button.inline("الــردود", data="group5vr"),
            ],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"warnzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تحذير`
**⪼** `.التحذيرات`
**⪼** `.حذف التحذيرات`


**- الوصـف :**
لـ تحذير شخص في المجموعة فاذا وصلت 3 تحذيرات يتم طرده من المجموعة
تستطيع ايضاً وضع سبب لتحذير الشخص تابع الاستخدام بالاسفل


**- الاستخـدام :**
`.تحذير`
**بالـرد ع شخـص لـ تحذيره او باضافة معرف/ايدي الشخص للامر**

`.التحذيرات`
**بالـرد ع شخـص لـ جلب عدد تحذيراتـه**

`.حذف التحذيرات`
**بالـرد ع شخـص لـ حذف تحذيراتـه**

`.تحذير + سبب`
**بالـرد ع شخـص لـ تحذيره او باضافة معرف/ايدي الشخص للامر**

**- مثـال :**
`.تحذير يزحف للبنات`
**بالـرد ع شخص او باضافة معرف/ايدي الشخص للامر**""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group4vr")))
@check_owner
async def _(event):
    await event.edit(
        """**- الامـر :**
**⪼** `.ترحيب`
**⪼** `.حذف الترحيب`
**⪼** `.الترحيبات`

**- الوصـف :**
لـ اضافة ترحيب في المجموعة للترحيب بالاعضاء الجدد اثناء الانضمام 
حيث يقوم البوت بارسال رساله ترحيبيه تلقائيـه انت تقوم باضافتها مسبقاً

**- المتغيـرات الاضافيـه :**
{mention}  اضافه منشن
{title}  اضافة اسم كروب الترحيب
{count}  اضافة عدد اعضاء الكروب
{first}  اضافة الاسم الاول
{last}  اضافة الاسم الاخر
{fullname}  اضافة الاسم الكامل
{userid}  اضافة ايدي الشخص
{username}  اضافة معرف الشخص
{my_first}  اضافة اسمك الاول
{my_fullname}  اضافة اسمك الكامل
{my_last}  اضافة اسمك الاخر
{my_mention}  اضافة تاك حسابك
{my_username}  اضافة معرفك

**- الاستخـدام :**
`.ترحيب` + نص الترحيب
`.ترحيب` بالـرد ع رسالـه ترحيبيـه 
`.ترحيب` بالـرد ع ميديـا تحتهـا نـص
`.حذف الترحيب`
`.الترحيبات`

**- مثـال :**
`.ترحيب اططلـق 🥳 دخـول {mention}, نـورت مجمـوعتنـا {title} `""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group5vr")))
@check_owner
async def _(event):
    await event.edit(
        """**- الامـر :**
**⪼** `.رد`
**⪼** `.حذف رد`
**⪼** `.ردودي`
**⪼** `.حذف الردود`

**- الوصـف :**
لـ اضافة رد في المجموعة لكلمـه معينـه كما في بوتات الحماية بالضبط عندما يقوم حد بارسال الكلمه سوف يتم الرد عليه تلقائياً بالرد الذي قمت باضافته لهذه الكلمه

**- المتغيـرات الاضافيـه :**
{mention}  اضافه منشن
{title}  اضافة اسم كروب الترحيب
{count}  اضافة عدد اعضاء الكروب
{first}  اضافة الاسم الاول
{last}  اضافة الاسم الاخر
{fullname}  اضافة الاسم الكامل
{userid}  اضافة ايدي الشخص
{username}  اضافة معرف الشخص
{my_first}  اضافة اسمك الاول
{my_fullname}  اضافة اسمك الكامل
{my_last}  اضافة اسمك الاخر
{my_mention}  اضافة تاك حسابك
{my_username}  اضافة معرفك

**- الاستخـدام :**
`.رد` + نص الـرد بالـرد ع كلمـة الـرد
`.رد` + نص الـرد بالـرد ع ميديـا
`.حذف رد` + كلمـة الـرد
`.ردودي`
`.حذف الردود`

**- مثـال :**
`.رد اططلـق 🥳 من يصيحني {mention}, لبيه سم آمر حبيبي`
بالــرد ع معرفـك مثـلاً""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group1vr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹ 🛗](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر المجمــوعــه¹ :**\n\n",
        buttons=[
            [
                Button.inline("البوتات", data="botveiw"),
                Button.inline("قفل البوتات", data="botlock"),
            ],
            [
                Button.inline("قفل الاضافه", data="addlock"),
                Button.inline("قفل الدخول", data="golock"),
            ],
            [
                Button.inline("قفل الميديا", data="medlock"),
            ],
            [
                Button.inline("قفل الروابط", data="urlock"),
                Button.inline("قفل المعرفات", data="userlock"),
            ],
            [
                Button.inline("قفل التوجيه", data="forlock"),
                Button.inline("قفل الانلاين", data="inilock"),
            ],
            [
                Button.inline("قفل الفارسيه", data="farslock"),
                Button.inline("قفل الفشار", data="fuklock"),
            ],
            [
                Button.inline("الاعدادات", data="setelock"),
                Button.inline("قفل الكل", data="alllock"),
            ],
            [Button.inline("تقييـد المحتـوى", data="lolzed")],
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"botveiw")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.البوتات`

**- الوصـف :**
لـ كشـف وتنظيف مجموعتـك من البوتات .. لمنع التصفير والتفليش والتخريب

**- الاستخـدام :**
ارسـل الامـر   `.البوتات`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"botlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل البوتات`
`.فتح البوتات`

**- الوصـف :**
لـ فتـح او قفـل البوتـات بالطـرد التلقائـي .. الامر يمنع حتى المشـرفين من اضافـة البوتات .. في حـال اراد احد المشرفين رفـع بوت وتصفير مجموعتك اثنـاء غيابـك.

**- الاستخـدام :**
ارسـل الامـر   `.قفل البوتات`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"addlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل الاضافه`
`.فتح الاضافه`

**- الوصـف :**
لـ فتـح او قفـل اضافـة الاعضـاء بالطـرد .. مـع تحذيـر صاحـب الاضـافه

**- الاستخـدام :**
ارسـل الامـر   `.قفل الاضافه`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"golock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل الدخول`
`.فتح الدخول`

**- الوصـف :**
لـ فتـح او قفـل الدخـول بالرابـط بالطـرد التلقائـي .. حيث يقـوم بطـرد المنضم تلقائيـاً .. مـع ارسـال رسـاله تحذيريـه

**- الاستخـدام :**
ارسـل الامـر   `.قفل الدخول`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"medlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل الميديا`
`.فتح الميديا`

**- الوصـف :**
لـ فتـح او قفـل الوسائـط بالمسـح + تقييـد المرسـل من صلاحيـة ارسال الوسائط تلقائيـاً .. مع السمـاح له بارسـال الرسـائل فقـط .. يفيدكـم لـ منـع التفليـش الاباحـي في حال غيابكـم او انشغـالكم .. يسمـح للمشـرفين فقـط بارسـال الوسائـط

**- الاستخـدام :**
ارسـل الامـر   `.قفل الميديا`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"urlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل الروابط`
`.فتح الروابط`

**- الوصـف :**
لـ فتـح او قفـل الروابـط بالمسـح التلقائـي .. مع تحذير الشخص المرسل

**- الاستخـدام :**
ارسـل الامـر   `.قفل الروابط`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"userlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل المعرفات`
`.فتح المعرفات`

**- الوصـف :**
لـ فتـح او قفـل المعرفـات بالمسـح التلقائـي .. مع تحذير الشخص المرسل

**- الاستخـدام :**
ارسـل الامـر   `.قفل المعرفات`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"forlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل التوجيه`
`.فتح التوجيه`

**- الوصـف :**
لـ فتـح او قفـل رسـائل التوجيـه المعـاد توجيههـا من القنـوات بالمسـح التلقائـي .. مع تحذير الشخص المرسل

**- الاستخـدام :**
ارسـل الامـر   `.قفل التوجيه`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"inilock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل الانلاين`
`.فتح الانلاين`

**- الوصـف :**
لـ فتـح او قفـل رسائل الانلايـن والهمسـات بالمسـح التلقائـي .. مع تحذير الشخص .. يسمـح للمشرفين فقـط بارسال الانلايـن

**- الاستخـدام :**
ارسـل الامـر   `.قفل الانلاين`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"farslock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل الفارسيه`
`.فتح الفارسيه`

**- الوصـف :**
لـ فتـح او قفـل مسـح رسـائل الايرانيين وبوتات الاعلانات الفارسيه تلقائيـاً .. مـع تحذيـر الشخـص المرسـل

**- الاستخـدام :**
ارسـل الامـر   `.قفل الفارسيه`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fuklock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل الفشار`
`.فتح الفشار`

**- الوصـف :**
لـ مسـح رسـائل الفشار والسب والتكفير تلقائيـاً .. مـع تحذيـر الشخـص المرسـل

**- الاستخـدام :**
ارسـل الامـر   `.قفل الفشار`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"alllock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قفل الكل`
`.فتح الكل`

**- الوصـف :**
لـ قفـل او فتـح كـل الاوامـر السابقـه

**- الاستخـدام :**
ارسـل الامـر   `.قفل الكل`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"setelock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه¹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.الاعدادات`

**- الوصـف :**
لـ عـرض اعـدادات المجمـوعـه

**- الاستخـدام :**
ارسـل الامـر   `.الاعدادات`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"lolzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قيد`

**- الوصـف :**
لـ تقييـد محتـوى مجمـوعتك او قنـاتك

لـ المايعرف ماذا يعني تقييد محتوى ؟!
هي اضافه قامت شركة تيليجرام مؤخراً باضافتها للمجموعات او القنوات لجعلها مقيدة اي يمنع اي شخص من النسخ والتوجيه او اخذ لقطة شاشة منها

**- الاستخـدام :**
ارسـل الامـر
`.قيد`
في مجموعتك او قناتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group2vr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه² 🛗](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر المجمــوعــه² :**\n\n",
        buttons=[
            [
                Button.inline("الرابط", data="urlveiw"),
                Button.inline("تاك all", data="tagvr"),
            ],
            [
                Button.inline("رفع مشرف", data="addmnvr"),
                Button.inline("رفع مالك", data="creatorvr"),
            ],
            [
                Button.inline("رسائلي/رسائله", data="msgvr"),
                Button.inline("اسمي/اسمه", data="delmsgvr"),
            ],
            [
                Button.inline("حذف رسائلي", data="delmsgvr"),
            ],
            [
                Button.inline("الاحداث", data="iundlt"),
                Button.inline("المعلومات", data="infoovr"),
            ],
            [
                Button.inline("الاعضاء", data="memver"),
                Button.inline("المشرفين", data="creatorrvr"),
                Button.inline("البوتات", data="botssvr"),
            ],
            [
                Button.inline("الصورة وضع", data="photoadd"),
                Button.inline("التثبيت", data="pinvr"),
            ],
            [Button.inline("المحذوفين", data="zomby")],
            [Button.inline("مسح المحظورين", data="delbans")],
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"urlveiw")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.الرابط`

**- الوصـف :**
لـ جـلب رابـط المجمـوعـة + يجب ان تكون مشرفـاً فيهـا

**- الاستخـدام :**
ارسـل الامـر   `.الرابط`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"tagvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تاك`
`.all`

**- الوصـف :**
الامـر + كلمـه او بالـرد ع رسـالـه لـ عمـل تـاك بشكـل متقطـع لـ الكـل بالمجمـوعـة

**- الاستخـدام :**
ارسـل الامـر   `.تاك`  +  نص او بالـرد ع رسـاله في مجموعتك
لـ ايقاف التاك ارسـل `.ايقاف التاك`

**- مثـال :**
`.تاك السلام عليكم`
`.ايقاف التاك`""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"addmnvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.رفع مشرف`
`.تنزيل مشرف`

**- الوصـف :**
لـ رفـع الشخـص مشـرفـاً بالكـروب بصـلاحيات محـدوده فقـط وليس كامل الصلاحيـات

**- الاستخـدام :**
ارسـل الامـر   `.رفع مشرف`   بالـرد ع شخص في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"creatorvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.رفع مالك`
`.تنزيل مالك`

**- الوصـف :**
لـ رفـع الشخـص مشـرفـاً بالكـروب بكامل الصـلاحيات

**- الاستخـدام :**
ارسـل الامـر   `.رفع مالك`   بالـرد ع شخص في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"msgvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.رسائلي`
**⪼** `.رسائله`

**- الوصـف :**
(.رسائلي) لـ عـرض عـدد رسـائلك في المجمـوعـة
(.رسائله) لـ عـرض عـدد رسائل شخـص في المجمـوعـة

**- الاستخـدام :**
`.رسائلي`
او  `.رسائله`   بالـرد ع شخص في المجمـوعـة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"msgvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اسمي`
**⪼** `.اسمه`

**- الوصـف :**
(.اسمي) لـ عـرض اسمـك على شكـل ماركداون
(.اسمه) لـ عـرض اسم شخص على شكـل ماركداون

**- الاستخـدام :**
`.اسمي`
`.اسمه`
**بالـرد ع شخص او باضافة معرف او ايدي للامـر**
`.اسمه` + كلمـه
**بالـرد ع شخص او باضافة معرف او ايدي للامـر 
يسوي تاك بكلمه للشخص**""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"delmsgvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.حذف رسائلي`
**⪼** `.مسح`

**- الوصـف :**
`.حذف رسائلي` + عـدد
لـ حـذف رسـائلك في المجمـوعـة بالعـدد .. كلمـا ضفت عـدد اكبـر كلمـا كان الحـذف اكبـر
`.مسح` 
بالـرد ع أي رسـاله لحذفهـا

**- الاستخـدام :**
`.حذف رسائلي` + عـدد

**- مثـال :**
`.حذف رسائلي 1000`

**- ملاحظـه :**
**اذا كنت تريد حذف جميـع رسائلك في المجمـوعـة استخـدم امريـن :**
`.رسائلي`
**راح يعطيك عـدد رسائلك**
**ثم ارسل بعدهـا :**
`.حذف رسائلي` + نفـس العـدد""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"iundlt")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.الاحداث`
`.الاحداث م`

**- الوصـف :**
(`.الاحداث` + عدد)لـ جـلب آخـر الرسـائـل المحـذوفـه مـن آخـر احـداث المجمـوعـة بـ العـدد
(`.الاحداث م`) لجـلب رسـائل الميديـا المحذوفـة من آخر الااحـداث

**- الاستخـدام :**
ارسـل الامـر    `.الاحداث` 7""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"infoovr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.المعلومات`

**- الوصـف :**
لـ جـلب معلومـات وتفاصيـل كاملـه عن اي مجمـوعـة او قنـاة مثل اسم المجموعه الحالي والاسم السابق وتاريخ الانشاء والمالك وعدد المشرفين و عدد الاعضاء المتصلين والمحظورين .. الـخ

**- الاستخـدام :**
ارسـل الامـر    `.المعلومات` داخـل المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"memver")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.الاعضاء`

**- الوصـف :**
لـ عـرض قائمـة او ملـف بـ اعضـاء المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.الاعضاء)   داخـل المجمـوعـة او القنـاة
او  (.الاعضاء + معرف او رابـط) المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"creatorrvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.المشرفين`

**- الوصـف :**
لـ عـرض قائمـة او ملـف بـ مشرفيـن المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.المشرفين)   داخـل المجمـوعـة او القنـاة
او  (.المشرفين + معرف او رابـط) المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"botssvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.البوتات`

**- الوصـف :**
لـ عـرض قائمـة او ملـف بـ بوتـات المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.البوتات)   داخـل المجمـوعـة او القنـاة
او  (.البوتات + معرف او رابـط) المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"photoadd")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.الصورة وضع`
`.الصورة حذف`

**- الوصـف :**
(.الصورة وضع) لـ وضـع او تغييـر صـورة المجمـوعـة
(.الصورة حذف) لـ حـذف صـورة المجمـوعـة

**- الاستخـدام :**
ارسـل الامـر   (.الصورة وضع)   بالـرد على صـورة في المجمـوعـة
او  (.الصورة حذف)""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pinvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تثبيت`
`.الغاء تثبيت`
`.الغاء تثبيت الكل`

**- الوصـف :**
بالـرد على رسـاله معينـه لـ تثبيتهـا او الغـاء تثبيتهـا في المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.تثبيت)   بالـرد على رسـاله في المجمـوعـة
او  (.الغاء تثبيت)""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zomby")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.المحذوفين`
`.المحذوفين تنظيف`

**- الوصـف :**
لـ عـرض او تنظيـف المجمـوعـة او القنـاة من الحسـابات المحذوفـه

**- الاستخـدام :**
ارسـل الامـر   (.المحذوفين)   داخـل المجمـوعـة او القنـاة
او  (.المحذوفين تنظيف)""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"delbans")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه²](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.مسح المحظورين`

**- الوصـف :**
لـ مسـح قائمـة المحظـورين في المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.مسح المحظورين)   داخـل المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group3vr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³ 🛗](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر المجمــوعــه³ :**\n\n",
        buttons=[
            [
                Button.inline("كتم", data="mutevr"),
                Button.inline("حظر", data="banvr"),
            ],
            [
                Button.inline("طرد", data="kickvr"),
                Button.inline("تقييد", data="tkkkvr"),
            ],
            [
                Button.inline("مغادره", data="byby"),
                Button.inline("طرد البوتات", data="banbot"),
            ],
            [Button.inline("المحذوفين", data="zoomby")],
            [Button.inline("مسح المحظورين", data="dellbans")],
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"mutevr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.كتم` + السبب بالـرد
`.كتم` + معرف/ايدي + السبب

**- مثـال :**
(.كتم يزحف للبنات) بالـرد ع شخص
(.كتم + معرف/ايدي + يزحف للبنات)

**- الوصـف :**
لـ كتـم شخص سـواء في المجمـوعـة او الخـاص اذا ارسلت الامر في المجموعة سوف ينكتم في المجموعة واذا في الخاص سوف ينكتم من الخاص فقط ماعدا اوامر الكتم العام فانهما تكتم الشخص من الخاص وجميع المجموعات والقنوات التي انت مشرف فيهـا

**- الاستخـدام :**
لـ الكتم ارسـل
`.كتم`   بالـرد ع شخص
`.كتم`   + معـرف/ايـدي الشخـص
`.الغاء كتم`   بالـرد ع شخص
`.الغاء كتم`   + معـرف/ايـدي الشخـص

**لـ الكتم العـام ارسـل**
`.ك عام`   بالـرد ع شخص
`.ك عام`   + معـرف/ايـدي الشخـص
`.الغاء ك عام`   بالـرد ع شخص
`.الغاء ك عام`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.حظر` + السبب بالـرد
`.حظر` + معرف/ايدي + السبب

**- مثـال :**
(.حظر يزحف للبنات) بالـرد ع شخص
(.حظر + معرف/ايدي + يزحف للبنات)

**- الوصـف :**
لـ حظـر شخص سـواء في المجمـوعـة او الخـاص اذا ارسلت الامر في المجموعة سوف ينحظر من المجموعة واذا في الخاص سوف ينحظر من الخاص فقط
ماعدا اوامر الحظر العام فانهما تحظر الشخص من الخاص وجميع المجموعات والقنوات التي انت مشرف فيهـا

**- الاستخـدام :**
لـ الحظر ارسـل
`.حظر`   بالـرد ع شخص
`.حظر`   + معـرف/ايـدي الشخـص
`.الغاء حظر`   بالـرد ع شخص
`.الغاء حظر`   + معـرف/ايـدي الشخـص

**لـ الحظر العـام ارسـل**
`.ح عام`   بالـرد ع شخص
`.ح عام`   + معـرف/ايـدي الشخـص
`.الغاء ح عام`   بالـرد ع شخص
`.الغاء ح عام`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"kickvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.طرد`

**- الوصـف :**
لـ طـرد شخص من المجمـوعـة سوف ينطرد مجرد طرد فقط وليس حظر مع استطاعته العوده للمجموعة مرة اخرى

**- الاستخـدام :**
ارسـل الامـر   `.طرد`   بالـرد ع شخص
او   `.طرد`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"tkkkvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تقييد`

**- الوصـف :**
لـ تقييـد شخص من المجمـوعـة

**- الاستخـدام :**
ارسـل الامـر   `.تقييد`   بالـرد ع شخص
او   `.تقييد`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nospam")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر مكـافح التكــرار 🛡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.ضع التكرار`

**- الوصـف :**
لـ منـع التكـرار في المجمـوعـة وتقييـد المستخـدم عند التكـرار تلقائيـاً

**- الاستخـدام :**
**لـ تفعيـل المكافـح ارسـل :**
`.ضع التكرار`  + **عـدد التكـرار**

**لـ تعطيـل المكافـح ارسـل :**
`.ضع التكرار`  + **عـدد كبيـر جـداً**""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"noway")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المنــع 🚫](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.منع`
**⪼** `.الغاء منع`
**⪼** `.قائمة المنع`

**- الوصـف :**
لـ منـع كلمـة ومسحهـا تلقائيـاً عند ارسالهـا في الدردشـة

**- الاستخـدام :**
`.منع`  + **الكلمـه المـراد منعهـا**
`.الغاء منع`  + **الكلمـه المـراد الغـاء منعهـا**
`.قائمة المنع`""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group0vr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الاضـافه والتفليـش 👾](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر الاضـافه والتفليـش :**\n\n",
        buttons=[
            [
                Button.inline("الاضافه", data="addvr"),
            ],
            [
                Button.inline("التفليش", data="zerovr"),
            ],
            [
                Button.inline("حظر_الكل", data="banall"),
                Button.inline("طرد_الكل", data="kickall"),
            ],
            [
                Button.inline("كتم_الكل", data="mutall"),
            ],
            [Button.inline("مسح المحظورين", data="dellbans")],
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"addvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.ضيف`
**⪼** `.اضافه`
**⪼** `.انضمام`

**- الوصـف :**
(.ضيف) لـ اضافة وسحب اعضـاء من مجمـوعـة الى مجمـوعـة آخـرى
(.اضافه) لـ اضافة شخص الى مجمـوعـة او قنـاة
(.انضمام) لـ الانضمام الى مجمـوعـة او قنـاة

**- الاستخـدام :**
**اولاً امر اضافة الاعضـاء :
**ارسـل الامـر التالـي في مجمـوعتـك
`.ضيف`   **+  رابـط المجمـوعـة المـراد سحب الاعضـاء منهـا**


**ارسـل الامـر التالـي في مجمـوعتـك او قنـاتك
`.اضافه`   +  معـرف/ايـدي الشخـص الذي تريد اضافته

او `.انضمام`   +  معـرف/رابـط القناة او المجموعة""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zerovr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تفليش`
`.تفليش بالطرد`

**- الوصـف :**
لـ تصفيـر جميـع اعضـاء المجمـوعـة + يجب ان يكون لديك اشـراف فيهـا بصلاحيات الحظـر

**- الاستخـدام :**
ارسـل احـد الاوامـر التالـيه في المجمـوعـة المـراد تفليشهـا
`.تفليش`
`.تفليش بالطرد`""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banall")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.حظر_الكل`

**- الوصـف :**
لـ حظـر جميـع اعضـاء المجمـوعـة عبـر بوت الحمايـة + لا تحتاج صلاحيات اشراف فيها كل الي تحتاجـه فقط رتبه ادمن او اعلى في بوت الحماية الموجود بالمجمـوعـة

**- الاستخـدام :**
ارسـل الامـر التالـي في المجمـوعـة المـراد تفليشهـا
`.حظر_الكل`
لـ ايقـاف عمليـة الحظـر الجاريـه
ارسـل    `.ايقاف التفليش`""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"kickall")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.طرد_الكل`

**- الوصـف :**
لـ طـرد جميـع اعضـاء المجمـوعـة عبـر بوت الحمايـة + لا تحتاج صلاحيات اشراف فيها كل الي تحتاجـه فقط رتبه ادمن او اعلى في بوت الحماية الموجود بالمجمـوعـة

**- الاستخـدام :**
ارسـل الامـر التالـي في المجمـوعـة المـراد تفليشهـا
`.طرد_الكل`
لـ ايقـاف عمليـة الطـرد الجاريـه
ارسـل    `.ايقاف التفليش`""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"mutall")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.كتم_الكل`

**- الوصـف :**
لـ كتـم جميـع اعضـاء المجمـوعـة عبـر بوت الحمايـة + لا تحتاج صلاحيات اشراف فيها كل الي تحتاجـه فقط رتبه ادمن او اعلى في بوت الحماية الموجود بالمجمـوعـة

**- الاستخـدام :**
ارسـل الامـر التالـي في المجمـوعـة المـراد كتـم اعضـائهـا
`.كتم_الكل`
لـ ايقـاف عمليـة الكتـم الجاريـه
ارسـل    `.ايقاف التفليش`""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"byby")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.غادر`
`.مغادره`
`.اطردني`

**- الوصـف :**
لـ مغـادرة المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر التالـي في المجمـوعـة او القنـاة
`.مغادره`""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banbot")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.البوتات طرد`
`.البوتات`

**- الوصـف :**
لـ كشف وطرد البوتات الموجـوده بالمجمـوعـه

**- الاستخـدام :**
ارسـل الامـر   `.البوتات`   للكشف عن البوتات
`.البوتات طرد`   لطـرد البوتـات""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zoomby")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.المحذوفين`
`.المحذوفين تنظيف`

**- الوصـف :**
لـ عـرض او تنظيـف المجمـوعـة او القنـاة من الحسـابات المحذوفـه

**- الاستخـدام :**
ارسـل الامـر   (.المحذوفين)   داخـل المجمـوعـة او القنـاة
او  (.المحذوفين تنظيف)""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"dellbans")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المجمــوعــه³](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.مسح المحظورين`

**- الوصـف :**
لـ مسـح قائمـة المحظـورين في المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.مسح المحظورين)   داخـل المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

############ الفارات ############
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"varszed")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات 🧬](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر الفــارات :**\n\n",
        buttons=[
            [
                Button.inline("فارات الفحص", data="alivevar"),
                Button.inline("فارات الحماية", data="pmvars"),
            ],
            [Button.inline("فارات الوقتي", data="namevar")],
            [Button.inline("فارات السورس", data="sourcevar")],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"namevar")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر فــارات الوقتــي 🕰](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر فــارات الوقتــي :**\n\n",
        buttons=[
            [
                Button.inline("اسم المستخدم", data="nameprvr"),
            ],
            [
                Button.inline("نبذة وقتيه", data="biolokvar"),
                Button.inline("صورة وقتيه", data="phovarlok"),
            ],
            [
                Button.inline("زخارف الوقتي", data="timevar"),
                Button.inline("زخارف الوقتيه", data="timavar"),
            ],
            [
                Button.inline("رمز الاسم الوقتي", data="symnamvar"),
            ],
            [
                Button.inline("المنطقه الزمنيه", data="contrytime"),
            ],
            [Button.inline("رجوع", data="varszed")],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"contrytime")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر فــارات المنطقـه الزمنيـة 🌐](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر فــارات المنطقـه الزمنيـة :**\n\n",
        buttons=[
            [Button.inline("وقت اليمن", data="yemenvar")],
            [Button.inline("وقت مصر", data="msrvar")],
            [Button.inline("وقت سوريا", data="syriavar")],
            [Button.inline("رجوع", data="namevar")],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"symnamvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف رمز الوقتي`

**- الوصـف :**
لـ تغيير الرمز الذي يظهر بداية الوقت عندما يكون الاسم الوقتي شغال

**- الاستخـدام :**
بالـرد على اي رمز بالامـر   `.اضف رمز الوقتي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"phovarlok")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف صورة الوقتي`

**- الوصـف :**
لوضع صورة لـ حسابك كبروفايل وعليها وقت عند تشغيل الصورة الوقتيه

**- الاستخـدام :**
بالـرد على صورة بالامـر   `.اضف صورة الوقتي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"biolokvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف البايو`

**- الوصـف :**
لوضع بايو محدد لـ حسابك يشتغل عند تفعيل البايو الوقتي

**- الاستخـدام :**
بالـرد على نص بالامـر   `.اضف البايو`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"timevar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**

**⪼** `.الوقتي 1`
**⪼** `.الوقتي 2`
**⪼** `.الوقتي 3`
**⪼** `.الوقتي 4`
**⪼** `.الوقتي 5`
**⪼** `.الوقتي 6`
**⪼** `.الوقتي 7`
**⪼** `.الوقتي 8`
**⪼** `.الوقتي 9`
**⪼** `.الوقتي 10`
**⪼** `.الوقتي 11`
**⪼** `.الوقتي 12`
**⪼** `.الوقتي 13`
**⪼** `.الوقتي 14`

**- الوصـف :**
هذا الامر يقوم بتغييـر زخرفـة ارقام الاسم الوقتي للعديد من الزخارف حسب اختيارك للامر

**- الاستخـدام :**
فقط ارسـل اي امر من الاوامر اعلاه""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nameprvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف الاسم`

**- الوصـف :**
هذا الامر يقوم بوضع اسم حسابك للعديد من الكلايش مثل امر الفحص والسورس .. الخ

**- الاستخـدام :**
بالـرد على اسمك بالامر   `.اضف الاسم`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmvars")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر فــارات حمايـة الخــاص 🛄](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر فــارات حمايـة الخــاص :**\n\n",
        buttons=[
            [
                Button.inline("صورة الحماية", data="picpmvar"),
                Button.inline("كليشة الحماية", data="pmvarkish"),
            ],
            [
                Button.inline("عدد التحذيرات", data="warnvars"),
            ],
            [Button.inline("رجوع", data="varszed")],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"warnvars")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف عدد التحذيرات`

**- الوصـف :**
لـ تغييـر عدد تحذيرات امـر حماية الخاص التي يقوم البوت باعطائها للشخص الذي يراسلك خاص قبل حظـره

**- الاستخـدام :**
**بالـرد على عدد بالامـر**   `.اضف عدد التحذيرات`""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmvarkish")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف كليشة الحماية`

**- الوصـف :**
لـ تغيير الكليشة التي يرد فيهـا البـوت عندما يكون امر الحماية شغال
حيث تعتبـر هاي الكليشـه بمثابـة الـرد الآلـي من البـوت لكـل شخـص يراسلك بالخـاص

**- الاستخـدام :**
**بالـرد على الكليشـه بالامـر**   `.اضف كليشة الحماية`""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"picpmvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف صورة الحماية`

**- الوصـف :**
لوضع صورة لـ الكليشة التي تظهر عندما يكون امر الحماية شغال ويراسلك احد بالخاص

**- الاستخـدام :**
**بالـرد على صورة بالامـر**   `.اضف صورة الحماية`""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"alivevar")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر فــارات الفحـص 🏮](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر فــارات الفحـص :**\n\n",
        buttons=[
            [
                Button.inline("كليشة الفحص", data="kleshalive"),
                Button.inline("رمز الفحص", data="rmzalive"),
            ],
            [Button.inline("صورة الفحص", data="picvars")],
            [Button.inline("رجوع", data="varszed")],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"picvars")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف صورة الفحص`

**- الوصـف :**
لوضع صورة لـ الكليشة التي تظهر عندما ترسل امر (.فحص) 

**- الاستخـدام :**
بالـرد على صورة بالامـر   `.اضف صورة الفحص`""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"kleshalive")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف كليشة الفحص`

**- الوصـف :**
لـ تغيير الكليشة (الكلام) التي تظهر عندما ترسل امر (.فحص)

**- الاستخـدام :**
بالـرد على الكليشـه بالامـر   `.اضف كليشة الفحص`""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"rmzalive")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف رمز الفحص`

**- الوصـف :**
لـ تغيير الرمز الذي يظهر عند ارسال الامـر (.فحص)

**- الاستخـدام :**
بالـرد على اي رمز بالامـر   `.اضف رمز الفحص`""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"katmvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف صورة الكتم`

**- الوصـف :**
لوضع صورة لـ كليشـة الكتم التي تظهر عندما تقوم بكتم احد

**- الاستخـدام :**
بالـرد على صورة بالامـر   `.اضف صورة الكتم`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"startbotvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف صورة البوت`

**- الوصـف :**
لوضع صورة لـ كليشـة الستارت التي تظهر عندما يقوم احد بالدخول للبوت المساعد الخاص بك

**- الاستخـدام :**
بالـرد على صورة بالامـر   `.اضف صورة البوت`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"rmsavar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف رمز ايدي`

**- الوصـف :**
لـ تغيير الرمز الذي يظهر بكليشة الايدي عندما تقوم بارسال (.ايدي)

**- الاستخـدام :**
بالـرد على اي رمز بالامـر   `.اضف رمز ايدي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"enoanvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف عنوان ايدي`

**- الوصـف :**
لـ تغيير العنوان الذي يظهر اعلى كليشة الايدي عندما تقوم بارسال (.ايدي)

**- الاستخـدام :**
بالـرد على اي نص بالامـر   `.اضف عنوان ايدي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"katvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف خط ايدي`

**- الوصـف :**
لـ تغيير الخط الذي يظهر بكليشة الايدي عندما تقوم بارسال (.ايدي)

**- الاستخـدام :**
بالـرد على اي خط ------ بالامـر   `.اضف خط ايدي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"msrvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.وقت مصر`

**- الوصـف :**
لـ تغيير المنطقه الزمنيه للاسم والبروفايل الوقتي عندما يكون مفعل بحيث يكون الوقت هو وقت دولة مصـر الحبيبـه توقيت القاهـرة 🇪🇬

**- الاستخـدام :**
فقط ارسـل الامـر   `.وقت مصر`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"yemenvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.وقت اليمن`

**- الوصـف :**
لـ تغيير المنطقه الزمنيه للاسم والبروفايل الوقتي عندما يكون مفعل بحيث يكون الوقت هو وقت دولة اليمن الحبيبـه توقيت صنعاء 🇾🇪

**- الاستخـدام :**
فقط ارسـل الامـر   `.وقت اليمن`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"syriavar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.وقت سوريا`

**- الوصـف :**
لـ تغيير المنطقه الزمنيه للاسم والبروفايل الوقتي عندما يكون مفعل بحيث يكون الوقت هو وقت دولة سوريا الحبيبـه توقيت دمشق 

**- الاستخـدام :**
فقط ارسـل الامـر   `.وقت سوريا`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"timavar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**

**⪼** `.وقتيه 1`
**⪼** `.وقتيه 2`
**⪼** `.وقتيه 3`
**⪼** `.وقتيه 4`
**⪼** `.وقتيه 5`
**⪼** `.وقتيه 6`
**⪼** `.وقتيه 7`
**⪼** `.وقتيه 8`
**⪼** `.وقتيه 9`
**⪼** `.وقتيه 10`
**⪼** `.وقتيه 11`
**⪼** `.وقتيه 12`
**⪼** `.وقتيه 13`
**⪼** `.وقتيه 14`
**⪼** `.وقتيه 15`
**⪼** `.وقتيه 16`
**⪼** `.وقتيه 17`

**- الوصـف :**
لـ تغييـر زخرفـة ارقام الوقت الذي يظهر على البروفايل الوقتي اثناء تفعيلها للعديد من الزخارف حسب اختيارك للامر

**- الاستخـدام :**
فقط ارسـل اي امر من الاوامر اعلاه

**- ملاحظـه :**
لرؤية زخارف الصورة الوقتيه بالترتيب ع حسب الرقم 
https://t.me/ZED_Thon/148""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pointvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الفــارات](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اضف نقطة الاوامر`

**- الوصـف :**
لـ تغيير النقطه التي ترسلها بداية اي امر لتنفيذه الى اي رمز اخر تريده

**- الاستخـدام :**
بالـرد على اي رمز بالامـر   `.اضف نقطة الاوامر`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zdownload")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر البحث والتحميـل من جميـع مواقـع الـ سوشـل ميديـا :**\n\n",
        buttons=[
            [
                Button.inline("فيديو", data="vedzed"),
                Button.inline("بحث", data="songzed"),
            ],
            [
                Button.inline("بحث انلايـن", data="youini"),
            ],
            [
                Button.inline("تحميل صوت", data="downsou"),
                Button.inline("تحميل فيديو", data="downved"),
            ],
            [
                Button.inline("متحركات", data="giff"),
                Button.inline("صور", data="pictures"),
            ],
            [
                Button.inline("يوتيوب", data="youtubb"),
                Button.inline("ساوند كلود", data="soundcloud"),
            ],
            [
                Button.inline("انستا", data="insta"),
                Button.inline("بنترست", data="pentrist"),
            ],
            [
                Button.inline("لايكي", data="likee"),
                Button.inline("تيك توك", data="tiktok"),
            ],
            [
                Button.inline("فيس بوك", data="facebook"),
                Button.inline("تويتر", data="tweter"),
            ],
            [Button.inline("سناب شات", data="snapchat")],
            [Button.inline("رجوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"songzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.بحث`
`.اغنيه`

**- الوصـف :**
لـ البحث وتحميـل الاغاني والمقاطـع الصوتيـه من يوتيـوب

**- الاستخـدام :**
`.بحث` + اسـم الاغنيـه

**- مثـال :**
`.بحث حسين الجسمي احبك`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"vedzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.فيديو`

**- الوصـف :**
لـ البحث وتحميـل مقاطـع الفيديـو مـن اليوتيـوب

**- الاستخـدام :**
`.فيديو` + اسـم المقطـع

**- مثـال :**
`.فيديو حسين الجسمي احبك`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"youini")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.يوت`

**- الوصـف :**
لـ البحث وتحميـل مقاطـع الصـوت والفيديـو
والافـلام والمسلسلات مـن يوتيـوب
بعـدة صيـغ عبـر لوحـة انلايـن شفافـه

هذا الامر يدعم تحميل مقاطع صوت وفيديو عالية الدقه
تصـل الى 5 جيجابايت وبسرعه تحميـل عاليـه

**- ملاحظـه :**
اللوحـه تشتغل فقط في المجموعات وليس في الخاص ⚠️
للبحث عن الاغاني في الخاص
استخدم امر (.بحث) او (.فيديو)

**- الاستخـدام :**
`.يوت` + اسـم المقطع او الاغنيه
`.يوت` بالـرد على رابـط

**- مثـال :**
`.يوت مسلسل الغازي عثمان الحلقه 1`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"downsou")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.تحميل صوت`

**- الوصـف :**
لـ تحميـل المقـاطع الصـوتيه من يوتيـوب عبر الرابـط

**- الاستخـدام :**
`.تحميل صوت` + رابـط
`.تحميل صوت` بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"downved")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.تحميل فيديو`

**- الوصـف :**
لـ تحميـل مقـاطع الفيديـو من يوتيـوب عبر الرابـط

**- الاستخـدام :**
`.تحميل فيديو` + رابـط
`.تحميل فيديو` بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"giff")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.متحركه`

**- الوصـف :**
لـ تحميـل صـور متحركـه من جـوجـل ..

**- الاستخـدام :**
`.متحركه` + كلمـه""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pictures")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.صور`

**- الوصـف :**
لـ البحث وتحميـل الصـور والخلفيـات من جـوجـل بدقـه HD ..

**- ملاحظـه :**
هـذا الامـر حصـري فقط وخاص بـ سـورس كرستين بقية السورسات ماتحمـل دقـة HD ؟!

**- الاستخـدام :**
`.صور` + كلمـه

**- مثــال :**
`.صور صدام حسين`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"youtubb")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.يوتيوب`

**- الوصـف :**
لـ البحـث عـن روابــط بالكلمــه المحــدده علـى يـوتيــوب

**- ملاحظـه :**
هذا الامر فقط يجلب لك نتائج بحث عن كلمـه على يوتيوب ولا يقم بتحميل المطلوب

**- الاستخـدام :**
`.يوتيوب` + كلمـه
`.يوتيوب` + عـدد + كلمـه""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"soundcloud")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.ساوند`

**- الوصـف :**
لـ تحميـل الاغـاني مـن سـاونـد كـلـود عـبر الرابـط

**- الاستخـدام :**
`.ساوند` + رابـط
`.ساوند` بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"insta")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.انستا`
`.تحميل صوت`
`.تحميل فيديو`

**- الوصـف :**
لـ تحميـل الصـور ومقاطـع الصـوت والفيديـو والستوريـات مـن انستجـرام عبر الرابـط

**- الاستخـدام :**
`.انستا` + رابـط
`.انستا` بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pentrist")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.بنترست`

**- الوصـف :**
لـ تحميـل الصــور ومقـاطـع الفيـديـو مـن بنتـرسـت عـبر الرابـط

**- الاستخـدام :**
`.بنترست` + رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"likee")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.لايكي`

**- الوصـف :**
لـ تحميـل مقـاطـع الفيـديــو مـن لايكـي عـبر الرابـط

**- الاستخـدام :**
`.لايكي` + رابـط
`.لايكي` + بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"tiktok")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.تيك`

**- الوصـف :**
لـ تحميـل مقـاطـع الفيـديــو مـن تيـك تـوك عـبر الرابـط

**- الاستخـدام :**
`.تيك` + رابـط
`.تيك` + بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"facebook")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.فيس`

**- الوصـف :**
لـ تحميـل مقـاطـع الفيـديــو مـن فيس بـوك عـبر الرابـط

**- الاستخـدام :**
`.فيس` + رابـط
`.فيس` + بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"tweter")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.تويتر`

**- الوصـف :**
لـ تحميـل مقاطـع الفيديـو من تويتـر عبـر الرابـط

**- الاستخـدام :**
`.تويتر` + رابـط
`.تويتر` + بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"snapchat")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر البحـث والتحميــل 🛰](t.me/S_EG_P) .
**- الامـر :**
`.سناب`

**- الوصـف :**
لـ تحميـل مقاطـع الفيديـو من سنـاب شـات عبـر الرابـط

**- الاستخـدام :**
`.سناب` + رابـط
`.سناب` + بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"funzed")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر التسليـه والتحشيش 🏂🎃](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر التسليـه والتحشيش :**\n\n",
        buttons=[
            [
                Button.inline("اوامــر تسليـه متحركـه", data="fun1zed"),
            ],
            [
                Button.inline("اوامــر تسليـه جديـدة", data="fun2zed"),
            ],
            [
                Button.inline("اوامــر التحـشيش", data="fun3zed"),
            ],
            [
                Button.inline("اوامــر الالعــاب", data="fun4zed"),
            ],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fun1zed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر التسليـه 🏂](t.me/S_EG_P) .
**⪼** `.تسليه1`
**⪼** `.تسليه2`
**⪼** `.تسليه3`
**⪼** `.تسليه4`
**⪼** `.تسليه5`
**⪼** `.تسليه6`
**⪼** `.تسليه7`
**⪼** `.تسليه8`
**⪼** `.تسليه9`
**⪼** `.تسليه10`

**- الوصـف :**
اكثـر من 70 امـر تسليـه متحركـه للترفيـه والمـرح فقـط

**- الاستخـدام :**
فقط ارسـل اي امـر من الاوامـر اعـلاه وانسـخ الامـر

**- ملاحظـه :**
لا تقم بتكرار هذه الاوامـر او استخدامهـا بكثـره حتى لا يحدث تعليق لحسابك""",
        buttons=[
            [Button.inline("رجوع", data="funzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fun2zed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر التسليـه ⛹🏻‍♀](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.حيوان`
**⪼** `.زاحف`
**⪼** `.مشهور`
**⪼** `.مشهوره`
**⪼** `.معاني`
**⪼** `.كت`
**⪼** `.اوصف`
**⪼** `.هينه`
**⪼** `.نسبه الحب`
**⪼** `.نسبه الانوثه`
**⪼** `.نسبه الغباء`
**⪼** `.نسبه الانحراف`
**⪼** `.نسبه المثليه`
**⪼** `.نسبه النجاح`
**⪼** `.نسبه الكراهيه`


**- الوصـف :**
اوامـر تسليـه جديـدة ممطـروقـه للترفيـه والمـرح فقـط

**- الاستخـدام :**
فقط ارسـل اي امـر من الاوامـر اعـلاه كالتالي :

.الامر بالـرد ع الشخـص
.الامر +معـرف او ايـدي الشخـص

او بالنسبه للنسب ارسـل :
الامر + اسم + اسم

**- ملاحظـه :**
يتم اضافة المزيد من اوامـر التسليه بالتحديثات الجايه""",
        buttons=[
            [Button.inline("رجوع", data="funzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fun3zed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر التحشيش 🎃](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.رفع تاج`
**⪼** `.رفع بقلبي`
**⪼** `.رفع مرتي`
**⪼** `.رفع صاك`
**⪼** `.رفع صاكه`
**⪼** `.رفع حات`
**⪼** `.رفع حاته`
**⪼** `.رفع ورع`
**⪼** `.رفع مزه`
**⪼** `.رفع مرتبط`
**⪼** `.رفع مرتبطه`
**⪼** `.رفع حبيبي`
**⪼** `.رفع خطيبتي`
**⪼** `.رفع جلب`
**⪼** `.رفع جريذي`
**⪼** `.رفع فرخ`
**⪼** `.رفع مطي`
**⪼** `.رفع حمار`
**⪼** `.رفع خروف`
**⪼** `.رفع حيوان`
**⪼** `.رفع بزون`
**⪼** `.رفع زباله`
**⪼** `.رفع منشئ`
**⪼** `.رفع مدير`
**⪼** `.رفع كواد`

**- الوصـف :**
اوامـر تحشيش للترفيـه والمـرح فقـط

**- الاستخـدام :**
فقط ارسـل اي امـر من الاوامـر اعـلاه كالتالي :

.الامر بالـرد ع الشخـص
.الامر +معـرف او ايـدي الشخـص

**- ملاحظـه :**
يتم اضافة المزيد من اوامـر التحشيش بالتحديثات الجايه""",
        buttons=[
            [Button.inline("رجوع", data="funzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fun4zed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الالـعــاب 🎮🎳](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.بلاي`
**العــاب الانـلايـن لســورس كرستين 🕹**
**⪼** `.كت`
**اسئلـة كـت تـويت ⁉️**
**⪼** `.احكام`
**لعبــة احكــام الشهيــرة ⚖👩🏻‍⚖**
**⪼** `.عقاب`
**لعبــة عقــاب ⛓**
**⪼** `.اكس او`
**لعبــة اكـس او 🧩**
**⪼** `.نرد`
**لعبــة رمـي النــرد 🎲**
**⪼** `.سهم`
**لعبــة رمـي السهــم 🎯**
**⪼** `.سله`
**لعبــة كــرة السلــة 🏀**
**⪼** `.كرة`
**- لعبــة كــرة القــدم ⚽️**
**⪼** `.حظ`
**لعبــة الحــظ 🎰**
**⪼** `.خيرني`
**لعبــة لـو خيـروك بالصـور ⁉️🌉**
**⪼** `.تويت`
**- لعبــة كـت تـويت بالصـور ⁉️🌁**


**- الوصـف :**
العـاب سـورس كرستين ممطـروقـه جربهـن راح يعجبنـك 🥳💞

**- ملاحظـه :**
سيتـم اضـافــة المـزيــد من الالعــاب بالتحديثــات الجــايـه 🎭

**- الاستخـدام :**
فقط ارسـل اي امـر من الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="funzed")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"acccount")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات الاوامـر المتعلقـه بالحسـاب :**\n\n",
        buttons=[
            [
                Button.inline("البايو الوقتي", data="biome"),
                Button.inline("الاسم الوقتي", data="namme"),
            ],
            [
                Button.inline("الصورة الوقتيه", data="picme"),
            ],
            [
                Button.inline("قنواتي", data="channelme"),
                Button.inline("كروباتي", data="groubme"),
            ],
            [
                Button.inline("حماية الخاص", data="pmme"),
            ],
            [
                Button.inline("رجـوع", data="ZEDHELP"),
                Button.inline("التالـي", data="nextacc"),
            ],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nextacc")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات الاوامـر المتعلقـه بالحسـاب :**\n\n",
        buttons=[
            [
                Button.inline("احصائياتي", data="infome"),
                Button.inline("الكشف", data="whome"),
            ],
            [
                Button.inline("التخزين", data="logme"),
            ],
            [
                Button.inline("الكتم", data="mutme"),
                Button.inline("الحظر", data="banme"),
            ],
            [Button.inline("سجل الاسماء", data="whonam")],
            [
                Button.inline("رجـوع", data="ZEDHELP"),
                Button.inline("التالـي", data="next2acc"),
            ],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"next2acc")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات الاوامـر المتعلقـه بالحسـاب :**\n\n",
        buttons=[
            [
                Button.inline("الازعاج", data="echozed"),
                Button.inline("الانتحال", data="enthalzed"),
            ],
            [
                Button.inline("الاذاعــة", data="gozzz"),
            ],
            [
                Button.inline("الحاظرهم", data="banzzz"),
                Button.inline("حذف دردشة", data="delzzz"),
            ],
            [
                Button.inline("رجـوع", data="ZEDHELP"),
            ],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"echozed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.ازعاج`
**⪼** `.الغاء ازعاج`
**⪼** `.تقليد`
**⪼** `.الغاء تقليد`
**⪼** `.المقلدهم`
**⪼** `.حذف المقلدهم`

**- الوصـف :**
لـ ازعاج شخص حيث يظل حسابك يكرر نفس كلام الشخص تماماً كالببغاء 🦜😹

**- الاستخـدام :**
`.ازعاج` **بالـرد ع شخـص**
`.الغاء ازعاج` **بالـرد ع شخـص**

بقيـة الاوامـر في الاعلـى""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"enthalzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.انتحال`
**⪼** `.اعاده`

**- الوصـف :**
لـ انتحـال حساب شخص حيث يصبح حسابك منتحل الشخص من حيث الاسم والبروفايل والبايو
يستخدم للتمويه فقط🥷😹

**- الاستخـدام :**
`.انتحال` **بالـرد ع شخـص لـ انتحالـه**
`.اعاده` **بالـرد ع شخـص لـ الغـاء انتحالـه**""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"gozzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.للكروبات`
**⪼** `.للخاص`
**⪼** `.خاص`

**- الوصـف :**
(.للكروبات) لـ اذاعة رسـالتك لجميـع المجموعات التي في حسابك

(.للخاص) لـ اذاعة رسـالتك لجميـع الاشخـاص الذين لديك خاص معهم

(.خاص) لـ ارسـال رسـالة لشخـص بدون الدخول للخاص

**- الاستخـدام :**
`.للكروبات` **بالـرد ع رسـاله**
`.للخاص` **بالـرد ع رسـاله**
`.خاص` **+ معـرف الشخص + الرسـاله**""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.الحاظرهم`

**- الوصـف :**
لـ جلب قائمـة بجميـع الاشخـاص الذين قمت بحظرهم من خاصك

**- الاستخـدام :**
`.الحاظرهم`""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"delzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.احذف`

**- الوصـف :**
لـ الدردشـة مع اي شخص بالخـاص

**- الاستخـدام :**
`.احذف` **+معـرف الشخـص**""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"biome")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.بايو وقتي`

**- الوصـف :**
لـ إضافة وقت او ساعة رقميه على نبذتك الخاصه

**- الاستخـدام :**
**اولاً قم باضافة فار البايو عبر الامر :**
`.اضف البايو` بالـرد ع النص الذي تريده نبذه لك

**ثانياً قم بتشغيل النبذه الوقتيه عبر الامر :**
`.بايو وقتي`

**- ملاحظـه :**
**لـ ايقاف البايو الوقتي قم بارسال الامر التالي :**
`.انهاء البايو`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"namme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اسم وقتي`

**- الوصـف :**
لـ إضافة وقت او ساعة رقميه بجانب اسم حسابك تيليجرام

**- الاستخـدام :**
**اولاً قم بتشغيل الاسم الوقتي عبر الامر :**
`.اسم وقتي`

**ثانياً قم بالذهاب ل اعدادات حسابك تيليجرام
سوف تلاحظ الوقت بالخانه الاولى للاسم
قم بادراج اسمك بالخانه الثانيه ليظهر بجانب الوقت**

**- ملاحظـه :**
**لـ ايقاف الاسم الوقتي قم بارسال الامر التالي :**
`.انهاء الاسم`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"picme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.صوره وقتيه`

**- الوصـف :**
لـ إضافة وقت او ساعة رقميه على صورة حسابك تيليجرام

**- الاستخـدام :**
**اولاً قم باضافة فار الصورة عبر الامر :**
`.اضف صورة الوقتي` بالـرد ع الصورة التي تريدها صورة لحسابك

**ثانياً قم بتشغيل الصورة الوقتيه عبر الامر :**
`.صوره وقتيه`

**- ملاحظـه :**
**لـ ايقاف الصورة الوقتيه قم بارسال الامر التالي :**
`.انهاء البروفايل`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"channelme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.قنواتي ادمن`
**⪼** `.قنواتي مالك`
**⪼** `.قنواتي الكل`

**- الوصـف :**
لـ جلب قائمـه فيها كل القنوات التي انت مشترك فيها على حسب الامر
كمثال الامر (.قنواتي ادمن) يقوم بجلب قائمه فيها كل اسماء القنوات التي انت ادمن فيها فقط وهكـذا لبقية الاوامر

**- الاستخـدام :**
**ارسـل احد الاوامـر ادناه**
`.قنواتي ادمن`
`.قنواتي مالك`
`.قنواتي الكل`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"groubme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.كروباتي ادمن`
**⪼** `.كروباتي مالك`
**⪼** `.كروباتي الكل`

**- الوصـف :**
لـ جلب قائمـه فيها كل المجموعات التي انت مشترك فيها على حسب الامر
كمثال الامر (.كروباتي ادمن) يقوم بجلب قائمه فيها كل اسماء المجموعات التي انت ادمن فيها فقط وهكـذا لبقية الاوامر

**- الاستخـدام :**
**ارسـل احد الاوامـر ادناه**
`.كروباتي ادمن`
`.كروباتي مالك`
`.كروباتي الكل`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmme")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر البحث والتحميـل من جميـع مواقـع الـ سوشـل ميديـا :**\n\n",
        buttons=[
            [
                Button.inline("اوامر حماية الخاص", data="pmcmd"),
            ],
            [
                Button.inline("فارات حماية الخاص", data="pmvar"),
            ],
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmcmd")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر حمـايــة الخــاص 🛡](t.me/S_EG_P) .
**⪼** `.الحمايه تفعيل`
**لـ تفعيـل حمايـة الخـاص لـ حسـابك**

**⪼** `.الحمايه تعطيل`
**لـ تعطيـل حمايـة الخـاص لـ حسـابك**

**⪼** `.قبول`
**لـ السمـاح لـ الشخـص بـ ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك بـدون تحـذير**

**⪼** `.رفض`
**لـ رفـض الشخـص من ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك**

**⪼** `.مرفوض`
**لـ حظـر الشخـص من الخـاص دون تحـذير**

**⪼** `.المقبولين`
**لـ عـرض قائمـة بالاشخـاص المقبـولين**

**⪼** `.بلوك`
**لـ حظـر شخـص من التكلم معـاك خـاص**

**⪼** `.الغاء بلوك`
**لـ الغـاء حظـر شخـص محظـور من الخـاص**


**- الوصـف :**
 حماية الخـاص هي عبـارة عن رد آلي تلقائي من البوت
لكل شخص يراسلك خاص في حال غيابك او انشغـالك لعـدم الـرد
عنـدما تكون حمايـة الخـاص مفعلـه عبـر الامـر (`.الحمايه تفعيل`) ..
حيث يقوم البوت بالرد الآلي ع الاشخاص اليراسلونك خاص
واعطائهم تحذيرات بعدم تكرار الرسائل والانتظار لك
والا يتم حظرهم اذا تجاوزو عدد التحذيرات

**- الاستخـدام :**
ارسـل اولاً
`.الحمايه تفعيل`
لتفعيـل الحمايـة والـرد الآلـي للبـوت بالخـاص

بقية الاوامـر مع شـرح كل أمـر في الاعلـى""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - فــارات حمـايــة الخــاص 🛡](t.me/S_EG_P) .
**⪼** `.اضف عدد التحذيرات`
**لـ تغييـر عدد تحذيرات امـر حماية الخاص التي يقوم البوت باعطائها للشخص الذي يراسلك خاص قبل حظـره**

**⪼** `.اضف كليشة الحماية`
**لـ تغيير الكليشة التي يرد فيهـا البـوت عندما يكون امر الحماية شغال
حيث تعتبـر هاي الكليشـه بمثابـة الـرد الآلـي من البـوت لكـل شخـص يراسلك بالخـاص**

**⪼** `.اضف صورة الحماية`
**لـ وضع صورة لـ الكليشة التي تظهر عندما يكون امر حماية الخاص شغال
حيث تظهـر هذه الصورة وتحتهـا كليشة الكلام عندما يراسلك احد بالخاص**


**- الوصـف :**
لـ تخصيص وتغييـر ملحقـات حماية الخاص من عدد تحذيرات وكليشـه وصـورة على حسب اختيارك انت ..

**- الاستخـدام :**
**بالـرد على عدد بالامـر**   `.اضف عدد التحذيرات`

**بالـرد على الكليشـه بالامـر**   `.اضف كليشة الحماية`

**بالـرد على صورة بالامـر**   `.اضف صورة الحماية`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"infome")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.احصائياتي`

**- الوصـف :**
لـ جلب قائمـه بـ احصائيات دردشـات حسابك من قنوات ومجموعات وبوتات .. الخ

**- الاستخـدام :**
**ارسـل** `.احصائياتي`""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"whome")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.ايدي`
**⪼** `.ا`
**⪼** `.ايديي`
**⪼** `.الايدي`
**⪼** `.اسمه`
**⪼** `.صورته`
**⪼** `.صورته الكل`

**- الوصـف :**
لـ عرض معلومات حسابك او حساب احد غيرك من ايدي وصورة ومعـرف وبايو ورتبـه
يشبه تمام امر (ايدي) في بوتات الحماية

**- الاستخـدام :**
**لجلب معلومات حسابك ارسـل فقط** 
`.ايدي`

**لجلب او الكشف عن شخص آخر ارسـل**
`.ايدي` **بالـرد ع الشخـص**
`.ايدي` **+ معـرف او ايـدي الشخص**

**لجلب ايديك فقـط ارسـل**
`.ايديي`

**لجلب اسـم شخص ارسـل**
`.اسمه` **بالـرد ع الشخـص**

**لجلب بروفايـلات شخص ارسـل**
`.صورته` **بالـرد ع الشخـص**
`.صورته الكل` **بالـرد ع الشخـص لجلب جميع برفايلاته**

**لجلب ايدي شخص او مجموعة او قناة ارسـل**
`.الايدي` **بالـرد ع الشخـص**
`.الايدي` **داخـل المجموعـة او القنـاة**""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"logme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تخزين الخاص تعطيل`
**⪼** `.تخزين الخاص تفعيل`
**⪼** `.تخزين الكروبات تعطيل`
**⪼** `.تخزين الكروبات تفعيل`

**- الوصـف :**
**اولاً تخزين الخاص :**
لـ تفعيل او تعطيل تخـزين جميـع رسـائل الخـاص بـ كـروب التخـزين
هذا الامر يحتاجه الكثيرين مثلا عندما يأتي شخص لمراسلتك خاص وانت مو موجود ثم يقوم بحذف المحادثه البوت يكون قد اخذ توجيهات من هذه الرسائل لتخزينها بكروب التخزين الخاص بك
طبعا هذا الامر بعد التنصيب يكون مفعل تلقائياً
**ثانياً تخزين الكروبات :**
لـ تفعيل او تعطيل تخـزين جميـع تاكـات الكـروبات بـ كـروب التخـزين
هذا الامر يحتاجه الكثيرين مثلا عندما يقوم شخص باحد المجموعات التي انت موجود فيها بالرد ع رسائلك في المجموعه وانت مو موجود يقوم البوت بمعل اشعار لك بالرساله او الرسائل وتخزينها بكروب التخزين الخاص بك
طبعا هذا الامر بعد التنصيب يكون مفعل تلقائياً

**- الاستخـدام :**
قم بـ ارسـال احد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"mutme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.كتم`
**⪼** `.الغاء كتم`
**⪼** `.ك عام`
**⪼** `.الغاء ك عام`

**- الوصـف :**
لـ كتـم شخص سـواء في المجمـوعـة او الخـاص اذا ارسلت الامر في المجموعة سوف ينكتم في المجموعة واذا في الخاص سوف ينكتم من الخاص فقط ماعدا اوامر الكتم العام فانهما تكتم الشخص من الخاص وجميع المجموعات والقنوات التي انت مشرف فيهـا

**- الاستخـدام :**
**لـ الكتم ارسـل**
`.كتم`   بالـرد ع شخص
`.كتم`   + معـرف/ايـدي الشخـص
`.الغاء كتم`   بالـرد ع شخص
`.الغاء كتم`   + معـرف/ايـدي الشخـص

**لـ الكتم العـام ارسـل**
`.ك عام`   بالـرد ع شخص
`.ك عام`   + معـرف/ايـدي الشخـص
`.الغاء ك عام`   بالـرد ع شخص
`.الغاء ك عام`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.حظر`
**⪼** `.الغاء حظر`
**⪼** `.ح عام`
**⪼** `.الغاء ح عام`

**- الوصـف :**
لـ حظـر شخص سـواء في المجمـوعـة او الخـاص اذا ارسلت الامر في المجموعة سوف ينحظر من المجموعة واذا في الخاص سوف ينحظر من الخاص فقط
ماعدا اوامر الحظر العام فانهما تحظر الشخص من الخاص وجميع المجموعات والقنوات التي انت مشرف فيهـا

**- الاستخـدام :**
**لـ الحظر ارسـل**
`.حظر`   بالـرد ع شخص
`.حظر`   + معـرف/ايـدي الشخـص
`.الغاء حظر`   بالـرد ع شخص
`.الغاء حظر`   + معـرف/ايـدي الشخـص

**لـ الحظر العـام ارسـل**
`.ح عام`   بالـرد ع شخص
`.ح عام`   + معـرف/ايـدي الشخـص
`.الغاء ح عام`   بالـرد ع شخص
`.الغاء ح عام`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"whonam")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الحســاب 🚹](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.الاسماء`
**⪼** `.المعرفات`

**- الوصـف :**
لـ جـلب قائمـة بسجـل اسمـاء ومعـرفـات حسـاب الشخـص

**- الاستخـدام :**
`.الاسماء`   **بالـرد ع شخص**
`.الاسماء`   **+ معـرف/ايـدي الشخـص**
`.المعرفات`   **بالـرد ع شخص**
`.المعرفات`   **+ معـرف/ايـدي الشخـص**""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"extras")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المـرفقــات 🖥](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر مرفقـات السـورس :**\n\n",
        buttons=[
            [
                Button.inline("الميديا والصيغ", data="meddia"),
            ],
            [
                Button.inline("ستوريات", data="story"),
                Button.inline("افتارات", data="avatar"),
            ],
            [
                Button.inline("الملصقات", data="stickerrs"),
            ],
            [Button.inline("رجوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"meddia")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المـرفقــات 🖥](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.لملصق`
⦇ الامـر بالـرد ع صـوره ⦈ لـ تحويـل الصـوره لـ ملصـق

**⪼** `.لصوره`
⦇ الامـر بالـرد ع ملصـق ⦈ لـ تحويـل الملصـق لـ صـوره

**⪼** `.لفيد`
⦇ الامـر بالـرد ع صـوره او ملصـق ⦈ لـ تحويـلهـا لـ تصميـم فيديـو

**⪼** `.دائري`
⦇ الامـر بالـرد ع صـوره او ملصـق او فيديـو او متحركـه ⦈ لـ تحويـلهـا لـ تصميـم فيديـو دائـري

**⪼** `.لمتحركة`
⦇ الامـر بالـرد ع ملصـق متحـرك ⦈ لـ تحويـله لـ متحـركـه

**⪼** `.حول بصمه`
⦇ الامـر بالـرد ع فيديـو ⦈ لـ استخـراج الصـوت كـ تسجيل صوت بصمه

**⪼** `.حول صوت`
⦇ الامـر بالـرد ع فيديـو ⦈ لـ استخـراج الصـوت كـ ملـف صوت MP3

**⪼** `.لمتحركه`
⦇ الامـر بالـرد ع صـوره او ملصـق ⦈ لـ تحويـلهـا الـى متحـركـه

**⪼** `.لمتحرك`
⦇ الامـر بالـرد ع فيديـو ⦈ لـ تحويـله الـى متحـركـه


**- الوصـف :**
اوامـر تحويـل الصيـغ

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="extras")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"story")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الستـوريـات 🎆🏖](t.me/S_EG_P) .
**- الامـر :**
`.حالات واتس`
**- اكثـر مـن 2000 فيديـو حالات واتسـاب قصيـرة 🎬**

`.ستوري انمي`
**- مقاطـع ستوريـات انمـي قصيـرة 🎞**

`.ادت`
**- مقاطـع ادت منـوعـة 🎥**

`.رياكشن`
**- مقاطـع رياكشـن ترفيهيــه 📺**

`.ميمز`
**- بصمـات ميمـز تحشيـش 🎃**

`.غنيلي`
**- مقاطـع اغـانـي قصيـره 🎶**

`.شعر`
**- مقاطـع صـوت شعـريـه 🎙**

`.رقيه`
**- رقيـه شرعيـة لعـدة مشائـخ 🕋**


**- الوصـف :**
اوامـر ستوريـات منـوعـة

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="extras")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"avatar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الآفتـــارات والصــور 🎆🏖](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.بنات`
**- آفتـارات بنـات تمبلـر 💅🎆**

**⪼** `.رمادي`
**- آفتـارات شبـاب رمـاديـه 🏂🏙**

**⪼** `.رماديه`
**- آفتـارات بنـات رمـاديـه ⛹🏻‍♀🌁**

**⪼** `.بيست`
**- آفتـارات بيست تطقيـم بنـات 👯‍♀🏖**

**⪼** `.حب`
**- آفتـارات بيست تطقيـم حب ♥️🧚‍♂🧚‍♀**

**⪼** `.ولد انمي`
**- اكثـر مـن 2500 آفتـار آنمـي شبـاب 🙋🏻‍♂🎆**

**⪼** `.بنت انمي`
**- اكثـر مـن 1800 آفتـار آنمـي بنـات 🙋🏻‍♀🎆**

**⪼** `.ري اكشن`
**- صـور رياكشـن تحشيـش 🎃😹**

**⪼** `.معلومه`
**- صـور ومعلومـات عـامـه 🗺**


**- الوصـف :**
اوامـر افتـارات تمبلـر ممطـروقـه

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="extras")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"stickerrs")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر المـرفقــات 🖥](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.ملصق`
⦇ .ملصق بالـرد ع صـوره او فيديـو ⦈  لـ صنـع ملصـق او ملصـق فيديـو متحـرك
 
**⪼** `.حزمه`
⦇ .حزمه بالـرد ع ملصـق ⦈  لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقوقـك

**⪼** `.حزمة`
⦇ .حزمة + اسـم بالـرد ع ملصـق ⦈  لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقـوق الاسـم الـذي ادخلتـه
 
**⪼** `.معلومات الملصق`
⦇ الامـر بالـرد ع ملصـق ⦈  لـ جـلب معلومـات حزمـة الملصـق

**⪼** `.ملصقات`
⦇ الامـر + اسـم ⦈  لـ البحـث عن حـزم ملصقـات بـ الاسـم


**- الوصـف :**
اوامـر الملصقـات

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="extras")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"toolzed")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر ادوات السـورس :**\n\n",
        buttons=[
            [
                Button.inline("الاشتـراك الاجبـاري", data="subszed"),
            ],
            [
                Button.inline("الصيـد والتشيكـر", data="huntzed"),
            ],
            [
                Button.inline("تجميع النقاط", data="pointzed"),
                Button.inline("النشر التلقائي", data="nashzed"),
            ],
            [
                Button.inline("حفـظ الذاتيـه التلقائـي", data="thatia"),
            ],
            [
                Button.inline("رجـوع", data="ZEDHELP"),
                Button.inline("التالـي", data="nexttools"),
            ],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nexttools")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر ادوات السـورس :**\n\n",
        buttons=[
            [
                Button.inline("الماسـح الضوئـي", data="scanner"),
            ],
            [
                Button.inline("الحاسبة", data="calczed"),
                Button.inline("الطقس", data="taks"),
            ],
            [
                Button.inline("ادوات الروابـط", data="urltools"),
            ],
            [
                Button.inline("نقل الملكيه", data="transzzz"),
                Button.inline("الإنشـاء", data="creatzzz"),
            ],
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"thatia")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تفعيل الذاتيه`
**⪼** `.تعطيل الذاتيه`
**⪼** `.ذاتيه`
**⪼** `.مم`

**- الوصـف :**
لـ حفظ الصورة او الميديـا الذاتيـه او المؤقتـه والممنـوع حفظهـا على تيليجـرام
بشكـل تلقائـي اول مايرسل لك شخص صوره ذاتيه سوف يقوم حسابك بحفظها في حافظـة حسابـك تلقائيـاً

**- ملاحظـه :**
اول ماتنصب راح يكون امر حفظ الذاتيه التلقائي مفعل يعني ماتحتاج انك تفعله
الا فقط في حال كنت تريد تعطيله او عطلته من قبل

**- الاستخـدام :**
`.تفعيل الذاتيه`
**لتفعيـل الحفظ التلقائـي**

`.تعطيل الذاتيه`
**لتعطيـل الحفظ التلقائـي**

`.ذاتيه`
**بالـرد ع الصـورة في حال كان الحفظ التلقائـي في وضع التعطيل**""",
        buttons=[
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"scanner")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** 

**- الوصـف :**
-

**- الاستخـدام :**
-""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"calczed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.احسب`

**- الوصـف :**
الـه حاسبـه بسيطـه لـ حسـاب المسـائل والمعـادلات الرياضيـه

**- الاستخـدام :**
`.احسب`   **+ مسئلـه**

**- مثـال :**
`.احسب 125 + 575`""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"taks")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.طقس`

**- الوصـف :**
لـ عـرض حالـة الطقـس اليومـي لـ اي مدينـه

**- الاستخـدام :**
`.طقس`   **+ مدينـه**

**- مثـال :**
`.طقس بغداد`""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"transzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تحويل ملكية`

**- الوصـف :**
لـ تحويـل ملكيـة القنـاة/الكـروب لـ شخـص

**- الاستخـدام :**
**قم اولاً بـ اضـافة كـود التحقق بخطوتين الخـاص بك لـ الفـارات
عبـر الامـر : ↶**
`.اضف التحقق`
**بالـرد ع كـود التحقق بخطوتين الخـاص بك**

**ثم انتظر البوت يعيد التشغيل وارسـل الامـر : ↶**
`.تحويل ملكية` **+ معـرف الشخص
داخـل القناة او المجموعة
لتحويـل ملكيـة القنـاة/الكـروب للشخـص**""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"creatzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.انشاء كروب`
**⪼** `.انشاء قناه`
**⪼** `.انشاء خارق`

**- الوصـف :**
لـ إنشـاء (كروب/قناه/كروب خارق) جاهـز باستخـدام البـوت

**- الاستخـدام :**
(`.انشاء كروب` + اسم الكروب)**:
لـ إنشـاء مجمـوعـة جـاهزه**

(`.انشاء قناه` + اسم القناه)**:
لـ إنشـاء قنـاة جـاهزه**

(`.انشاء خارق` + اسم الكروب) **:
لـ إنشـاء مجمـوعـة خـارقـه**""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"urltools")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - ادوات الروابــط 💡](t.me/S_EG_P) .\n\n**- اليك عـزيـزي شروحـات اوامـر ادوات الروابــط :**\n\n",
        buttons=[
            [
                Button.inline("اختصـار الروابـط", data="shorturl"),
            ],
            [
                Button.inline("سكريـن", data="screenzed"),
                Button.inline("عـرض", data="viewzzz"),
            ],
            [
                Button.inline("دوميـن", data="dnszzz"),
            ],
            [
                Button.inline("اخفـاء الرابـط", data="hideurl"),
            ],
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"shorturl")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اختصار`
**⪼** `.الغاء اختصار`

**- الوصـف :**
لـ اختصـار روابـط الصفحـات او فك الروابـط المختصـره

**- الاستخـدام :**
`.اختصار`   **+ رابـط او بالـرد ع رابـط**

`.الغاء اختصار`   **+ رابـط مختصر او بالـرد ع رابـط مختصر**
**- مثـال :**
`.اختصار https://github.com/Zed-Thon/ZelZal`

`.الغاء اختصار https://da.gd/rm6qri`""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"screenzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.سكرين`
**⪼** `.ss`

**- الوصـف :**
لـ جلب لقطـة شاشـة لأي رابـط صفحـه بدون الدخول اليهـا

**- الاستخـدام :**
`.سكرين`  **+ رابـط**""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"viewzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.عرض`

**- الوصـف :**
لـ جلب رابـط عـرض فـوري للتصفح من التلي لأي رابـط صفحـه بدون الدخول اليهـا

**- الاستخـدام :**
`.عرض`  **بالـرد ع رابـط**""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"dnszzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.دومين`

**- الوصـف :**
لـ دوميـن dns لأي صفحـه او موقـع ع الانتـرنت

**- الاستخـدام :**
`.دومين`   **+ رابـط او بالـرد ع رابـط**

**- مثــال :**
`.دومين google.com`""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"hideurl")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الادوات 💡](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.اخفاء`

**- الوصـف :**
لـ اخفـاء اي رابـط بعلامـة مموهـه
هـذا الامـر يفيد اي حدا عنده رابـط ملغـم ويريـد اخفائـه

**- الاستخـدام :**
`.اخفاء`   **+ رابـط او بالـرد ع رابـط**""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"subszed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الاشتــراك الاجبــاري 🛗](t.me/S_EG_P) .
**- الامـر :**
**- اولاً اوامـر اضافـة القنـاة المطلوبـه للفـارات :**

**⪼** `.ضع الاشتراك خاص`  **او**  `.وضع الاشتراك خاص`
**لـ اضافة قناة اشتراك الخاص للفارات .. استخدم الامر + معرف القناة او الامر داخل القناة ✓**

**⪼** `.ضع الاشتراك كروب`  **او**  `.وضع الاشتراك كروب`
** لـ اضافة قناة اشتراك الكروب للفارات .. استخدم الامر + معرف القناة داخل الكروب ✓**


**- ثانيـاً اوامـر تفعيـل الاشتـراك بعـد اضافة القنـاة :**

**⪼** `.اشتراك خاص`
**لـ تفعيـل الاشتـراك الاجبـاري للخـاص بعـد اضافة الفـار ✓**

**⪼** `.اشتراك كروب`
**لـ تفعيـل الاشتـراك الاجبـاري للكروب بعـد اضافة الفـار .. استخدم الامر داخل الكروب ✓**


**- ثالثـاً اوامـر تعطيـل الاشتــراك :**

**⪼** `.تعطيل اشتراك الخاص`  **او**  `.تعطيل خاص`
**لـ تعطيـل الاشتـراك الاجبـاري للخـاص اذا كـان مفعـل ✓**

**⪼** `.تعطيل اشتراك الكروب`  **او**  `.تعطيل كروب`
**لـ تعطيـل الاشتـراك الاجبـاري للكـروب اذا كـان مفعـل ✓**


**- الوصـف :**
تمكنك ميزة الاشتراك الاجباري من وضع قناتك وتمويلها اعضاء حقيقي عبر حسابك او مجموعتك
بحيث لا يستطيع احد مراسلتك بالخاص الا يشترك اجبارياً بالقناة اذا كان الاشتراك مفعل للخاص حيث يقوم البوت بكتم الشخص خاص لـ إجباره للاشتراك بالقناة
والسماح له بالتحدث بعد الاشتراك بالقناة وكذلك نفس الشي بالنسبـه للمجمـوعة اذا كان الاشتراك مفعل للمجموعة لا يستطيع احد التحدث بالمجموعة الا اذا اشترك بقناتك التي انت قمت باضافتها للاشتراك

**- ملاحظـه :**
سـورس زدثـون هو اول من كتب فكرة الاشتراك الاجباري واضافها للسورس كـ فكرة جديدة لسورسات تيليثون

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"huntzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر الصيـد & التشيكـر ❇️](t.me/S_EG_P) .
**⎉╎شـروحـات اوامـر تشيكـر صيـد معـرفات تيليجـرام :**

**- النـوع :**
**(** `سداسي حرفين`/`ثلاثيات`/`سداسيات`/`بوتات`/`خماسي حرفين`/`خماسي`/`سباعيات` **)**

**- الامـر :**
**⪼** `.صيد`  + النـوع
**لـ صيـد يـوزرات عشوائيـه على حسب النـوع**

**⪼** `.تثبيت`  + اليـوزر
**لـ تثبيت اليـوزر بقنـاة معينـه اذا اصبح متاحـاً يتم اخـذه**

**⪼** `.حالة الصيد` 
**لـ معرفـة حالـة تقـدم عمليـة الصيـد**

**⪼** `.حالة التثبيت` 
**لـ معرفـة حالـة تقـدم التثبيت التلقـائـي**

**⪼** `.ايقاف الصيد` 
**لـ إيقـاف عمليـة الصيـد الجاريـه**

**⪼** `.ايقاف التثبيت` 
**لـ إيقـاف عمليـة التثبيت التلقـائـي**


**- الوصـف :**
اوامـر تشكيـر وصيـد يـوزرات تيليجـرام المميـزه

**- ملاحظـه :**
لا تقم باستخـدام اوامـر الصيد بكثـره حتى لا يحدث تعليق وبطئ لحسـابك

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pointzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر تجميــع النقــاط 🛂](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.المليار`
**لـ تجميـع النقـاط مـن بـوت المليـار ( @t06bot ) .. تلقـائيـاً ✓**

**⪼** `.الجوكر`
**لـ تجميـع النقـاط مـن بـوت الجوكـر ( @A_MAN9300BOT ) .. تلقـائيـاً ✓**

**⪼** `.الجنرال`
**لـ تجميـع النقـاط مـن بـوت الجنــرال ( @MARKTEBOT ) .. تلقـائيـاً ✓**

**⪼** `.المليون`
**لـ تجميـع النقـاط مـن بـوت المليــون ( @qweqwe1919bot ) .. تلقـائيـاً ✓**

**⪼** `.ايقاف المليار`
**لـ ايقـاف عمليـة تجميـع النقـاط من بوت المليـار ..**

**⪼** `.ايقاف الجوكر`
**لـ ايقـاف عمليـة تجميـع النقـاط من بوت الجوكـر ..**

**⪼** `.ايقاف الجنرال`
**لـ ايقـاف عمليـة تجميـع النقـاط من بوت الجنــرال ..**

**⪼** `.ايقاف المليون`
**لـ ايقـاف عمليـة تجميـع النقـاط من بوت المليــون ..**


**- الوصـف :**
اوامـر تجميـع نقـاط من بوتات تمويل طاشه
- طبعا المايعرف ايش هي النقاط ؟!
هي عبارة عن نقاط يقوم بتجميعها الشخص من بوتات تمويل عبر الاشتراك بالقنوات من داخل البوت لربح النقاط ثم بعد ذلك يستطيع شراء اعضاء من نفس البوت عبر هذه النقاط

**- ملاحظـه :**
افضل بوت تمويل طاش حاليـاً لتجميع النقاط هو بوت المليـار

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nashzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامــر النشــر التلقــائي 🌐](t.me/S_EG_P) .
**- الامـر :**
**⪼** `.تلقائي`
**الامـر + (معـرف/ايـدي/رابـط) القنـاة المـراد النشـر التلقـائي منهـا .. استخـدم الامـر داخـل قناتك✓**

**⪼** `.ستوب`
**الامـر + (معـرف/ايـدي/رابـط) القنـاة المـراد ايقـاف النشـر التلقـائي منهـا .. استخـدم الامـر داخـل قناتك ✓**


**- الوصـف :**
النشـر التلقائـي هي عبارة عن خاصيه تسمح لـ البوت الموجود بحسابك بنشـر منشورات تلقائيـه بقناتك من قنـاة انت تحددهـا

**- ملاحظـه 🧧:**
- الاوامـر صـارت تدعـم القنـوات الخاصه ايضـاً والمعـرفات والروابـط ايضاً الى جـانب الايـدي .. ع عكس بقية السورسات 🏂🎗
🛃 سيتـم اضـافة المزيـد من اوامــر النشـر التلقـائي بالتحديثـات الجـايه

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

