import logging
from fastapi import Depends
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse

from api import card
from controller.get_card_controller import GetCardController


logger = logging.getLogger(__name__)


def create_app():
    doc_opt = {
        "docs_url": "/api_doc/tes/swagger",
        "redoc_url": "/api_doc/tes/redoc",
        "openapi_url": "/api_doc/tes/openapi.json",
    }
    app = FastAPI(
                    title='Zettelkasten sender API',
                    description= 'Send daily card',
                    version='v1',
                    **doc_opt
                )

    # add all routes here
    prefix = "/api/v1"
    app.include_router(card.router, prefix=prefix)

    @app.get('/', include_in_schema=False)
    def health_check():
        return PlainTextResponse("This page is for health check.")

    return app
