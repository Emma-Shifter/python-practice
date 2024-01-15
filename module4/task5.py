input = input("Введите строку: ")

print("Развёрнутая последовательность между первым и последним h: "
      f"{input[input.rindex('h') - 1:input.index('h'):-1]}")