#!/usr/bin/env python3

# Naiv Bayes osztályozó példa - Iris adathalmazon
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# 1. Adatok betöltése
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 2. Tanító- és tesztadatok szétválasztása
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. Modell létrehozása
model = GaussianNB()

# 4. Modell betanítása
model.fit(X_train, y_train)

# 5. Predikció a teszt adatokon
y_pred = model.predict(X_test)

# 6. Eredmények kiértékelése
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


plt.figure(figsize=(8, 6))
for i, color in zip(range(3), ["red", "blue", "green"]):
    plt.scatter(
        X_test[y_test == i, 0],
        X_test[y_test == i, 1],
        color=color,
        label=iris.target_names[i],
    )
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.title("Iris tesztadatok - Valós osztályok")
plt.legend()
plt.grid(True)
plt.show()
