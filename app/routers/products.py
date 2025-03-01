from fastapi import APIRouter

router = APIRouter(prefix='/products', tags=['products'])


@router.get('/') # Метод получения всех товаров
async def all_products():
    pass


@router.post('/create') # Метод создания товара
async def create_products():
    pass


@router.get('/{category_slug}') # Метод получения товаров определенной категории
async def product_dy_category(category_slug: str):
    pass

@router.get('/detail/{product_slug}') # Метод получения детальной информации о товаре
async def product_detail(product_slug: str):
    pass


@router.put('/detail/{product_slug}') # Метод изменения и удаления товара
async def update_product(product_slug: str):
    pass


@router.delete('/delete') 
async def delete_product(product_id: int):
    pass