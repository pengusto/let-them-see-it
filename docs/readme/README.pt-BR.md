# Let Them See It

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

[![Agent skill](https://img.shields.io/badge/type-agent%20skill-blue)](../../SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](../../LICENSE)

Prepare um repositório para publicação no GitHub: examine o estado atual, receba propostas de melhorias e implemente as mudanças que você aprovar.

## Como funciona

1. Avalia a documentação, a organização e a estrutura do repositório, o conteúdo sensível, as licenças e as verificações úteis sem alterar arquivos.
2. Apresenta um plano por prioridade, com evidências e critérios de aceitação. Você aprova ou ajusta o escopo.
3. Implementa as mudanças combinadas e informa o que foi verificado, o que está pendente e se houve publicação.

Os idiomas padrão do README são inglês, alemão, chinês simplificado, japonês, espanhol, coreano, português do Brasil e francês. O README em inglês fica na raiz; as traduções usam `docs/readme/`, salvo outra convenção do projeto. Antes de editar, o skill lista os idiomas e caminhos previstos. Ele verifica a consistência das traduções e, quando possível, o início rápido a partir de um clone novo. Também avalia a desorganização da raiz usando os caminhos reais de execução, build, testes e empacotamento, sem impor uma árvore genérica. As propostas dependem do tipo de projeto e incluem esclarecer o estado de manutenção; uma imagem de prévia para redes sociais é opcional. Badges, exemplos de configuração, arquivos da comunidade e CI são adicionados quando ajudam o projeto. Publicar exige autorização e é uma ação separada da preparação.

Também pode avaliar GitHub Sponsors, Discussions, Releases, `CITATION.cff`, tópicos, prévia social e tráfego do Insights. Recomenda apenas recursos adequados, não promete viralização e não publica externamente.

## Instalação e uso

Você precisa do Git e de um agente compatível com skills no formato `SKILL.md`. Na configuração padrão do Codex, clone em um diretório de skills que ainda não exista:

```sh
git clone https://github.com/pengusto/let-them-see-it.git ~/.codex/skills/let-them-see-it
```

Se usar um local personalizado, clone nele. Inicie uma nova sessão do agente se o skill ainda não aparecer e peça:

```text
Use $let-them-see-it para avaliar se este repositório está pronto para publicação.
Mostre as mudanças propostas antes de editar qualquer arquivo.
```

Depois de revisar o plano, aprove os itens desejados. O skill em si não exige pacotes de execução nem chaves de API. O acesso ao GitHub e outras ferramentas do projeto só são necessários para as ações que os utilizam.

## Escopo e limitações

Este é um skill baseado em instruções, não uma certificação automática de segurança. Os scanners disponíveis e o comportamento do agente variam. Ele deve informar as verificações não realizadas e não exibir valores secretos. Dúvidas sobre licenças e direitos de recursos exigem uma decisão do responsável. As traduções foram geradas por IA e não passaram por revisão linguística independente.

Veja o fluxo em [SKILL.md](../../SKILL.md) e as verificações de comportamento repetíveis em [TESTING.md](../../TESTING.md).

## Contribuir

Abra uma issue com o comportamento observado e o esperado, ou um pull request com escopo definido. Mantenha os oito READMEs alinhados. Não inclua credenciais nem conteúdo de repositórios privados nos relatos.

## Licença

[MIT](../../LICENSE) © 2026 Pengusto.
