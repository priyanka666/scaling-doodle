def reorderLines(logLines):
    """
    :param logLines: unordered log lines
    :return: ordered logLines
    """
    letter_based_logs, integer_based_logs = [], []
    for logLine in logLines:
        if logLine.split()[1].isdigit():
            integer_based_logs.append(logLine)
        else:
            letter_based_logs.append(logLine.split())
    # first we are sorting based on alphanumeric identifier
    # later we are sorting based on words
    # this way we can be sure even if both the letter based logs are same
    # they are sorted using alphanumeric identifier
    letter_based_logs.sort(key=lambda x:x[0])
    letter_based_logs.sort(key=lambda x:[a.lower() for a in x[1:]])

    for i in range(len(letter_based_logs)):
        letter_based_logs[i] = (" ".join(letter_based_logs[i]))
    return letter_based_logs + integer_based_logs
