#!/usr/bin/env python3
"""
Karasu — One-shot formatter enforcer for Python repos.

This is the Feza-compatible entry point. The actual implementation
is in the karasu package.
"""

from karasu import main as _main


# Expose main for entry point
def main():
    """Entry point for karasu CLI."""
    _main()


if __name__ == "__main__":
    main()
