import os 
import shutil

#Define file categories 
file_categories = {
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",".webp", ".heif", ".jfif", ".pjpeg", ".pjp", ".avif",".svg",".cr2",],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp",],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx",".pdf",],
    "Audio": [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl", ".m4a", ".m4b", ".m4p",],
    "Text": [".txt", ".in", ".out", ".log", ".md", ".markdown", ".json", ".xml", ".csv", ".yaml", ".yml", ".tsv", ".html", ".htm", ".xhtml", ".php", ".css", ".js", ".jsx", ".c", ".cpp", ".h", ".hpp", ".java", ".py", ".rb", ".pl", ".sql", ".swift", ".go", ".kt", ".ts", ".lua", ".sh", ".bat", ".ps1", ".psm1", ".psd1", ".ps1xml", ".clj", ".cljc", ".cljs", ".groovy", ".r", ".rmd", ".rhistory", ".rdata", ".rproj", ".rprojuser", ".rmd",],
    "Compressed": [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip",],
    "Disc": [".bin", ".dmg", ".iso", ".toast", ".vcd",],
    "Data": [".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".xml", ".json",],
    "Executables": [".apk", ".bat", ".com", ".exe", ".gadget", ".jar", ".wsf",],
    "Fonts": [".fnt", ".fon", ".otf", ".ttf",],
    "Projects": [".wfp", ".pxz", ".fla",".psd",],
    "Emulation": [".cia", ".3ds", ".3dsx", ".nds", ".srl", ".wad", ".wii", ".wiiu", ".iso", ".wbfs", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl", ".elf", ".dol", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl", ".elf", ".dol", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl", ".elf", ".dol", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl", ".elf", ".dol", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl", ".elf", ".dol", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl", ".elf", ".dol", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl", ".elf", ".dol", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl", ".elf", ".dol", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl", ".elf", ".dol", ".gcm", ".gcz", ".ciso", ".wbfs", ".wdf", ".wia", ".rvz", ".rvl", ".rpx", ".rpl",]
}

def organize_files(directory):
    """Organizes files into folders based on their type."""
    try:
        files = os.listdir(directory)

        for file in files: 
            file_path = os.path.join(directory,file) # Full path to file
            if os.path.isfile(file_path): #Ensure it's a file, not a folder
                file_ext = os.path.splitext(file)[1].lower()

                # Move files to the correct category folder
                for category, extensions in file_categories.items():
                    if file_ext in extensions:
                        category_folder = os.path.join(directory, category)

                        # Create folder if it doesn't exist 
                        if not os.path.exists(category_folder):
                            os.makedirs(category_folder)

                        # Move the file
                        shutil.move(file_path, os.path.join(category_folder, file))
                        print(f"Moved {file} -> {category}/")

    except FileNotFoundError:
        print("Directory not found")

organize_files("C://Users/mrcom/Desktop")
                            