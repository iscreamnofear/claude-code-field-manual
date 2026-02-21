# Claude Code: comprehensive research brief (February 2026)

**Claude Code is Anthropic's terminal-based agentic coding assistant — now on a reported $500 million annual revenue run rate — that reads, writes, and executes code across entire projects.** It has emerged as the leading AI coding CLI, powering workflows from solo indie hacking to enterprise development teams. This brief synthesizes official documentation, industry analyst intelligence, community patterns, and technical context current as of February 20, 2026, organized to support writing a practical manual from beginner setup through advanced workflows.

---

## 1. Installation, setup, and system requirements

### Exact install command
```bash
npm install -g @anthropic-ai/claude-code
```
After installation, navigate to any project directory and run `claude` to start an interactive session. Claude Code is also available at `https://www.npmjs.com/package/@anthropic-ai/claude-code` and the source code has been published under the Apache 2.0 license at `https://github.com/anthropics/claude-code`.

### Node.js requirement
Claude Code requires **Node.js 18+**, with **Node.js 20+ recommended**. As of February 2026, **Node.js 22.x is the current Active LTS** (codename "Jod," entered LTS October 2025), and Node.js 20.x ("Iron") remains in Maintenance LTS until April 2026. Node.js 18.x reached end-of-life in April 2025. The recommended installation method is via nvm (Node Version Manager):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
nvm install 22
nvm use 22
```

### Supported platforms
- **macOS**: Fully supported (primary development platform)
- **Linux**: Fully supported
- **Windows**: Supported **only via WSL** (Windows Subsystem for Linux) — native Windows is not directly supported

### Authentication flow
Claude Code offers two authentication paths. The **default method** is a browser-based OAuth flow that opens on first run, authenticating against an Anthropic Console account (linked to a Claude Pro, Max, Team, or Enterprise subscription). Alternatively, users can set the `ANTHROPIC_API_KEY` environment variable to authenticate directly via API key, billing per-token against their Anthropic account. Authentication tokens are cached locally after first login. Claude Code can also connect via **Amazon Bedrock** or **Google Cloud Vertex AI** with appropriate cloud credentials.

**Key reference URLs:**
- Official documentation: `https://docs.anthropic.com/en/docs/claude-code`
- Product page: `https://www.anthropic.com/claude-code`
- npm package: `https://www.npmjs.com/package/@anthropic-ai/claude-code`

---

## 2. Pricing, plans, and the $100/month sweet spot

### Subscription tiers for interactive use

| Plan | Price | Claude Code access | Notes |
|------|-------|--------------------|-------|
| Claude Free | $0 | ❌ No | Not available |
| Claude Pro | $20/month | ✅ Yes | Rate-limited; heavy users hit caps quickly |
| Claude Max | $100/month | ✅ Yes | **5× Pro usage** — the popular power-user tier |
| Claude Max | $200/month | ✅ Yes | 20× Pro usage — heaviest individual tier |
| Claude Team | $30/user/month | ✅ Yes | Team admin, higher per-user limits |
| Claude Enterprise | Custom | ✅ Yes | SSO, SCIM, audit logs, admin controls |

Real-world pricing confirmation: An internal purchase order from February 10, 2026, shows an enterprise team purchasing Anthropic access at **$100/month per seat** for "AI platform for code execution, research, and UI building" — consistent with the Claude Max tier being the standard choice for professional development use.

### API key billing
When using an API key directly, standard per-token pricing applies. Approximate rates (verify at `https://www.anthropic.com/pricing`):
- **Claude Sonnet 4**: ~$3/MTok input, ~$15/MTok output
- **Claude Opus 4**: ~$15/MTok input, ~$75/MTok output
- **Claude 3.5 Haiku**: ~$0.80/MTok input, ~$4/MTok output
- Extended thinking tokens carry their own pricing tier

API usage can be **substantial** — Claude Code is agentic and often consumes 100K+ tokens per complex session. Many power users report the **Max plan at $100/month is more cost-effective** than API billing for heavy daily use.

### Market context
According to Constellation Research (September 2025), **Claude Code alone is on a $500 million annual revenue run rate**, within Anthropic's broader $5 billion ARR at a $183 billion valuation. By February 2026, Constellation Research also noted that "Anthropic plug-ins for Claude Cowork wiped out SaaS stocks," indicating Anthropic expanded beyond Claude Code into broader collaboration tooling ("Claude Cowork") that disrupted the SaaS market.

