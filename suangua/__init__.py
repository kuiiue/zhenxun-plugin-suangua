import random
from pathlib import Path
from services.log import logger
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, Message
from nonebot.params import CommandArg
from utils.message_builder import image


__zx_plugin_name__ = "算卦"
__plugin_usage__ = """
usage：
    算卦不算命
    指令：
        算卦
""".strip()


dir_path=Path(__file__).parent
gua_path=str((dir_path/'images').absolute())+"/"


suangua=on_command("算卦", priority=5, block=True)


@suangua.handle()
async def _(bot: Bot, event: Event, arg: Message=CommandArg()):
    try:
        rand=int(arg.extract_plain_text().strip())
    except:
        rand=random.randint(0, 64)
    logger.info(f"算卦：第{rand}卦")
    msg_image=image(f"{gua_path}{rand}.jpg")
    await suangua.finish(msg_image, at_sender=True)
