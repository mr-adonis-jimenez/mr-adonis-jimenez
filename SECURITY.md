# Security Policy

## Supported Versions

All actively maintained repositories under [@mr-adonis-jimenez](https://github.com/mr-adonis-jimenez) are in scope for security reports. Security fixes are prioritized for the latest release versions unless otherwise stated in individual repository README files.

## Reporting a Vulnerability

### 🔒 Private Disclosure (Preferred)

**Please do NOT open public issues for security vulnerabilities.**

Report security issues privately through:

1. **GitHub Security Advisories:** [Report a vulnerability](https://github.com/mr-adonis-jimenez/mr-adonis-jimenez/security/advisories/new)
2. **Email:** [adonis-jimenez@outlook.com](mailto:adonis-jimenez@outlook.com)

### What to Include

Please provide:
- **Description** of the vulnerability
- **Steps to reproduce** the issue
- **Potential impact** and severity assessment
- **Affected versions** or commits
- **Proof of concept** code (if applicable)
- **Suggested remediation** (optional)

## Response Timeline

- **Initial Response:** Within 3 business days
- **Status Update:** Within 7 business days
- **Patch Release:** Within 30 days for high-severity issues

We strive to address critical vulnerabilities as quickly as possible and will keep you informed throughout the remediation process.

## Disclosure Policy

We follow a coordinated disclosure approach:

- **90-day disclosure window** by default
- Earlier disclosure once a fix is available and users have been notified
- CVE IDs can be requested through GitHub Security Advisories
- We'll credit researchers unless anonymity is requested

## Preferred Languages

- English
- Spanish

## Bounty Program

While we don't currently have a formal bug bounty program, we may offer:

- Public acknowledgment in security advisories
- Recognition in project documentation
- Swag or stipends for high-impact discoveries (at our discretion)

## Out of Scope

The following are generally **not** considered security vulnerabilities:

- Clickjacking on pages without sensitive actions
- Missing security headers on non-production domains
- Missing SPF/DMARC/DKIM records on example domains
- Rate limiting issues without demonstrated impact
- Brute force attacks without successful exploitation
- Publicly disclosed dependency vulnerabilities that are already patched
- Social engineering attacks
- Denial of Service (DoS) attacks

## Security Best Practices

When contributing to our projects:

✅ Use the latest stable versions of dependencies  
✅ Enable two-factor authentication (2FA) for your GitHub account  
✅ Sign commits with GPG keys  
✅ Review code changes carefully before approval  
✅ Use environment secrets with least privilege  
✅ Follow OWASP security guidelines  
✅ Run security scans before merging  

## Security Tools & Scanning

Our repositories utilize:

- **Dependabot** for dependency updates
- **CodeQL** for static analysis
- **OSSF Scorecard** for supply chain security
- **Gitleaks** for secret detection
- **GitHub Security Advisories** for vulnerability tracking

## Contact

**Security Team:** [adonis-jimenez@outlook.com](mailto:adonis-jimenez@outlook.com)  
**GitHub:** [@mr-adonis-jimenez](https://github.com/mr-adonis-jimenez)

---

**Thank you for helping keep our projects secure!** 🔒