---

## 3. Available models and how to select them

### Default model
Claude Code defaults to **Claude Sonnet** (the latest Sonnet version — as of late 2025, Claude Sonnet 4) for its optimal balance of speed, intelligence, and cost in coding tasks.

### Model selection methods
- **CLI flag at launch**: `claude --model claude-sonnet-4-20250514`
- **Environment variable**: `ANTHROPIC_MODEL` or `CLAUDE_MODEL`
- **In-session**: The `/model` slash command
- **Configuration**: Via settings files or `claude config`

### Available models

| Model | Use case | Notes |
|-------|----------|-------|
| **Claude Sonnet 4** | Default for coding | Best speed-to-quality ratio |
| **Claude Opus 4** | Complex architecture, deep reasoning | Higher cost, superior capability |
| **Claude 3.5 Sonnet** | Previous generation | Still performant, lower cost |
| **Claude 3.5 Haiku** | Simple tasks, cost optimization | Fastest and cheapest |

Claude Code is **Anthropic-only** — it does not support OpenAI, Google, or other third-party models. It is specifically optimized for Claude's extended thinking capabilities.

---

## 4. CLI commands, slash commands, and keyboard shortcuts

### CLI flags and options

| Command | Description |
|---------|-------------|
| `claude` | Start interactive REPL in current directory |
| `claude "query"` | Start with an initial prompt |
| `claude -p "query"` | **Print mode** — non-interactive, outputs and exits |
| `claude -c` / `--continue` | Continue most recent conversation |
| `claude --resume <id>` | Resume a specific past session |
| `claude --model <model>` | Specify Claude model |
| `claude --output-format json` | JSON output for scripting/CI |
| `claude --dangerously-skip-permissions` | Skip ALL permission checks (CI/CD only) |
| `claude --allowedTools <tools>` | Pre-approve specific tools |
| `claude --max-turns <n>` | Limit agentic loop iterations |
| `claude config` | Manage configuration |
| `claude update` | Update to latest version |
| `claude mcp` | Manage MCP server connections |
| `claude mcp add <name> -- <cmd>` | Add an MCP server |
| `claude mcp remove <name>` | Remove an MCP server |
| `claude mcp list` | List configured servers |
| `cat file \| claude -p "query"` | Pipe stdin input |

### Slash commands (inside the interactive REPL)

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history and context |
| `/compact` | Condense context (summarize to save tokens) |
| `/config` | View or modify configuration |
| `/cost` | Show token usage and cost for session |
| `/doctor` | Check installation health |
| `/init` | Initialize a new CLAUDE.md file |
| `/login` | Switch accounts or re-authenticate |
| `/logout` | Log out |
| `/model` | Switch model |
| `/permissions` | View or manage tool permissions |
| `/pr-review` | Review a pull request |
| `/review` | Request a code review |
| `/terminal-setup` | Install shell integration (Shift+Enter) |
| `/vim` | Toggle vim keybindings |
| `/bug` | Report a bug |

Custom slash commands can be created by placing Markdown files in `.claude/commands/` (project-level, shared) or `~/.claude/commands/` (personal). For example, `.claude/commands/review.md` becomes accessible as `/project:review`. Commands support the `$ARGUMENTS` placeholder for dynamic input.

### Keyboard shortcuts

| Shortcut | Action |
|----------|--------|
| Enter | Send message |
| Shift+Enter | New line (requires `/terminal-setup`) |
| Escape | Cancel current generation |
| Ctrl+C | Cancel current operation |
| Ctrl+D | Exit Claude Code |
| Tab | Accept a suggestion |
| Up/Down arrows | Navigate command history |

---

## 5. The CLAUDE.md convention explained

`CLAUDE.md` is the single most impactful feature for improving Claude Code output quality, according to both official documentation and overwhelming community consensus. It acts as a persistent "system prompt" for your project — Claude reads these files automatically at session start.

### File placement and scopes (loaded in order)

