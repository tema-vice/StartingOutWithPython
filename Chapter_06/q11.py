# Exercise 11
def main():
    user_name = input("Enter your name: ")
    personal_data = input("Describe yourself: ")
    html_file(user_name, personal_data)

def html_file(user_name, personal_data):
    try:
        file = open("index.html",'w')
        file.write(f"<html>\n<head>\n</head>\n<body>\n  <center>\n      <h1>{user_name}</h1>\n  </center>")
        file.write(f"\n  <hr />\n    {personal_data}\n  <hr />\n</body>\n</html>")
        print("Файл html создан.")
    except Exception as error:
        print(error)
    finally:
        file.close()

main()
