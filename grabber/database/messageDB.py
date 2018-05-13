from bson import ObjectId
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

    def get_title_id_by_name(self, title_name) -> dict:
        return self.__titles.find_one({"name": title_name})["_id"]

    def get_title_by_id(self, id) -> dict:
        return self.__titles.find_one({"_id": ObjectId(id)})

    def get_messages_count(self, id: str):
        title = self.get_title_by_id(id)
        messages = list(self.__messages.find({"title_name": title["name"]}))
        print(len(messages))
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


forum = ForumDatabase()
# titles = forum.get_titles()
# for title in titles:
#     page_count = title['url'].replace(
#         "https://www.youth4work.com/Talent/C-Language/Forum/113752-what-is-the-purpose-of-getch-function-in-c?page=",
#         "")
#     print(title['url'])

# print(forum.get_messages_count("What is vector in C ?"))
print(forum.get_title_id_by_name("What is vector in C ?"))
print(forum.get_title_name_by_id("5af88941b5d5103243bce9d2"))

# forum.clear()
# forum.get_messages_count("Ітератори")
# message = {'d': "sdsdsd"}
# forum.save_message(message)

# self.__topics_coll.remove()
