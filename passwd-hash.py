#!/usr/bin/env python3
#
# Helper script for generating password hash.
# Author: Stanislav V. Emets <emetssv@mail.ru>
#

# This file is part of passwd-hash.
#    Passwd-hash is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Passwd-hash is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

import crypt, getpass, os

# Get environment congiguration
DEBUG = int(os.environ.get('DEBUG', '0'))
SALT_LENGTH = int(os.environ.get('SALT_LENGTH', '16'))
ENV_CIPHER = os.environ.get('CIPHER', '6')
ENV_SALT = os.environ.get('SALT', '')

if DEBUG > 0:
    print(f'Salt length: {SALT_LENGTH} (ignored in python version)')
    print(f'Cipher: {ENV_CIPHER}')

CIPHER = None

for method in crypt.methods:
    if method.ident == ENV_CIPHER:
        CIPHER = method

if not ENV_SALT:
    salt = crypt.mksalt(CIPHER)
else:
    salt = ENV_SALT

if DEBUG > 0:
    print(f'Salt: {salt}')

passwd1 = getpass.getpass(prompt='Password:')
passwd2 = getpass.getpass(prompt='Re-type password:')

if passwd1:
    if passwd1 == passwd2:
        passwd_hash = crypt.crypt(passwd1, salt)
        print(passwd_hash)
    else:
        print('Passwords is different! Please try again!')
else:
    print('Password is empty!')
