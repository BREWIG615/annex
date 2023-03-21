import jinja2
import os
from jinja2 import Template
from numpy import random
import pandas as pd
import subprocess

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

df = pd.read_excel('data.xlsx')

df['stateOfMatter'] = pd.Categorical(df.stateOfMatter, categories=['gas', 'liquid', 'solid'], ordered=True)

df.sort_values('stateOfMatter', inplace=True)

if __name__ == "__main__":

    for i, row in df.iterrows():
        print(row)

    with open("annex_a.tex", "w"
    ) as tf:
        tf.write(
            df[["assetName", 
                "desc", 
                "electronConfig", 
                "sub", 
                "etymology" ]]
                .rename(columns={'assetName' : 'Element', 'desc' : 'Description'})
                .to_latex(
                    index=False,
                    # caption=df['assetName'],
                    column_format="|p{1in}|p{2in}|p{0.5in}|p{1in}|p{2in}|" 
                )
        )

    # subprocess.run(["pdflatex", "annex_a.tex"])