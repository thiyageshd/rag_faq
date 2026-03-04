# Authentication FAQ

## Q: How do users sign in?
A: Users sign in with email and password. Enterprise customers can enable SSO using SAML or OIDC.

## Q: Is multi-factor authentication supported?
A: Yes. We support TOTP-based MFA and enforce MFA for admin roles.

## Q: How are sessions managed?
A: Access tokens are short-lived. Refresh tokens are rotated and invalidated on suspicious activity.

## Q: What happens after multiple failed logins?
A: Accounts are temporarily locked after repeated failed attempts. Security alerts are generated.

## Q: Can service accounts be used?
A: Yes. Service accounts use scoped API keys with least-privilege permissions.
