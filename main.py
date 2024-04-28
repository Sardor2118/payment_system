from fastapi import FastAPI
from card.card_api import card_router
from transfers.transfer_api import transaction_router
from user.user_api import user_router
from database import Base, engine
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/")
app.include_router(card_router)
app.include_router(transaction_router)
app.include_router(user_router)