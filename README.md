# ninoCan - Zettelkasten

> [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten): card file, coming from (German) _zetteln_ meaning slip/note, and _kasten_ meaning crate/box.

This is a collection of personal notes.


## How to zettelkasten?

This is the process of producing semi-structured, concise notes for future reference, and rapid brain off-loading.
**My** Zettelkasten notes follows this template:

```
---
date: <date-of-creation>
<metadata>
---

# <unique id> - <title>

<Few sentencences exploring a concept or idea>

## connections:
[<anchor>]: <link> "title"
```

## Additional tools

Because of the semi-structured nature of the notes, it might be useful to leverage external tools to reduce redundant operations.

### Custom uv script 

In the `generator` directory, there should be at least two files `note.md.j2` and `new_note.py`.

To invoke the note rendering call:

```
new-note "Title of the note"
```
