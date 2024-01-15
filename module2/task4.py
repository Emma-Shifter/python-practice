films = {"Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо",
         "Отступники", "Деревня"}

favFilms = set()
favCount = int(input("Сколько фильмов хотите добавить? "))

for i in range(favCount):
    film = input("Введите название фильма: ")

    if film in films:
        if film in favFilms:
            print("Фильм уже добавлен в избранные!")
        else:
            favFilms.add(film)
    else:
        print(f"Ошибка: фильма {film} у нас нет :(")

print(f"Ваш список любимых фильмов: {', '.join(favFilms)}")