#!/usr/bin/env python3
#
# Creates a tex table of all reported midpoints.
#
import base


filename = 't1-all-midpoints.tex'

# Collect journal references
refs = {}
with base.connect() as con:
    c = con.cursor()
    q = 'select key, tex from publication_tex'
    for k, row in enumerate(c.execute(q)):
        refs[row['key']] = row['tex']

# Create table file
fields = [
    'pub',
    'va',
    'na',
    'stda',
    'vi',
    'ni',
    'stdi',
    'sequence',
    'cell',
    'beta1',
]


# Sequence formatting
def seq(s):
    if s == 'astar':
        return 'a*'
    elif s == 'bstar':
        return 'b*'
    elif s is None:
        return '?'
    return s


# Create table
print(f'Writing to {filename}...')
with open(filename, 'w') as f:
    # Header
    eol = '\n'
    f.write(r'\startrowcolors' + eol)
    f.write(r'\begin{longtable}{p{5cm}|lll|lll|lll}' + eol)
    f.write(r'\hline' + eol)
    f.write(r'Publication')
    f.write(r' & $V_a$ & $\sigma_a$  & $n_a$')
    f.write(r' & $V_i$ & $\sigma_i$  & $n_i$')
    f.write(r' & Cell & $\alpha$ & $\beta1$ \\' + eol)
    f.write(r'\hline' + eol)
    f.write(r'\endfirsthead' + eol)
    f.write(r'\hline' + eol)
    f.write(r'\rowcolor{white}' + eol)
    f.write('Publication')
    f.write(r' & $V_a$ & $\sigma_a$  & $n_a$')
    f.write(r' & $V_i$ & $\sigma_i$  & $n_i$')
    f.write(r' & Cell & $\alpha$ & $\beta1$ \\' + eol)
    f.write(r'\hline' + eol)
    f.write(r'\endhead' + eol)
    f.write(r'\hline' + eol)
    f.write(r'\endfoot' + eol)
    # Body
    form = '{:.3g}'
    with base.connect() as con:
        c = con.cursor()
        q = 'select ' + ', '.join(fields) + ' from midpoints_wt'
        for k, row in enumerate(c.execute(q)):
            x = []
            x.append(r'\citet{' + refs[row['pub']] + '}')
            if row['na'] != 0:
                x.append(form.format(row['va']))
                x.append(form.format(row['stda']))
                x.append(form.format(row['na']))
            else:
                x.append('&&')
            if row['ni'] != 0:
                x.append(form.format(row['vi']))
                x.append(form.format(row['stdi']))
                x.append(form.format(row['ni']))
            else:
                x.append('&&')
            x.append(row['cell'].replace('Oocyte', 'Ooc.'))
            x.append(seq(row['sequence']))
            x.append(row['beta1'])
            f.write(' & '.join(x) + r' \\' + eol)
    # Footer
    f.write(r'\end{longtable}' + eol)

print('Done.')