#!/usr/bin/env python3
#
# Helper script for generating password hash.
# Author: Stanislav V. Emets <emetssv@mail.ru>
#

import crypt, getpass, os

# Get environment congiguration
DEBUG = int(os.environ.get('DEBUG', '0'))
SALT_LENGTH = int(os.environ.get('SALT_LENGTH', '16'))
ENV_CIPHER = os.environ.get('CIPHER', '6')

if DEBUG > 0:
    print(f'Salt length: {SALT_LENGTH} (ignored in python version)')
    print(f'Cipher: {ENV_CIPHER}')

CIPHER = None

for method in crypt.methods:
    if method.ident == ENV_CIPHER:
        CIPHER = method

salt = crypt.mksalt(CIPHER)

if DEBUG > 0:
    print(f'Random salt: {salt}')

passwd = getpass.getpass()

if passwd:
    passwd_hash = crypt.crypt(passwd, salt)
    print(passwd_hash)
else:
    print('Empty password!')
