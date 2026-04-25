import sqlite3

con = sqlite3.connect('shop.db')
cur = con.cursor()
while True:
    print('1. Вивести всі товари')
    print('2. Додати товар')
    print('3. Видалити товар')
    print('4. Вихід')
    choice = input('Виберіть дію: ')

    if choice == '1':
        cur.execute('SELECT * FROM products')
        products = cur.fetchall()
        for product in products:
            print(product)

    elif choice == '2':
        name = input('Введіть назву товару: ')
        price = float(input('Введіть ціну товару: '))
        cur.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        con.commit()
        print('Товар додано!')
    
    elif choice == '3':
        product_id = int(input('Введіть ID товару для видалення: '))
        cur.execute('DELETE FROM products WHERE id = ?', (product_id,))
        con.commit()
        print('Товар видалено!')
    
    elif choice == '4':
        print('Вихід з програми.')
        break
    else:
        print('Невірний вибір, спробуйте ще раз.')

con.close()