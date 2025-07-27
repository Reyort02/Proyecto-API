from fastapi import Request, HTTPException, status
from src.security.jwt import verify_token

async def verify_token_middleware(request: Request):
    if request.url.path.startswith("/tasks"):
        try:
            auth_header = request.headers["Authorization"]
            if not auth_header.startswith("Bearer "):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication scheme",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            token = auth_header.split(" ")[1]
            user = verify_token(token)
            request.state.user = user
        except KeyError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except HTTPException as e:
            raise e
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
