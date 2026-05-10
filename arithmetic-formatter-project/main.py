def arithmetic_arranger(problems, show_answers=False):
    # Check for too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Initialize lists to store each line
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []
    
    # Process each problem
    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        
        # Check operator
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if operands contain only digits
        if not parts[0].isdigit() or not parts[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        
        # Check operand length
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Get operands and operator
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]
        
        # Calculate width (max length of operands + 2 for operator and space)
        width = max(len(operand1), len(operand2)) + 2
        
        # Format each line
        first_line.append(operand1.rjust(width))
        second_line.append(operator + ' ' + operand2.rjust(width - 2))
        dashes_line.append('-' * width)
        
        # Calculate answer if needed
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answers_line.append(answer.rjust(width))
    
    # Join lines with four spaces between problems
    arranged_problems = '    '.join(first_line) + '\n' + \
                       '    '.join(second_line) + '\n' + \
                       '    '.join(dashes_line)
    
    # Add answers if needed
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers_line)
    
    return arranged_problems