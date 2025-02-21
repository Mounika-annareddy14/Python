scores = [100,34,78,69,45,32,67,87,34,67,98,23]

#total sum
print(sum(scores))

#using for
sum_ = 0
for score in scores:
    sum_ += score
print(sum_)

#highest number
print(max(scores))

max_ = 0
for score in scores:
    if score > max_:
        max_ = score
print(max_)


total = 0
for i in range(1 , 101):
    total+=i
print(total)
