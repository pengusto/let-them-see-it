# Let Them See It

[English](README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

[![智能体技能](https://img.shields.io/badge/type-agent%20skill-blue)](SKILL.md)

为 GitHub 仓库的公开发布做好准备：检查项目、提出具体改进建议，并实施你批准的修改。

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 工作流程

1. 检查文档、仓库整洁度、敏感内容、许可证和适用的验证步骤，不修改文件。
2. 提交按优先级排序的计划，附上依据和验收方法。由你确认或调整范围。
3. 实施已批准的修改，说明验证结果、待处理事项以及是否已经发布。

默认 README 语言为英语、德语、简体中文、日语、西班牙语、韩语、巴西葡萄牙语和法语。修改前，技能会列出计划使用的语言和文件名，供你调整。它会检查翻译内容的一致性，并在可行时从全新克隆验证快速入门步骤。建议根据项目类型制定，并包括明确维护状态；社交分享预览图为可选项。只有在对项目有帮助时，才添加徽章、配置示例、社区文件和 CI。发布需要授权，与准备工作分开处理。

## 安装与使用

你需要 Git，以及支持 `SKILL.md` 技能的智能体。对于默认的 Codex 配置，请克隆到尚未使用的技能目录：

```sh
git clone https://github.com/pengusto/let-them-see-it.git ~/.codex/skills/let-them-see-it
```

如果你使用自定义技能目录，请改为克隆到该目录。若技能尚未显示，请启动新的智能体会话，然后输入：

```text
使用 $let-them-see-it 评估此仓库是否适合公开发布。
在修改任何文件之前，先向我展示建议的改动。
```

审阅计划后，批准需要实施的项目。技能本身不需要运行时软件包或 API 密钥。只有执行相关操作时，才需要 GitHub 访问权限和其他项目工具。

## 范围与限制

这是基于指令的技能，不是自动安全认证。可用的扫描器和智能体行为可能不同。它必须说明未验证的检查项，且不得输出密钥值。许可证和素材使用权不明确时，需要维护者作出决定。翻译由 AI 生成，尚未经过独立的语言审核。

工作流程见 [SKILL.md](SKILL.md)，可重复执行的行为测试见 [TESTING.md](TESTING.md)。

## 参与贡献

请提交包含实际行为和预期结果的 Issue，或范围明确的 Pull Request。保持八种语言的 README 内容一致。请勿在报告中包含凭据或私有仓库内容。

## 许可证

[MIT](LICENSE) © 2026 Pengusto。
