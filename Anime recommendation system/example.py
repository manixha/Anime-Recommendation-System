# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:55:43 2023

@author: Admin
"""

import secrets


def get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]


code_verifier = code_challenge = get_new_code_verifier()

print(len(code_verifier))
print(code_verifier)

