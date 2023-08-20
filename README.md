# Johnny Translator

This is a simple Johnny Assembler to RAM code translator written in Python. It converts Johnny Assembler code into a format that can be executed by the Johnny Decimal computer simulator.

## Instructions

### Installation

1. Clone the repository or download the code.
2. Navigate to the directory where the code is located.

### Usage

To run the translator, execute the following command:

```bash
python3 translator/johnny_translator.py -a Example_IDIV.asm
```

- The `-a` flag outputs a formatted assembler file that is closer to the RAM code, which can be helpful for debugging.

Alternatively, you can make the script executable:

```bash
chmod +x translator/johnny_translator.py
```

Then run it directly:

```bash
./translator/johnny_translator.py -a Example_IDIV.asm
```

If this isn't working, check out [this guide on Python shebang](https://realpython.com/python-shebang/).

### Johnny Commands

| Command | Decimal Code | Description                          |
|---------|-------------|--------------------------------------|
| TAKE    | 01          | Load a value into the accumulator    |
| ADD     | 02          | Add a value to the accumulator       |
| SUB     | 03          | Subtract a value from the accumulator|
| SAVE    | 04          | Save the accumulator's value         |
| JUMP    | 05          | Jump to a specific line              |
| TST     | 06          | Test the accumulator's value         |
| INC     | 07          | Increment the value at an address    |
| DEC     | 08          | Decrement the value at an address    |
| NULL    | 09          | No operation                         |
| HLT     | 10          | Halt the program                     |

### Variables and Labels

- Variables can be defined using the `#define` directive, like so: `#define variable_name value`.
- Variables are automatically moved to the end of the code, rounded to the next multiple of 10.
- The script will provide a variable map as terminal output for easier debugging.

- Labels can be defined with a colon, like so: `test_label:`.
- Use `JUMP test_label` to jump to the label's location in the code.

---

Feel free to add or modify any sections as you see fit!
