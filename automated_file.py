import os
import shutil

class FileOrganizer:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.extensions = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
            "Archives": [".zip", ".tar", ".gz"],
            "Code": [".py", ".js", ".html", ".css"]
        }

    def organize(self):
        if not os.path.exists(self.target_dir):
            print("Directory not found.")
            return

        for filename in os.listdir(self.target_dir):
            file_path = os.path.join(self.target_dir, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower()
                moved = False
                for category, ext_list in self.extensions.items():
                    if ext in ext_list:
                        dest_folder = os.path.join(self.target_dir, category)
                        os.makedirs(dest_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(dest_folder, filename))
                        print(f"Moved: {filename} -> {category}/")
                        moved = True
                        break

# Usage
# organizer = FileOrganizer("./Downloads")
# organizer.organize()
