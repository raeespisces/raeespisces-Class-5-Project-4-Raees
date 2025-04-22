def add_copies(lst,data):
   for i in range(3):
      lst.append(data)

def main():
   message =input ("Enter a message to copy:")
   lst = []
   print("Before list:",lst)
   add_copies(lst,message)
   print("After list:",lst)

if __name__ == "__main__":
   main()
