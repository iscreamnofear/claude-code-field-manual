# Claude Code Manual for Real Projects

## Deliverable

[Download the Word document](sandbox:/mnt/data/Claude_Code_Manual_Feb_20_2026.docx)

## Verified snapshot of Claude Code as of February 20, 2026

Claude Code ships as a native CLI with an official installer script for macOS, Linux, WSL, and Windows, plus package manager options for Homebrew and WinGet. Native installs auto-update. Homebrew and WinGet installs require manual upgrades. Node.js is only required for a deprecated npm installation path. citeturn5view1

Claude Code uses permission modes to control autonomy. The CLI supports a Plan mode intended for read-only analysis and planning, and the mode can be toggled during a session with Shift+Tab. citeturn4view1turn6view2turn6view3

Claude Code supports “checkpoints” that snapshot file state before edits. You can open the rewind menu with Esc Esc or the /rewind command. Official docs describe checkpointing as distinct from git and limited to local file changes, with external side effects requiring separate handling. citeturn21search0turn21search3

Claude Code supports persistent project context via CLAUDE.md plus an “auto memory” system. Official docs describe two persistent memory types: auto memory and user-maintained CLAUDE.md files. citeturn3search20

Model defaults in Claude Code vary by plan, with official docs describing plan-dependent defaults for “default” and behavior for model aliases like “opusplan” that route planning and execution to different models. citeturn6view6

Official pricing pages list Claude Pro at $17/month with annual billing ($200 up front) or $20 billed monthly, and Claude Max tiers at $100/month (Max 5x) and $200/month (Max 20x). The same pricing pages state Pro includes Claude Code and Cowork. citeturn14view0turn16view1turn16view0

Official docs describe Claude Code data retention windows that depend on account type and privacy preferences, including longer retention for consumer users who opt in to data use for model improvement, and 30-day retention for users who do not opt in. Official docs also describe commercial defaults and a zero data retention option in specific configurations. citeturn11view1

Claude Code can integrate with external tools via MCP (Model Context Protocol). Official docs warn that third-party MCP servers are not all verified by entity["company","Anthropic","ai company"] and can increase prompt injection risk, especially when servers fetch untrusted content. citeturn4view6

## Manual contents and structure

The Word document is a practical manual designed for beginners who want to build real projects immediately. It follows a progression from “Claude Code 101” through intermediate workflows and advanced patterns, then a 10-project playbook section, then troubleshooting and templates.

Each chapter includes:
- What you will be able to do after the chapter
- Core concepts in plain language
- Hands-on steps with copyable commands and snippets
- Common mistakes with fixes
- A mini checkup checklist
- Community tips (labeled) where relevant
- A Sources section with links used

The Project Playbooks section includes 10 buildable-in-a-week projects covering:
- Marketing website + blog
- Full-stack web app with auth and database CRUD
- Cross-platform mobile app
- Browser extension
- Automation scripts
- Data dashboard
- Financial analysis notebook
- Scoped support chatbot using the Claude API with safety guidance
- Internal tools app
- API service + SDK

Each project includes: who it’s for, why it matters, stack options, milestones, repo structure, reusable Claude Code prompt patterns, testing strategy, deployment plan, debugging guide, and three extensions.

## Build notes

### Assumptions

- I treated February 20, 2026 as “today” and prioritized official documentation on code.claude.com, platform.claude.com, claude.com, and anthropic.com for versioned facts, commands, plan names, capabilities, and pricing.
- For project deployment steps, I used provider-agnostic guidance when provider-specific steps are likely to change frequently.

### Unverified items

- Some claude.ai pages were blocked to this research environment, so I avoided relying on claude.ai pages as primary sources. I used the official documentation domains listed above instead.
- YouTube links are included as community resources. Video content was not transcribed or independently validated line-by-line in this environment. Treat them as walkthrough references and verify steps against official docs.
- For browser extension scaffolding tooling and certain optional libraries in the project playbooks, I did not lock to exact versions. Verify current commands in those tools’ official docs before running.

### Sources grouped by chapter

