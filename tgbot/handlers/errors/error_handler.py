import logging

from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import ErrorEvent

router = Router()


class NotCorrectMassage(Exception):
    pass


@router.error()
async def errors_handler(event: ErrorEvent):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging

    Parameters
    ----------
    event
    """

    #  MUST BE THE  LAST CONDITION (ЭТО УСЛОВИЕ ВСЕГДА ДОЛЖНО БЫТЬ В КОНЦЕ)
    if isinstance(event.exception, TelegramAPIError):
        logging.exception(
            f"TelegramAPIError: {event.exception} \nUpdate: {event.update}"
        )
        return True

    # At least you have tried.
    logging.exception(f"Update: {event.update} \n{event.exception}")
