import inspect
from googletrans import Translator

translator = Translator()

async def translate_text(text: str) -> str:
    result = translator.translate(text, dest="en")
    if inspect.isawaitable(result):
        result = await result
    return result.text