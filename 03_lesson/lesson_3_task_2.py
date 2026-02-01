from smartphone import Smartphone

# Создаем список книг (библиотеку)
catalog = [
    Smartphone("Samsyng", "S27", "89123456789"),
    Smartphone("APPL", "17 pro", "89987654321"),
    Smartphone("Xiomi", "Redmi Note 14", "89753124680"),
    Smartphone("Huawei", "Pura 80 Pro", "8908642135799"),
    Smartphone("Oppo", "A5 PRO", "89654372819")
]

# Печатаем библиотеку
for smartphone in catalog:
    print(f"{smartphone.p_b} - {smartphone.p_m}"
          f". {smartphone.number}")
