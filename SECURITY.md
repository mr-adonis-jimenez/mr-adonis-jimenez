# ===================================================================
# File: .github/SECURITY.md
# ===================================================================
# NOTE: Edit org/repo names, emails, and SLA days as needed.

# Security Policy

## Supported projects & versions
All actively maintained repositories under this organization are in scope. Security fixes are prioritized for the latest minor release line unless otherwise stated in a repo’s README.

## Reporting a vulnerability (responsible disclosure)
- **Do not** open public issues for security problems.
- Report privately via **GitHub Security Advisories**: https://github.com/mr-adonis-jimenez/mr-adonis-jimenez/security/advisories/new
- Or email: **security@mr-adonis-jimenez.example** (PGP below).
- Include reproduction steps, impact, affected versions/commits, and any PoC.

We’ll acknowledge reports within **3 business days**, provide a status update within **7 days**, and coordinate a fix + disclosure timeline. We strive to release a patch within **30 days** for high severity issues.

## Preferred languages
English, Spanish.

## Bounties
No formal bounty program. Reasonable rewards (credit, swag, or stipend) may be offered at our discretion for high-impact findings.

## Disclosure
We request a **90-day** disclosure window by default, or earlier once a fix is available and users have had time to update. CVEs may be requested via GHSA; we’ll assist.

## Out of scope (examples)
- Clickjacking on static pages without sensitive actions
- Missing SPF/DMARC/SSL best-practices on non-prod domains
- Rate-limit or brute-force without demonstrated impact
- Dependency advisories that are already public and patched

## PGP
Fingerprint: `0000 1111 2222 3333 4444 5555 6666 7777 8888 9999`
Key: https://mr-adonis-jimenez.example/pgp.txt

## Hardening references
- Use latest releases
- Enable 2FA for org members
- Require signed commits for protected branches
- Use environment/organization secrets with least privilege

---

# ===================================================================
# File: .github/ISSUE_TEMPLATE/config.yml
# ===================================================================
# Deflects security reports away from public issues to private channels.

blank_issues_enabled: false
contact_links:
  - name: Report a security vulnerability (private)
    url: https://github.com/OWNER/REPO/security/advisories/new
    about: This creates a private advisory thread with maintainers.
  - name: Email the security team
    url: mailto:security@mr-adonis-jimenez.example
    about: Use if the advisory form is unavailable.

# ===================================================================
# File: .github/CODEOWNERS
# ===================================================================
# Ensures security-savvy reviewers are auto-requested on changes to critical areas.

# Core
* @mr-adonis-jimenez/security-team

# Optional tighter scoping examples:
# /infrastructure/ @mr-adonis-jimenez/sec-infra
# /pkg/ @mr-adonis-jimenez/maintainers

# ===================================================================
# File: .github/dependabot.yml
# ===================================================================

version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule: { interval: "weekly" }
    open-pull-requests-limit: 5
  - package-ecosystem: "npm"
    directory: "/"
    schedule: { interval: "weekly" }
    versioning-strategy: increase
    groups:
      minor-and-patch:
        applies-to: version-updates
        update-types: ["minor", "patch"]
  - package-ecosystem: "pip"
    directory: "/"
    schedule: { interval: "weekly" }
    insecure-external-code-execution: deny
  # Add more ecosystems as needed (gomod, maven, gradle, cargo, nuget, composer, etc.)

# ===================================================================
# File: .github/workflows/codeql.yml
# ===================================================================
# GitHub-native static analysis for supported languages.

name: "CodeQL"
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  schedule:
    - cron: "24 2 * * 1"
permissions:
  contents: read
  security-events: write
  actions: read
jobs:
  analyze:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        language: [ "javascript", "python" ]  # Add languages as needed: cpp, go, java, ruby
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: ${{ matrix.language }}
      - uses: github/codeql-action/autobuild@v3
      - uses: github/codeql-action/analyze@v3

# ===================================================================
# File: .github/workflows/scorecard.yml
# ===================================================================
# OSSF Scorecard supply-chain checks + SARIF upload.

name: "OSSF Scorecard"
on:
  branch_protection_rule:
  schedule:
    - cron: "37 1 * * 1"
  push:
    branches: [ "main" ]
permissions:
  actions: read
  contents: read
  id-token: write
  security-events: write
  pull-requests: read
jobs:
  analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: ossf/scorecard-action@v2.3.3
        with:
          results_file: results.sarif
          results_format: sarif
          publish_results: true
      - uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: results.sarif

# ===================================================================
# File: .github/workflows/gitleaks.yml
# ===================================================================
# Secret scanning on pushes/PRs to complement GitHub's native scanning.

name: "Gitleaks"
on:
  pull_request:
  push:
    branches: [ "main", "develop" ]
permissions:
  contents: read
  security-events: write
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # why: scan history in PRs
      - name: Run Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITLEAKS_LICENSE: ${{ secrets.GITLEAKS_LICENSE }} # why: optional, enables enterprise policy
        with:
          args: >-
            detect
            --redact
            --no-banner
            --report-format sarif
            --report-path gitleaks.sarif
      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: gitleaks.sarif

# ===================================================================
# File: .github/pull_request_template.md
# ===================================================================
# Nudges for secure PRs.

## Summary
- What changed? Why?

## Security considerations
- Any auth/ACL/crypto/input-validation changes?
- Any secrets, tokens, or keys touched?
- Backwards compatibility and migration risks?

## Checklist
- [ ] Added/updated tests
- [ ] No secrets committed
- [ ] Dependencies updated safely
- [ ] Docs updated
