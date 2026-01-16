height = int(input())
width = int(input())

lights = []
differ = set()

for i in range(height):
  l = "".join(input().split())
  lights.append(l)

differ.add(lights[height-1])

while len(lights) > 1:
  light1 = lights.pop()
  light2 = lights.pop()
  light3 = ""
  for light in range(width):
    if light1[light] == light2[light]:
      light3 += "0"
    else:
      light3 += "1"
  differ.add(light3)
  lights.append(light3)

print(len(differ))
