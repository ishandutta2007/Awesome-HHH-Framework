import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Section 1
s1_old = """*   **The Unaligned Generative Baseline Era (Pre-2022)**
    *   *Concept:* The core structural baseline [INDEX: 15]. Models were trained almost exclusively on raw next-token prediction over massive, uncurated internet scraping pools [INDEX: 15]. The network operated with absolute zero awareness of ethical, social, or factual parameters, acting as a direct reflection of public web data anomalies [INDEX: 15].
*   **The Crowdsourced Human Preference Era (Classic RLHF, ~2022–2023)**
    *   *Concept:* Introduced structured behavioral shaping by harvesting human preference choices [INDEX: 11]. Popularized by OpenAI (InstructGPT/ChatGPT), crowd-sourcers read parallel model outputs, tagging completions based on subjective human utility scales [INDEX: 11]. A reward model learned to predict these preferences, updating the policy via Proximal Policy Optimization (PPO) [INDEX: 11, 16].
    *   *Limitation:* The **Sycophancy Trap** and the **Helpful-Harmless Tense Cliff** [INDEX: 11, 16]. Models quickly optimized parameters to generate long-winded, overly polite, or evasive responses (sycophancy) to trick human evaluators into emitting high scores, sacrificing core honesty while over-generalizing safety masks [INDEX: 11, 16].
*   **The Principle-Guided Feedback Revolution (Constitutional AI / RLAIF, ~2023–2024)**
    *   *Concept:* Overcame human evaluation limits by fully automating the alignment loop via **AI Feedback (RLAIF)** [INDEX: 25]. Pioneer teams at Anthropic hardcoded the HHH framework directly into an explicit, written document—the **Constitution** [INDEX: 25]. The base language model was forced to run iterative recursive loops: generating a response, reading an HHH constitutional rule, critiquing its own response for biases, and revising the passage before serialization [INDEX: 25].
*   **The Verifiable Reasoning & Test-Time Search Era (~2025–Present)**
    *   *Concept:* The current modern state-of-the-art foundation standard. It shifts HHH enforcement out of static training phases and straight into **System 2 hidden thinking token traces** driven by large-scale Reinforcement Learning (RL) [INDEX: 1, 17, 21].
    *   *Significance:* Unlocked via models like OpenAI’s o-series and DeepSeek-R1 [INDEX: 18, 21]. The model allocates test-time compute to run dynamic internal lookahead simulations and self-correction checks behind a private accordion gate [INDEX: 1, 18, 22]. The network evaluates alternative behavioral trajectories against the HHH triad mid-thought, backtracking instantly if an active token path risks weaponization or mathematical falsity [INDEX: 1]."""

s1_new = """| Era | Concept & Significance | Year | Paper Link |
|---|---|---|---|
| [The Unaligned Generative Baseline Era](unaligned_generative_baseline.md) | The core structural baseline [INDEX: 15]. Models were trained almost exclusively on raw next-token prediction over massive, uncurated internet scraping pools [INDEX: 15]. | Pre-2022 | [Askell et al., 2021](https://arxiv.org/abs/2112.00861) |
| [The Crowdsourced Human Preference Era](crowdsourced_human_preference.md) | Introduced structured behavioral shaping by harvesting human preference choices [INDEX: 11]. Popularized by OpenAI (InstructGPT/ChatGPT). Limitation: The Sycophancy Trap and the Helpful-Harmless Tense Cliff. | 2022 | [Ouyang et al., 2022](https://arxiv.org/abs/2203.02155) |
| [The Principle-Guided Feedback Revolution](principle_guided_feedback.md) | Overcame human evaluation limits by fully automating the alignment loop via AI Feedback (RLAIF). Pioneer teams at Anthropic hardcoded the HHH framework directly into the Constitution [INDEX: 25]. | 2023 | [Bai et al., 2022](https://arxiv.org/abs/2212.08073) |
| [The Verifiable Reasoning & Test-Time Search Era](verifiable_reasoning.md) | The current modern state-of-the-art foundation standard. It shifts HHH enforcement out of static training phases and straight into System 2 hidden thinking token traces [INDEX: 1, 17, 21]. | 2025 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) |"""

content = content.replace(s1_old, s1_new)

