from fastapi import APIRouter

router = APIRouter(prefix='/category', tags=['category'])

@router.get('/all_categories')  # Метод получения всех категорий
async def get_all_categories():
    pass
 
@router.post('/create') # Метод создания категории
async def create_categories():
    pass

@router.put('/update_categories') # Метод изменения категории
async def update_categories():
    pass

@router.delete('/delete') # Метод удаления категории
async def delete_categories():
    pass
