def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return 'I ' + instructions[11:]
    if instructions.endswith("Simon says"):
        return 'I ' + instructions[:11]
    return "I won't do it!"