```text
Chapter 1: Claude Code 101
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/features-overview
- https://code.claude.com/docs/en/how-claude-code-works

Chapter 2: Setup and first run
- https://code.claude.com/docs/en/setup
- https://code.claude.com/docs/en/quickstart
- https://code.claude.com/docs/en/vs-code
- https://code.claude.com/docs/en/jetbrains
- https://code.claude.com/docs/en/desktop-quickstart
- https://code.claude.com/docs/en/claude-code-on-the-web
- https://code.claude.com/docs/en/slack
- https://code.claude.com/docs/en/chrome
- https://code.claude.com/docs/en/authentication
- https://claude.com/pricing
- https://claude.com/pricing/max
- https://code.claude.com/docs/en/model-config
- https://www.anthropic.com/news/claude-opus-4-6
- https://www.anthropic.com/news/claude-sonnet-4-6

Chapter 3: Daily workflow fundamentals
- https://code.claude.com/docs/en/interactive-mode
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/common-workflows
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/keybindings

Chapter 4: Prompting that ships
- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/common-workflows
- https://code.claude.com/docs/en/how-claude-code-works
- https://code.claude.com/docs/en/model-config
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

Chapter 5: Your project’s Claude layer
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/hooks-guide
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/mcp

Chapter 6: Quality engineering with Claude Code
- https://code.claude.com/docs/en/github-actions
- https://code.claude.com/docs/en/gitlab-ci-cd
- https://code.claude.com/docs/en/headless
- https://platform.claude.com/docs/en/agent-sdk/overview

Chapter 7: Security, privacy, and safety
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/security
- https://code.claude.com/docs/en/data-usage
- https://code.claude.com/docs/en/devcontainer
- https://code.claude.com/docs/en/mcp
- https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
- https://platform.claude.com/docs/en/agent-sdk/secure-deployment
- https://www.anthropic.com/news/claude-sonnet-4-6

Chapter 8: Project playbooks
- https://nextjs.org/docs/app/getting-started/installation
- https://nextjs.org/docs/app/getting-started/deploying
- https://vite.dev/guide/
- https://docs.expo.dev/more/create-expo/
- https://fastapi.tiangolo.com/tutorial/
- https://docs.streamlit.io/get-started/installation
- https://docs.astral.sh/uv/getting-started/installation/
- https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat
- https://platform.claude.com/docs/en/build-with-claude/working-with-messages

Chapter 9: Troubleshooting and debugging
- https://code.claude.com/docs/en/troubleshooting
- https://code.claude.com/docs/en/setup
- https://code.claude.com/docs/en/vs-code
- https://code.claude.com/docs/en/mcp

Chapter 10: Templates and starter kit
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/cli-reference

Community sources used
Reddit
- https://www.reddit.com/r/ClaudeCode/comments/1r8uzax/six_claude_code_strategies_for_a_productive/
- https://www.reddit.com/r/ClaudeCode/comments/1qobg1g/how_to_refactor_50k_lines_of_legacy_code_without/
- https://www.reddit.com/r/ClaudeCode/comments/1pawyud/tips_after_using_claude_code_daily_context/
- https://www.reddit.com/r/ClaudeCode/comments/1r8oaef/the_workflow_that_actually_makes_claude_code_fast/
- https://www.reddit.com/r/ClaudeCode/comments/1q193fr/awesome_list_of_claude_code_tips_tricks_gotchas/
- https://www.reddit.com/r/ClaudeCode/comments/1r5ldvp/the_instruction_is_clear_i_just_didnt_follow_it/
- https://www.reddit.com/r/ClaudeAI/comments/1qgccgs/25_claude_code_tips_from_11_months_of_intense_use/
- https://www.reddit.com/r/ClaudeAI/comments/1r66oo0/how_i_structure_claude_code_projects_claudemd/

YouTube
- https://www.youtube.com/watch?v=mymUF7wEJQo
- https://www.youtube.com/shorts/oku8up2w4UI
- https://www.youtube.com/watch?v=PV4bqqsZPH8
- https://www.youtube.com/watch?v=PYmaHbQ45Y8
- https://www.youtube.com/watch?v=JUTx6MxOjhE
- https://www.youtube.com/watch?v=WdD6uD_kupY
- https://www.youtube.com/watch?v=UZb0if-7wGE
- https://www.youtube.com/watch?v=kZ-zzHVUrO4
- https://www.youtube.com/watch?v=rnFNwwwq1D8
- https://www.youtube.com/watch?v=hOiwqYfDCbc
```