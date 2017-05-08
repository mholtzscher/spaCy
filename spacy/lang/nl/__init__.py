# coding: utf8
from __future__ import unicode_literals

from .stop_words import STOP_WORDS

from ..language_data import BASE_EXCEPTIONS
from ..language import Language
from ..attrs import LANG
from ..util import update_exc



class Dutch(Language):
    lang = 'nl'

    class Defaults(Language.Defaults):
        lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
        lex_attr_getters[LANG] = lambda text: 'nl'

        tokenizer_exceptions = update_exc(BASE_EXCEPTIONS)
        stop_words = set(STOP_WORDS)


__all__ = ['Dutch']