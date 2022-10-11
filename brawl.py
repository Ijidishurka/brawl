from .. import loader
from telethon.tl.types import Message


@loader.tds
class brawl(loader.Module):
    """Подпишись на канал @modwini"""

    strings = {"name": "brawl"}

    async def 👎cmd(self, message: Message):
        """Скидывает 👎 из Brawl Stars"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/radiofmonline/291">­</a>',
        )

    async def lcmd(self, message: Message):
        """Скидывает 👍 из Brawl Stars"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/radiofmonline/292">­</a>',
        )