# Contributing to GIF Viewer

Thank you for your interest in contributing to GIF Viewer! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and constructive
- Welcome diverse perspectives
- Focus on the code, not the person
- Help create a positive community

## How to Contribute

### Reporting Bugs

Found a bug? Please create an issue with:

1. **Clear title** - What doesn't work?
2. **Description** - What's the problem?
3. **Steps to reproduce** - How can we reproduce it?
4. **Expected behavior** - What should happen?
5. **Actual behavior** - What actually happens?
6. **Log excerpts** - Include relevant log lines
7. **Environment** - OS, Python version, etc.

### Requesting Features

Have an idea? Create an issue with:

1. **Clear title** - What feature?
2. **Description** - Why is it useful?
3. **Example usage** - How would you use it?
4. **Implementation notes** - Suggestions for how (optional)

### Submitting Changes

#### Before You Start
1. Check existing issues/PRs - avoid duplicate work
2. Create an issue for discussion (for large features)
3. Fork the repository
4. Create a feature branch

#### Making Changes

```bash
# Create and switch to feature branch
git checkout -b feature/description

# Make your changes
# Test thoroughly
# Update documentation

# Commit with clear messages
git commit -m "Add feature: clear description"
git commit -m "Fix bug: clear description"
git commit -m "Docs: update for new feature"
```

#### Code Style

Follow PEP 8:
```python
# Good
def load_gif_files(directory):
    """Load all GIF files from directory."""
    files = []
    for file in os.listdir(directory):
        if file.lower().endswith('.gif'):
            files.append(file)
    return sorted(files)

# Bad
def loadGifFiles(dir):
    f=[]
    for x in os.listdir(dir):
        if x.lower().endswith('.gif'):f.append(x)
    return sorted(f)
```

#### Documentation

- Add docstrings to all functions:
```python
def my_function(param1, param2):
    """Short description.
    
    Longer description if needed.
    
    Args:
        param1: Description
        param2: Description
        
    Returns:
        Description of return value
    """
    pass
```

- Update relevant documentation files
- Add comments for complex logic

#### Testing

```bash
# Test your code
cd GifViewerData
python main.py

# Check for errors in logs
python log_viewer.py errors

# Test all input methods
# - Joystick/gamepad
# - Keyboard
# - Different file browser scenarios
# - Background selection
```

#### Submitting a Pull Request

1. **Push to your fork**
   ```bash
   git push origin feature/description
   ```

2. **Create Pull Request**
   - Clear title describing changes
   - Reference any related issues (#123)
   - Explain what and why (not how - code explains that)
   - Include any relevant screenshots/logs

3. **PR Template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Other
   
   ## Related Issue
   Closes #(issue number if applicable)
   
   ## Changes Made
   - Change 1
   - Change 2
   
   ## Testing Done
   - Tested on Windows/Linux/macOS
   - Tested with joystick/keyboard
   - Verified logs show correct messages
   
   ## Screenshots/Logs
   If applicable, include relevant screenshots or log excerpts
   ```

## Project Structure

```
GifViewer/
├── GifViewerData/
│   ├── main.py              # Main application
│   ├── modules/             # Modules package
│   │   ├── config.py        # Configuration
│   │   ├── helpers.py       # Utilities
│   │   └── logger.py        # Logging
│   ├── images/              # GIF files
│   ├── backgrounds/         # Background images
│   └── logs/                # Application logs
├── log_viewer.py            # Log utility
├── README.md                # Main documentation
├── requirements.txt         # Python dependencies
└── LICENSE                  # MIT License
```

## Development Workflow

### Setup Development Environment

```bash
# Clone your fork
git clone https://github.com/yourusername/GifViewer.git
cd GifViewer

# Install dependencies
pip install -r requirements.txt

# Run the app
cd GifViewerData
python main.py
```

### Making Changes

```bash
# Create feature branch
git checkout -b feature/my-feature

# Make changes, test thoroughly
python main.py

# Check logs for errors
python log_viewer.py errors

# Commit changes
git add .
git commit -m "Add feature description"

# Push to your fork
git push origin feature/my-feature
```

### Code Review Process

1. Maintainer reviews code
2. Feedback provided if needed
3. Make requested changes
4. Code approved and merged

## Areas for Contribution

### Easy Tasks (Good for Beginners)
- [ ] Bug fixes
- [ ] Documentation improvements
- [ ] Typo corrections
- [ ] Code examples
- [ ] Test additions

### Medium Tasks
- [ ] Feature enhancements
- [ ] Logging improvements
- [ ] Configuration options
- [ ] Error handling
- [ ] Performance optimizations

### Complex Tasks
- [ ] New major features
- [ ] Architecture changes
- [ ] Plugin system
- [ ] Network support
- [ ] Advanced UI features

## Documentation

### Files to Update
1. **README.md** - Main documentation
2. **Quick guides** - Feature-specific documentation
3. **Code comments** - In-code documentation
4. **CHANGELOG.md** - If adding new file

### Writing Documentation
- Use clear, simple language
- Include examples
- Add screenshots if helpful
- Update table of contents

## Commit Message Format

```
Type: Brief description

Longer explanation if needed. Explain the "why", not the "what".
The code shows what changed, explain why it's better.

Fixes #123
```

### Commit Types
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Code style
- `refactor:` - Code organization
- `perf:` - Performance
- `test:` - Tests
- `chore:` - Maintenance

## Questions or Need Help?

- **Documentation**: Check README.md and docs/
- **Issues**: Search existing issues
- **Discussions**: Create a discussion if unsure

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- GitHub contributors page
- Release notes

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to GIF Viewer! 🙏✨
