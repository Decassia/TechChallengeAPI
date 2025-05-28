from typing import List, Optional

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.deps import get_session, get_current_user
from models.user_model import UserModel
from models.comercializacao_model import ComercializacaooModel
from schemas.comercializacao_schema import ComercializacaoSchema



router = APIRouter()


# GET Produtos
@router.get('/', response_model=List[ComercializacaoSchema])
async def get_comercializacao(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ComercializacaooModel)
        result = await session.execute(query)
        comercializacao: List[ComercializacaooModel] = result.scalars().unique().all()

        return comercializacao


@router.get('/filtro_ano', response_model=List[ComercializacaoSchema], status_code=status.HTTP_200_OK)
async def filtrar_ano(
        ano_min: Optional[int] = None,
        ano_max: Optional[int] = None,
        db: AsyncSession = Depends(get_session),

):
    async with db as session:
        query = select(ComercializacaooModel)

        if ano_min is not None:
            query = query.where(ComercializacaooModel.ano >= ano_min)
        if ano_max is not None:
            query = query.where(ComercializacaooModel.ano <= ano_max)

        result = await session.execute(query)
        comercializacao = result.scalars().all()

        if comercializacao:
            return comercializacao
        else:
            raise HTTPException(status_code=404, detail="Nenhum dado encontrado no intervalo especificado.")




