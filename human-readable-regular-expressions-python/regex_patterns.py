import re
from dataclasses import dataclass


class PatternException(Exception):
    pass


@dataclass
class PatternPart(object):
    """A regex pattern fragment."""
    pattern: str

    def __str__(self):
        return self.pattern


class LookaheadLookbehindMixin(object):
    """Lookahead and lookbehind assertion mixin.

    Attributes:
        negative: A boolean denoting a negative lookahead/-behind.
    """
    negative: bool = False

    @property
    def polarity(self):
        return r'!' if self.negative else r'='


@dataclass
class LookAhead(LookaheadLookbehindMixin, PatternPart):
    """Lookahead assertion."""
    def __str__(self):
        return r'(?{polarity}{pattern})'.format(
            polarity=self.polarity,
            pattern=self.pattern
        )


@dataclass
class LookBehind(LookaheadLookbehindMixin, PatternPart):
    """Lookbehind assertion."""
    def __str__(self):
        return r'(?<{polarity}{pattern})'.format(
            polarity=self.polarity,
            pattern=self.pattern,
        )


@dataclass
class Group(PatternPart):
    """Group.

    Attributes:
        name: A string that identifies this as a named capture group.
        capturing: A boolean indicating whether this group matches.
    """
    greedy: bool = True
    name: str = ''
    capturing: bool = True
    one_or_more: bool = False
    zero_or_more: bool = False

    def __str__(self):
        if self.one_or_more and self.zero_or_more:
            raise PatternException(
                'Pattern cannot be both one and zero or more'
            )
        if self.name:
            pattern = r'(?P<{name}>{pattern})'.format(
                name=self.name, pattern=self.pattern
            )
        else:
            capturing_symbol = r'?:' if not self.capturing else r''
            pattern = r'({capturing_symbol}{pattern})'.format(
                capturing_symbol=capturing_symbol, pattern=self.pattern
            )

        if self.one_or_more:
            pattern += r'+'

        if self.zero_or_more:
            pattern += r'*'

        if not self.greedy:
            pattern += r'?'

        return pattern


def build_pattern(*pattern_parts) -> str:
    """Joins PatternPart instance strings."""
    return r''.join(str(part) for part in pattern_parts)


if __name__ == '__main__':
    one_or_more_lines_non_greey = Group(
        '.*\n', capturing=False, one_or_more=True, greedy=False
    )

    pattern = build_pattern(
        LookBehind('```python\n'),
        Group(one_or_more_lines_non_greey),
        LookAhead('```'),
    )

    markdown_content = """
# Markdown File

```python
def print_banana():
    print('banana')
```

This is a lovely--albeit unimportant--paragraph.

```python
def print_chocolate():
    print('chocolate')
```
"""

    matches = re.findall(pattern, markdown_content, re.MULTILINE)
    print(matches)
