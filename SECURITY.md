# Security Policy

## Supported Projects & Versions

All actively maintained repositories under [@mr-adonis-jimenez](https://github.com/mr-adonis-jimenez) are in scope for security reports. Security fixes are prioritized for the latest release unless otherwise stated in a repository's README.

---

## 🚨 Reporting a Vulnerability

### Responsible Disclosure Process

**⚠️ DO NOT open public issues for security vulnerabilities.**

Please report security issues privately through one of these channels:

### 1. GitHub Security Advisories (Preferred)

🔗 **[Create Private Security Advisory](https://github.com/mr-adonis-jimenez/mr-adonis-jimenez/security/advisories/new)**

This creates a private thread with maintainers for coordinated disclosure.

### 2. Email

📧 **[adonis-jimenez@outlook.com](mailto:adonis-jimenez@outlook.com)**

Use this method if the advisory form is unavailable or for urgent issues.

### 3. PGP Encrypted Email (High Sensitivity)

For highly sensitive disclosures, use PGP encryption:

- **Email:** adonis-jimenez@outlook.com
- **PGP Key:** Available upon request
- **Fingerprint:** Contact via email to verify

---

## 📝 What to Include in Your Report

To help us understand and address the issue quickly, please include:

- **Description:** Clear explanation of the vulnerability
- **Impact:** What can an attacker achieve?
- **Affected Versions:** Which releases or commits are vulnerable?
- **Reproduction Steps:** Detailed steps to reproduce the issue
- **Proof of Concept:** Code, screenshots, or video demonstration
- **Suggested Fix:** If you have ideas for remediation
- **Disclosure Timeline:** Your preferred disclosure schedule

---

## ⏱️ Response Timeline

We take security seriously and commit to:

| Stage | Timeline |
|-------|----------|
| **Initial Acknowledgment** | Within 3 business days |
| **Status Update** | Within 7 days |
| **Fix Development** | 30 days for high severity issues |
| **Disclosure** | 90 days after report (or when fix is available) |

---

## 🌐 Preferred Languages

- English
- Spanish (Español)

---

## 🏆 Recognition & Rewards

While we don't have a formal bug bounty program, we may offer:

- ⭐ **Public Credit:** Recognition in release notes and security advisories
- 🎯 **Swag:** GitHub-themed merchandise for significant findings
- 💵 **Stipend:** Reasonable rewards at our discretion for high-impact discoveries
- 🏅 **Hall of Fame:** Featured in our security acknowledgments

---

## 📅 Coordinated Disclosure

We request a **90-day disclosure window** by default to:

1. Develop and test a comprehensive fix
2. Coordinate with affected downstream projects
3. Allow users time to update
4. Prepare security advisories and CVEs

We're flexible on this timeline and will work with you to find a mutually agreeable disclosure date.

### CVE Assignment

For qualifying vulnerabilities, we can:
- Request CVEs through GitHub Security Advisories (GHSA)
- Coordinate with MITRE or other CVE Numbering Authorities
- Assist with CVE descriptions and impact assessments

---

## ❌ Out of Scope

The following are generally **not considered security vulnerabilities**:

- ❌ Clickjacking on static pages without sensitive actions
- ❌ Missing security headers (SPF/DMARC/HSTS) on non-production domains
- ❌ Rate limiting or brute-force attacks without demonstrated impact
- ❌ Dependency advisories that are already public and patched
- ❌ Social engineering attacks requiring significant user interaction
- ❌ Denial of service via resource exhaustion (unless severe)
- ❌ Issues in third-party dependencies (report to upstream project)
- ❌ Self-XSS or issues requiring physical access

If unsure, please report it anyway—we'll make the determination.

---

## 🛡️ Security Best Practices

When working with this organization's repositories:

### For Contributors
- ✅ Use the latest stable release
- ✅ Enable 2FA on your GitHub account
- ✅ Sign commits with GPG keys
- ✅ Never commit secrets, tokens, or credentials
- ✅ Review dependencies for known vulnerabilities
- ✅ Follow principle of least privilege

### For Repository Maintainers
- ✅ Enable branch protection rules
- ✅ Require signed commits for protected branches
- ✅ Use GitHub Security Advisories for private discussions
- ✅ Enable Dependabot security updates
- ✅ Use environment secrets with proper scoping
- ✅ Regularly audit access permissions
- ✅ Enable CodeQL scanning for supported languages

---

## 📚 Security Resources

- [GitHub Security Documentation](https://docs.github.com/en/code-security)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE List](https://cwe.mitre.org/)
- [CVE Program](https://www.cve.org/)
- [OSSF Scorecard](https://github.com/ossf/scorecard)

---

## 📞 Contact Information

| Method | Details |
|--------|----------|
| **Primary Contact** | Adonis Jimenez |
| **Email** | adonis-jimenez@outlook.com |
| **GitHub** | [@mr-adonis-jimenez](https://github.com/mr-adonis-jimenez) |
| **LinkedIn** | [linkedin.com/in/adonisjimenez](https://linkedin.com/in/adonisjimenez) |
| **Response Time** | 3 business days |

---

## 📜 Version History

| Version | Date | Changes |
|---------|------|----------|
| 1.0 | 2026-01-22 | Initial comprehensive security policy |

---

<div align="center">

**Thank you for helping keep our projects secure!** 🔒

*This policy is subject to change. Check back regularly for updates.*

</div>