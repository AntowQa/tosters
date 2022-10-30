from bs4 import BeautifulSoup
from settings import PERSONAL_PRONOUNS, FIRST_PERSON_PRONOUNS


def get_personal_pronouns(html_doc) -> list:
    soup = BeautifulSoup(html_doc, 'html.parser')
    text = soup.get_text().split()
    return [text for text in text if text.lower() in PERSONAL_PRONOUNS]


def get_personal_pronouns_of_the_1st_person(personal_pronouns) -> list:
    return [pronoun for pronoun in personal_pronouns if pronoun.lower() in FIRST_PERSON_PRONOUNS]


def get_second_and_third_person_pronouns(personal_pronouns) -> list:
    return [pronoun for pronoun in personal_pronouns if pronoun.lower() not in FIRST_PERSON_PRONOUNS]
