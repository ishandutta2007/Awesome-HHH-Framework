import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Badges to add
badges = '<p align="center">\n  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>\n  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>\n</p>\n\n'

# SEO keywords paragraph
seo_paragraph = "<!-- SEO tags: Awesome List, HHH Framework, Helpfulness, Harmlessness, Honesty, AI Alignment, LLM Safety, Constitutional AI, RLAIF, Prompt Engineering, Model Guardrails -->\n\n"

# Add badges after the banner
content = content.replace('</p>\n\n## 🌟 The', '</p>\n\n' + badges + seo_paragraph + '## 🌟 The')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
