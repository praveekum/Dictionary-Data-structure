x=str(input("Enter the word:"))
y=x.lower()
z=y.capitalize()
content=True
i=1
with open("list.txt") as f:
    while content:
        content = f.readline()
        if y in content.lower():
            print(content,end="")
            print(f"Yes is prestent on line number {i}\n")
        i+=1