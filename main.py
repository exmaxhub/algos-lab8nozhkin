"""
### Задача 1: Средние расходы по семестрам  
Джон записал свои ежемесячные расходы за прошлый год:  
```python
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
```  
Напишите программу, которая с помощью цикла `for` вычисляет средние расходы Джона за первый семестр (январь–июнь) и второй семестр (июль–декабрь).  

monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
first_semester = monthly_spending[:6]
second_semester = monthly_spending[6:]
avg_one = sum(one_semester) / len(one_semester)
avg_two = sum(two_semester) / len(two_semester)
print("Первый: ", avg_one)
print("Второй: ", avg_two)


### Задача 2: Кто тратил больше? 
У Джона есть друг Сэм, который также записал свои ежемесячные расходы за прошлый год:  
```python
john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]  
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]
```  
Напишите программу, которая сравнивает расходы Джона и Сэма по месяцам и подсчитывает количество месяцев, в которых Джон тратил больше.  

john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]  
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]
print(sum(john_monthly_spending > sam_monthly_spending for john_monthly_spending, sam_monthly_spending in zip(john_monthly_spending, sam_monthly_spending)))

    
### Задача 3: Список друзей  
У Пола и Тины есть списки друзей:  
```python
paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
```  
Объедините оба списка в один, исключив дублирующиеся имена.  

paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
all_friends = set(paul_friends + tina_friends)
print (all_friends)



### Задача 4: Общие друзья  
Используя те же списки друзей Пола и Тины, напишите программу, которая с помощью цикла находит их общих друзей.  

paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
all_friends = []
for friend in paul_friends:
    if friend in tina_friends:
        all_friends.append(friend)
print (all_friends)



### Задача 5: Игроки в баскетбол  
В спортивном клубе зарегистрированы игроки:  
```python
football_players = {"Eve", "Tom", "Richard", "Peter"}  
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}
```  
Напишите программу, которая определяет игроков, зарегистрированных только в баскетболе (не в футболе и не в волейболе).  

football_players = {"Eve", "Tom", "Richard", "Peter"}  
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}
only_basket = basketball_players - volleyball_players - football_players
print(only_basket)


### Задача 6: Подсчёт голосов  
Результаты опроса о любимом языке программирования:  
```python
poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]
```  
Используя словарь, подсчитайте количество голосов за каждый язык.  

poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]
poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]
voice_count = {}
for results in poll_results:
    if results in voice_count:
        voice_count[results] += 1 
    else:
        voice_count[results] = 1 
    for option, count in voice_count.items():
        print(f"{option}: {count} голосов")


### Задача 7: Подсчёт очков  
Три друга играют в игру, где каждый игрок зарабатывает очки в трёх раундах. Их результаты:  
```python
scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]
```  
Создайте словарь, где ключами будут имена игроков, а значениями — их суммарные очки.  

scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]
all_points = {}
for name, score in scores:
    if name in all_points:
        all_points[name] += score
    else:
        all_points[name] = score
print(all_points)


### Задача 8: Статистика списка  
Дан список чисел:  
```python
numbers = [10, 3, 5, 9, 18, 3, 0, 7]
```  
Напишите функцию, которая возвращает максимальное значение, сумму и среднее арифметическое чисел в списке.  

def statistic(numbers):
    if not numbers: 
        return max_value, total_sum, average

    numbers = [10, 3, 5, 9, 18, 3, 0, 7]

    max_value = max(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)

    return max_value, total_sum, average 

numbers = [10, 3, 5, 9, 18, 3, 0, 7]
max_value, total_sum, average = statistic(numbers)

print(f"Максимальное значение: {max_value}")
print(f"Сумма: {total_sum}")
print(f"Среднее арифметическое чисел: {average}")


### Задача 9: Длинные и короткие слова  
Дан список слов:  
```python
word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
```  
Напишите программу, которая определяет самое длинное и самое короткое слово в списке.  

def long_and_short(words): 
    if not words: 
        return None, None
    
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    return longest_word, shortest_word
    
word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]

longest_word, shortest_word = long_and_short(word_list)

print(f"Самое длинное слово: {longest_word}")
print(f"Самое короткое слово: {shortest_word}")


### Задача 10: Фильтрация по частоте  
Дан список чисел:  
```python
number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]
```  
Создайте новый список, содержащий только числа, которые встречаются в оригинальном списке не менее трёх раз.  

from collections import Counter

number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]

frequency = Counter(number_list)
filter_list = [num for num in frequency 
               if frequency[num] >= 3]

print(f"Числа, которые встречаются не менее трех раз: {filter_list}")


### Задача 11: Второй лучший результат  
Дан список результатов экзамена:  
```python
exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]
```  
Напишите программу, которая определяет второй по величине результат в списке.  

exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]

unique_results = set(exam_results)

sorted_results = sorted(unique_results)

if len(sorted_results) >= 2: 
    second_best_result = sorted_results[-2]

    print("Второй по величине результат:", second_best_result)    

else: 

    print("Недостаточно уникальных результатов для определения второго по величине результата")



