# 🤝 Contributing to LDS Home Assistant Integration

Thank you for your interest in contributing to the LDS Home Assistant Integration! This project welcomes contributions from the community.

## 🎯 Ways to Contribute

### 🐛 Bug Reports
- Check existing issues before creating new ones
- Provide detailed reproduction steps
- Include Home Assistant version and integration version
- Add relevant log entries

### ✨ Feature Requests
- Describe the feature clearly
- Explain the use case and benefits
- Consider if it aligns with the project's spiritual mission

### 🔧 Code Contributions
- Follow the existing code style
- Add appropriate tests
- Update documentation
- Ensure backwards compatibility when possible

### 📚 Documentation
- Improve setup guides
- Add example configurations
- Fix typos and clarify instructions
- Add translations for other languages

## 🛠️ Development Setup

### Prerequisites
- Home Assistant development environment
- Python 3.11+
- Git

### Setup Steps
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/ha-lds.git
   cd ha-lds
   ```
3. Create a development branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Install in development mode in your Home Assistant instance

### Testing
- Test with multiple language configurations
- Verify card functionality across different browsers
- Test on both desktop and mobile interfaces
- Ensure integration doesn't break existing setups

## 📝 Pull Request Process

### Before Submitting
- [ ] Code follows the project style
- [ ] Changes are tested locally
- [ ] Documentation is updated if needed
- [ ] Commit messages are clear and descriptive

### PR Requirements
- Clear description of changes
- Link to related issues
- Screenshots for UI changes
- Test results and verification steps

### Review Process
1. Maintainers will review within a few days
2. Address any requested changes
3. Once approved, changes will be merged
4. Thanks and recognition in changelog!

## 🎨 Custom Card Development

### Card Guidelines
- Follow Home Assistant design patterns
- Use consistent color schemes
- Ensure mobile responsiveness
- Include proper error handling
- Add configuration options where helpful

### Card Structure
```javascript
class YourCard extends HTMLElement {
  setConfig(config) {
    // Validation and setup
  }

  set hass(hass) {
    // Data handling and rendering
  }

  render() {
    // HTML and CSS generation
  }

  getCardSize() {
    // Return appropriate card size
  }
}
```

## 🌍 Internationalization

### Adding Language Support
- Update language configuration options
- Test with Church website in target language
- Ensure proper character encoding
- Add language-specific examples

### Translation Guidelines
- Use appropriate religious terminology
- Maintain respectful tone
- Follow Church style guides when available
- Test with native speakers when possible

## 📖 Documentation Standards

### README Updates
- Keep installation instructions current
- Update example configurations
- Add new features to feature list
- Maintain clear formatting

### Code Documentation
- Comment complex logic
- Document configuration options
- Include usage examples
- Explain data structures

## 🔍 Code Review Guidelines

### What We Look For
- **Functionality**: Does it work as intended?
- **Security**: No security vulnerabilities
- **Performance**: Efficient and optimized
- **Maintainability**: Clean, readable code
- **Compatibility**: Works with current HA versions

### Code Style
- Follow Python PEP 8 for Python code
- Use meaningful variable names
- Keep functions focused and small
- Include appropriate error handling

## 🎯 Project Values

### Spiritual Mission
This integration aims to bring spiritual content into smart homes to:
- Encourage daily scripture study
- Share inspirational messages
- Support family religious activities
- Make spiritual content easily accessible

### Technical Excellence
- Reliable and stable operation
- User-friendly configuration
- Beautiful, functional interfaces
- Comprehensive documentation

### Community Focus
- Welcoming to all skill levels
- Respectful and helpful interactions
- Clear communication
- Collaborative problem-solving

## 🚀 Release Process

### Version Numbering
- Major.Minor.Patch (e.g., 2.1.0)
- Major: Breaking changes or major features
- Minor: New features, no breaking changes
- Patch: Bug fixes and small improvements

### Release Checklist
- [ ] Update version in manifest.json
- [ ] Update CHANGELOG.md
- [ ] Test on multiple HA versions
- [ ] Update documentation
- [ ] Create GitHub release
- [ ] Notify HACS if needed

## 🔧 Debugging and Troubleshooting

### Common Issues
- **Cards not loading**: Check resource configuration
- **No data**: Verify internet connectivity and Church website availability
- **Styling issues**: Clear browser cache, check for theme conflicts

### Debug Logging
```yaml
logger:
  default: warning
  logs:
    custom_components.lds: debug
```

### Testing Resources
- Use Church website directly to verify data availability
- Test with different network conditions
- Verify with multiple Home Assistant configurations

## 📞 Getting Help

### Questions and Support
- Open an issue for bugs or feature requests
- Use discussions for general questions
- Check existing documentation first
- Be specific about your setup and issue

### Communication Guidelines
- Be respectful and courteous
- Provide detailed information
- Be patient with responses
- Help others when you can

## 🏆 Recognition

Contributors will be:
- Listed in the CHANGELOG
- Credited in release notes
- Thanked in the community
- Given collaborator access for significant contributions

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make this project better! Your contributions help bring spiritual content to Home Assistant users worldwide. 🙏
