
class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        retuned = {
            "books": [],
            "total": "0",
            "keyword": keyword
        }

        if data:
            retuned["total"] = "1"
            retuned["books"] = [cls._cut_book_data(data)]
        return retuned

    @classmethod
    def package_collection(cls, data, keyword):
        retuned = {
            "books": [],
            "total": "0",
            "keyword": keyword
        }
        if data:
            retuned["total"] = data["total"]
            retuned["books"] = [cls._cut_book_data(da) for da in data["books"]]
        return retuned

    @classmethod
    def _cut_book_data(cls, data):
        book = {
            "title": data["title"],
            "publisher": data["publisher"],
            "pages": data["pages"] or "",
            "author": "、".join(data["author"]),
            "price": data["price"],
            "summary": data["summary"] or "",
            "image": data["image"],
        }
        return book