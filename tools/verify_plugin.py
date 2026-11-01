#!/usr/bin/env python3
"""Offline structural checks; not a comprehensive security audit."""
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
PLUGIN=ROOT/'plugins'/'leantail'
EXPECTED={'.claude-plugin/plugin.json','skills/lean/SKILL.md'}

def fail(s):
    raise SystemExit('FAILED: '+s)

def main():
    if not PLUGIN.is_dir(): fail('Plugin directory missing')
    paths={p.relative_to(PLUGIN).as_posix() for p in PLUGIN.rglob('*') if p.is_file()}
    if paths != EXPECTED:
        fail(f'Plugin files differ from strict allowlist: actual {sorted(paths)}')
    for p in PLUGIN.rglob('*'):
        if p.is_symlink(): fail('Symbolic links not allowed in plugin')
    manifest=json.loads((PLUGIN/'.claude-plugin/plugin.json').read_text('utf-8'))
    if manifest.get('name')!='leantail': fail('Plugin name mismatch')
    forbidden={'hooks','mcpServers','lspServers','commands','agents','userConfig'}
    if forbidden.intersection(manifest): fail('Executable or external components declared in manifest')
    skill=(PLUGIN/'skills/lean/SKILL.md').read_text('utf-8')
    if not skill.startswith('---\n') or 'disable-model-invocation: true' not in skill:
        fail('Manual invocation setting missing')
    forbidden_skill_patterns=('!`', 'curl ', 'wget ', 'https://', 'http://', 'ANTHROPIC_API_KEY')
    for phrase in forbidden_skill_patterns:
        if phrase.lower() in skill.lower(): fail('Review suspicious instruction: '+phrase)
    marketplace=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text('utf-8'))
    entries=marketplace.get('plugins',[])
    if len(entries)!=1 or entries[0].get('name')!='leantail' or entries[0].get('source')!='./plugins/leantail':
        fail('Marketplace does not point to a single local plugin')
    print('PASS: Exactly two non-executable plugin files; no hook/MCP declaration; manual skill; local marketplace.')
    print('LIMITATION: Text-only checks cannot guarantee the safety of model behavior or provider data handling.')

if __name__=='__main__': main()
