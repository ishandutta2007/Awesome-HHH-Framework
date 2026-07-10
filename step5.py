import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

right_badge = '  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>\n'

# Add the right badge to the end of the badge paragraph (before </p>)
content = content.replace('alt="Discord" /></a>\n</p>', 'alt="Discord" /></a>\n' + right_badge + '</p>')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
