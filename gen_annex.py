import jinja2
import os
from jinja2 import Template
from numpy import random
import pandas as pd
import re

latex_annex_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

template = latex_annex_env.get_template('annex_a.jinja2')

if __name__ == "__main__":

    df = pd.read_excel('data.xlsx')
    # df['stateOfMatter'] = pd.Categorical(df.stateOfMatter, categories=['gas', 'liquid', 'solid'], ordered=True)
    # df.sort_values('stateOfMatter', inplace=True)

    rows = df.to_dict(orient = 'records')
    isotopes = [
        [
            {
                'name': n,
                'weight': re.search(r"[0-9]+", n).group(0)
            } for n in row['isotope'].split(";")
        ] for row in rows
    ]

    with open("annex.tex", "w") as f:
            f.write(template.render(
                    rows = rows, isotopes = isotopes
                ))
        

