# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands
- Run the script: `python stardate.py [arguments]` or `./stardate.py [arguments]`
- Run with specific arguments: `./stardate.py --metadata 1d`
- Run tests: No dedicated test framework yet, use manual testing with `./stardate.py --help`
- Lint Python: `pylint stardate.py`

## Code Style Guidelines
- Python: Follow PEP 8 conventions
- Indentation: 4 spaces for Python
- Function naming: snake_case for functions and variables
- Module imports: Group standard library imports first, then third-party packages
- Error handling: Use try/except for file operations, use argparse for input validation
- Docstrings: Include for all functions, use """triple quotes"""
- Time ranges: Follow the established pattern of '1d', '7d', '1w' format
- Directory paths: Use os.path.join() for cross-platform compatibility