from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = (
    "mysql+pymysql://4Q4gau7PkjqR9sR.root:"
    "D0GNS1Wf1O8df4Me"
    "@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test"
    "?ssl_ca=ca.pem"
    "&ssl_verify_cert=true"
    "&ssl_verify_identity=true"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()