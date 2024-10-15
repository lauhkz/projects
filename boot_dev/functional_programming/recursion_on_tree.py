filetree = {
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {"receipt1.txt": None, "receipt2.txt": None},
            "February": {"receipt3.txt": None},
        },
    },
}


def list_files(current_filetree, current_path=""):
    files = []
    for node in current_filetree:
        if current_filetree.get(node) == None:
            files.append(f"{current_path}/{node}")

        if isinstance(current_filetree.get(node), dict):
            files.extend(
                list_files(
                    current_filetree[node], current_path=f"{current_path}/{node}"
                )
            )

    return files


print(list_files(filetree, ""))
