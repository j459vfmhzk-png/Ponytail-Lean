#!/usr/bin/env python3
"""Analyze a normalized, privacy-safe LeanTail CSV; never runs Claude or sends data."""
import argparse
import csv
from collections import defaultdict
from statistics import mean, median

NUMS = ('total_tokens', 'cost_usd', 'elapsed_s')
VALID = {'baseline', 'ponytail_skill', 'leantail'}

def yes(v):
    return str(v).strip().lower() in {'1', 'true', 'yes', 'pass'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('csv_file', help='Normalized runs CSV (private source file; no data upload)')
    args=p.parse_args()
    with open(args.csv_file, newline='', encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    if not rows:
        raise SystemExit('No run rows; benchmark has not been executed.')
    if any(r.get('condition') not in VALID for r in rows):
        raise SystemExit('Invalid condition. Expected baseline / ponytail_skill / leantail.')
    group=defaultdict(list)
    for r in rows:
        try:
            for key in NUMS: r[key]=float(r[key])
        except (ValueError, TypeError) as ex:
            raise SystemExit(f'Missing/invalid numeric data in row {r}: {ex}')
        if r['total_tokens'] < 0 or r['cost_usd'] < 0 or r['elapsed_s'] < 0:
            raise SystemExit('Negative metrics are not valid.')
        group[r['condition']].append(r)
    print('Results are descriptive; not a significance test.\n')
    for condition in ('baseline', 'ponytail_skill', 'leantail'):
        rr=group[condition]
        if not rr: continue
        successful=[r for r in rr if yes(r['passed']) and yes(r['security_passed']) and not yes(r['timeout'])]
        rate=len(successful)/len(rr)
        mean_success_tokens=round(mean(r['total_tokens'] for r in successful)) if successful else None
        mean_success_cost=(sum(r['cost_usd'] for r in rr)/len(successful)) if successful else None
        print(f'{condition}: runs={len(rr)} verified_success={len(successful)} success_rate={rate:.1%} '
              f'mean_tokens_on_success={mean_success_tokens} '
              f'total_cost_per_verified_success={mean_success_cost:.4f}' if mean_success_cost is not None
              else f'{condition}: runs={len(rr)} verified_success=0 (no cost/token efficiency claim possible)')
    by_task=defaultdict(dict)
    for condition,rr in group.items():
        for task in sorted({r['task_id'] for r in rr}):
            completed=[r['total_tokens'] for r in rr if r['task_id']==task and yes(r['passed']) and yes(r['security_passed']) and not yes(r['timeout'])]
            if completed: by_task[task][condition]=mean(completed)
    diffs=[]
    print('\nPer-task token changes, successful runs only (NOT adjusted for different success rates):')
    for task in sorted(by_task):
        if {'baseline','leantail'} <= by_task[task].keys():
            b=by_task[task]['baseline']; l=by_task[task]['leantail']
            if b>0:
                improvement=(b-l)/b*100
                diffs.append(improvement)
                print(f'{task}: LeanTail vs baseline: {improvement:+.1f}% fewer tokens')
    if diffs: print(f'Median task-level token reduction: {median(diffs):+.1f}% (descriptive only)')
    print('\nAlways publish counts of failures, cost and security failures alongside token results.')

if __name__=='__main__': main()
