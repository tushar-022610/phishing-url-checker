# Phishing URL Awareness Checker

A beginner-friendly Python command-line tool that checks a URL for common phishing-awareness warning signs.

## Project Overview

The Phishing URL Awareness Checker helps users understand some common characteristics that may appear in suspicious URLs.

The tool analyzes the URL text locally and displays warning indicators. It does not open the URL or make any network requests.

## Features

The checker looks for these common warning signs:

1. `@` symbol in the URL
2. URL longer than 100 characters
3. IP address used as the hostname
4. Five or more hostname labels/subdomains
5. Possible punycode (`xn--`) in the hostname
6. HTTP instead of HTTPS

## How It Works

The user enters a URL into the command-line program.

The program parses the URL and checks it against the warning-sign rules.

If warning signs are found, they are displayed as a numbered list.

If no common warning signs are detected, the program displays a message indicating that no common indicators were found.

## Example

A normal example:

```text
https://example.com
