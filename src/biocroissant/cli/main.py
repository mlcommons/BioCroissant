"""CLI entry point for biocroissant. Stub only; subcommands not implemented."""

import sys


def main():
    """Print usage and exit. No real logic yet."""
    if len(sys.argv) < 2 or sys.argv[1] not in ("validate", "convert", "describe"):
        print("usage: biocroissant validate | convert | describe [options]", file=sys.stderr)
        print("  validate  - validate Bio-Croissant metadata (not implemented)", file=sys.stderr)
        print("  convert   - convert to/from OMOP or other formats (not implemented)", file=sys.stderr)
        print("  describe  - print human-readable summary of metadata (not implemented)", file=sys.stderr)
        sys.exit(1)
    subcommand = sys.argv[1]
    print(f"biocroissant {subcommand}: not implemented (skeleton only)", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()
