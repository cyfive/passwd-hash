#!/bin/bash
#
# Helper script for generating salted password hashes
# Author: Stanislav V. Emets <emetssv@mail.ru>
#

DEBUG=${DEBUG:-0}

if [ $DEBUG -gt 1 ]; then
    set -xe
else
    set -e
fi

# Configuration parameters, adjust it for your security policy
# like:
#   export SALT_LENGTH=10
#
# Salt lenght, default: 16
SALT_LENGTH=${SALT_LENGTH:-16}
# Hashing method, default is: SHA512
# MD5: 1, SHA256: 5, SHA512: 6
CIPHER="-${CIPHER:-'6'}"

# Generate random salt
SALT=`head /dev/urandom | tr -dc A-Za-z0-9 | head -c ${SALT_LENGTH}`

# Debug output
if [ $DEBUG -gt 0 ]; then
    echo "Salt lenght: ${SALT_LENGTH}"
    echo "Chipher: ${CIPHER}"
    echo "Random salt: \$${CIPHER/-/}\$${SALT}"
fi
if [ -z "$CIPHER" ]; then
    echo "Hash algorithm not defined!"
    exit 1
fi
if [ -z "$SALT" ]; then
    echo "Salt not generated, please check SALT_LENGTH parameter!"
    exit 2
fi

openssl passwd ${CIPHER} --salt ${SALT}
