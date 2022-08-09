#!/bin/bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
if [ ! -d cppcheck/ ]; then
  git clone https://github.com/danmar/cppcheck.git
fi

cd cppcheck
git fetch --all
git checkout 61f846073d9c348b408b21230790007bc8a022c2
make clean
make MATCHCOMPILTER=yes CXXFLAGS="-O2" -j8
