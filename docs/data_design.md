# Data Design

## Dataset Overview
Synthetic dataset simulating a Jira-like bug tracking system.

## Fields
- bug_id 
- created_at 
- closed_at 
- priority: Low / Medium / High / Critical 
- severity - Minor / Major / Critical / Blocker 
- component - Auth / Payments / Registration/ Obfuscation/ UI / Backend / Infra 
- assignee_id 
- labels: ui/backend/regression/performace/ 
- summary (not mandatory on it1) 
- description (not mandatory on it1) 

## Target Variable
Description of FAST / MEDIUM / SLOW derived from resolution time.
- FAST — bugs typically resolved quickly with minimal investigation
- MEDIUM — bugs requiring analysis or coordination but resolved within a reasonable time
- SLOW — bugs involving complex fixes, infrastructure, or long investigation cycles

## Assumptions and Dependencies
- Higher priority increases probability of FAST, but does not guarantee it
- assignee_1 — slow, medium quality
- assignee_2 — medium speed, low quality
- assignee_3 — fast, medium quality
- assignee_4 — fastest, high quality
- Blocker + Infra → rarely FAST
- Blocker + Infra → rarely FAST 
- Slowest - labeled "Performance"
- Backend tasks are slightly faster than "Performance"
- Other tasks are the fastest. 
- Multiple labels → higher probability of MEDIUM/SLOW

## Simplifications
- Changing priorities after creation
- Reopening
- Dependencies between bugs
- Human factor
- Emergencies - a crashed server, illness, etc.
- Sprints, releases, deadlines
