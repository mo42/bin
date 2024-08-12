#!/bin/sh

shopt -s nullglob globstar
prefix=${PASSWORD_STORE_DIR:-$HOME/.password-store}

for file in "$prefix"/**/*.gpg; do
    file="${file/$prefix/}"
    printf "%s\n" "${file%.*}" >> exported_passes
    pass "${file%.*}" >> exported_passes
    printf "\n" >> exported_passes
done
