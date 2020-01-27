import default_text

def generater(indent, colorshceme, langSettings):
    vimrc = default_text.default_vimrc.format(colorshceme, str(indent), str(indent), str(indent), str(indent))

    if langSettings != None:
        for e in langSettings:
            vimrc += default_text.indent_setting_base.format(\
                    e['language'], e['language'],\
                    e['indent'], e['indent'], e['indent'])

    return vimrc
