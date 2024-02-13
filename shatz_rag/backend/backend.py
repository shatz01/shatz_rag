import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


def get_index():
    this_file_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(os.path.dirname(this_file_dir), "data")
    documents = SimpleDirectoryReader(data_dir).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index

def get_response(query):
    index = get_index()
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response


if __name__ == "__main__":
    response = get_response("What did the author do growing up?")
    print(response)
