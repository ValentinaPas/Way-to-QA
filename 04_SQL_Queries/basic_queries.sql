-- Примеры SQL-запросов для проверки данных (тестирование БД интернет-магазина)

-- 1. Выборка всех активных пользователей (базовый SELECT + WHERE)
-- Проверяем, что в базе нет удаленных пользователей (is_active = 0)
SELECT id, email, created_at 
FROM users 
WHERE is_active = 1;

-- 2. Поиск заказов конкретного пользователя (JOIN двух таблиц)
-- Проверяем, что история заказов привязана к правильному пользователю
SELECT o.order_id, o.total_amount, u.email 
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.email = 'test@mail.ru';

-- 3. Подсчет количества заказов по статусам (GROUP BY)
-- Проверяем корректность статусов заказов (например, сколько заказов в обработке, сколько доставлено)
SELECT status, COUNT(*) as order_count
FROM orders
GROUP BY status;

-- 4. Выборка товаров, которых нет в наличии (проверка остатков)
SELECT product_name, quantity 
FROM products 
WHERE quantity = 0;

-- 5. Поиск дубликатов email в базе (частая проверка на баг с регистрацией)
SELECT email, COUNT(email) 
FROM users 
GROUP BY email 
HAVING COUNT(email) > 1;
