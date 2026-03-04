# Deployment FAQ

## Q: How should we deploy AI services?
A: Use staged environments (dev, staging, prod) with automated tests and progressive rollout.

## Q: What is needed before production release?
A: Passing quality gates, security review, performance checks, and rollback readiness.

## Q: How do we handle rollback?
A: Keep previous model/prompt/version artifacts and route traffic back via feature flags.

## Q: How do we manage prompt/version changes?
A: Version prompts and configs in Git with change history and approval workflow.

## Q: How is cost controlled after deployment?
A: Use model routing, caching, token budgets, and workload-based autoscaling.