| Location | Scope | Version control? |
|----------|-------|-----------------|
| `~/.claude/CLAUDE.md` | **Global** (all projects) | No |
| `<project-root>/CLAUDE.md` | **Project** (team-shared) | Yes — commit it |
| `<project-root>/.claude/CLAUDE.md` | **Project-local** (personal) | No — gitignore |
| Subdirectory `CLAUDE.md` files | **Directory-specific** | Varies |

### What to put in CLAUDE.md
The community-refined template that consistently produces the best results:

```markdown
# Project: [Name]

## Tech Stack
- Frontend: React 19 + TypeScript + Tailwind CSS
- Backend: Python FastAPI
- Database: PostgreSQL with Prisma ORM

## Build & Test Commands
- `npm run build` — build the project
- `npm test` — run all tests
- `npm run test:unit -- path/to/test` — run single test
- `npm run lint` — run linter

## Code Conventions
- Use functional components with hooks, no class components
- Use named exports, not default exports
- All API responses follow {data, error, message} format
- Use absolute imports from @/ prefix
- Keep components under 200 lines

## Architecture
- `/src/api` — API route handlers
- `/src/components` — React components
- `/src/lib` — Shared utilities

## Important Rules
- Never modify migration files directly
- Always run tests before committing
- Never use `any` type in TypeScript
```

Initialize a starter file with the `/init` slash command inside the REPL.

---

## 6. Permission model and auto-accept modes

Claude Code uses a **layered permission system** designed to keep humans in control of destructive operations.

### Tool permission categories
**Read-only tools** (always auto-approved): reading files, listing directories, searching code. **Write/modify tools** (require approval): file editing, creation, deletion. **Command execution** (require approval): running shell commands.

### Permission prompt options
When Claude requests a write or execute action, the user sees: **Allow Once** (this specific action), **Allow Always** (this type for the session), or **Deny**.

### Auto-accept configuration

| Mode | How to enable | Use case |
|------|--------------|----------|
| Default | N/A | All writes/commands need approval |
| `--allowedTools` | `--allowedTools "Edit,Bash(npm test)"` | Pre-approve specific tools |
| `--dangerously-skip-permissions` | CLI flag | **CI/CD and sandboxed environments only** |
| Settings file | `.claude/settings.json` with `"allow"` and `"deny"` arrays | Persistent project rules |

AllowedTools supports wildcards: `Bash(npm run *)` approves all npm scripts. Configure persistently via `claude config` or in `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": ["Edit", "Bash(git *)", "Bash(npm test)"],
    "deny": ["Bash(rm -rf *)"]
  }
}
```

### Safety guardrails
Claude Code detects potentially destructive commands (`rm -rf`, production database operations) and adds extra warnings. Commands that could exfiltrate data are flagged. Permissions reset between sessions unless configured otherwise. When using `--dangerously-skip-permissions`, **Anthropic recommends running inside a Docker container or VM**.

---

## 7. Core feature set: what Claude Code can do

### File operations
Claude Code reads, creates, edits, and deletes files across the project. It performs **diff-based edits** showing proposed changes before applying, supports **multi-file editing** for coordinated refactors (e.g., renaming an import across dozens of files), and is syntax-aware across languages.

### Git integration
Deep git awareness is one of Claude Code's strongest differentiators. It understands current branch, staged changes, and commit history. It can create commits with descriptive messages, manage branches, resolve merge conflicts, generate PR descriptions, and review PRs via `/pr-review`. It reads git log and diff for context.

### Project understanding
Claude Code does **not** pre-build a static index. Instead, it explores on demand — reading `package.json`, traversing file trees, and using `grep`/`ripgrep` for code search. CLAUDE.md files augment this with human-curated architectural knowledge.

### Terminal command execution
With permission, Claude Code runs arbitrary shell commands, sees stdout/stderr, and reacts to output. It excels at **iterative test-fix cycles**: run test → analyze failure → fix code → re-run, continuing until green.

### Extended thinking
Claude Code leverages Claude's extended thinking capability automatically for complex reasoning. Users report that prompting for deeper analysis ("think step by step about the architecture before writing code") produces markedly better results for non-trivial tasks.

### Image and screenshot analysis
Leveraging Claude's vision capabilities, Claude Code can analyze images pasted into the terminal, read screenshots for UI debugging, and process referenced images.

