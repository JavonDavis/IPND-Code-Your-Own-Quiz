# IPND Stage 2 Final Project

quiz = {
    'easy': ('''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.}''',
             ['world', 'Python', 'print', 'HTML']),

    'medium': ('''A __1__ is created with the def keyword.  You specify the inputs to a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to return.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.''',
               ['function', 'arguments', 'None', 'list']),

    'hard': ('''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).''',
             ['class', 'method', '__init__', 'instance', '__repr__', '__add__', '__sub__', '__lt__', '__gt__',
              '__eq__'])
}

prompt_choose_level = '''Please select a game difficulty by typing it in!
Possible choices include easy, medium, and hard.
'''

level_choice_message = '''You've chosen {}!

You will get 5 guesses per problem
    
    '''

guess_prompt = 'What should be substituted in for {}? '


def play(paragraph, answers, guesses=5):
    """
    Runs through the main gameplay, prompts the user at most 5 times for each possible option, until they've got it all
    or they've used their 5 times
    :param paragraph: The paragraph for the user to guess as a string
    :param answers: the list of string answers
    :param guesses: the number of guesses allowed per possible option, default to 5
    :return: the result as a String, either the user won or they've used too many guesses
    """
    number_of_answers = len(answers)
    for i in range(number_of_answers):
        current_guess_number = 0
        answer = answers[i]
        key = '__{}__'.format(i + 1)
        while current_guess_number < guesses:
            print 'The current paragraph reads as such:\n\n'
            print paragraph

            guess = raw_input(guess_prompt.format(key).lower()).lower()
            print '\n'
            if guess == answer.lower():
                print 'Correct!\n'
                paragraph = paragraph.replace(key, answer)
                break
            current_guess_number += 1
            guesses_left = guesses - current_guess_number
            if guesses_left > 1:
                print 'That isn\'t the correct answer!  Let\'s try again; you have {} trys left!'.format(guesses_left)
            elif guesses_left == 1:
                print 'That isn\'t the correct answer!  You only have 1 try left!  Make it count!'

        if current_guess_number == guesses:
            return 'You\'ve failed too many straight guesses!  Game over!'

    print 'The current paragraph reads as such:\n\n'
    print paragraph
    return 'You won!'


if __name__ == '__main__':
    choice = str(raw_input(prompt_choose_level)).lower()

    print level_choice_message.format(choice)
    quiz_round = quiz[choice]
    result = play(quiz_round[0], quiz_round[1])
    print result
