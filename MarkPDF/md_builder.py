import emoji_data_python, mistune

from mistune.plugins.url import url
from mistune.plugins.abbr import abbr
from mistune.plugins.math import math
from mistune.plugins.ruby import ruby
from mistune.plugins.table import table
from mistune.plugins.formatting import *
from mistune.plugins.spoiler import spoiler
from mistune.plugins.def_list import def_list
from mistune.plugins.footnotes import footnotes
from mistune.plugins.task_lists import task_lists

class MDBuilder:
        
    @classmethod
    def render(cls, content):
        content = emoji_data_python.replace_colons(content)
        
        renderer = mistune.HTMLRenderer()
        markdown = mistune.Markdown(renderer, plugins=[
            math,
            footnotes,
            table,
            url,
            abbr,
            ruby,
            spoiler,
            task_lists, def_list,
            strikethrough, subscript, superscript, mark, insert,
        ])

        return markdown(content)

    