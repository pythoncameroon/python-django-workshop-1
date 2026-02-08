# Contributing Guide - ActiveShare Platform

Welcome! We're excited that you want to contribute to this project. 🎉

## 🎯 Project Goal

This project aims to help you learn Django while practicing **vibecoding** with the **Antigravity** editor.

> **⚠️ IMPORTANT**: Vibecoding doesn't mean coding without thinking! The goal is to **understand what you're doing** while using AI capabilities to accelerate your development.

## 📋 Features to Implement

### 1. Django Models (High Priority)

Implement the following models with their relationships:

#### Models to create:
- **Shareholder**
- **Buyer**
- **Share**

#### Integrity Rules:
- Each `Shareholder` and `Buyer` must be linked to a Django `User`
- A `Shareholder` can create **one or more** `Share`s
- A `Buyer` can purchase **zero or more** `Share`s
- A `Share` is created by **one and only one** `Shareholder`
- A `Share` can be purchased by **one or more** `Buyer`s

#### Technical Constraints:
- Use appropriate Django relationships (`ForeignKey`, `ManyToManyField`, etc.)
- Implement `__str__()` methods for better readability
- Add `Meta` classes with `verbose_name` and `ordering`
- Consider `related_name` to facilitate reverse queries

### 2. Web Interface (High Priority)

Create a **modern and attractive** user interface using HTML, CSS, and JavaScript.

#### Pages to create:
- 🏠 **Homepage**: Platform presentation
- 📝 **Registration page**: Account creation (with role selection: Shareholder/Buyer)
- 🔐 **Login page**: Authentication
- 👤 **User profile page**: Details based on user type (Shareholder/Buyer)
- ➕ **Share creation page**: Form for Shareholders
- 📊 **Share details page**: Complete information about a share
- 🛒 **Share listing page**: Catalog of available shares
- 📈 **Dashboard**: Overview of owned/created shares

#### Design Requirements:
- ✨ **Modern and professional** interface
- 📱 **Responsive** design (mobile, tablet, desktop)
- 🎨 Cohesive color palette
- ♿ Basic accessibility (labels, contrast, keyboard navigation)
- 🚀 Subtle animations and smooth transitions

> **Note**: Initially, you can create static mockups before Django integration.

### 3. Django Views and Integration (High Priority)

Implement Django views and integrate them with templates.

#### Requirements:
- Use **Django Forms** for data validation
- Implement Class-Based Views (CBV) or Function-Based Views (FBV) as appropriate
- Handle permissions (only Shareholders can create Shares)
- Add user feedback messages (success, errors)
- Implement pagination for lists
- Handle error cases (404, 403, etc.)

## 🏗️ Architecture and Best Practices

### Code Structure
- Follow standard Django structure
- Separate business logic from views (use services if necessary)
- Keep your views simple and readable
- Use serializers or forms for validation

### Code Quality
- ✅ Follow PEP 8 (Python style guide)
- 📝 Comment complex code
- 🧪 Write unit tests (bonus)
- 🔒 Always validate data server-side
- 🚫 Never expose sensitive data

### Git and Commits
- 📌 Atomic and descriptive commits
- 💬 Clear commit messages in French or English
  - Recommended format: `type: short description`
  - Examples:
    - `feat: add Shareholder model`
    - `fix: correct Share form validation`
    - `style: improve homepage design`

## 🔄 Contribution Process

### 1. Setup

```bash
# Fork the project on GitHub, then clone your fork
git clone <your-fork-url>
cd python-django-workshop

# Add the original repo as upstream remote
git remote add upstream <original-repo-url>

# Create a branch for your feature
git checkout -b feat/feature-name
```

### 2. Development

- ⚠️ **Before starting**: Sync with the main branch
  ```bash
  git fetch upstream
  git rebase upstream/main
  ```
- 💻 Develop your feature
- 🧪 Test locally
- 📝 Commit regularly

### 3. Pull Request (PR)

#### Important Rules:
- ✅ **One PR = One feature**
- ❌ **No long PRs** (avoid PRs with 500+ lines)
- 🔄 **Sync before each PR**
  ```bash
  git fetch upstream
  git rebase upstream/main
  git push origin feat/feature-name
  ```

#### PR Template:

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] New model
- [ ] New view
- [ ] New template
- [ ] Bug fix
- [ ] Design improvement

## Checklist
- [ ] My code follows the project conventions
- [ ] I have tested locally
- [ ] I have synced with the main branch
- [ ] My commits are clear and atomic
- [ ] I have updated documentation if necessary

## Screenshots (if applicable)
Add screenshots for visual changes.
```

### 4. Review

- Maintainers (@yokwejuste and @Edmond22-prog) will review your PR
- Be responsive to comments
- Make requested changes
- Once approved, your PR will be merged! 🎉

## ❓ Questions and Support

If you have questions or encounter difficulties:

1. 🔍 First consult the Django documentation
2. 💬 Create an **Issue** on GitHub with:
   - A clear title
   - A detailed description of the problem
   - Steps to reproduce (if bug)
   - Your environment (OS, Python version, etc.)
3. 🏷️ Tag **@yokwejuste** and **@Edmond22-prog**

## 💡 New Ideas

Do you have an idea for an additional feature? Great!

1. Create an **Issue** with the `enhancement` label
2. Describe your proposal
3. Wait for feedback before starting implementation

## 📚 Useful Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [MDN Web Docs - HTML/CSS/JS](https://developer.mozilla.org/)
- [PEP 8 - Style Guide](https://pep8.org/)

## 🙏 Acknowledgments

Thank you for contributing to this project and being part of the Python Cameroon community! 🇨🇲

---

**Happy Coding! 🚀**
