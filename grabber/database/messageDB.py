from pymongo import MongoClient


class ForumDatabase:
    def __init__(self):
        self.__client = MongoClient("mongodb://localhost:27017/")
        self.__db = self.__client["forum"]
        self.__messages = self.__db.messages
        self.__titles = self.__db.titles

    def save_message(self, message: dict):
        self.__messages.save(message)

    def save_title(self, title: dict):
        self.__titles.save(title)

    def get_titles(self):
        return list(self.__titles.find())

    def get_messages_count(self, title_name: str):
        messages = list(self.__messages.find({"title_name": title_name}))
        authors_list = list({})
        for message in messages:
            authors_list.insert(len(authors_list), message["author"])
        authors_dict = dict.fromkeys(authors_list, 0)
        for message in messages:
            authors_dict[message["author"]] += 1
        return authors_dict

    def delete_all(self):
        self.__messages.remove()
        self.__titles.remove()

    def close(self):
        self.__client.close()

# forum = ForumDatabase()
# titles = forum.get_titles()
# for title in titles:
#     page_count = title['url'].replace(
#         "https://www.youth4work.com/Talent/C-Language/Forum/113752-what-is-the-purpose-of-getch-function-in-c?page=",
#         "")
#     print(title['url'])

# print(forum.get_messages_count("Ітератори"))
# forum.clear()
# forum.get_messages_count("Ітератори")
# message = {'d': "sdsdsd"}
# forum.save_message(message)

# self.__topics_coll.remove()
