class Figure:
    pass


class Page:

    def open(self):
        print("Opened")


new_page = Page()
login_page = Page()

new_page.open()
login_page.open()

print(new_page, login_page)
