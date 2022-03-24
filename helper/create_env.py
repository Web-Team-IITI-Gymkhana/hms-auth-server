def create_env():
    with open(".env", "w") as f:
        f.write("ENVIRONMENT=DEVELOPMENT\n")
        f.write("PGUSER=\n")
        f.write("PGPASSWORD=\n")
        f.write("PGHOST=\n")
        f.write("PGPORT=\n")
        f.write("PGDATABASE=\n")
        f.write("PRIVATE_KEY=\n")
        f.write("PUBLIC_KEY=\n")
        f.write("API_ALGORITHM=\n")
        f.write("ACCESS_TOKEN_EXPIRE_MINUTES=\n")
        f.write("REFRESH_TOKEN_EXPIRE_MINUTES=\n")