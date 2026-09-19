# Let Them See It

[English](README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

[![Agent skill](https://img.shields.io/badge/type-agent%20skill-blue)](SKILL.md)

Prepare a repository for public GitHub release: inspect it, propose specific improvements, and implement the changes you approve.

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## How it works

1. Evaluate documentation, repository hygiene, sensitive content, licensing, and useful checks without editing files.
2. Present a prioritized plan with evidence and acceptance checks. You approve or adjust the scope.
3. Implement the agreed changes and report what was verified, what remains open, and whether publication happened.

The default README languages are English, German, Simplified Chinese, Japanese, Spanish, Korean, Brazilian Portuguese, and French. Before editing, the skill lists the planned languages and filenames so you can adjust the selection. It checks translation consistency and, where feasible, the quickstart from a fresh clone. Proposals depend on the project type and include clarifying maintenance status; a social-preview image is optional. It adds badges, configuration examples, community files, and CI only when they help the project. Publishing requires authorization; it is separate from preparation.

It can also evaluate GitHub Sponsors, Discussions, Releases, `CITATION.cff`, topics, social preview, and Insights traffic. It recommends only surfaces that fit the project and does not promise virality or post externally.

## Install and use

You need Git and an agent that supports `SKILL.md` skills. For a default Codex setup, install into an unused skill directory:

```sh
git clone https://github.com/pengusto/let-them-see-it.git ~/.codex/skills/let-them-see-it
```

If you use a custom skill location, clone there instead. Start a new agent session if the skill is not yet listed, then ask:

```text
Use $let-them-see-it to evaluate this repository for public release.
Show me the proposed changes before editing anything.
```

After reviewing the plan, approve the items you want. No runtime packages or API keys are required by the skill itself. GitHub access and additional project tools are needed only for actions that use them.

## Scope and limitations

This is an instruction-based skill, not an automated security certification. Scanner availability and agent behavior vary. It must report unverified checks and must not expose secret values. License and asset-rights uncertainties need a maintainer decision. Translations are AI-produced and have not received independent fluent review.

See [SKILL.md](SKILL.md) for the workflow and [TESTING.md](TESTING.md) for repeatable behavioral checks.

## Contributing

Open an issue with the observed behavior and expected result, or a focused pull request. Keep all eight READMEs aligned. Do not include credentials or private repository content in reports.

## License

[MIT](LICENSE) © 2026 Pengusto.
