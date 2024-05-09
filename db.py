import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

ejemplos_sucursales = [
        ('Don Miguel', 'Av. Arequipa 123, Lima'),
        ('Supermercado El Inca', 'Calle 9 de Octubre 456, Arequipa'),
        ('Mini Market La Esquina', 'Jr. Manco Capac 789, Cusco'),
        ('Bodega La Perla', 'Av. España 012, Trujillo'),
        ('Mini Market Doña Rosa', 'Calle Los Algarrobos 345, Piura')
]
ejemplos_itemproveedor = [
        ('Arroz Doria 1 kg', 'Doria Distribuciones', '1 kg', 102, 10, 2.50),
        ('Azúcar Blanca Inca 1 kg', 'Inca Azúcares', '1 kg', 52, 10, 3.20),
        ('Aceite Girasol Primor 1 litro', 'Aceites Primor', '1 litro', 186, 10, 5.50),
        ('Sal Marasal 500 g', 'Marasal SA', '500 g', 342, 10, 1.80),
        ('Fideos Tallarín Don Vicente 500 g', 'Fideos Don Vicente', '500 g', 95, 10, 2.00)
    ]

for item in ejemplos_itemproveedor:
    cursor.execute("INSERT INTO compras_itemproveedor (item, proveedor, cantidad_por_unidad, unidades, minimo_unidades, costo) VALUES (?, ?, ?, ?, ?, ?)", item)

for sucursal in ejemplos_sucursales:
    cursor.execute("INSERT INTO compras_sucursal (nombre, direccion) VALUES (?, ?)", sucursal)
    
conn.commit()
conn.close()