<!-- page-journey: all -->
<!-- page-adventure: side-quest -->
# Side Quest: Environment Reference

> _Optional: quick glossary and visual reference for workshop tools and environments._

**What you'll learn:** Name each tool, match it to its role, and know when you use it.

## :clipboard: Before You Start

Reference page — read anytime. Return here when a term needs clarification. No terminal required to read.

When ready to verify, see the [Checkpoint](#white_check_mark-checkpoint) section at the bottom.

## Environment and tool glossary

| Term | Role / When to use |
|------|-------------------|
| **GitHub Codespaces** | Cloud dev environment, browser-based setup. Steps 2–14. |
| **Visual Studio Code (VS Code)** | Editor inside Codespaces or locally. Edit workflows, read output. |
| **Terminal (command line)** | Shell for `gh`, `gh aw`, `git`. Any `bash` step. |
| **GitHub CLI (`gh`)** | GitHub's official CLI. Pre-installed in Codespace. Step 6 onward. |
| **`gh-aw` CLI extension** | Compile agentic workflow files. Step 6 onward. |
| **GitHub Copilot CLI** | AI-assisted help in the terminal. Any `prompt` step. |
| **GitHub Copilot app** | Desktop/web app for repos, agent sessions, PRs. Optional. |
| **Claude** | AI model option in Copilot/agentic workflows. Non-default steps. |
| **OpenAI Codex** | Coding-focused model option. Non-default steps. |

**Docs:** [Codespaces](https://docs.github.com/en/codespaces) • [VS Code](https://code.visualstudio.com/docs) • [GitHub CLI](https://cli.github.com/manual/) • [`gh-aw`](https://github.com/github/gh-aw#readme) • [Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli) • [Copilot app](https://github.com/features/ai/github-app) • [Claude](https://docs.anthropic.com/) • [OpenAI Codex](https://github.com/openai/codex#readme)

> [!NOTE]
> **GitHub Enterprise (GHES/GHEC) users**: same tools/commands apply. Codespace URL uses your enterprise hostname. Self-hosted runners: `gh aw compile` runs locally. See [Step 6](06-install-gh-aw.md).

> [!TIP]
> **Quick check:** Without looking, which tool compiles agentic workflow files? *(Answer: `gh aw`)*

### :white_check_mark: Verify your tools are ready

Open a terminal in your Codespace and run: