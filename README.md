# scanned.sh
Make files look like scanned for troublesome bureaucrats who require you to print out documents, sign them, and send an electronic copy.
```shell
scanned.sh original.pdf original_scanned.pdf
```

# calc
Evaluate arithmetic expression directly from the command line:
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

```sh
git clone https://github.com/mo42/bin.git && cd bin
make -C calc install
```

# License

This project is licensed under the MIT License - see the LICENSE file for details.
