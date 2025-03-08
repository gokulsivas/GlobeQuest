from fastapi import APIRouter,Depends,status,Response,Query
from gq.schemas import Pkg_schema
from gq.database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from gq.repository.package import create_pkg, get_pkg, get_pkg_by_id, delete_pkg

router = APIRouter(
    prefix="/packages",
    tags = ['Packages']
)

@router.post('/',status_code=status.HTTP_201_CREATED)  
def create(request: Pkg_schema, db: Session = Depends(get_db)):    
    return create_pkg(request, db)

@router.get('/')
def getpkgs(country: Optional[str]=None, 
            price_min: Optional[float]=Query(None, ge=0), 
            price_max: Optional[float]=Query(None, ge=0),
            db: Session = Depends(get_db)):
    return get_pkg(db)

@router.get('/{id}')
def show(id: int ,response: Response, db: Session = Depends(get_db)):
    return get_pkg_by_id(id,response,db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return delete_pkg(id, db)