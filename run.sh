#! /bin/bash

if [ ! -d daggen ]; then
  git clone https://github.com/frs69wq/daggen.git
fi

cd daggen &&  make > /dev/null && cd -

if [ "$1" == "check" ]; then
  ./daggen/daggen
  exit 0
fi

./daggen/daggen -n 20 2> /dev/null | python3 tss.py
