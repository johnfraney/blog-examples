# Human-Readable Python Regular Expressions

This repo contains the sample classes as described in my blog post, "[Human-Readable Python Regular Expressions](https://johnfraney.ca/posts/2019/03/22/human-readable-python-regular-expressions)".

## Example

```pycon
>>> from regex_patterns import Group
>>> group = Group('banana')
>>> print(group)
(banana)

>>> group.name = 'named_group'
>>> print(group)
(?P<named_group>banana)
```

Thanks for visiting!
