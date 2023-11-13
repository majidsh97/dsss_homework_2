import random


def get_random_num(min, max):
    """
    this function gets two numbers and returns one random number
    :param
    `min`= minimum number,
    `max`= maximuim number
    :return
    Random integer.
    """
    #try:
    r = random.randint(min, max)
    #except:
        #r = random.randint(int(min), int(max))
    return r


def get_random_operation():
    
    """
    @param: no Args
    :)
    ------------------------------------
    @return: a random char
    """
    return random.choice(['+', '-', '*'])


def operation(n1, n2, o):
    """
    
    do the operation
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    Executes a math quiz game by presenting math problems and evaluating user answers.

    This function runs a simple math quiz game. It prompts the user with math problems
    and evaluates the user's input against the correct answer. The user's score is calculated
    based on correct answers.

    The user is presented with a set number of questions determined by the value of `t_q`.

    Parameters:
    None

    Returns:
    None
    """


    s = 0
    t_q = 3 #3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = get_random_num(1, 10); n2 = get_random_num(1, 5); o = get_random_operation()

        PROBLEM, ANSWER = operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
    
