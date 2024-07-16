

def check_rule1(formula):
    if isinstance(formula, str):
        # It's a literal, hence valid.
        return True
    elif isinstance(formula, dict):
        for operator, operands in formula.items():
            if operator == 'NOT':
                # Check that the operand of NOT is a literal.
                if not isinstance(operands, str):
                    return False
            else:
                # Recursively check each operand.
                for operand in operands:
                    if not check_rule1(operand):
                        return False
    return True





def check_rule2(formula, expect=None):
    if isinstance(formula, str):
        # It's a literal, hence valid.
        return True
    elif isinstance(formula, dict):
        for operator, operands in formula.items():
            if expect and operator != expect:
                return False
            # Determine the next expected operator
            next_expect = 'AND' if operator == 'OR' else 'OR'
            # Recursively check each operand.
            for operand in operands:
                if not check_rule2(operand, next_expect):
                    return False
    return True



# Negation applied only to literals
valid_formula_rule1_1 = {
    'AND': [
        'x1',
        {'NOT': 'x2'}
    ]
}

# Check Rule 1
is_rule1_valid_1 = check_rule1(valid_formula_rule1_1)
print(f"Rule 1 valid (Example 1): {is_rule1_valid_1}")  # Output should be True

# Negation applied only to literals
valid_formula_rule1_2 = {
    'OR': [
        {'AND': ['x1', 'x2']},
        {'NOT': 'x3'}
    ]
}

# Check Rule 1
is_rule1_valid_2 = check_rule1(valid_formula_rule1_2)
print(f"Rule 1 valid (Example 2): {is_rule1_valid_2}")  # Output should be True


# Negation applied to a non-literal (AND operation)
invalid_formula_rule1_1 = {
    'AND': [
        'x1',
        {'NOT': {'AND': ['x2', 'x3']}}
    ]
}

# Check Rule 1
is_rule1_valid_3 = check_rule1(invalid_formula_rule1_1)
print(f"Rule 1 valid (Example 3): {is_rule1_valid_3}")  # Output should be False

# Negation applied to a non-literal (OR operation)
invalid_formula_rule1_2 = {
    'OR': [
        'x1',
        {'NOT': {'OR': ['x2', 'x3']}}
    ]
}

# Check Rule 1
is_rule1_valid_4 = check_rule1(invalid_formula_rule1_2)
print(f"Rule 1 valid (Example 4): {is_rule1_valid_4}")  # Output should be False


# Alternating levels of conjunction and disjunction
valid_formula_rule2_1 = {
    'OR': [
        {'AND': ['x1', 'x2']},
        {'AND': ['x3', 'x4']}
    ]
}

# Check Rule 2
is_rule2_valid_1 = check_rule2(valid_formula_rule2_1)
print(f"Rule 2 valid (Example 1): {is_rule2_valid_1}")  # Output should be True

# Alternating levels of conjunction and disjunction
valid_formula_rule2_2 = {
    'AND': [
        {'OR': ['x1', 'x2']},
        {'OR': ['x3', 'x4']}
    ]
}

# Check Rule 2
is_rule2_valid_2 = check_rule2(valid_formula_rule2_2)
print(f"Rule 2 valid (Example 2): {is_rule2_valid_2}")  # Output should be True

# Non-alternating levels (two consecutive ORs)
invalid_formula_rule2_1 = {
    'OR': [
        {'OR': ['x1', 'x2']},
        {'AND': ['x3', 'x4']}
    ]
}



# Check Rule 2
is_rule2_valid_3 = check_rule2(invalid_formula_rule2_1)
print(f"Rule 2 valid (Example 3): {is_rule2_valid_3}")  # Output should be False


# Non-alternating levels (two consecutive ANDs)
invalid_formula_rule2_2 = {
    'AND': [
        {'AND': ['x1', 'x2']},
        {'OR': ['x3', 'x4']}
    ]
}

# Check Rule 2
is_rule2_valid_4 = check_rule2(invalid_formula_rule2_2)
print(f"Rule 2 valid (Example 4): {is_rule2_valid_4}")  # Output should be False
