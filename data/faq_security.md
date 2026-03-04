# Security FAQ

## Q: How is data encrypted?
A: Data is encrypted in transit using TLS 1.2+ and encrypted at rest using AES-256.

## Q: How are secrets managed?
A: Secrets are stored in a centralized secret manager and rotated on a scheduled cadence.

## Q: How is access controlled?
A: Access is controlled using RBAC with environment-level separation and audited admin actions.

## Q: Do you store customer prompts for training?
A: By default, customer prompts are not used for model training unless explicitly opted in.

## Q: How is sensitive data handled in logs?
A: Logs are redacted for PII and secrets before storage.
