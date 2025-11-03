#!/usr/bin/env python3
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


BASE_URL = "https://github-readme-stats.vercel.app/api"

DARK = "&theme=catppuccin_mocha"
LIGHT = "&theme=catppuccin_latte"
TRANSPARENT = "&theme=transparent"
DARK = LIGHT = TRANSPARENT

COMMON_PARAMS = f"username=magniquick&border_radius=5&hide_border=true&show_icons=true"
PREF_DARK = 'source media="(prefers-color-scheme: dark)"'
PREF_LIGHT = 'source media="(prefers-color-scheme: light)"'

STATS_URL = f"{BASE_URL}?{COMMON_PARAMS}"
STATS = f"""<picture> <{PREF_DARK} srcset="{STATS_URL}{DARK}"/> <{PREF_LIGHT} srcset="{STATS_URL}{LIGHT}"/><img alt="Magniquick's GitHub stats" src="{STATS_URL}{TRANSPARENT}"/></picture>"""


def get_width() -> int:
    img = requests.get(STATS_URL).content.decode("utf-8")
    fields = img.split("width=")
    fields = fields[1].split('"')
    width = int(fields[1])
    eprint(f"Image width: {width}")
    return width


WIDTH = 467
try:
    import requests

    WIDTH = get_width()
except ImportError as e:
    eprint(f"Error importing modules: {e}, falling back to default width.")
except ValueError as e:
    eprint(f"Error getting image width: {e}, falling back to default width.")

LANG_URL = f"{BASE_URL}/top-langs/?{COMMON_PARAMS}&card_width={WIDTH}&layout=compact&size_weight=0.5&count_weight=0.5"
LANG = f"""<picture> <{PREF_DARK} srcset="{LANG_URL}{DARK}"/> <{PREF_LIGHT} srcset="{LANG_URL}{LIGHT}"/><img alt="Top languages used by Magniquick" src="{LANG_URL}{TRANSPARENT}"/></picture>"""

a = f"""
<h1 align='center'>
  👋 Hi there! I am Magniquick.
</h1>

- 📚 I'm currently learning Rust
- 📫 DM me on [Discord](https://discordapp.com/users/715159111355990058) to chat :D
- 😄 Pronouns: he / him  

### ✨ My Status  
| {STATS} | {LANG} |
|---------|--------|

---

<!-- I'm thinking Miku, Miku, Ooh-ee-ooh -->
<img src="https://count.getloli.com/@Magniquick?theme=miku" alt="count" width="300">
""".strip()
print(a)
