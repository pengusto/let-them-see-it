# Let Them See It

[English](README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

[![Agent skill](https://img.shields.io/badge/type-agent%20skill-blue)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Prepara un repositorio para publicarlo en GitHub: revisa su estado, propone mejoras concretas e implementa los cambios que apruebes.

## Cómo funciona

1. Revisa la documentación, el orden del repositorio, el contenido sensible, las licencias y las comprobaciones útiles sin modificar archivos.
2. Presenta un plan priorizado con evidencias y criterios de aceptación. Tú apruebas o ajustas el alcance.
3. Implementa los cambios acordados e informa de lo verificado, lo pendiente y si se ha publicado.

Los idiomas predeterminados del README son inglés, alemán, chino simplificado, japonés, español, coreano, portugués de Brasil y francés. Antes de editar, el skill enumera los idiomas y archivos previstos para que puedas ajustar la selección. Comprueba la coherencia de las traducciones y, cuando es posible, el inicio rápido desde un clon nuevo. Adapta las propuestas al tipo de proyecto y aclara su estado de mantenimiento; una imagen de vista previa para redes sociales es opcional. Añade insignias, ejemplos de configuración, archivos de comunidad y CI cuando ayudan al proyecto. Publicar requiere autorización y es una acción distinta de preparar.

También puede evaluar GitHub Sponsors, Discussions, Releases, `CITATION.cff`, temas, vista previa social y tráfico de Insights. Solo recomienda funciones adecuadas, no promete viralidad ni publica externamente.

## Instalación y uso

Necesitas Git y un agente compatible con skills en formato `SKILL.md`. Para la configuración predeterminada de Codex, clona en un directorio de skills que no exista todavía:

```sh
git clone https://github.com/pengusto/let-them-see-it.git ~/.codex/skills/let-them-see-it
```

Si usas una ubicación personalizada, clona allí. Inicia una nueva sesión del agente si el skill aún no aparece y pide:

```text
Usa $let-them-see-it para evaluar si este repositorio está listo para publicarse.
Muéstrame los cambios propuestos antes de editar archivos.
```

Tras revisar el plan, aprueba los puntos que quieras. El skill no requiere paquetes de ejecución ni claves API. El acceso a GitHub y otras herramientas del proyecto solo son necesarios para las acciones que los utilizan.

## Alcance y limitaciones

Es un skill basado en instrucciones, no una certificación automática de seguridad. Los escáneres disponibles y el comportamiento del agente varían. Debe informar de las comprobaciones pendientes y no mostrar valores secretos. Las dudas sobre licencias y derechos de los recursos requieren una decisión del responsable. Las traducciones son de IA y no han recibido una revisión lingüística independiente.

Consulta el flujo en [SKILL.md](SKILL.md) y las comprobaciones de comportamiento repetibles en [TESTING.md](TESTING.md).

## Contribuir

Abre un issue con el comportamiento observado y el esperado, o un pull request con cambios acotados. Mantén alineados los ocho README. No incluyas credenciales ni contenido de repositorios privados en los informes.

## Licencia

[MIT](LICENSE) © 2026 Pengusto.
