# LeanTail installeren en testen

Deze openbare repository is: https://github.com/j459vfmhzk-png/Ponytail-Lean

## Lokale tests

1. Gebruik een testcomputer en uitsluitend fictieve of openbare data.
2. Controleer dat Python 3 en Claude Code zijn geïnstalleerd.
3. Clone de repository en open een terminal in de projectmap.
4. Draai: `python3 tools/verify_plugin.py`.
5. Draai: `claude plugin validate ./plugins/leantail` en `claude plugin validate .`.
6. Test: `claude --plugin-dir ./plugins/leantail` en gebruik `/leantail:lean`.
7. Controleer dat Claude Code zelf communiceert met de modelprovider; de skill is geen volledige beveiligingslaag.

## Installatie uit GitHub

Binnen Claude Code:

```text
/plugin marketplace add j459vfmhzk-png/Ponytail-Lean
/plugin install leantail@leantail-marketplace
```

Start daarna een testopdracht met `/leantail:lean`.

## Naam en eigendom

LeanTail is een zelfstandig project, geïnspireerd op Ponytail van Dietrich Gebert, en wordt niet door de oorspronkelijke ontwikkelaar of Anthropic ondersteund. Zie NOTICE.md en LICENSE.
