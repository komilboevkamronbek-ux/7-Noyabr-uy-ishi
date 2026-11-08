#                   1-masala
# def count_passing_students(grades:list[int],passing_grade:int) -> int:
#     count = 0
#     for i in grades:
#         if i >= passing_grade:
#             count += 1
#     return count

# lst = list(map(int,input(">>> ").split()))
# passing_grade = int(input("Passing grade: "))
# print(count_passing_students(lst, passing_grade))

#                   2-masala
def ends_with_gram(words: list[str]) -> list[str]:
    new = []
    for i in words:
        if i.lower().endswith("gram"):
            new.append(i)
    return new        
        

lst = input(">>> ").split()
natija = ends_with_gram(lst)
print(natija)