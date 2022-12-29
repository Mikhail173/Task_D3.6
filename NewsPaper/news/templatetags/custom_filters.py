from django import template

register = template.Library()

CENSORED = ['редиска', 'плохиш', 'смерть', 'шантаж']


@register.filter()
def censor(text):
    text_cens = ''
    for word in text.split():
        if word.strip('.,"/') in CENSORED:
            word = (word[:1] + ('*' * (len(word) - 1)))
        text_cens += f'{word + " "}'
    return text_cens