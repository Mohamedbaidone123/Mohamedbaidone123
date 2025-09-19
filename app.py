import os
import base64
import requests
from pathlib import Path

class GitHubUploader:
    def __init__(self, token, repo_owner, repo_name):
        self.token = token
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def upload_file(self, file_path, repo_path=""):
        """
        Upload a single file to GitHub repository
        """
        try:
            with open(file_path, "rb") as file:
                content = file.read()
            
            content_b64 = base64.b64encode(content).decode("utf-8")
            
            github_path = f"{repo_path}/{os.path.basename(file_path)}" if repo_path else os.path.basename(file_path)
            
            data = {
                "message": f"Upload {os.path.basename(file_path)}",
                "content": content_b64
            }
            
            response = requests.put(
                f"{self.base_url}/{github_path}",
                headers=self.headers,
                json=data
            )
            
            if response.status_code in [200, 201]:
                print(f"✅ Successfully uploaded {file_path} to {github_path}")
                return True
            else:
                print(f"❌ Failed to upload {file_path}: {response.json().get('message', 'Unknown error')}")
                return False
                
        except Exception as e:
            print(f"⚠️ Error uploading {file_path}: {str(e)}")
            return False
    
    def upload_directory(self, directory_path, repo_path=""):
        """
        Upload a directory and all its contents to GitHub repository
        """
        success_count = 0
        total_count = 0
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                total_count += 1
                file_path = os.path.join(root, file)
                
                rel_path = os.path.relpath(root, directory_path)
                target_path = repo_path if rel_path == "." else (os.path.join(repo_path, rel_path) if repo_path else rel_path)
                
                if self.upload_file(file_path, target_path):
                    success_count += 1
        
        print(f"📂 Uploaded {success_count} out of {total_count} files")
        return success_count == total_count

def main():
    # Configuration - Replace these placeholders
    GITHUB_TOKEN = "{TOKEN}"       # 🔑 Replace with your GitHub token
    REPO_OWNER = "{OWNER}"         # 👤 Replace with your GitHub username/org
    REPO_NAME = "{REPO_NAME}"      # 📦 Replace with your repository name
    
    uploader = GitHubUploader(GITHUB_TOKEN, REPO_OWNER, REPO_NAME)
    
    print("GitHub File Uploader")
    print("1️⃣ Upload a single file")
    print("2️⃣ Upload a directory")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        file_path = input("Enter the path to the file: ")
        repo_path = input("Enter the target directory in repository (leave empty for root): ")
        uploader.upload_file(file_path, repo_path)
    elif choice == "2":
        dir_path = input("Enter the path to the directory: ")
        repo_path = input("Enter the target directory in repository (leave empty for root): ")
        uploader.upload_directory(dir_path, repo_path)
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()