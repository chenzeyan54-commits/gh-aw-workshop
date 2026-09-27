<!-- page-journey: all -->
<!-- page-adventure: core -->
# GitHub Actions in 5 Minutes

<details>
<summary><b>Already know GitHub Actions?</b> Confirm these three statements and skip ahead:</summary>

- You know workflows live in `.github/workflows/` as YAML files
- You can read `on`, `jobs`, and `steps` keys in a workflow file
- You know each step runs on a GitHub-hosted runner

**→ [Skip to What Are Agentic Workflows?](05-agentic-workflows-intro.md)**
(or [jump to Install gh-aw](06-install-gh-aw.md) if you know both)

</details>

## :dart: What You'll Do

You'll do a fast refresher on the Actions primitives used in this workshop: [triggers](https://github.github.com/gh-aw/reference/triggers/), jobs, steps, and workflow files. After this step, you'll be able to read any classic GitHub Actions workflow file.

## :clipboard: Before You Start

- Practice repository is set up from a previous step.
- No tools or credentials needed for this step.

## Quick Refresher

A GitHub Actions workflow is a YAML file in `.github/workflows/` that tells GitHub:

- _when_ to run (`on`)
- _what_ to run (`jobs`)
- _how_ each job executes (`steps`)