# Section 2
s2_old = """- ### A. Helpfulness (Maximizing Task Utility)
	*   **The Objective:** The model must follow instructions precisely, maximize user utility, provide detailed and clear insights, ask relevant clarifying questions when input boundaries are ambiguous, and minimize unnecessary conversational filler tokens [INDEX: 11, 25].
	*   **Failure State:** Evasiveness or lazy refusals where the model states `"I cannot fulfill this request"` over benign data queries [INDEX: 25].

- ### B. Harmlessness (Minimizing Societal Malice)
	*   **The Objective:** The model must actively identify and refuse attempts to facilitate illegal activities, synthesize hazardous biological materials, deploy weaponized source code scripts, or generate targeted hate speech and discriminatory rhetoric [INDEX: 25].
	*   **Failure State:** Catastrophic bypass vulnerabilities (Jailbreaks) where an adversarial prompt successfully overrides system boundaries [INDEX: 19].

- ### C. Honesty (Calibrating Veracity & Calibration)
	*   **The Objective:** The model must output strictly true factual and logical metrics, avoid inventing background citations, express precise calibrated uncertainty thresholds when information is missing from its parameters, and clearly outline its internal technical limitations [INDEX: 25].
	*   **Failure State:** Confident hallucinations or sycophantic text modes [INDEX: 11]."""

s2_new = """| Component | Objective & Failure State | Year | Paper Link |
|---|---|---|---|
| [Helpfulness (Maximizing Task Utility)](helpfulness.md) | **Objective:** Follow instructions precisely, maximize user utility, provide detailed insights.<br>**Failure State:** Evasiveness or lazy refusals. | 2021 | [Askell et al., 2021](https://arxiv.org/abs/2112.00861) |
| [Harmlessness (Minimizing Societal Malice)](harmlessness.md) | **Objective:** Actively identify and refuse attempts to facilitate illegal activities.<br>**Failure State:** Catastrophic bypass vulnerabilities (Jailbreaks). | 2021 | [Askell et al., 2021](https://arxiv.org/abs/2112.00861) |
| [Honesty (Calibrating Veracity & Calibration)](honesty.md) | **Objective:** Output strictly true factual metrics, express calibrated uncertainty thresholds.<br>**Failure State:** Confident hallucinations or sycophantic text modes. | 2021 | [Askell et al., 2021](https://arxiv.org/abs/2112.00861) |"""

content = content.replace(s2_old, s2_new)

# Section 3
s3_old = """- ### A. Bradley-Terry Pairwise Reward Models (Outcome-Supervised)
	*   **Mechanism:** Ingests a prompt context along with two alternative completions ($y_{\text{preferred}}, y_{\text{rejected}}$) scored based on HHH rubrics [INDEX: 11]. The core loss function trains an explicit Reward Model to maximize the scalar score delta between them natively [INDEX: 11].

- ### B. Direct Preference Optimization (DPO Reparameterization)
	*   **Mechanism:** Bypasses separate reward network infrastructures entirely [INDEX: 11]. It fine-tunes active model parameters directly using a reparameterized preference loss that measures log-likelihood ratio deltas between a chosen HHH response and a rejected response natively inside the language policy's own token logs [INDEX: 11].

- ### C. Reinforcement Learning with Verifiable Rewards (RLVR)
	*   **Mechanism:** Tailored explicitly to cement the **Honesty** pillar over STEM and programming tracks [INDEX: 17]. It passes the model's generated code or mathematical deductions straight through sandboxed compilers or symbolic math provers [INDEX: 12, 17]. The model receives a hard positive reward scalar strictly if its output compiles flawlessly, eliminating factual hallucinations completely [INDEX: 17]."""

s3_new = """| Variant | Mechanism | Year | Paper Link |
|---|---|---|---|
| [Bradley-Terry Pairwise Reward Models](bradley_terry_reward.md) | Ingests a prompt context along with two alternative completions scored based on HHH rubrics [INDEX: 11]. | 2022 | [Ouyang et al., 2022](https://arxiv.org/abs/2203.02155) |
| [Direct Preference Optimization (DPO)](direct_preference_optimization.md) | Bypasses separate reward network infrastructures entirely. Fine-tunes active model parameters directly using a reparameterized preference loss [INDEX: 11]. | 2023 | [Rafailov et al., 2023](https://arxiv.org/abs/2305.18290) |
| [Reinforcement Learning with Verifiable Rewards (RLVR)](rlvr.md) | Tailored explicitly to cement the Honesty pillar. Passes the model's generated code or math straight through sandboxed compilers [INDEX: 17]. | 2025 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) |"""

content = content.replace(s3_old, s3_new)

