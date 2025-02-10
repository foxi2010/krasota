import matplotlib.pyplot as plt  

def plot_statistics(data):  
    plt.bar(data.keys(), data.values())  
    plt.title("Статистика парсинга")  
    plt.xlabel("Сайты")  
    plt.ylabel("Количество данных")  
    plt.show()  