import tkinter as tk

# Создаем основное окно
root = tk.Tk()
root.title("Дом на холсте")

# Создаем холст
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Рисуем основание дома
canvas.create_rectangle(100, 200, 300, 400, fill="lightbrown", outline="black")

# Рисуем крышу
canvas.create_polygon(100, 200, 200, 100, 300, 200, fill="darkred", outline="black")

# Рисуем дверь
canvas.create_rectangle(175, 300, 225, 400, fill="brown", outline="black")

# Рисуем окна
canvas.create_rectangle(125, 225, 175, 275, fill="lightblue", outline="black")  # Левое окно
canvas.create_rectangle(225, 225, 275, 275, fill="lightblue", outline="black")  # Правое окно

# Рисуем ручку двери
canvas.create_oval(210, 350, 220, 360, fill="yellow", outline="black")

# Запускаем главный цикл обработки событий
root.mainloop()