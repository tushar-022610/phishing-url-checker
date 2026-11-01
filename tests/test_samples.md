# Test Samples

## Test 1 — Normal URL

Input:
https://example.com

Expected:
No common warning signs detected.

## Test 2 — IP Address and HTTP

Input:
http://192.0.2.10/account

Expected warning signs:
- Hostname is an IP address.
- URL uses HTTP instead of HTTPS.

## Test 3 — URL with @ Symbol

Input:
https://example.com@192.0.2.10/login

Expected warning signs:
- URL contains '@' symbol.
- Hostname is an IP address.

## Test 4 — Many Subdomains

Input:
https://a.b.c.d.example.com/login

Expected warning sign:
- Hostname contains 5 or more labels/subdomains.
