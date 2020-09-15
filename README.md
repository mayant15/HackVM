# Hack Virtual Machine

An implementation for the Hack Virtual Machine created as part of the course [nand2tetris](https://www.nand2tetris.org/), but adapted to generate NASM style x86 assembly.

## Run
```
python ./VMTranslator.py <input>
```

As part of the VM specification, the `<input>` could be a single `.vm` file or a directory with multiple VM files combined to a single assembly file.

## Tests
The VM files in `tests/` are from the nand2tetris course and can be used to check if the translations are working.
