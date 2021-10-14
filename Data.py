from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nI can search words from Urban Dictionary and give them to you. I will provide it's definition as well as example \n\nYou can send any word here or Try using my inline mode. \n\nBy @M2Botz"

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔍 Search Inline 🔍", switch_inline_query_current_chat="")],
        [
            InlineKeyboardButton(
                "➕ Add to your Group ➕", url="https://t.me/TGDictionary_M2Bot?startgroup=True"
            )
        ],
        [InlineKeyboardButton(text="🏠Home", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("Search Inline 🔍", switch_inline_query_current_chat=""),
            InlineKeyboardButton("How to Use ❔", callback_data="help")
        ],
        [
            InlineKeyboardButton("About😎", callback_data="about")
        ],
        [
            InlineKeyboardButton(
                "➕ Add to your Group ➕", url="https://t.me/TGDictionary_M2Bot?startgroup=True"
            )
        ],
        [InlineKeyboardButton("♥ Updates Channel ♥", url="https://t.me/m2botz")],
        [InlineKeyboardButton("✍️ Support Group ✍️", url="https://t.me/m2botzsupport")],
    ]

    # Help Message
    HELP = """
1) **Inline Mode** (recommended)
 ~ Search any word or word sequence in inline mode, any time.
 ~ Use "`-r`" to get random word

2) **Private Chat**
 ~ Send any word or word sequence privately, any time.
 ~ Send "/random" to get random word.

3) **Group Chats**
 ~ Add in group and reply to any message with /ud or /search".
 ~ You can also use: "/ud text here" or "/search text here" in groups.
 ~ Send "/random" to get random word.
(If doesn't responds in group then make it admin. Telegram is weird)

Made With ❤️ By @M2Botz
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @M2Botz

Updates Channel : [Click Here](https://t.me/m2botz)

Support Group : [Click Here](https://t.me/m2botzsupport)

Source Code : [Releasing Soon](https://t.me/m2botz)

Developer : [M2](https://t.me/ask_admin01)
    """
