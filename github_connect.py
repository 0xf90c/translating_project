# from github import Github
# from github import Auth

# auth = Auth.Token("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")

# g = Github(auth=auth)

# repo = g.get_repo("0xf90c/translating_project")

# # file_content1 = repo.get_contents("README.md")
# # file_content2 = repo.get_contents("Translate")

# for file in folder_contents:
#     print(f"file: {file.name}")
#     print(file.decoded_content.decode("utf-8"))
# # 

from github import Github
from github import Auth

# 🔹 Replace with your GitHub token
GITHUB_TOKEN = "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"

# 🔹 Authenticate using the token
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

# 🔹 Define repo details
REPO_OWNER = "0xf90c"
REPO_NAME = "translating_project"

# 🔹 Get the repository object
try:
    repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")
    print(f"✅ Connected to repository: {REPO_OWNER}/{REPO_NAME}")
except Exception as e:
    print(f"❌ Error connecting to repository: {e}")
    exit()

# 🔹 Function to fetch file content
def fetch_file_content(file_path):
    try:
        file = repo.get_contents(file_path)
        content = file.decoded_content.decode("utf-8")
        print(f"\n📄 File: {file_path}\n{content}\n")
    except Exception as e:
        print(f"❌ Error fetching file '{file_path}': {e}")

# 🔹 Function to fetch all files in a folder
def fetch_folder_contents(folder_path):
    try:
        contents = repo.get_contents(folder_path)
        print(f"\n📂 Folder: {folder_path}")
        for file in contents:
            if file.type == "file":  # Ignore subdirectories
                fetch_file_content(file.path)
    except Exception as e:
        print(f"❌ Error fetching folder '{folder_path}': {e}")

# 🔹 Fetch specific files
fetch_file_content("README.md")  # Fetch README.md from repo root

# 🔹 Fetch all files inside the "Translate" folder
fetch_folder_contents("Translate")
