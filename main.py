def average_closure():
    dictionary = []
    def add_number(number):
        dictionary.append(number)
    def get_average():
        print(dictionary)
        return sum(dictionary) / len(dictionary)
    return add_number , get_average
add_number , get_average = average_closure()
add_number(4)
add_number(3)
add_number(12)
print(f"Середньо арифметичне число -> {round(get_average() , 2)}")