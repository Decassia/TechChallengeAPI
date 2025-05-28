from typing import List, Optional

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.deps import get_session, get_current_user
from models.user_model import UserModel
from schemas.exportacao_schema import ExportacaoSchema
from models.exportacao_model import ExportacaoModel



router = APIRouter()


# GET Produtos
@router.get('/', response_model=List[ExportacaoSchema])
async def get_exportacao(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ExportacaoModel)
        result = await session.execute(query)
        exportacao = result.scalars().unique().all()

        return [ExportacaoSchema.model_validate(item) for item in exportacao]



@router.get('/filtro_ano', response_model=List[ExportacaoSchema], status_code=status.HTTP_200_OK)
async def filtrar_ano(
        ano_min: Optional[int] = None,
        ano_max: Optional[int] = None,
        db: AsyncSession = Depends(get_session),

):
    async with db as session:
        query = select(ExportacaoModel)

        if ano_min is not None:
            query = query.where(ExportacaoModel.ano >= ano_min)
        if ano_max is not None:
            query = query.where(ExportacaoModel.ano <= ano_max)

        result = await session.execute(query)
        exportacao = result.scalars().all()

        if exportacao:
            return exportacao
        else:
            raise HTTPException(status_code=404, detail="Nenhum dado encontrado no intervalo especificado.")
