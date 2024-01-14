# calc
This is my little CLI calculator. I did this once just to learn the basics of
Yacc and Flex. But actually, I use it every day.

The main feature is to evaluate arithmetic expression directly from the command line:
```shell
calc 21 * 2
```
To use it like this, I disable globbing for this command, by putting
```zshrc
alias calc='noglob calc'
```
into the `zshrc`.

# Build and Installation

To build calc, you need:
- GCC,
- Flex, and
- Bison

Clone the repository and build the command by running:

```sh
git clone https://github.com/mo42/calc.git && cd calc
make
```

# License

This project is licensed under the MIT License - see the LICENSE file for details.