### Headless / CI mode
`claude -p "prompt"` runs in non-interactive mode — ideal for CI/CD pipelines, GitHub Actions, and scripting. Combine with `--output-format json` for structured output and `--max-turns` to limit agentic loops.

---

## 8. MCP (Model Context Protocol) integration

### What MCP is
MCP is an **open protocol created by Anthropic** (announced November 2024) that standardizes how AI applications connect to external tools and data sources. It follows a client-server architecture similar to LSP for IDEs. The specification is maintained at `https://spec.modelcontextprotocol.io` with a significant update released on **2025-03-26** adding Streamable HTTP transport, JSON-RPC batching, structured tool output, and OAuth 2.1 authorization.

### Configuring MCP servers in Claude Code
MCP servers are configured in JSON settings files at two levels:

**Project-level** (shared): `.claude/settings.json`
**Project-local** (personal): `.claude/settings.local.json`
**Global** (user-wide): `~/.claude/settings.json`

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "ghp_xxx" }
    }
  }
}
```

**CLI management**: `claude mcp add <name> -- <command> [args]`, `claude mcp remove <name>`, `claude mcp list`. Use `--scope project` or `--scope user` to control where config is stored.

### Most commonly used MCP servers

| Server | Package | Purpose |
|--------|---------|---------|
| **Filesystem** | `@modelcontextprotocol/server-filesystem` | Broad file access patterns |
| **GitHub** | `@modelcontextprotocol/server-github` | PR, issue, and repo management |
| **PostgreSQL** | `@modelcontextprotocol/server-postgres` | Schema inspection, query execution |
| **SQLite** | `@modelcontextprotocol/server-sqlite` | Local database operations |
| **Puppeteer** | `@modelcontextprotocol/server-puppeteer` | Browser automation and screenshots |
| **Brave Search** | `@modelcontextprotocol/server-brave-search` | Web search integration |
| **Slack** | `@modelcontextprotocol/server-slack` | Workspace messaging and search |
| **Memory** | `@modelcontextprotocol/server-memory` | Persistent knowledge graph across sessions |
| **Git** | `@modelcontextprotocol/server-git` | Advanced git operations |
| **Fetch** | `@modelcontextprotocol/server-fetch` | Web content fetching |
| **Sequential Thinking** | `@modelcontextprotocol/server-sequential-thinking` | Complex multi-step reasoning |
| **Figma** | Figma's official MCP server | Design-to-code workflows |

The Figma MCP server is particularly notable — as of February 2026, Figma actively promotes it for "Claude Skills" that "guide coding agents through Figma workflows — from connecting code components and generating design system rules to implementing designs." A curated list of hundreds of community MCP servers is maintained at `https://github.com/punkpeye/awesome-mcp-servers`.

---

## 9. Community-reported tips, pitfalls, and workflows

### The five most consistent tips from experienced users

**1. Invest heavily in CLAUDE.md.** The single most-repeated recommendation across Reddit's r/ClaudeAI. Users report "night and day" quality differences with a well-crafted project context file including build commands, conventions, architecture, and explicit anti-patterns.

**2. Break tasks into focused, single-purpose requests.** Don't ask Claude Code to "build an entire feature." Instead decompose: (1) create the data model, (2) write the API endpoint, (3) build the frontend component, (4) add tests. One concern per prompt consistently outperforms monolithic requests.

**3. Ask Claude to plan before executing.** The most popular workflow pattern: "Before writing any code, outline the steps needed to implement [feature]." Review the plan, adjust, then execute step-by-step. This dramatically reduces wasted iterations.

**4. Commit frequently and use branches.** Run Claude Code on feature branches. Commit between sessions for easy rollback. Review diffs with `git add -p` before committing. Never blindly accept all changes.

**5. Use `/compact` proactively.** Context degradation after ~20-30 exchanges is consistently reported. Using `/compact` (optionally with focus instructions like `/compact focus on the database migration work`) maintains quality in extended sessions.

### The five most common pitfalls

**1. The "rewrite everything" problem.** Asking Claude to "refactor this file" without constraints leads to far more changes than intended. Be specific: "Refactor only the `processPayment` function to use async/await."

**2. Context window overload.** Loading too many files or running very long conversations degrades output quality. Start fresh sessions for unrelated tasks.

