qntd_videos = int(input())

minimo_qntd_cortes = 0
maxima_qntd_videos = 0
for i in range(qntd_videos):
    video = int(input())
    maxima_qntd_videos += video
    pilha = [video] if video != 1 else []
    while pilha:
        video = pilha.pop(0)
        clip1 = video//2
        clip2 = video - (video//2)
        minimo_qntd_cortes += 1

        pilha.append(clip1) if clip1 != 1 else None
        pilha.append(clip2) if clip2 != 1 else None

print(minimo_qntd_cortes, maxima_qntd_videos)