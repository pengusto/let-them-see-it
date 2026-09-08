# Let Them See It

[English](README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Agent-Skill](https://img.shields.io/badge/type-agent%20skill-blue)](SKILL.md)

Bereite ein Repository auf die öffentliche Veröffentlichung bei GitHub vor: prüfen, konkrete Verbesserungen vorschlagen und die freigegebenen Änderungen umsetzen.

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Ablauf

1. Dokumentation, Repository-Ordnung, sensible Inhalte, Lizenzierung und sinnvolle Checks prüfen, ohne Dateien zu ändern.
2. Einen priorisierten Plan mit Belegen und Abnahmekriterien vorlegen. Du bestätigst oder änderst den Umfang.
3. Die abgestimmten Änderungen umsetzen und berichten, was geprüft wurde, was offenbleibt und ob veröffentlicht wurde.

Der Skill schlägt READMEs auf Englisch, Deutsch, vereinfachtem Chinesisch und Japanisch vor. Badges, Konfigurationsbeispiele, Community-Dateien und CI ergänzt er nur, wenn sie dem Projekt helfen. Die Veröffentlichung benötigt einen Auftrag und ist von der Vorbereitung getrennt.

## Installation und Nutzung

Du benötigst Git und einen Agenten, der `SKILL.md`-Skills unterstützt. Für eine Standardinstallation von Codex klonst du in ein noch nicht belegtes Skill-Verzeichnis:

```sh
git clone https://github.com/pengusto/let-them-see-it.git ~/.codex/skills/let-them-see-it
```

Bei einem eigenen Skill-Verzeichnis klonst du stattdessen dorthin. Starte eine neue Agentensitzung, falls der Skill noch nicht erscheint, und verwende:

```text
Prüfe mit $let-them-see-it dieses Repository auf Veröffentlichungsreife.
Zeige mir die vorgeschlagenen Änderungen, bevor du Dateien bearbeitest.
```

Gib nach der Prüfung die gewünschten Punkte frei. Der Skill selbst benötigt keine Laufzeitpakete oder API-Schlüssel. GitHub-Zugriff und weitere Projektwerkzeuge sind nur für entsprechende Aktionen erforderlich.

## Umfang und Grenzen

Dies ist ein anweisungsbasierter Skill, keine automatische Sicherheitszertifizierung. Verfügbare Scanner und Agentenverhalten unterscheiden sich. Der Skill muss ungeprüfte Punkte melden und darf keine Secret-Werte ausgeben. Unklare Lizenz- und Nutzungsrechte benötigen eine Entscheidung der betreuenden Person. Die Übersetzungen stammen von KI und wurden nicht unabhängig sprachlich geprüft.

[SKILL.md](SKILL.md) beschreibt den Ablauf; [TESTING.md](TESTING.md) enthält wiederholbare Verhaltenstests.

## Mitmachen

Eröffne ein Issue mit beobachtetem und erwartetem Verhalten oder einen fokussierten Pull Request. Halte die vier READMEs inhaltlich synchron. Teile keine Zugangsdaten oder privaten Repository-Inhalte in Berichten.

## Lizenz

[MIT](LICENSE) © 2026 Pengusto.
