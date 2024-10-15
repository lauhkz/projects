example = {1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}
second_example = {1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}


def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id, document_docs in nested_documents.items():
        if document_id == target_document_id:
            return level
        elif not isinstance(document_docs, dict) or not document_docs:
            return -1
        else:
            rec = count_nested_levels(document_docs, target_document_id, level + 1)

            print(f"type:{type(document_id)}, and:{document_id}")
            print(f"type:{type(document_docs)}, and:{document_docs}")


# print(count_nested_levels(second_example, 9, 4))
print(count_nested_levels(example, 2, 2))
