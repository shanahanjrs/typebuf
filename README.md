# TypeBuf

[![CircleCI](https://circleci.com/gh/shanahanjrs/typebuf/tree/master.svg?style=svg)](https://circleci.com/gh/shanahanjrs/typebuf/tree/master)
[![codecov](https://codecov.io/gh/shanahanjrs/typebuf/branch/master/graph/badge.svg?token=9J1OCNHSZF)](https://codecov.io/gh/shanahanjrs/typebuf)

---

### Dead simple way to define shared type definitions between applications

- Other tools have too much setup? Too much boilerplate? Do too much "magic"? Just:
  - Define your Types in `types.yaml`
  - Run TypeBuf: `$ typebuf compile -f types.yaml -l python -l typescript`

## Install

`pip install typebuf`


## Quickstart

1. Create a file called `types.yaml`, it can be anywhere, like your project's root dir
 

2. Add the following lines to the newly created file:

```
---
typedefs:
  - typename: User
    fields:
      - name: first_name
        type: string
        optional: false
      - name: age
        type: int
        optional: true
```


3. Now call TypeBuf with: `$ typebuf compile -l python -l typescript`


4. You now have two new files, one called `user.py` and one called `user.ts` that can you use for 
    things like data serialization/deserialization, validation, subclassing, etc


## Demo

> Here's a quick demo of me using TypeBuf. First I show the contents of the _types.yaml_ file
> then I generate Python and TypeScript source code and show the contents of the new files

[![asciicast](https://asciinema.org/a/KRGKPMQ1HCd3OtwJbLvHYWUlJ.svg)](https://asciinema.org/a/KRGKPMQ1HCd3OtwJbLvHYWUlJ)


## Documentation

- Reads only a file named `types.yaml` (for now)
- Inside that file there is an array called `typedefs`. This is where you add your shared type definitions
- Each type will have the following fields:
  - `typename: string`
  - `fields: array[Field]`
    - A `Field` has the following attributes:
      - name: _string_
      - type: _string_
      - optional: _boolean_
