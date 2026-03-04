# Code Review and Defect Fixing FAQ

## Q: What is the recommended Git workflow?
A: Use short-lived feature branches, pull requests, and mandatory status checks before merge.

## Q: How are defects resolved safely?
A: Reproduce the bug, write a failing test, apply minimal fix, and validate with regression tests.

## Q: What should be in a good PR?
A: Problem statement, root cause, fix summary, test evidence, and rollback considerations.

## Q: How are high-severity bugs handled?
A: Prioritize hotfix branch, involve incident owner, and perform expedited but reviewed release.

## Q: What checks should block merges?
A: Unit tests, lint, security scan, and code owner approval.
