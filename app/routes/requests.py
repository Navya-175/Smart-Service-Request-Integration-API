from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import get_db
from ..dependencies import get_current_user
from ..models import ServiceRequest, User
from ..schemas import ServiceRequestCreate, ServiceRequestResponse, ServiceRequestUpdate, StatusUpdate

router = APIRouter(prefix="/api/v1/requests", tags=["Service Requests"])

def owned(request_id: int, user: User, db: Session):
    item = db.scalar(select(ServiceRequest).where(ServiceRequest.id == request_id, ServiceRequest.user_id == user.id))
    if not item:
        raise HTTPException(status_code=404, detail="Service request not found")
    return item

@router.post("", response_model=ServiceRequestResponse, status_code=status.HTTP_201_CREATED)
def create(data: ServiceRequestCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    item = ServiceRequest(**data.model_dump(), user_id=user.id)
    db.add(item); db.commit(); db.refresh(item)
    return item

@router.get("", response_model=list[ServiceRequestResponse])
def list_all(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.scalars(select(ServiceRequest).where(ServiceRequest.user_id == user.id).order_by(ServiceRequest.id.desc())).all()

@router.get("/{request_id}", response_model=ServiceRequestResponse)
def get_one(request_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return owned(request_id, user, db)

@router.put("/{request_id}", response_model=ServiceRequestResponse)
def update(request_id: int, data: ServiceRequestUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    item = owned(request_id, user, db)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit(); db.refresh(item)
    return item

@router.patch("/{request_id}/status", response_model=ServiceRequestResponse)
def update_status(request_id: int, data: StatusUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    item = owned(request_id, user, db)
    item.status = data.status
    db.commit(); db.refresh(item)
    return item

@router.delete("/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(request_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    item = owned(request_id, user, db)
    db.delete(item); db.commit()
    return None
