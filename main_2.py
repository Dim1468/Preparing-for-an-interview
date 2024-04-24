class Stack:
    def __init__(self, stack):
        self.stack = stack

    def is_balanced_brackets(self):
        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']
        bracket_stack = []

        for bracket in self.stack:
            if bracket in opening_brackets:
                bracket_stack.append(bracket)
            elif bracket in closing_brackets:
                if len(bracket_stack) == 0:
                    return f'{self.stack} - несбалансированная последовательность'

                popped_bracket = bracket_stack.pop()
                if (popped_bracket == '(' and bracket == ')') or (popped_bracket == '{' and bracket == '}') or (
                        popped_bracket == '[' and bracket == ']'):
                    continue
                else:
                    return f'{self.stack} - несбалансированная последовательность'

        if len(bracket_stack) != 0:
            return f'{self.stack} - несбалансированная последовательность'
        return f'{self.stack} - сбалансированная последовательность'


def is_balanced(stack):
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    bracket_stack = []

    for bracket in stack:
        if bracket in opening_brackets:
            bracket_stack.append(bracket)
        elif bracket in closing_brackets:
            if len(bracket_stack) == 0:
                return False

            popped_bracket = bracket_stack.pop()
            if (popped_bracket == '(' and bracket == ')') or (popped_bracket == '{' and bracket == '}') or (
                    popped_bracket == '[' and bracket == ']'):
                continue
            else:
                return False

    if len(bracket_stack) != 0:
        return False
    return True


def test():
    stack = '(((([{}]))))'
    assert is_balanced(stack)
    stack = '[([])((([[[]]])))]{()}'
    assert is_balanced(stack)
    stack = '{{[()]}}'
    assert is_balanced(stack)
    stack = '}{}'
    assert not is_balanced(stack)
    stack = '{{[(])]}}'
    assert not is_balanced(stack)
    stack = '[[{())}]'
    assert not is_balanced(stack)
    stack = '()(((((((((((((((((('
    assert not is_balanced(stack)
    print('Все тесты прошли успешно!')


if __name__ == '__main__':
    check_balance = Stack("(((([{}]))))")
    print(check_balance.is_balanced_brackets())

    check_balance_2 = Stack("}{}")
    print(check_balance_2.is_balanced_brackets())

    test()