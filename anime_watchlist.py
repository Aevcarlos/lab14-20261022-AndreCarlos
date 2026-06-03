# Step 2
class Anime:
    def __init__(self, title, genre, status):
        self.title=title
        self.genre=genre
        self.status=status
        # self.anime_list=anime_list

# Step 3 
    def display_info(self):
        print("Title:", self.title,)
        print("Genre:", self.genre)
        print("Status:", self.status)


    def update_status(self, new_status="Watching"):
        self.status = new_status




print("========== Anime Watched ==========")
a1 = Anime("Bleach", "Action", "Completed")
a1.display_info()
a2 = Anime("Code Geass", "Political", "Completed")
a2.display_info()
a3 = Anime("Naruto", "Action", "Plan to Watch")
a3.display_info()

anime_list = [a1, a2, a3]


a3.update_status("Watching")
print("========== Updated Anime... ==========")
a3.display_info()
