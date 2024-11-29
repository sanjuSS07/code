N = int(input())
super = list(map(int, input().split()))

batch_m_supers= 0
batch_n_supers = 0


super.sort(key=lambda y: (abs(y), -y), reverse=True)


super_man = True

for i in super:
    if super_man:
        batch_m_supers += i
    else:
        batch n supers += i
    super_man = not super_man

super_difference = abs(batch_m_supers - batch_n_supers)
print(super_difference)
