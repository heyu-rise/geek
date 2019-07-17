class SearchEngineBase:
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus')

    def search(self, query):
        raise Exception('search')


def main(search_engine):
    for file_path in ['D:/python/1.txt', 'D:/python/2.txt', 'D:/python/3.txt', 'D:/python/4.txt', 'D:/python/5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        for result in results:
            print(result)


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SearchEngineBase, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


search_engine = SimpleEngine()
main(search_engine)
