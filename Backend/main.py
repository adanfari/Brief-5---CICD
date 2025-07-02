from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from loguru import logger
from Backend.modules.calcul import calcul  # noqa: E402

app = FastAPI(title='FastAI Template API')


class Input(BaseModel):
    n: int


@app.get('/')
async def root():
    logger.info('Root endpoint called')
    return {'message': 'Bienvenue sur l\'API FastAI template'}


@app.get('/health')
async def health():
    logger.info('Healthcheck OK')
    return {'status': 'OK'}


@app.post('/calcul')
async def compute_square(payload: Input):
    try:
        result = calcul(payload.n)
        logger.info(f'Square computed for {payload.n}: {result}')
        return {'result': result}
    except Exception as exc:
        logger.error(f'Error computing square: {exc}')
        raise HTTPException(status_code=500, detail=str(exc))