**3. Silent removal of defensive code.** Claude may remove error handling, logging, or edge-case guards when "cleaning up." Always review removed lines in diffs.

**4. Over-relying on Claude for architecture.** Community consensus: Claude is excellent at implementation but makes questionable high-level design choices. Make architectural decisions yourself, then use Claude to implement them.

**5. Not using .claudeignore.** Without it, Claude Code may index `node_modules`, build artifacts, or large data files, causing confusion and slow startup.

---

## 10. Prompt patterns for different task types

### Feature building
```
I need to add [feature description] to [project area].
Requirements:
1. [Specific requirement]
2. [Specific requirement]
Follow the patterns in [existing similar file].
The data model should go in [specific file].
Include unit tests.
```

### Debugging
```
I'm seeing [error message] when [specific action].
Expected: [what should happen]
Actual: [what happens]
Relevant files: [file1], [file2]
I've already tried [previous attempts].
Diagnose the root cause and suggest a fix.
```

### Refactoring
```
Refactor [specific function] in [file] to:
- [Specific change, e.g., "extract validation into a separate function"]
- [Specific change, e.g., "replace callbacks with async/await"]
Do NOT change: the function signature, existing test assertions, or other files.
Preserve all error handling and logging.
```

### Test writing
```
Write tests for [function/module] in [file].
Cover: happy path, edge cases, error cases.
Use [framework] with [patterns, e.g., "Jest describe/it blocks"].
Mock [external deps] using [approach].
Follow testing patterns in [existing test file].
```

---

## 11. Configuration files and environment variables

### Configuration hierarchy
1. **Global**: `~/.claude/settings.json` — user-wide preferences
2. **Project shared**: `.claude/settings.json` — version controlled, team config
3. **Project local**: `.claude/settings.local.json` — gitignored, personal overrides
4. **Enterprise**: Managed via Anthropic admin controls

### Key environment variables

| Variable | Purpose |
|----------|---------|
| `ANTHROPIC_API_KEY` | API key authentication |
| `CLAUDE_MODEL` / `ANTHROPIC_MODEL` | Override default model |
| `CLAUDE_CODE_MAX_TURNS` | Limit turns in non-interactive mode |
| `ANTHROPIC_BASE_URL` | Custom API endpoint (proxies, enterprise) |
| `DISABLE_AUTOUPDATER` | Disable auto-updates |
| `MCP_TIMEOUT` | Timeout for MCP server connections |

---

## 12. Claude Code SDK for programmatic use

Claude Code provides a **TypeScript/JavaScript SDK** for programmatic embedding:

```typescript
import { claude } from '@anthropic-ai/claude-code';

const result = await claude({
  prompt: "Fix the type errors in src/index.ts",
  options: {
    maxTurns: 10,
    allowedTools: ["Edit", "Bash", "Read"],
    cwd: "/path/to/project"
  }
});
```

The SDK supports conversation management, tool control, streaming responses, abort control, custom system prompts, and JSON structured output. This enables **multi-agent patterns** where an orchestrator Claude Code instance delegates subtasks to worker instances running in parallel — each with its own conversation context and tool permissions.

---

## 13. Real-world projects and successful use cases

Based on community reports across Reddit and YouTube, Claude Code has been successfully used for: **full-stack web applications** (React/Next.js frontends with Python/Node backends), **CLI tools** with argument parsing and help text, **REST and GraphQL APIs** with validation and documentation, **database migrations**, **comprehensive test suites** for existing codebases, **documentation generation**, **legacy code refactoring** (JavaScript → TypeScript, callbacks → async/await), **DevOps** (Dockerfiles, CI/CD configs, infrastructure-as-code), **Chrome extensions** (Manifest V3), and **mobile apps** via React Native/Expo.

The "vibe coding" phenomenon — using Claude Code to rapidly prototype ideas through natural-language conversation — has become culturally significant enough that Pendo.io described Claude as "the viral vibe coding tool" in February 2026.

---

## 14. Technical context for the current ecosystem

### Web framework versions to target

