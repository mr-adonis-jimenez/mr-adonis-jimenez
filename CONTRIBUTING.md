# Contributing to Adonis Jimenez's Projects

Thank you for your interest in contributing! This document provides guidelines for contributing to repositories under [@mr-adonis-jimenez](https://github.com/mr-adonis-jimenez).

---

## 👋 Welcome Contributors

Whether you're fixing a typo, reporting a bug, or proposing a major feature, your contributions are valued and appreciated!

### What You Can Contribute

- 🐛 **Bug Reports:** Detailed issues with reproduction steps
- ✨ **Feature Requests:** Well-thought-out enhancement proposals
- 📝 **Documentation:** Improvements to README, guides, or code comments
- 🛠️ **Code Contributions:** Bug fixes, new features, or optimizations
- 🧪 **Testing:** Additional test cases or QA feedback
- 🎨 **Design:** UI/UX improvements or visual assets

---

## 🚀 Getting Started

### 1. Fork the Repository

```bash
# Fork via GitHub UI, then clone your fork
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME

# Add upstream remote
git remote add upstream https://github.com/mr-adonis-jimenez/REPO-NAME.git
```

### 2. Create a Branch

```bash
# Use descriptive branch names
git checkout -b feature/your-feature-name
git checkout -b fix/issue-description
git checkout -b docs/documentation-update
```

### 3. Make Your Changes

- Write clean, readable code
- Follow existing code style and conventions
- Add tests for new functionality
- Update documentation as needed
- Commit with clear, descriptive messages

### 4. Commit Your Work

```bash
# Stage your changes
git add .

# Commit with conventional commit format
git commit -m "feat: add new feature"
git commit -m "fix: resolve bug in component"
git commit -m "docs: update installation guide"
```

#### Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create PR via GitHub UI
# Fill out the PR template completely
```

---

## 📝 Pull Request Guidelines

### Before Submitting

- ✅ Code follows project style guidelines
- ✅ All tests pass locally
- ✅ New tests added for new functionality
- ✅ Documentation updated
- ✅ No merge conflicts with `master`/`main`
- ✅ Commits are squashed if needed
- ✅ No secrets or sensitive data committed

### PR Template Checklist

Your PR should include:

1. **Description:** What does this PR do?
2. **Motivation:** Why is this change needed?
3. **Testing:** How was this tested?
4. **Screenshots:** For UI changes
5. **Breaking Changes:** Document any breaking changes
6. **Related Issues:** Link to related issues (Fixes #123)

### Review Process

1. **Automated Checks:** CI/CD pipelines must pass
2. **Code Review:** Maintainer reviews code quality
3. **Testing:** Functionality verification
4. **Approval:** Approved PRs are merged by maintainers

**Response Time:** Expect initial feedback within 3-5 business days.

---

## 💻 Development Setup

### Prerequisites

- Git 2.40+
- Python 3.10+ (for Python projects)
- Node.js 18+ (for JavaScript projects)
- Docker (for containerized projects)

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt  # Python
npm install                       # Node.js

# Run tests
pytest                            # Python
npm test                          # Node.js

# Run linters
flake8 .                          # Python
npm run lint                      # Node.js

# Format code
black .                           # Python
npm run format                    # Node.js
```

---

## 🧠 Code Style Guidelines

### Python

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for formatting
- Maximum line length: 88 characters
- Use type hints where applicable
- Docstrings for all public functions/classes

### JavaScript/TypeScript

- Follow [Airbnb Style Guide](https://github.com/airbnb/javascript)
- Use [Prettier](https://prettier.io/) for formatting
- ESLint for linting
- Prefer functional components (React)
- Use TypeScript for type safety

### General Principles

- **DRY:** Don't Repeat Yourself
- **KISS:** Keep It Simple, Stupid
- **YAGNI:** You Aren't Gonna Need It
- **Write self-documenting code**
- **Comment why, not what**

---

## 🧪 Testing Requirements

### Test Coverage

- Minimum 80% code coverage for new code
- All critical paths must be tested
- Include edge cases and error scenarios

### Test Types

1. **Unit Tests:** Test individual functions/components
2. **Integration Tests:** Test component interactions
3. **E2E Tests:** Test complete user workflows
4. **Performance Tests:** For performance-critical code

```bash
# Run tests with coverage
pytest --cov=src --cov-report=html
npm run test:coverage
```

---

## 🔒 Security Considerations

### Before Committing

- ❌ **NEVER** commit secrets, API keys, or credentials
- ❌ **NEVER** commit `.env` files
- ✅ Use environment variables for sensitive data
- ✅ Run `git-secrets` or `gitleaks` locally
- ✅ Review changes before pushing

### Reporting Security Issues

**DO NOT** open public issues for security vulnerabilities.

See [SECURITY.md](SECURITY.md) for responsible disclosure process.

---

## 🐛 Bug Reports

### Good Bug Reports Include

1. **Clear Title:** Concise description of the issue
2. **Environment:** OS, versions, dependencies
3. **Steps to Reproduce:** Minimal reproduction steps
4. **Expected Behavior:** What should happen
5. **Actual Behavior:** What actually happens
6. **Screenshots:** If applicable
7. **Error Messages:** Full stack traces
8. **Additional Context:** Any other relevant info

### Template

```markdown
## Bug Description
A clear description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., Ubuntu 22.04]
- Browser: [e.g., Chrome 120]
- Version: [e.g., 1.2.3]

## Screenshots
If applicable, add screenshots.

## Additional Context
Any other context about the problem.
```

---

## ✨ Feature Requests

### Good Feature Requests Include

1. **Problem Statement:** What problem does this solve?
2. **Proposed Solution:** Your suggested implementation
3. **Alternatives Considered:** Other approaches you've thought about
4. **Additional Context:** Use cases, examples, mockups

### Template

```markdown
## Feature Description
A clear description of the feature.

## Problem Statement
What problem does this feature solve?

## Proposed Solution
How should this feature work?

## Alternatives Considered
What other approaches did you consider?

## Additional Context
Use cases, mockups, or examples.
```

---

## 🌐 Community Guidelines

### Be Respectful

- ✅ Be kind and courteous
- ✅ Respect different viewpoints
- ✅ Accept constructive criticism gracefully
- ✅ Focus on what's best for the community

### Code of Conduct

All contributors must follow the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## ❓ Questions?

- **GitHub Discussions:** For general questions and discussions
- **Issues:** For bug reports and feature requests
- **Email:** [adonis-jimenez@outlook.com](mailto:adonis-jimenez@outlook.com)
- **LinkedIn:** [linkedin.com/in/adonisjimenez](https://linkedin.com/in/adonisjimenez)

---

## 👏 Recognition

Contributors are recognized in:

- Project README (for significant contributions)
- Release notes
- GitHub Insights
- Special thanks section

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the project's license (typically MIT).

---

<div align="center">

**Thank you for contributing!** 🚀

*Your contributions make open source better for everyone.*

</div>
