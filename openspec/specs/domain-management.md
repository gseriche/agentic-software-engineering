# Domain management — baseline specification

## Requirements
- A hosting account MAY have multiple domains.
- A domain MUST belong to exactly one hosting account.
- A domain name MUST be globally unique (case-insensitive).
- Creating a domain for a missing account MUST return HTTP 404.
- Creating a duplicate domain MUST return HTTP 409.
- Domains MUST be listable by account.

## Acceptance
Automated tests cover ownership, duplicate rejection and missing accounts.
