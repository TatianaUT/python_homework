# Task 1
def hello():
    return "Hello!"
print(hello())

# Task 2

def greet(name):
    return f"Hello, {name}!"
print(greet("Tatiana"))
print(greet("Kira"))

# Task 3

def calc(a, b, operation = "multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a%b
        elif operation == "int_divide":
            return a//b
        elif operation == "power":
            return a ** b
        else:
            return "Unknown operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# Task 4

def data_type_conversion(value, type_name):
    try:
        if type_name == "float":
            return float(value)
        elif type_name == "str":
            return str(value)
        elif type_name == "int":
            return int(value)
        else:
            return f"Unknown type: {type_name}"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type_name}."

# Task 5
    
def grade(*args):
    try:
       average = sum(args) / len(args)
       if average >= 90:
           return "A"
       elif average >= 80:
           return "B"
       elif average >= 70:
           return "C"
       elif average >= 60:
           return "D"
       else:
           return "F"

    except Exception:
        return "Invalid data was provided."

# Task 6

def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

# Task 7

def student_scores(mode, **kwargs):
    try:
        if mode == "best":
            # to find the student with max grade
            best_student = max(kwargs, key=kwargs.get)
            return best_student
        elif mode == "mean":
            # to count the average score
            mean_score = sum(kwargs.values()) / len(kwargs)
            return mean_score
        else:
            return "Invalid mode."

    except Exception:
        return "Invalid data was provided."

# Task 8
    
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word in little_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()
    return " ".join(words)

# Task 9

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# Task 10

def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        #if starts with a vowel
        if word[0] in vowels:
            result.append(word + "ay")

        # if starts with "qu"
        elif "qu" in word[:3]:
            index = word.index("qu") + 2
            result.append(word[index:] + word[:index] + "ay")

        # otherwise move all consonants before first vowel to the end 
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:   
                index += 1
            result.append(word[index:] + word[:index] + "ay")
    
    return " ".join(result)

print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("queen"))



