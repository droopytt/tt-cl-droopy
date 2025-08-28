#!/bin/sh
cd ../astron

# This assumes that your astrond build is located in the
# "astron" directory, and is named "astrond".
./astrond --loglevel info config/astrond.yml
