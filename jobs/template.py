from .jobs_ import CmdJob, add_job

# noinspection SpellCheckingInspection
pairs = [
    ("Character", "Infobox character"),
    ("Re:Zero Light Novel Volumes", "Infobox novel"),
    ("Parent Tab", None),
    ("Lugnica Navbox", None),
    ("Vollachia Navbox", None),
    ("Gusteko Navbox", None),
    ("Royal Election Navbox", None),
    ("Royal Selection Navbox", None),
    ("Anime Navigation", None),
    ("Manga Navigation", None),
    ("Disambig", None),
    ("LN Navigation", None),
    ("Re:Zero Manga Navigation", None),
    ("Music Navigation", None),
]

repl = ["template", "-always"]
rm = repl + ["-remove"]

for o, n in pairs:
    if n:
        repl += [o, n]
    else:
        rm.append(o)

add_job(CmdJob(repl))
add_job(CmdJob(rm))
