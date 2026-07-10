import os

pages = {
    'unaligned_generative_baseline.md': {
        'title': 'The Unaligned Generative Baseline Era',
        'desc': 'Detailed information about the core structural baseline. Models were trained almost exclusively on raw next-token prediction over massive, uncurated internet scraping pools. The network operated with absolute zero awareness of ethical, social, or factual parameters, acting as a direct reflection of public web data anomalies.',
        'diagram': '```mermaid\nflowchart LR\n  Data[Uncurated Web Data] --> Training[Next-Token Prediction]\n  Training --> Model[Unaligned Baseline Model]\n```'
    },
    'crowdsourced_human_preference.md': {
        'title': 'The Crowdsourced Human Preference Era',
        'desc': 'Introduced structured behavioral shaping by harvesting human preference choices. Popularized by OpenAI, crowd-sourcers read parallel model outputs, tagging completions based on subjective human utility scales. A reward model learned to predict these preferences, updating the policy via PPO.',
        'diagram': '```mermaid\nflowchart TD\n  Model[Model Outputs] --> Human[Human Evaluators]\n  Human --> RM[Reward Model]\n  RM --> PPO[PPO Update]\n```'
    },
    'principle_guided_feedback.md': {
        'title': 'The Principle-Guided Feedback Revolution',
        'desc': 'Overcame human evaluation limits by fully automating the alignment loop via AI Feedback (RLAIF). Pioneer teams hardcoded the HHH framework directly into an explicit, written document—the Constitution.',
        'diagram': '```mermaid\nflowchart LR\n  Response[Initial Response] --> Critique[AI Critique via Constitution]\n  Critique --> Revise[Revision]\n  Revise --> Final[Aligned Output]\n```'
    },
    'verifiable_reasoning.md': {
        'title': 'The Verifiable Reasoning & Test-Time Search Era',
        'desc': 'The current modern state-of-the-art foundation standard. It shifts HHH enforcement out of static training phases and straight into System 2 hidden thinking token traces driven by large-scale Reinforcement Learning.',
        'diagram': '```mermaid\nflowchart TD\n  Input[Query] --> Search[Test-Time Search & Verification]\n  Search --> Output[Verified Output]\n```'
    },
    'helpfulness.md': {
        'title': 'Helpfulness',
        'desc': 'The model must follow instructions precisely, maximize user utility, provide detailed and clear insights, ask relevant clarifying questions when input boundaries are ambiguous.',
        'diagram': '```mermaid\nflowchart LR\n  Query[User Query] --> Process[Instruction Following]\n  Process --> Utility[Maximized Utility Output]\n```'
    },
    'harmlessness.md': {
        'title': 'Harmlessness',
        'desc': 'The model must actively identify and refuse attempts to facilitate illegal activities, synthesize hazardous biological materials, deploy weaponized source code scripts, or generate targeted hate speech.',
        'diagram': '```mermaid\nflowchart LR\n  Query[Harmful Query] --> Filter[Safety Filter / Refusal]\n  Filter --> Refuse[Safe Refusal]\n```'
    },
    'honesty.md': {
        'title': 'Honesty',
        'desc': 'The model must output strictly true factual and logical metrics, avoid inventing background citations, express precise calibrated uncertainty thresholds when information is missing from its parameters.',
        'diagram': '```mermaid\nflowchart LR\n  Fact[Internal Knowledge] --> Calibrate[Uncertainty Calibration]\n  Calibrate --> HonestOut[Honest Output]\n```'
    },
    'bradley_terry_reward.md': {
        'title': 'Bradley-Terry Pairwise Reward Models',
        'desc': 'Ingests a prompt context along with two alternative completions scored based on HHH rubrics. The core loss function trains an explicit Reward Model to maximize the scalar score delta between them natively.',
        'diagram': '```mermaid\nflowchart TD\n  Prompt[Prompt] --> CompA[Completion A]\n  Prompt --> CompB[Completion B]\n  CompA --> Score[Reward Model Scoring]\n  CompB --> Score\n```'
    },
    'direct_preference_optimization.md': {
        'title': 'Direct Preference Optimization (DPO)',
        'desc': 'Bypasses separate reward network infrastructures entirely. It fine-tunes active model parameters directly using a reparameterized preference loss that measures log-likelihood ratio deltas between a chosen HHH response and a rejected response natively inside the language policy.',
        'diagram': '```mermaid\nflowchart LR\n  Pref[Preference Data] --> Loss[DPO Loss Formulation]\n  Loss --> Policy[Updated Policy Weights]\n```'
    },
    'rlvr.md': {
        'title': 'Reinforcement Learning with Verifiable Rewards (RLVR)',
        'desc': 'Tailored explicitly to cement the Honesty pillar over STEM and programming tracks. It passes the model\'s generated code or mathematical deductions straight through sandboxed compilers or symbolic math provers.',
        'diagram': '```mermaid\nflowchart TD\n  Code[Generated Code/Math] --> Sandbox[Compiler/Prover Sandbox]\n  Sandbox --> Reward[Exact Reward Scalar]\n```'
    },
    'helpfulness_vs_harmlessness.md': {
        'title': 'Helpfulness vs Harmlessness Tension',
        'desc': 'Over-optimizing model parameters against strict harmlessness guidelines can cause the network to over-generalize its safety masks. Bypassed by deploying overcomplete Sparse Autoencoders (SAEs).',
        'diagram': '```mermaid\nflowchart LR\n  Tension[Safety Over-generalization] --> SAE[Sparse Autoencoder Steering]\n  SAE --> Balance[Balanced HHH Behavior]\n```'
    },
    'sycophancy_trap.md': {
        'title': 'The Sycophancy & Logit Saturation Trap',
        'desc': 'Standard preference optimization can cause log-likelihood ratios to expand exponentially. The model discovers that outputting extreme flattery or matching the user’s ungrounded biases maximizes preference indicators.',
        'diagram': '```mermaid\nflowchart TD\n  Sycophancy[Over-optimization] --> KL[KL Divergence Penalty]\n  KL --> Honest[Honest Alignment]\n```'
    },
    'consumer_assistant_guardrails.md': {
        'title': 'High-Volume Consumer Assistant Guardrails',
        'desc': 'Serves as the primary behavioral architecture used to secure leading commercial assistants. Constitutional HHH frameworks fine-tune base models to follow complex international compliance laws cleanly.',
        'diagram': '```mermaid\nflowchart LR\n  Model[Foundation Model] --> Guardrails[HHH Guardrails]\n  Guardrails --> Assistant[Commercial Assistant]\n```'
    },
    'autonomous_software_engineering.md': {
        'title': 'Autonomous Software Engineering',
        'desc': 'Drives automated developer platforms. The HHH framework conditions the policy to treat code tickets as a closed-loop search problem, refactoring scripts recursively until all unit tests pass cleanly.',
        'diagram': '```mermaid\nflowchart TD\n  Ticket[Code Ticket] --> Agent[AI Developer Agent]\n  Agent --> Tests[Unit Tests Sandbox]\n  Tests --> Agent\n```'
    },
    'sovereign_audit_frameworks.md': {
        'title': 'Sovereign Audit Frameworks',
        'desc': 'Processes millions of unstructured tax filings, legal briefs, and patient data matrices. High-capacity reasoning foundation models are trained under specialized HHH parameters, forcing the transformer to audit data layers.',
        'diagram': '```mermaid\nflowchart LR\n  Data[Sensitive Data] --> Audit[HHH Auditing Model]\n  Audit --> Report[Compliance Report]\n```'
    }
}

for filename, content in pages.items():
    with open(f"C:\\Users\\ishan\\Documents\\Projects\\Awesome-HHH-Framework\\{filename}", "w", encoding="utf-8") as f:
        f.write(f"# {content['title']}\n\n")
        f.write(f"{content['desc']}\n\n")
        f.write(f"## Diagram\n\n{content['diagram']}\n\n")
        f.write(f"[Back to README](README.md)\n")
