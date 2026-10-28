## Классы Product и Category

### Product
- `name` (str) — название товара
- `description` (str) — описание
- `price` (float) — цена
- `quantity` (int) — количество на складе

### Category
- `name` (str) — название категории
- `description` (str) — описание
- `products` (list[Product]) — список товаров
- `category_count` (class attribute) — общее количество созданных категорий
- `product_count` (class attribute) — общее количество товаров во всех категориях

При создании категории `category_count` увеличивается на 1, а `product_count` — на длину переданного списка `products`. 