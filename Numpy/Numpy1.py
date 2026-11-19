import numpy as np

# مصفوفة 1D
arr1 = np.array([1, 2, 3, 4])
print(arr1)

# مصفوفة 2D (جدول)
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)


print("=" * 20)
print(".shape" , arr1.shape)  # عدد العناصر في كل بعد
print(".shape" , arr2.shape)  # 2 صفوف × 2 أعمدة
print(".dtype" , arr2.dtype)  # نوع البيانات
print(".ndim" , arr2.ndim)   # عدد الأبعاد


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # [5 7 9]
print(a - b)  # [-3 -3 -3]
print(a * b)
print(a / b)

arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))      # مجموع العناصر
print(np.mean(arr))     # المتوسط
print(np.max(arr))      # أكبر قيمة
print(np.min(arr))      # أصغر قيمة
print(np.sqrt(arr))     # الجذر التربيعي لكل عنصر
print(np.arange(0, 10, 2)) # create array with arange [0 2 4 6 8]
print(np.linspace(0, 1, 5)) # [0.   0.25 0.5 0.75 1. ]



arr = np.arange(6)  # [0 1 2 3 4 5]
arr = arr.reshape(3, 2)
print(arr)


# مصفوفة 1D طولها 5
arr = np.random.random(5)
print(arr)
# مصفوفة 2x3
arr2 = np.random.random((2, 3))
print(arr2)

arr = np.random.random((3, 3)) * 10
print(arr)


arr = np.full((3, 3), 5)
print(arr)

arr = np.array([1, 2, 3, 4])
print(arr.tolist())

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("affiche le diagonal " ,arr.diagonal())

arr = np.array([[0, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr.trace())
print(arr.astype(int))
arr = np.array([1, 0, 1, 0])
print(arr.astype(bool))

arr = np.array([1, 0, 1, 0])
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.reshape(arr1, (4, 1))
print(arr2)




