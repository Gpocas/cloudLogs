import logging
import logging_loki


handler = logging_loki.LokiHandler(
    url="http://localhost:3100/loki/api/v1/push", 
    tags={"application": "teste-app"},
    version="1",
)

logger = logging.getLogger(__name__)
logger.addHandler(handler)


# logger.error(
#     "Esse é um teste de erro", 
#     extra={"tags": {"service": "teste"}},
# )


try:
   32 / 0
except Exception as exc:
    logger.exception(exc,
                     extra={"tags": {"severity": "exception"}})
    

logger.info('requisição enviada')
# logger.warning('requisição demorou muito')