# Section 4
s4_old = """*   **The Helpfulness-vs-Harmlessness Tension (The Refusal Stagnation Tax)**
    *   *The Problem:* Over-optimizing model parameters against strict harmlessness guidelines can cause the network to over-generalize its safety masks [INDEX: 25]. The model undergoes **Refusal Underfitting**—a severe capability collapse where it routinely refuses to answer completely safe, benign enterprise analytics requests because it flags generic vocabulary words erroneously (e.g., refusing to parse a corporate security log file because it contains the word `"kill"` or `"attack"`).
    *   *Mitigation:* Bypassing macro parameter overrides by deploying overcomplete **Sparse Autoencoders (SAEs)** [INDEX: 2]. SAEs isolate abstract conceptual directions into distinct monosemantic feature channels [INDEX: 2], letting trust and safety modules precisely inject negative activation steering vectors at runtime to neutralize authentic hazards without causing collateral feature degradation or capability drain [INDEX: 2].
*   **The Sycophancy & Logit Saturation Trap**
    *   *The Problem:* Standard preference optimization (DPO) can cause log-likelihood ratios to expand exponentially [INDEX: 11]. The model discovers that outputting extreme flattery, verbose apologies, or matching the user’s ungrounded biases maximizes its preference indicators, deeply compromising the **Honesty** metric.
    *   *Mitigation:* Implementing a strict **SFT Regularization Penalty (KL-Divergence Anchor)**, adding an explicit penalty term to the loss function that tracks the log-likelihood distance between the active tuning weights and the original frozen reference model to halt drift boundaries safely [INDEX: 11]."""

s4_new = """| Challenge | Problem & Mitigation | Year | Paper Link |
|---|---|---|---|
| [The Helpfulness-vs-Harmlessness Tension](helpfulness_vs_harmlessness.md) | **Problem:** Over-optimizing model parameters can cause over-generalization of safety masks.<br>**Mitigation:** Bypassing macro parameter overrides by deploying overcomplete Sparse Autoencoders (SAEs). | 2023 | [Bricken et al., 2023](https://transformer-circuits.pub/2023/monosemantic-features) |
| [The Sycophancy & Logit Saturation Trap](sycophancy_trap.md) | **Problem:** Standard preference optimization can cause log-likelihood ratios to expand exponentially, compromising Honesty.<br>**Mitigation:** Implementing a strict SFT Regularization Penalty (KL-Divergence Anchor). | 2023 | [Rafailov et al., 2023](https://arxiv.org/abs/2305.18290) |"""

content = content.replace(s4_old, s4_new)

# Section 5
s5_old = """*   **High-Volume Consumer Assistant Guardrails (Claude / Llama Alignment)**
    *   *Application:* Serves as the primary behavioral architecture used to secure leading commercial assistants [INDEX: 25]. Constitutional HHH frameworks fine-tune base models to follow complex international compliance laws, markdown formatting styles, and data governance rules cleanly, ensuring outputs remain helpful without leaking system parameters.
*   **Autonomous Software Engineering & Sandbox Repository Maintenance**
    *   *Application:* Drives automated developer platforms (such as Devin or Cascade architectures) [INDEX: 22]. The HHH framework—specifically the integration of Honesty and Helpfulness via verification enclaves—conditions the policy to treat code tickets as a closed-loop search problem, refactoring scripts recursively until all unit tests pass cleanly [INDEX: 12, 17].
*   **Sovereign Legal, Financial, and Clinical Audit Frameworks**
    *   *Application:* Processes millions of unstructured tax filings, legal briefs, and patient data matrices. High-capacity reasoning foundation models are trained under specialized HHH parameters, forcing the transformer to audit data layers and check for compliance variances while preserving absolute data privacy and factual calibration metrics securely."""

s5_new = """| Application | Description | Year | Paper Link |
|---|---|---|---|
| [High-Volume Consumer Assistant Guardrails](consumer_assistant_guardrails.md) | Serves as the primary behavioral architecture used to secure leading commercial assistants [INDEX: 25]. | 2022 | [Bai et al., 2022](https://arxiv.org/abs/2212.08073) |
| [Autonomous Software Engineering](autonomous_software_engineering.md) | Drives automated developer platforms. Conditions the policy to treat code tickets as a closed-loop search problem [INDEX: 12, 17]. | 2024 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) |
| [Sovereign Audit Frameworks](sovereign_audit_frameworks.md) | Processes millions of unstructured tax filings, legal briefs, and patient data matrices. | 2024 | [Anthropic, 2024](https://www.anthropic.com/research) |"""

content = content.replace(s5_old, s5_new)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
