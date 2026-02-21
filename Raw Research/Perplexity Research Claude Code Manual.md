# The Claude Code Manual — Build Notes

## Document Delivered
A comprehensive .docx manual (~60-75 pages) covering Claude Code from 101 through 10 real-world projects, verified against current sources as of February 20, 2026.

## Chapters Delivered
1. What Is Claude Code (And What It Isn't)
2. Setup — Install It, Auth It, Connect It
3. Your First Session — The Mental Model
4. The CLAUDE.md File — Your Project Brain
5. Prompting Patterns That Actually Work
6. Beyond Basics — Plan, Build, Test, Ship
7. Quality Engineering with Claude Code
8. Advanced Patterns — Hooks, Skills, Subagents, and Teams
9. Security, Secrets, and Safety
10. Templates — Copy, Paste, Build (7 templates)
11. Project Playbook — 10 Real Projects
12. Troubleshooting and Debugging
13. Sources

## Build Notes

### Verified Facts (with sources)
- Installation methods: npm, native binary, Homebrew, WinGet — confirmed via official docs[^1][^2][^3]
- Pricing: Free, Pro ($20/mo), Max $100, Max $200, Team Premium ($150/user), Enterprise, API — confirmed via multiple sources[^4][^5][^6]
- Models: Sonnet 4.6 (Feb 17, 2026, SWE-bench 79.6%), Opus 4.6 (Feb 4, 2026, SWE-bench 80.8%) — confirmed[^7][^8][^9]
- CLAUDE.md system: /init, @imports, multi-location, best practices — confirmed via official docs[^10][^11][^12]
- Hooks system: all events, types (command, prompt, agent), matchers — confirmed via official docs[^13]
- Skills, subagents, agent teams — confirmed via official docs[^11][^14][^15][^16]
- Custom slash commands: project-scoped and user-scoped — confirmed[^17][^18]
- MCP integration: add, import, serve — confirmed[^19]
- Security: .claudeignore, permission system, command blocklist, prompt injection protections — confirmed[^20][^21][^22][^23]
- CI/CD: GitHub Actions, GitLab CI/CD, headless mode — confirmed[^24][^25]
- IDE integration: VS Code, Cursor (VSIX workaround) — confirmed[^26][^27][^28]

### Community Tips (cross-referenced)
- Plan-first workflow, break into 3-5 tasks, test-driven approach, checkpointing — multiple Reddit users corroborate[^29][^30][^31]
- Context management: fresh sessions, /clear between tasks — official docs + community[^32][^11]
- Smaller skill files improve efficiency 40-60% — Reddit (anecdotal, labeled)[^33]
- plan.md and phases.md documents pattern — Reddit (136 upvotes)[^31]

### Assumptions Made
- Project examples assume users have basic familiarity with the terminal and Git (as specified in prerequisites)
- Tech stack recommendations for projects reflect what's current and well-supported as of Feb 2026
- Pricing confirmed from multiple independent sources but Anthropic may adjust at any time
- The 10 projects are designed to be completable in a few days each by a motivated beginner with Claude Code guidance — actual time varies by experience

### Unverified Items
- Exact session/message limits for Max plans (Anthropic doesn't publish precise numbers consistently; the "50 sessions/month" figure for Max $200 came from a third-party source)[^6]
- Some third-party pricing pages report slightly different annual pricing for Team seats ($100/mo annual vs $125/mo) — the official pricing may have changed recently[^34]
- The native binary installer version numbers (1.0.58 shown in docs) may have been superseded

### Sources Used

**Official Documentation:**
- Claude Code Setup[^2][^3][^1]
- Claude Code Best Practices[^11]
- Claude Code Common Workflows[^35]
- Claude Code Hooks Guide[^13]
- Claude Code MCP[^19]
- Claude Code Security[^23]
- Claude Code Agent Teams[^16]
- Claude Code GitLab CI/CD[^24]
- Claude Prompting Best Practices[^36]
- Using CLAUDE.md Files[^10]
- Introducing Claude 4[^37]
- Introducing Claude Sonnet 4.6[^8]
- Introducing Claude Opus 4.6[^9]

**Reddit:**
- r/ClaudeCode: Real project workflows, 6-month tips[^29][^33]
- r/ClaudeAI: Workflow that works, CLAUDE.md setup, security concerns, custom commands[^38][^39][^40][^30][^21][^31]

**YouTube:**
- Leon van Zyl: Setup tutorial 2026, MCP guide[^41][^42]
- SnapperAI: Boris Cherny workflow[^43]
- IndyDevDan: Claude Code 2.0[^44]
- Full Course 4 Hours[^45]
- Kevin Stratvert: Beginner tutorial[^46]
- NextWork: Tutorial[^47]
- EricTech: Full setup[^48]
- App building tutorial[^49]

**Other:**
- 32 Claude Code Tips (YK Sugi)[^32]
- Custom Slash Commands guide[^17]
- Skills vs Sub-agents guide[^14]
- Sonnet 4.6 vs Opus 4.6 comparison[^7]
- E2E Testing guide[^50]
- Skills/Agents/MCP explainer[^51]
- Pricing analysis[^5][^4][^6]

---

## References

1. [Set up Claude Code - Anthropic](https://docs.anthropic.com/en/docs/claude-code/setup?e45d281a_page=2&hsa_acc=4274135664&hsa_ad=670851261305&hsa_cam=18419792792&hsa_grp=143270969922&hsa_kw=astronomer+astro&hsa_mt=e&hsa_net=adwords&hsa_src=g&hsa_tgt=kwd-1777215822168&hsa_ver=3&lang=de&wtime=1986s) - Install, authenticate, and start using Claude Code on your development machine.

2. [Set up Claude Code](https://docs.anthropic.com/en/docs/claude-code/setup?trk=psm_a131L000005vJtOQAU) - Install, authenticate, and start using Claude Code on your development machine.

3. [Set up Claude Code - Claude Code Docs](https://code.claude.com/docs/en/setup) - Install, authenticate, and start using Claude Code on your development machine.

4. [ClaudeLog - Claude Code Docs, Guides, Tutorials & Best Practices](https://claudelog.com/pricing/) - Claude AI price breakdown: Pro from $17/month vs Max from $100/month plans, API costs, usage limits....

5. [Claude Pricing Explained: Subscription Plans & API Costs](https://intuitionlabs.ai/articles/claude-pricing-plans-api-costs) - A Premium seat in a Team plan costs $150 per month per person and explicitly “includes Claude Code” ...

6. [Claude Code - Pricing & Plans](https://claudecode.io/pricing) - Compare Claude Code pricing plans: Free, Pro ($17/month), Max ($100/month), and Enterprise. API pric...

7. [Claude Sonnet 4.6 vs Opus 4.6: Which Model Should You ...](https://www.nxcode.io/resources/news/claude-sonnet-4-6-vs-opus-4-6-which-model-to-choose-2026) - Claude Sonnet 4.6 vs Opus 4.6 detailed comparison. Benchmarks, pricing, features, and real-world per...

8. [Introducing Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) - Claude Sonnet 4.6 is our most capable Sonnet model yet. It's a full upgrade of the model's skills ac...

9. [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) - The new Claude Opus 4.6 improves on its predecessor's coding skills. It plans more carefully, sustai...

10. [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) - Learn how to use CLAUDE.md files to give Claude Code persistent context about your project structure...

11. [Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices) - Tips and patterns for getting the most out of Claude Code, from configuring your environment to scal...

12. [Claude Code - Setting up CLAUDE.md Files Tutorial](https://claudecode.io/tutorials/claude-md-setup) - Learn how to configure project-specific settings and context with CLAUDE.md files. Optimize Claude C...

13. [Automate workflows with hooks - Claude Code Docs](https://code.claude.com/docs/en/hooks-guide) - Run shell commands automatically when Claude Code edits files, finishes tasks, or needs input. Forma...

14. [When to Use a Claude Skill vs a Claude Sub-Agent - PRPM](https://prpm.dev/blog/when-to-use-claude-skill-vs-subagent) - Confused when to use Claude skills vs sub-agents? This guide shows developers exactly when to use ea...

15. [Subagents in the SDK - Claude API Docs](https://platform.claude.com/docs/en/agent-sdk/subagents) - Define and invoke subagents to isolate context, run tasks in parallel, and apply specialized instruc...

16. [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams) - Manual parallel sessions: Git worktrees let you run multiple Claude Code sessions yourself without a...

17. [Claude Code Tips & Tricks: Custom Slash Commands](https://cloudartisan.com/posts/2025-04-14-claude-code-tips-slash-commands/) - Learn how to create custom slash commands in Claude Code to automate repetitive tasks and enhance yo...

18. [Claude Code: Part 4 - Slash Commands and Custom ...](https://dev.to/letanure/claude-code-part-4-slash-commands-and-custom-commands-4fkf) - Stop repeating the same instructions every day. Learn to use built-in slash commands and create cust...

19. [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp) - Learn how to connect Claude Code to your tools with the Model Context Protocol.

20. [[FEATURE] Mark sensitive environment variables and file ...](https://github.com/anthropics/claude-code/issues/25053) - Claude Code can access secrets through multiple vectors that existing mitigations don't cover: File ...

21. [[Security] Claude Code reads .env files by default - This needs immediate attention from the team and awareness from devs](https://www.reddit.com/r/ClaudeAI/comments/1lgudw2/security_claude_code_reads_env_files_by_default/) - [Security] Claude Code reads .env files by default - This needs immediate attention from the team an...

22. [Claude Code Automatically Loads .env Secrets, Without ...](https://www.knostic.ai/blog/claude-loads-secrets-without-permission) - Claude Code loads .env secrets into memory without consent, creating an unnecessary and avoidable se...

23. [Security - Claude Code Docs](https://code.claude.com/docs/en/security) - Learn about Claude Code's security safeguards and best practices for safe usage.

24. [Claude Code GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd) - Claude Code uses GitLab CI/CD to run AI tasks in isolated jobs and commit results back via MRs: Even...

25. [How to Integrate Claude Code with CI/CD: Full 2025 ...](https://skywork.ai/blog/how-to-integrate-claude-code-ci-cd-guide-2025/) - Set up Claude Code in your CI/CD for automated PR reviews and testing. Step-by-step 2025 guide with ...

26. [Claude Code Cursor Extension: Complete Installation &amp](https://www.cursor-ide.com/blog/claude-code-cursor-extension-guide) - Master the Claude Code extension in Cursor IDE with this comprehensive guide. Learn 3 proven install...

27. [Integrating Claude Code With Cursor or VS Code IDE](https://www.youtube.com/watch?v=gRNVCeD1br8) - The latest buzz on the A.I. scene is the ability to use Claude Code inside our graphical IDE Cursor ...

28. [Claude Code: in Terminal, in Cursor IDE, or in VS Code Extension?](https://www.youtube.com/watch?v=xU18PCIDQ8Y) - There are different ways how to use Claude Code, not only the original Terminal app, I prefer IDE. L...

29. [How I Use Claude Code Effectively in Real Projects (My ...](https://www.reddit.com/r/ClaudeCode/comments/1p1w2vk/how_i_use_claude_code_effectively_in_real/) - I always start with a detailed plan: I don't let Claude jump straight into code. I begin with a step...

30. [I finally found a Claude Code workflow that actually works (sharing it)](https://www.reddit.com/r/ClaudeAI/comments/1p1vy31/i_finally_found_a_claude_code_workflow_that/) - I finally found a Claude Code workflow that actually works (sharing it)

31. [Claude Code workflow that's been working well for me](https://www.reddit.com/r/ClaudeAI/comments/1mhgskk/claude_code_workflow_thats_been_working_well_for/) - Claude Code workflow that's been working well for me

32. [32 Claude Code Tips: From Basics to Advanced](https://www.linkedin.com/pulse/32-claude-code-tips-from-basics-advanced-yk-sugi-kexec) - Here are my tips for getting the most out of Claude Code, including a custom status line script, cut...

33. [Claude Code is a Beast – Tips from 6 Months of Hardcore Use](https://www.reddit.com/r/ClaudeCode/comments/1oivs81/claude_code_is_a_beast_tips_from_6_months_of/) - Claude Code is a Beast – Tips from 6 Months of Hardcore Use

34. [Claude is dropping max plans for enterprise (maybe ...](https://www.reddit.com/r/ClaudeCode/comments/1r82req/claude_is_dropping_max_plans_for_enterprise_maybe/) - Eventually gave everyone the Copilot Pro+ plan, then rolled out $100/mo limit API to everyone on Cla...

35. [Common workflows - Claude Code Docs](https://code.claude.com/docs/en/common-workflows) - This page covers practical workflows for everyday development: exploring unfamiliar code, debugging,...

36. [Prompting best practices - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) - Be explicit with your instructions. Claude responds well to clear, explicit instructions. Being spec...

37. [Introducing Claude 4 - Anthropic](https://www.anthropic.com/news/claude-4)

38. [A Brief Guide to Setting Up Claude Code from Scratch](https://www.reddit.com/r/ClaudeAI/comments/1mx255o/a_brief_guide_to_setting_up_claude_code_from/) - A Brief Guide to Setting Up Claude Code from Scratch

39. [Can hooks in CC custom slash commands trigger other commands?](https://www.reddit.com/r/ClaudeAI/comments/1m4ntms/can_hooks_in_cc_custom_slash_commands_trigger/) - Can hooks in CC custom slash commands trigger other commands?

40. [is claude able to use custom slash commands inside a custom slash command?](https://www.reddit.com/r/ClaudeAI/comments/1lwsfo4/is_claude_able_to_use_custom_slash_commands/) - is claude able to use custom slash commands inside a custom slash command?

41. [How to Set Up Claude Code in 2026 (Beginner Tutorial)](https://www.youtube.com/watch?v=kddjxKEeCuM) - 🚀 Access ALL video resources & get personalized help in my community:
https://www.skool.com/agentic-...

42. [Claude Code MCP: How to Add MCP Servers (Complete Guide)](https://www.youtube.com/watch?v=DfWHX7kszQI) - 🚀 Access ALL video resources & get personalized help in my community:
https://www.skool.com/agentic-...

43. [How the Creator of Claude Code Sets Up His Workflow (Setup Tutorial)](https://www.youtube.com/watch?v=aqtseECSdtY) - The creator of Claude Code, Boris Cherny, recently shared a detailed thread explaining exactly how h...

44. [Claude Code 2.0 Agentic Coding: No, other agents aren't even close.](https://www.youtube.com/watch?v=nGhsgdQplHw) - Codex CLI and Gemini CLI are NOWHERE NEAR Claude Code 2.0 and it's not even close.

Claude 4.5 Sonne...

45. [CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell ...](https://www.youtube.com/watch?v=QoQBzR1NIqI) - Head of Claude Code: What happens after coding is solved | Boris Cherny. Lenny's Podcast · 51K views...

46. [Claude Code Tutorial for Beginners](https://www.youtube.com/watch?v=eMZmDH3T2bY&vl=en) - This Claude Code Tutorial teaches you what I wish I knew as a software developer about Claude Code b...

47. [Claude Code Tutorial 2025](https://www.youtube.com/watch?v=2eHgWt_WBuc) - For ALL hands-on tech projects to add to your resume: https://link.nextwork.org/youtube

Join our co...

48. [Claude Code Setup That Actually Works | Full Tutorial 2025](https://www.youtube.com/watch?v=P-5bWpUbO60) - Master Claude Code with the ultimate tutorial and guide for 2025. This video covers the full setup, ...

49. [Claude Code Tutorial for Beginners: Build App with AI (2026)](https://www.youtube.com/watch?v=6q8joS_592k) - I'm going to walk you through the entire process step by step showing you the exact prompts I used a...

50. [E2E Testing with Claude Code - Shipyard.build](https://shipyard.build/blog/e2e-testing-claude-code/) - Claude Code can help make end-to-end (E2E) testing more approachable, especially when prompted throu...

51. [Understanding Skills, Agents, Subagents, and MCP in Claude Code](https://colinmcnamara.com/blog/understanding-skills-agents-and-mcp-in-claude-code) - A comprehensive guide to Claude Code's extension ecosystem - Skills for portable tools, Subagents fo...

