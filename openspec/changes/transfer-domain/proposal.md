# Change: Transfer domain ownership

## Intent
Allow a domain to move from one existing hosting account to another.

## Acceptance criteria
- Domain must exist; otherwise HTTP 404.
- Destination account must exist; otherwise HTTP 404.
- Ownership remains unique after transfer.
- Transfer to current account is idempotent.
- Tests cover valid and invalid transfers.

## Student exercise
Propose a plan, update the specification, implement the endpoint, and run tests.
