import logging
import logging_loki


handler = logging_loki.LokiHandler(
    url="http://localhost:3100/loki/api/v1/push", 
    tags={"application": "cloudLogs"},
    version="1",
)

logger = logging.getLogger(__name__)
logger.addHandler(handler)


logger.warning('requisição demorou muito',
    extra={"tags": {"service": "api"}},

)
logger.error(
    "Erro com banco de dados", 
    extra={"tags": {"service": "postgres"}},
)


try:
   32 / 0
except Exception as exc:
    logger.exception(exc,
                     extra={"tags": {"severity": "exception"}})
    

