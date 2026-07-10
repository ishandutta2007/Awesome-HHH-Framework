import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Add banner at the top
content = content.replace('# Awesome-HHH-Framework', '# 🚀 Awesome-HHH-Framework\n\n<p align="center">\n  <img src="assets/banner.svg" alt="Awesome HHH Framework Banner" width="100%">\n</p>\n')

# Add emojis to headers
content = content.replace('## The Helpfulness-Harmlessness-Honesty (HHH)', '## 🌟 The Helpfulness-Harmlessness-Honesty (HHH)')
content = content.replace('## 1. The Macro Chronological Evolution', '## 🕰️ 1. The Macro Chronological Evolution')
content = content.replace('## 2. Core Components of the Triad Matrix', '## 🧩 2. Core Components of the Triad Matrix')
content = content.replace('## 3. The Core Objective & Optimization Variants', '## 🎯 3. The Core Objective & Optimization Variants')
content = content.replace('## 4. Production Engineering Challenges & Hardening Mitigations', '## 🛠️ 4. Production Engineering Challenges & Hardening Mitigations')
content = content.replace('## 5. Frontier Real-World AI Infrastructure Applications', '## 🌐 5. Frontier Real-World AI Infrastructure Applications')
content = content.replace('## References', '## 📚 References')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