| Framework | Current version | Key notes |
|-----------|----------------|-----------|
| **Next.js** | 15.x | App Router is the default; requires React 19; Turbopack stable for dev |
| **React** | 19.x | Server Components, Actions, `use()` hook, `useOptimistic` |
| **Vue.js** | 3.5–3.6 | Composition API standard; Pinia for state; Nuxt 3 as meta-framework |
| **Svelte** | 5.x | Runes (`$state`, `$derived`, `$effect`) — major paradigm shift from v4 |
| **SvelteKit** | 2.x | File-based routing, SSR/SSG, adapter-based deployment |
| **Express** | 4.21.x / 5.x | Express 5 adds async error handling |
| **FastAPI** | 0.115+ | Pydantic v2 integration, async-first |
| **Django** | 5.1.x / 5.2 LTS | Progressive async ORM support |

### Mobile development

**React Native** 0.76+ has the **New Architecture enabled by default** (Fabric, TurboModules, Bridgeless mode). **Expo SDK 52–53** makes Expo Router and EAS (Build, Submit, Update) standard. **Flutter** 3.27+ uses Impeller rendering engine by default on iOS and Android with stable web/desktop support.

### Browser extensions
**Manifest V3 is now mandatory** for Chrome Web Store. MV2 extensions were removed in 2025. Key pattern: service workers replace background pages (terminated after ~30s inactivity — use `chrome.alarms` for periodic tasks), `chrome.declarativeNetRequest` replaces blocking `webRequest`, and `chrome.sidePanel` enables sidebar UIs.

### Deployment platforms
**Vercel** (`npm i -g vercel`) remains the default for Next.js with zero-config deployment. **Netlify** (`npm i -g netlify-cli`) offers Edge Functions and Forms. **Railway** (`npm i -g @railway/cli`) provides Nixpacks-based builds with built-in databases. **Fly.io** (`flyctl`) deploys Docker containers globally via Firecracker microVMs. **AWS Amplify Gen 2** uses a code-first TypeScript DX.

### Data visualization
**D3.js** 7.9.x (low-level, composable; Observable Plot gaining popularity as higher-level alternative), **Chart.js** 4.4.x (canvas-based, tree-shakeable), **Recharts** 2.13–2.14 (React-native, built on D3), **Plotly.js** 2.35+ (interactive, 3D, statistical charts).

---

## 15. YouTube creators and tutorial landscape

The Claude Code tutorial ecosystem is robust. Key creators include **Fireship** (concise explainers), **Theo/t3.gg** (web dev opinions and comparisons), **IndyDevDan** (deep technical demos), **Cole Medin** (MCP-focused tutorials), **AI Jason** (practical tutorials), and **NetworkChuck** (beginner-friendly guides). The most common comparison topic is **Claude Code vs. Cursor** — community consensus positions Claude Code as stronger for terminal-native workflows, large-scale refactoring, and agentic multi-step tasks, while Cursor excels at inline editing UX, visual diffs, and lower friction for small edits. Many power users report using both depending on task type.

**Recommended search queries** for finding the latest tutorials: `"Claude Code tutorial 2026" site:youtube.com`, `"Claude Code workflow" site:youtube.com`, `"Claude Code MCP" site:youtube.com`, `"Claude Code vs Cursor" site:youtube.com`.

---

## Conclusion: what this brief reveals for manual authors

Claude Code has matured from a February 2025 research preview into a **$500M+ revenue product** that enterprises actively procure at $100/month per developer. The tool's power lies not in any single feature but in the **agentic loop** — read files, reason, make changes, verify via tests, iterate — combined with extensibility through MCP servers and the CLAUDE.md convention.

Three insights stand out for manual construction. First, **CLAUDE.md is the highest-leverage topic to teach well** — it's the single intervention that most improves output quality, yet most beginners skip it. Second, the **permission model deserves dedicated coverage** because the spectrum from interactive approval to `--dangerously-skip-permissions` in CI/CD represents fundamentally different trust levels that beginners must understand. Third, **MCP is the gateway to advanced workflows** — connecting Claude Code to databases, browsers, GitHub, Figma, and custom tools transforms it from a coding assistant into an orchestration platform. The ecosystem of MCP servers has grown to hundreds by early 2026, and Figma's official MCP server exemplifies how major design tools are building native Claude Code integration paths.

The manual should progress from installation → first interactive session → CLAUDE.md setup → prompt patterns → permission configuration → git workflows → MCP integration → CI/CD automation → SDK/multi-agent patterns, mirroring the natural progression from beginner to power user.