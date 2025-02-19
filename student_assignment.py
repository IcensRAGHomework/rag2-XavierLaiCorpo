from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

def load_with_PyPdf(file_path: str):
    loader = PyPDFLoader(file_path)
    return loader.load()

def print_docs(docs):
    page_num = 0
    for doc in docs:
        print("----- Doc", page_num, "begin ------")
        print(f"Length={len(doc.page_content)}")
        print("**** Page Content ****")
        print(doc.page_content)
        print("**********************")
        #print("===== MetaData ====")
        #print(doc.metadata)
        #print("===================")
        print("----- Doc", page_num, "end ------")
        print()
        page_num += 1

def recursive_split_with_regex(text):
    spliter = RecursiveCharacterTextSplitter(separators=["第 .+ 章 .+\n", "第 \\d+-?\\d* 條\n"],
                                    chunk_size=0,
                                    chunk_overlap=0,
                                    is_separator_regex=True,
                                    keep_separator=True)
    result = spliter.create_documents([text], metadatas=[{"spliter": "Xavier_Lai"}])
    #print_docs(result)
    return result

def hw02_1(q1_pdf):
    docs = load_with_PyPdf(q1_pdf)
    return docs[-1]

def hw02_2(q2_pdf):
    docs = load_with_PyPdf(q2_pdf)
    text = ""
    for doc in docs:
        text = text + doc.page_content + "\n"
    result = recursive_split_with_regex(text)
    return len(result)

