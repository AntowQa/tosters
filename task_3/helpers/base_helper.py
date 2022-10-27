from bs4 import BeautifulSoup
from pymystem3 import Mystem

m = Mystem()


def get_all_pronouns(html_doc) -> list:
    soup = BeautifulSoup(html_doc, 'html.parser')
    text = soup.get_text()
    info = m.analyze(text)

    def get_analyzed_text(info) -> list:
        return [text.get("analysis", None)[0] for text in info
                if text.get("analysis", None) is not None and text.get("analysis", None) != []
                ]
    return [text for text in get_analyzed_text(info)
            if text.get('gr', None).find("SPRO") != -1
            ]


def get_all_personal_pronouns(pronouns) -> list:
    return [text.get('lex', None) for text in pronouns
            if text.get('gr', None).find("1-л") != -1
            or text.get('gr', None).find("2-л") != -1
            or text.get('gr', None).find("3-л") != -1
            ]


def get_personal_pronouns_of_the_1st_person(pronouns) -> list:
    return [text.get('lex', None) for text in pronouns
            if text.get('gr', None).find("1-л") != -1
            ]
