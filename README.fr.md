# Let Them See It

[English](README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

[![Agent skill](https://img.shields.io/badge/type-agent%20skill-blue)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Préparez un dépôt pour sa publication sur GitHub : examinez son état, obtenez des propositions concrètes et faites appliquer les changements que vous approuvez.

## Fonctionnement

1. Examiner la documentation, l'organisation du dépôt, les données sensibles, les licences et les vérifications utiles sans modifier les fichiers.
2. Présenter un plan par priorité, avec des preuves et des critères de validation. Vous approuvez ou ajustez le périmètre.
3. Appliquer les changements convenus et indiquer les vérifications effectuées, les points ouverts et si la publication a eu lieu.

Les langues par défaut du README sont l'anglais, l'allemand, le chinois simplifié, le japonais, l'espagnol, le coréen, le portugais du Brésil et le français. Avant toute modification, le skill énumère les langues et les fichiers prévus pour vous permettre d'ajuster la sélection. Il vérifie la cohérence des traductions et, lorsque c'est possible, le démarrage rapide depuis un nouveau clone. Les propositions dépendent du type de projet et comprennent la clarification de son état de maintenance ; une image d'aperçu pour les réseaux sociaux reste facultative. Badges, exemples de configuration, fichiers communautaires et CI sont ajoutés lorsqu'ils servent le projet. Publier nécessite une autorisation distincte de la préparation.

Il peut aussi évaluer GitHub Sponsors, Discussions, Releases, `CITATION.cff`, les sujets, l'aperçu social et le trafic Insights. Il recommande seulement les fonctions adaptées, ne promet pas la viralité et ne publie rien à l'extérieur.

## Installation et utilisation

Vous avez besoin de Git et d'un agent prenant en charge les skills au format `SKILL.md`. Pour la configuration par défaut de Codex, clonez dans un répertoire de skills qui n'existe pas encore :

```sh
git clone https://github.com/pengusto/let-them-see-it.git ~/.codex/skills/let-them-see-it
```

Si vous utilisez un emplacement personnalisé, clonez-y le dépôt. Démarrez une nouvelle session si le skill n'apparaît pas, puis demandez :

```text
Utilise $let-them-see-it pour évaluer si ce dépôt est prêt à être publié.
Montre-moi les modifications proposées avant de modifier les fichiers.
```

Après examen du plan, approuvez les points souhaités. Le skill lui-même ne nécessite ni paquet d'exécution ni clé API. L'accès à GitHub et les outils du projet ne sont nécessaires que pour les actions qui les utilisent.

## Portée et limites

Ce skill repose sur des instructions ; il ne fournit pas de certification automatique de sécurité. Les scanners disponibles et le comportement de l'agent varient. Il doit signaler les vérifications non effectuées et ne pas afficher de secrets. Les incertitudes sur les licences et les droits des ressources nécessitent une décision du responsable. Les traductions proviennent de l'IA et n'ont pas fait l'objet d'une révision linguistique indépendante.

Consultez [SKILL.md](SKILL.md) pour la procédure et [TESTING.md](TESTING.md) pour les vérifications de comportement reproductibles.

## Contribuer

Ouvrez une issue avec le comportement observé et le résultat attendu, ou une pull request ciblée. Gardez les huit README cohérents. N'incluez pas d'identifiants ni de contenu de dépôts privés dans les rapports.

## Licence

[MIT](LICENSE) © 2026 Pengusto.
