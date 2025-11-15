for i in range(0, 10_000):
    if i == 3:
        print("Encontré a 3...")
        continue
    if i == 8:
        print("Encontré a 8...")
        break
    print(i)
else:
    print("✅")