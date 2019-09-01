def is_isbn_or_key(word):
    """
    判断q是关键字还是isbn
    q.isdigit() 判断是否全为数字
    isbn13 ： 0-9（13位） isbn10： 0-9（10） 有可能有_
    """
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"

    short_word = word.replace("-", "")
    if short_word.isdigit() and len(short_word) == 10 and "-" in word:
        isbn_or_key = "isbn"
    return isbn_or_key
