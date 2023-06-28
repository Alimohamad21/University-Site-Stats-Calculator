def retryUntilElementFound(find_method, element):
    while True:
        try:
            find_method(element)
            break
        except:
            pass