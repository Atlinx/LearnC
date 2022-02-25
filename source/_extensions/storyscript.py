# -*- coding: utf-8 -*-
"""
    pygments.lexers.storyscript
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for StoryScript.

    :copyright: Copyright 2xxx by The Godot Engine Community
    :license: MIT.

    modified by Daniel J. Ramirez <djrmuv@gmail.com> based on the original python.py pygment
"""

import re

from pygments.lexer import (
    RegexLexer,
    include,
    bygroups,
    default,
    words,
    combined,
)
from pygments.token import (
    Text,
    Comment,
    Operator,
    Keyword,
    Name,
    String,
    Number,
    Punctuation,
    STANDARD_TYPES,
)

__all__ = ["StoryScriptLexer"]

line_re = re.compile(".*?\n")

# Add custom tokens
# STANDARD_TYPES[Keyword.Secondary] = "kw2"
# STANDARD_TYPES[Keyword.Tertiary] = "kw3"

class StoryScriptLexer(RegexLexer):
    name = "StoryScript"
    aliases = ["storyscript", "gd"]
    filenames = ["*.gd"]
    mimetypes = ["text/x-storyscript", "application/x-storyscript"]

    def innerstring_rules(ttype):
        return [
            # the old style '%s' % (...) string formatting
            (
                r"%(\(\w+\))?[-#0 +]*([0-9]+|[*])?(\.([0-9]+|[*]))?"
                "[hlL]?[E-GXc-giorsux%]",
                String.Interpol,
            ),
            # backslashes, quotes and formatting signs must be parsed one at a time
            (r'[^\\\'"%\n]+', ttype),
            (r'[\'"\\]', ttype),
            # unhandled string formatting sign
            (r"%", ttype),
            # newlines are an error (use "nl" state)
        ]

    tokens = {
        "root": [
            (r"\n", Text),
            (
                r'^(\s*)([rRuUbB]{,2})("""(?:.|\n)*?""")',
                bygroups(Text, String.Affix, String.Doc),
            ),
            (
                r"^(\s*)([rRuUbB]{,2})('''(?:.|\n)*?''')",
                bygroups(Text, String.Affix, String.Doc),
            ),
            (r"[^\S\n]+", Text),
            (r"#.*$", Comment.Single),
            (r"[]{}:(),;[]", Punctuation),
            (r"\\\n", Text),
            (r"\\", Text),
            (r"(in|and|or|not)\b", Operator.Word),
            (
                r"!=|==|<<|>>|&&|\+=|-=|\*=|/=|%=|&=|\|=|\|\||[-~+/*%=<>&^.!|$]",
                Operator,
            ),
            include("keywords"),
            (r"(\w+)(\()", bygroups(Name.Function, Text)),
            (r"(func)((?:\s|\\\s)+)", bygroups(Keyword, Text), "funcname"),
            (
                '([rR]|[uUbB][rR]|[rR][uUbB])(""")',
                bygroups(String.Affix, String.Double),
                "tdqs",
            ),
            (
                "([rR]|[uUbB][rR]|[rR][uUbB])(''')",
                bygroups(String.Affix, String.Single),
                "tsqs",
            ),
            (
                '([rR]|[uUbB][rR]|[rR][uUbB])(")',
                bygroups(String.Affix, String.Double),
                "dqs",
            ),
            (
                "([rR]|[uUbB][rR]|[rR][uUbB])(')",
                bygroups(String.Affix, String.Single),
                "sqs",
            ),
            (
                '([uUbB]?)(""")',
                bygroups(String.Affix, String.Double),
                combined("stringescape", "tdqs"),
            ),
            (
                "([uUbB]?)(''')",
                bygroups(String.Affix, String.Single),
                combined("stringescape", "tsqs"),
            ),
            (
                '([uUbB]?)(")',
                bygroups(String.Affix, String.Double),
                combined("stringescape", "dqs"),
            ),
            (
                "([uUbB]?)(')",
                bygroups(String.Affix, String.Single),
                combined("stringescape", "sqs"),
            ),
            include("name"),
            include("numbers"),
        ],
        "keywords": [
            (
                r"var\b",
                Keyword.Declaration,
            ),
            (
                words(
                    (
                        "if",
                        "elif",
                        "else",
                        "pass",
                        "label",
                        "choice",
                        "transition",
                        "animate",
                        "with",
                        "show",
                        "hide",
                        "jump",
                        "move",
                        "pass",
                        "pause",
                        "remove",
                        "scene",
                        "sound",
                        "import",
                    ),
                    suffix=r"\b",
                ),
                Keyword,
            ),
        ],
        "numbers": [
            (r"(\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?j?", Number.Float),
            (r"\d+[eE][+-]?[0-9]+j?", Number.Float),
            (r"0[xX][a-fA-F0-9]+", Number.Hex),
            (r"\d+j?", Number.Integer),
        ],
        "name": [(r"@?[a-zA-Z_]\w*", Name)],
        "funcname": [(r"[a-zA-Z_]\w*", Name.Function, "#pop"), default("#pop")],
        "stringescape": [
            (
                r'\\([\\abfnrtv"\']|\n|N\{.*?\}|u[a-fA-F0-9]{4}|'
                r"U[a-fA-F0-9]{8}|x[a-fA-F0-9]{2}|[0-7]{1,3})",
                String.Escape,
            )
        ],
        "strings-single": innerstring_rules(String.Single),
        "strings-double": innerstring_rules(String.Double),
        # Shorthand for parsing double quotes
        "dqs": [
            (r'"', String.Double, "#pop"),
            (r'\\\\|\\"|\\\n', String.Escape),  # included here for raw strings
            include("strings-double"),
        ],
        # Shorthand for parsing single quotes
        "sqs": [
            (r"'", String.Single, "#pop"),
            (r"\\\\|\\'|\\\n", String.Escape),  # included here for raw strings
            include("strings-single"),
        ],
        # Shorthand for parsing triple double quotes
        "tdqs": [
            (r'"""', String.Double, "#pop"),
            include("strings-double"),
            (r"\n", String.Double),
        ],
        # Shorthand for parsing triple single quotes
        "tsqs": [
            (r"'''", String.Single, "#pop"),
            include("strings-single"),
            (r"\n", String.Single),
        ],
    }


def setup(sphinx):
    sphinx.add_lexer("storyscript", StoryScriptLexer)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
	}
