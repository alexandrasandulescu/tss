#! /bin/bash

if [ ! -d daggen ]; then
  git clone https://github.com/frs69wq/daggen.git
fi

cd daggen && make && cd -

echo $(./daggen/daggen 2> /dev/null) | python tss.py
