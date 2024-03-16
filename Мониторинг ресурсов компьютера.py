# Сначала через командную строку установили psutil
import psutil
import time

def monitor_resources(interval=2): # Частота обновления информации
    try:
        while True:
    # Получаем информацию о состоянии процессора
            cpu_percent = psutil.cpu_percent(interval=interval)
    # Получаем информацию о оперативной памяти
            memory_info = psutil.virtual_memory()  
    # Получаем информацию о дисковом пространстве
            disk_info = psutil.disk_usage("/")
    # Вывод информацию на экран
            print("-" * 70)
            #Вывод информации о потоках
            print("Количество потоков процессора", psutil.cpu_count())
            #Вывод информации о ядрах
            print("Количество физических ядер процессора", psutil.cpu_count(logical=False))
            #Вывод информации о процессах
            print(f"Процессор: {cpu_percent}% ")
            #Вывод информации об оперативной памяти
            print(f"Оперативная память: {memory_info.percent}% используется")
            #Вывод информации о дисках
            print(f"Диск: {disk_info.percent}% занято")
            print("-" * 70)
            print("Команда разработчиков ЕРАВНА")
            #70 знаков -
            print("-" * 70)
            
            # Ждем указанный интервал перед следующим измерением
            time.sleep(interval)
    
    except KeyboardInterrupt:
        print("Мониторинг завершен.")

# Вызываем функцию для мониторинга ресурсов
monitor_resources()



      #Пытались сделать, но что то пошло не так
    #print(psutil.sensors_temperatures())
