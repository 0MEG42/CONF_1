from ctypes import * ;
import matplotlib.pyplot as plt ;



if __name__=='__main__':
    
    C_Complement_Function =  CDLL('build\Debug\comp_1.dll')
    print(C_Complement_Function.ras(34))
    fig, ax = plt.subplots()
    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [C_Complement_Function.ras(70), C_Complement_Function.ras(100), 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')
    plt.show()
