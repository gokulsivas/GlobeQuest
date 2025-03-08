from fastapi import Depends,status, Response, Query
from gq.models import Pkg_model
from gq.database import get_db
from sqlalchemy.orm import Session
from typing import List

def create_pkg(request: Pkg_model, db: Session = Depends(get_db)):
    new_pkg = Pkg_model(title=request.title,
                    description=request.description,
                    country=request.country,
                    type=request.type,
                    nodays=request.nodays,
                    price=request.price,
                    imgname=request.imgname)
    db.add(new_pkg)
    db.commit()
    db.refresh(new_pkg)
    return new_pkg

def get_pkg(db: Session = Depends(get_db)):
    result =db.query(Pkg_model).all()
    return result

def get_pkg_by_id(id: int,response: Response,db: Session= Depends(get_db)):
    package = db.query(Pkg_model).filter(Pkg_model.id == id).first()
    if not package:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Detail':f"Blog with the id {id} is not found"}
    return package

def delete_pkg(id: int, db: Session = Depends(get_db)):
    pkgs = db.query(Pkg_model).filter(Pkg_model.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'