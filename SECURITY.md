# Security Policy

## Supported Versions

PassGenesis is a small utility project and currently only the latest version is supported.

| Version        | Supported |
| -------------- | --------- |
| Latest         | ✅         |
| Older releases | ❌         |

---

## Reporting a Vulnerability

If you discover a security issue, please report it responsibly.

Please avoid opening public issues for vulnerabilities.

Instead:

* Open a private discussion (if enabled)
* Contact the maintainer directly
* Provide reproduction steps and expected impact

Include:

* Environment details
* Steps to reproduce
* Screenshots (if applicable)
* Suggested remediation (optional)

---

## Security Principles

PassGenesis is designed around a minimal and privacy-first approach.

Current design choices:

* Password generation uses Python's `secrets` module
* Passwords are generated locally during runtime
* Passwords are not stored
* Passwords are not transmitted
* No database is used
* No analytics or tracking

---

## Scope

This project focuses on generating random passwords only.

PassGenesis does **not**:

* Evaluate password strength
* Store passwords
* Sync passwords
* Manage credentials
* Replace a password manager

Users remain responsible for:

* Selecting an appropriate password length
* Secure storage of generated passwords
* Following account-specific password requirements

---

## Dependency Security

Dependencies should be kept updated regularly.

Recommended checks:

```bash
pip list --outdated
pip install -U -r requirements.txt
```

Optional:

```bash
pip install pip-audit
pip-audit
```

---

## Disclosure Process

Reported issues will generally follow this process:

1. Report received
2. Validation
3. Fix implementation
4. Release update
5. Public acknowledgement (optional)

---

Thank you for helping improve PassGenesis security.
