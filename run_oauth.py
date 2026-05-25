"""One-shot OAuth runner for open-ghl-mcp custom mode.

Triggers the full OAuth flow: builds the chooselocation URL, starts a callback
listener on localhost:8080, waits for the user to authorize, exchanges the code
for tokens, and writes them to config/tokens.json.
"""

import asyncio
import sys

from src.services.oauth import OAuthService, AuthMode


async def main() -> int:
    svc = OAuthService()
    if svc.settings.auth_mode != AuthMode.CUSTOM:
        print(f"[error] auth_mode={svc.settings.auth_mode.value}, expected 'custom'", file=sys.stderr)
        print("[hint] Set AUTH_MODE=custom in .env", file=sys.stderr)
        return 2

    print(f"[oauth] client_id={svc.settings.ghl_client_id}")
    print(f"[oauth] redirect_uri={svc.settings.oauth_redirect_uri}")
    print("[oauth] starting flow ...")
    token = await svc.authenticate()
    await svc.save_token(token)
    print(f"[oauth] saved tokens to {svc.settings.token_storage_path}")
    print(f"[oauth] access_token (first 12): {token.access_token[:12]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
