import default_text
import re

def extraction_colorscheme(colorschceme):
    pattern = '\/.*$'

    result = re.search(pattern, colorschceme).group()

    return result[1:]

def generater(indent, colorscheme, langSettings):
    colorscheme_name = extraction_colorscheme(colorscheme)
    vimrc = default_text.default_vimrc.format(colorscheme, colorscheme_name, str(indent), str(indent), str(indent), str(indent))

    if langSettings != None:
        for e in langSettings:
            vimrc += default_text.indent_setting_base.format(\
                    e['language'], e['language'],\
                    e['indent'], e['indent'], e['indent'])

    return vimrc
